import logging
import os
import tarfile
import tempfile
from time import strftime
from galaxy import eggs
from galaxy import util
from galaxy import web
from galaxy.util import json
from galaxy.web.base.controller import BaseAPIController
from galaxy.web.framework.helpers import time_ago
import tool_shed.repository_types.util as rt_util
import tool_shed.util.shed_util_common as suc
from tool_shed.galaxy_install import repository_util
from tool_shed.util import encoding_util
from tool_shed.util import import_util
from tool_shed.util import metadata_util
from tool_shed.util import repository_maintenance_util
from tool_shed.util import tool_util

eggs.require( 'mercurial' )

from mercurial import hg

log = logging.getLogger( __name__ )


class RepositoriesController( BaseAPIController ):
    """RESTful controller for interactions with repositories in the Tool Shed."""

    @web.expose_api_anonymous
    def get_ordered_installable_revisions( self, trans, name, owner, **kwd ):
        """
        GET /api/repositories/get_ordered_installable_revisions

        :param name: the name of the Repository
        :param owner: the owner of the Repository

        Returns the ordered list of changeset revision hash strings that are associated with installable revisions.
        As in the changelog, the list is ordered oldest to newest.
        """
        # Example URL: http://localhost:9009/api/repositories/get_installable_revisions?name=add_column&owner=test
        if name and owner:
            # Get the repository information.
            repository = suc.get_repository_by_name_and_owner( trans.app, name, owner )
            if repository is None:
                error_message = "Error in the Tool Shed repositories API in get_ordered_installable_revisions: "
                error_message += "cannot locate repository %s owned by %s." % ( str( name ), str( owner ) )
                log.debug( error_message )
                return []
            repo_dir = repository.repo_path( trans.app )
            repo = hg.repository( suc.get_configured_ui(), repo_dir )
            ordered_installable_revisions = suc.get_ordered_metadata_changeset_revisions( repository, repo, downloadable=True )
            return ordered_installable_revisions
        else:
            error_message = "Error in the Tool Shed repositories API in get_ordered_installable_revisions: "
            error_message += "invalid name %s or owner %s received." % ( str( name ), str( owner ) )
            log.debug( error_message )
            return []

    @web.expose_api_anonymous
    def get_repository_revision_install_info( self, trans, name, owner, changeset_revision, **kwd ):
        """
        GET /api/repositories/get_repository_revision_install_info

        :param name: the name of the Repository
        :param owner: the owner of the Repository
        :param changeset_revision: the changeset_revision of the RepositoryMetadata object associated with the Repository

        Returns a list of the following dictionaries::
        - a dictionary defining the Repository.  For example:
        {
            "deleted": false,
            "deprecated": false,
            "description": "add_column hello",
            "id": "f9cad7b01a472135",
            "long_description": "add_column hello",
            "name": "add_column",
            "owner": "test",
            "private": false,
            "times_downloaded": 6,
            "url": "/api/repositories/f9cad7b01a472135",
            "user_id": "f9cad7b01a472135"
        }
        - a dictionary defining the Repository revision (RepositoryMetadata).  For example:
        {
            "changeset_revision": "3a08cc21466f",
            "downloadable": true,
            "has_repository_dependencies": false,
            "has_repository_dependencies_only_if_compiling_contained_td": false,
            "id": "f9cad7b01a472135",
            "includes_datatypes": false,
            "includes_tool_dependencies": false,
            "includes_tools": true,
            "includes_tools_for_display_in_tool_panel": true,
            "includes_workflows": false,
            "malicious": false,
            "repository_id": "f9cad7b01a472135",
            "url": "/api/repository_revisions/f9cad7b01a472135"
        }
        - a dictionary including the additional information required to install the repository.  For example:
        {
            "add_column": [
                "add_column hello",
                "http://test@localhost:9009/repos/test/add_column",
                "3a08cc21466f",
                "1",
                "test",
                {},
                {}
            ]
        }
        """
        # Example URL: 
        # http://<xyz>/api/repositories/get_repository_revision_install_info?name=<n>&owner=<o>&changeset_revision=<cr>
        if name and owner and changeset_revision:
            # Get the repository information.
            repository = suc.get_repository_by_name_and_owner( trans.app, name, owner )
            if repository is None:
                log.debug( 'Cannot locate repository %s owned by %s' % ( str( name ), str( owner ) ) )
                return {}, {}, {}
            encoded_repository_id = trans.security.encode_id( repository.id )
            repository_dict = repository.to_dict( view='element',
                                                  value_mapper=self.__get_value_mapper( trans ) )
            repository_dict[ 'url' ] = web.url_for( controller='repositories',
                                                    action='show',
                                                    id=encoded_repository_id )
            # Get the repository_metadata information.
            repository_metadata = suc.get_repository_metadata_by_changeset_revision( trans,
                                                                                     encoded_repository_id,
                                                                                     changeset_revision )
            if repository_metadata is None:
                # The changeset_revision column in the repository_metadata table has been updated with a new
                # value value, so find the changeset_revision to which we need to update.
                repo_dir = repository.repo_path( trans.app )
                repo = hg.repository( suc.get_configured_ui(), repo_dir )
                new_changeset_revision = suc.get_next_downloadable_changeset_revision( repository, repo, changeset_revision )
                repository_metadata = suc.get_repository_metadata_by_changeset_revision( trans,
                                                                                         encoded_repository_id,
                                                                                         new_changeset_revision )
                changeset_revision = new_changeset_revision
            if repository_metadata is not None:
                encoded_repository_metadata_id = trans.security.encode_id( repository_metadata.id )
                repository_metadata_dict = repository_metadata.to_dict( view='collection',
                                                                        value_mapper=self.__get_value_mapper( trans ) )
                repository_metadata_dict[ 'url' ] = web.url_for( controller='repository_revisions',
                                                                 action='show',
                                                                 id=encoded_repository_metadata_id )
                # Get the repo_info_dict for installing the repository.
                repo_info_dict, \
                includes_tools, \
                includes_tool_dependencies, \
                includes_tools_for_display_in_tool_panel, \
                has_repository_dependencies, \
                has_repository_dependencies_only_if_compiling_contained_td = \
                    repository_util.get_repo_info_dict( trans, encoded_repository_id, changeset_revision )
                return repository_dict, repository_metadata_dict, repo_info_dict
            else:
                log.debug( "Unable to locate repository_metadata record for repository id %s and changeset_revision %s" % \
                    ( str( repository.id ), str( changeset_revision ) ) )
                return repository_dict, {}, {}
        else:
            debug_msg = "Error in the Tool Shed repositories API in get_repository_revision_install_info: "
            debug_msg += "Invalid name %s or owner %s or changeset_revision %s received." % \
                ( str( name ), str( owner ), str( changeset_revision ) )
            log.debug( debug_msg )
            return {}, {}, {}

    def __get_value_mapper( self, trans ):
        value_mapper = { 'id' : trans.security.encode_id,
                         'repository_id' : trans.security.encode_id,
                         'user_id' : trans.security.encode_id }
        return value_mapper

    @web.expose_api
    def import_capsule( self, trans, payload, **kwd ):
        """
        POST /api/repositories/new/import_capsule
        Import a repository capsule into the Tool Shed.

        :param key: the user's API key

        The following parameters are included in the payload.
        :param tool_shed_url (required): the base URL of the Tool Shed into which the capsule should be imported.
        :param capsule_file_name (required): the name of the capsule file.
        """
        # Get the information about the capsule to be imported from the payload.
        tool_shed_url = payload.get( 'tool_shed_url', '' )
        if not tool_shed_url:
            raise HTTPBadRequest( detail="Missing required parameter 'tool_shed_url'." )
        capsule_file_name = payload.get( 'capsule_file_name', '' )
        if not capsule_file_name:
            raise HTTPBadRequest( detail="Missing required parameter 'capsule_file_name'." )
        capsule_file_path = os.path.abspath( capsule_file_name )
        capsule_dict = dict( error_message='',
                             encoded_file_path=None,
                             status='ok',
                             tar_archive=None,
                             uploaded_file=None,
                             capsule_file_name=None )
        if os.path.getsize( os.path.abspath( capsule_file_name ) ) == 0:
            log.debug( 'Your capsule file %s is empty.' % str( capsule_file_name ) )
            return {}
        try:
            # Open for reading with transparent compression.
            tar_archive = tarfile.open( capsule_file_path, 'r:*' )
        except tarfile.ReadError, e:
            log.debug( 'Error opening capsule file %s: %s' % ( str( capsule_file_name ), str( e ) ) )
            return {}
        capsule_dict[ 'tar_archive' ] = tar_archive
        capsule_dict[ 'capsule_file_name' ] = capsule_file_name
        capsule_dict = import_util.extract_capsule_files( trans, **capsule_dict )
        capsule_dict = import_util.validate_capsule( trans, **capsule_dict )
        status = capsule_dict.get( 'status', 'error' )
        if status == 'error':
            log.debug( 'The capsule contents are invalid and cannot be imported:<br/>%s' % \
                str( capsule_dict.get( 'error_message', '' ) ) )
            return {}
        encoded_file_path = capsule_dict.get( 'encoded_file_path', None )
        if encoded_file_path is None:
            log.debug( 'The capsule_dict %s is missing the required encoded_file_path entry.' % str( capsule_dict ) )
            return {}
        file_path = encoding_util.tool_shed_decode( encoded_file_path )
        export_info_file_path = os.path.join( file_path, 'export_info.xml' )
        export_info_dict = import_util.get_export_info_dict( export_info_file_path )
        manifest_file_path = os.path.join( file_path, 'manifest.xml' )
        # The manifest.xml file has already been validated, so no error_message should be returned here.
        repository_info_dicts, error_message = import_util.get_repository_info_from_manifest( manifest_file_path )
        # Determine the status for each exported repository archive contained within the capsule.
        repository_status_info_dicts = import_util.get_repository_status_from_tool_shed( trans, repository_info_dicts )
        # Generate a list of repository name / import results message tuples for display after the capsule is imported.
        import_results_tups = []
        # Only create repositories that do not yet exist and that the current user is authorized to create.  The
        # status will be None for repositories that fall into the intersection of these 2 categories.
        for repository_status_info_dict in repository_status_info_dicts:
            # Add the capsule_file_name and encoded_file_path to the repository_status_info_dict.
            repository_status_info_dict[ 'capsule_file_name' ] = capsule_file_name
            repository_status_info_dict[ 'encoded_file_path' ] = encoded_file_path
            import_results_tups = \
                repository_maintenance_util.create_repository_and_import_archive( trans,
                                                                                  repository_status_info_dict,
                                                                                  import_results_tups )
        import_util.check_status_and_reset_downloadable( trans, import_results_tups )
        suc.remove_dir( file_path )
        # NOTE: the order of installation is defined in import_results_tups, but order will be lost
        # when transferred to return_dict.
        return_dict = {}
        for import_results_tup in import_results_tups:
            ok, name_owner, message = import_results_tup
            name, owner = name_owner
            key = 'Archive of repository "%s" owned by "%s"' % ( str( name ), str( owner ) )
            val = message.replace( '<b>', '"' ).replace( '</b>', '"' )
            return_dict[ key ] = val
        return return_dict

    @web.expose_api_anonymous
    def index( self, trans, deleted=False, **kwd ):
        """
        GET /api/repositories
        Displays a collection (list) of repositories.
        """
        # Example URL: http://localhost:9009/api/repositories
        repository_dicts = []
        deleted = util.asbool( deleted )
        for repository in trans.sa_session.query( trans.app.model.Repository ) \
                                          .filter( trans.app.model.Repository.table.c.deleted == deleted ) \
                                          .order_by( trans.app.model.Repository.table.c.name ):
            repository_dict = repository.to_dict( view='collection',
                                                  value_mapper=self.__get_value_mapper( trans ) )
            repository_dict[ 'url' ] = web.url_for( controller='repositories',
                                                    action='show',
                                                    id=trans.security.encode_id( repository.id ) )
            repository_dicts.append( repository_dict )
        return repository_dicts

    @web.expose_api
    def repository_ids_for_setting_metadata( self, trans, my_writable=False, **kwd ):
        """
        GET /api/get_repository_ids_for_setting_metadata

        Displays a collection (list) of repository ids ordered for setting metadata.

        :param key: the API key of the Tool Shed user.
        :param my_writable (optional): if the API key is associated with an admin user in the Tool Shed, setting this param value
                                       to True will restrict resetting metadata to only repositories that are writable by the user
                                       in addition to those repositories of type tool_dependency_definition.  This param is ignored
                                       if the current user is not an admin user, in which case this same restriction is automatic.
        """
        if trans.user_is_admin():
            my_writable = util.asbool( my_writable )
        else:
            my_writable = True
        handled_repository_ids = []
        repository_ids = []
        query = suc.get_query_for_setting_metadata_on_repositories( trans, my_writable=my_writable, order=False )
        # Make sure repositories of type tool_dependency_definition are first in the list.
        for repository in query:
            if repository.type == rt_util.TOOL_DEPENDENCY_DEFINITION and repository.id not in handled_repository_ids:
                repository_ids.append( trans.security.encode_id( repository.id ) )
        # Now add all remaining repositories to the list.
        for repository in query:
            if repository.type != rt_util.TOOL_DEPENDENCY_DEFINITION and repository.id not in handled_repository_ids:
                repository_ids.append( trans.security.encode_id( repository.id ) )
        return repository_ids

    @web.expose_api
    def reset_metadata_on_repositories( self, trans, payload, **kwd ):
        """
        PUT /api/repositories/reset_metadata_on_repositories

        Resets all metadata on all repositories in the Tool Shed in an "orderly fashion".  Since there are currently only two
        repository types (tool_dependecy_definition and unrestricted), the order in which metadata is reset is repositories of
        type tool_dependecy_definition first followed by repositories of type unrestricted, and only one pass is necessary.  If
        a new repository type is introduced, the process will undoubtedly need to be revisited.  To facilitate this order, an
        in-memory list of repository ids that have been processed is maintained.
        
        :param key: the API key of the Tool Shed user.

        The following parameters can optionally be included in the payload.
        :param my_writable (optional): if the API key is associated with an admin user in the Tool Shed, setting this param value
                                       to True will restrict resetting metadata to only repositories that are writable by the user
                                       in addition to those repositories of type tool_dependency_definition.  This param is ignored
                                       if the current user is not an admin user, in which case this same restriction is automatic.
        :param encoded_ids_to_skip (optional): a list of encoded repository ids for repositories that should not be processed.
        :param skip_file (optional): A local file name that contains the encoded repository ids associated with repositories to skip.
                                     This param can be used as an alternative to the above encoded_ids_to_skip.
        """

        def handle_repository( trans, repository, results ):
            log.debug( "Resetting metadata on repository %s" % str( repository.name ) )
            repository_id = trans.security.encode_id( repository.id )
            try:
                invalid_file_tups, metadata_dict = metadata_util.reset_all_metadata_on_repository_in_tool_shed( trans, repository_id )
                if invalid_file_tups:
                    message = tool_util.generate_message_for_invalid_tools( trans, invalid_file_tups, repository, None, as_html=False )
                    results[ 'unsuccessful_count' ] += 1
                else:
                    message = "Successfully reset metadata on repository %s owned by %s" % ( str( repository.name ), str( repository.user.username ) )
                    results[ 'successful_count' ] += 1
            except Exception, e:
                message = "Error resetting metadata on repository %s owned by %s: %s" % ( str( repository.name ), str( repository.user.username ), str( e ) )
                results[ 'unsuccessful_count' ] += 1
            status = '%s : %s' % ( str( repository.name ), message )
            results[ 'repository_status' ].append( status )
            return results

        start_time = strftime( "%Y-%m-%d %H:%M:%S" )
        results = dict( start_time=start_time,
                        repository_status=[],
                        successful_count=0,
                        unsuccessful_count=0 )
        handled_repository_ids = []
        encoded_ids_to_skip = payload.get( 'encoded_ids_to_skip', [] )
        skip_file = payload.get( 'skip_file', None )
        if skip_file and os.path.exists( skip_file ) and not encoded_ids_to_skip:
            # Load the list of encoded_ids_to_skip from the skip_file.
            # Contents of file must be 1 encoded repository id per line.
            lines = open( skip_file, 'rb' ).readlines()
            for line in lines:
                if line.startswith( '#' ):
                    # Skip comments.
                    continue
                encoded_ids_to_skip.append( line.rstrip( '\n' ) )
        if trans.user_is_admin():
            my_writable = util.asbool( payload.get( 'my_writable', False ) )
        else:
            my_writable = True
        query = suc.get_query_for_setting_metadata_on_repositories( trans, my_writable=my_writable, order=False )
        # First reset metadata on all repositories of type repository_dependency_definition.
        for repository in query:
            encoded_id = trans.security.encode_id( repository.id )
            if encoded_id in encoded_ids_to_skip:
                log.debug( "Skipping repository with id %s because it is in encoded_ids_to_skip %s" % \
                           ( str( repository.id ), str( encoded_ids_to_skip ) ) )
            elif repository.type == rt_util.TOOL_DEPENDENCY_DEFINITION and repository.id not in handled_repository_ids:
                results = handle_repository( trans, repository, results )
        # Now reset metadata on all remaining repositories.
        for repository in query:
            encoded_id = trans.security.encode_id( repository.id )
            if encoded_id in encoded_ids_to_skip:
                log.debug( "Skipping repository with id %s because it is in encoded_ids_to_skip %s" % \
                           ( str( repository.id ), str( encoded_ids_to_skip ) ) )
            elif repository.type != rt_util.TOOL_DEPENDENCY_DEFINITION and repository.id not in handled_repository_ids:
                results = handle_repository( trans, repository, results )
        stop_time = strftime( "%Y-%m-%d %H:%M:%S" )
        results[ 'stop_time' ] = stop_time
        return json.to_json_string( results, sort_keys=True, indent=4 )

    @web.expose_api
    def reset_metadata_on_repository( self, trans, payload, **kwd ):
        """
        PUT /api/repositories/reset_metadata_on_repository

        Resets all metadata on a specified repository in the Tool Shed.
        
        :param key: the API key of the Tool Shed user.
        
        The following parameters must be included in the payload.
        :param repository_id: the encoded id of the repository on which metadata is to be reset.
        """

        def handle_repository( trans, start_time, repository ):
            results = dict( start_time=start_time,
                            repository_status=[] )
            try:
                invalid_file_tups, metadata_dict = metadata_util.reset_all_metadata_on_repository_in_tool_shed( trans,
                                                                                                                trans.security.encode_id( repository.id ) )
                if invalid_file_tups:
                    message = tool_util.generate_message_for_invalid_tools( trans, invalid_file_tups, repository, None, as_html=False )
                else:
                    message = "Successfully reset metadata on repository %s owned by %s" % ( str( repository.name ), str( repository.user.username ) )
            except Exception, e:
                message = "Error resetting metadata on repository %s owned by %s: %s" % ( str( repository.name ), str( repository.user.username ), str( e ) )
            status = '%s : %s' % ( str( repository.name ), message )
            results[ 'repository_status' ].append( status )
            return results

        repository_id = payload.get( 'repository_id', None )
        if repository_id is not None:
            repository = suc.get_repository_in_tool_shed( trans, repository_id )
            start_time = strftime( "%Y-%m-%d %H:%M:%S" )
            log.debug( "%s...resetting metadata on repository %s" % ( start_time, str( repository.name ) ) )
            results = handle_repository( trans, start_time, repository )
            stop_time = strftime( "%Y-%m-%d %H:%M:%S" )
            results[ 'stop_time' ] = stop_time
        return json.to_json_string( results, sort_keys=True, indent=4 )

    @web.expose_api_anonymous
    def show( self, trans, id, **kwd ):
        """
        GET /api/repositories/{encoded_repository_id}
        Returns information about a repository in the Tool Shed.

        :param id: the encoded id of the Repository object
        """
        # Example URL: http://localhost:9009/api/repositories/f9cad7b01a472135
        repository = suc.get_repository_in_tool_shed( trans, id )
        if repository is None:
            log.debug( "Unable to locate repository record for id %s." % ( str( id ) ) )
            return {}
        repository_dict = repository.to_dict( view='element',
                                              value_mapper=self.__get_value_mapper( trans ) )
        repository_dict[ 'url' ] = web.url_for( controller='repositories',
                                                action='show',
                                                id=trans.security.encode_id( repository.id ) )
        return repository_dict
