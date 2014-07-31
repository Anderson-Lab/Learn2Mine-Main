import logging
import os
from galaxy import eggs
from galaxy.util import asbool
from galaxy.util import json
from galaxy.util import listify
import tool_shed.util.shed_util_common as suc
from tool_shed.util import common_util
from tool_shed.util import common_install_util
from tool_shed.util import container_util
from tool_shed.util import encoding_util
from tool_shed.util import metadata_util
from tool_shed.util import tool_util

eggs.require( 'mercurial' )

from mercurial import commands
from mercurial import hg
from mercurial import ui

log = logging.getLogger( __name__ )

def build_repository_dependency_relationships( trans, repo_info_dicts, tool_shed_repositories ):
    """
    Build relationships between installed tool shed repositories and other installed tool shed repositories upon which they depend.  These
    relationships are defined in the repository_dependencies entry for each dictionary in the received list of repo_info_dicts.  Each of
    these dictionaries is associated with a repository in the received tool_shed_repositories list.
    """
    log.debug( "Building repository dependency relationships..." )
    for repo_info_dict in repo_info_dicts:
        for name, repo_info_tuple in repo_info_dict.items():
            description, repository_clone_url, changeset_revision, ctx_rev, repository_owner, repository_dependencies, tool_dependencies = \
                suc.get_repo_info_tuple_contents( repo_info_tuple )
            if repository_dependencies:
                for key, val in repository_dependencies.items():
                    if key in [ 'root_key', 'description' ]:
                        continue
                    d_repository = None
                    repository_components_tuple = container_util.get_components_from_key( key )
                    components_list = suc.extract_components_from_tuple( repository_components_tuple )
                    d_toolshed, d_name, d_owner, d_changeset_revision = components_list[ 0:4 ]
                    for tsr in tool_shed_repositories:
                        # Get the the tool_shed_repository defined by name, owner and changeset_revision.  This is the repository that will be
                        # dependent upon each of the tool shed repositories contained in val.  We'll need to check tool_shed_repository.tool_shed
                        # as well if/when repository dependencies across tool sheds is supported.
                        if tsr.name == d_name and tsr.owner == d_owner and tsr.changeset_revision == d_changeset_revision:
                            d_repository = tsr
                            break
                    if d_repository is None:
                        # The dependent repository is not in the received list so look in the database.
                        d_repository = suc.get_or_create_tool_shed_repository( trans, d_toolshed, d_name, d_owner, d_changeset_revision )
                    # Process each repository_dependency defined for the current dependent repository.
                    for repository_dependency_components_list in val:
                        required_repository = None
                        rd_toolshed, rd_name, rd_owner, rd_changeset_revision, rd_prior_installation_required, rd_only_if_compiling_contained_td = \
                            common_util.parse_repository_dependency_tuple( repository_dependency_components_list )
                        # Get the the tool_shed_repository defined by rd_name, rd_owner and rd_changeset_revision.  This is the repository that will be
                        # required by the current d_repository.
                        # TODO: Check tool_shed_repository.tool_shed as well when repository dependencies across tool sheds is supported.
                        for tsr in tool_shed_repositories:
                            if tsr.name == rd_name and tsr.owner == rd_owner and tsr.changeset_revision == rd_changeset_revision:
                                required_repository = tsr
                                break
                        if required_repository is None:
                            # The required repository is not in the received list so look in the database.
                            required_repository = suc.get_or_create_tool_shed_repository( trans, rd_toolshed, rd_name, rd_owner, rd_changeset_revision )
                        # Ensure there is a repository_dependency relationship between d_repository and required_repository.
                        rrda = None
                        for rd in d_repository.repository_dependencies:
                            if rd.id == required_repository.id:
                                rrda = rd
                                break
                        if not rrda:
                            # Make sure required_repository is in the repository_dependency table.
                            repository_dependency = get_repository_dependency_by_repository_id( trans, required_repository.id )
                            if not repository_dependency:
                                repository_dependency = trans.install_model.RepositoryDependency( tool_shed_repository_id=required_repository.id )
                                trans.install_model.context.add( repository_dependency )
                                trans.install_model.context.flush()
                            # Build the relationship between the d_repository and the required_repository.
                            rrda = trans.install_model.RepositoryRepositoryDependencyAssociation( tool_shed_repository_id=d_repository.id,
                                                                                          repository_dependency_id=repository_dependency.id )
                            trans.install_model.context.add( rrda )
                            trans.install_model.context.flush()

def can_add_to_key_rd_dicts( key_rd_dict, key_rd_dicts ):
    """Handle the case where an update to the changeset revision was done."""
    k = key_rd_dict.keys()[ 0 ]
    rd = key_rd_dict[ k ]
    partial_rd = rd[ 0:3 ]
    for kr_dict in key_rd_dicts:
        key = kr_dict.keys()[ 0 ]
        if key == k:
            repository_dependency = kr_dict[ key ]
            if repository_dependency[ 0:3 ] == partial_rd:
                return False
    return True

def create_repository_dependency_objects( trans, tool_path, tool_shed_url, repo_info_dicts, install_repository_dependencies=False,
                                          no_changes_checked=False, tool_panel_section_id=None, new_tool_panel_section_label=None ):
    """
    Discover all repository dependencies and make sure all tool_shed_repository and associated repository_dependency records exist as well as
    the dependency relationships between installed repositories.  This method is called when uninstalled repositories are being reinstalled.
    If the user elected to install repository dependencies, all items in the all_repo_info_dicts list will be processed.  However, if repository
    dependencies are not to be installed, only those items contained in the received repo_info_dicts list will be processed.
    """
    log.debug( "Creating repository dependency objects..." )
    # The following list will be maintained within this method to contain all created or updated tool shed repositories, including repository
    # dependencies that may not be installed.
    all_created_or_updated_tool_shed_repositories = []
    # There will be a one-to-one mapping between items in 3 lists: created_or_updated_tool_shed_repositories, tool_panel_section_keys and
    # filtered_repo_info_dicts.  The 3 lists will filter out repository dependencies that are not to be installed.
    created_or_updated_tool_shed_repositories = []
    tool_panel_section_keys = []
    # Repositories will be filtered (e.g., if already installed, if elected to not be installed, etc), so filter the associated repo_info_dicts
    # accordingly.
    filtered_repo_info_dicts = []
    # Discover all repository dependencies and retrieve information for installing them.  Even if the user elected to not install repository
    # dependencies we have to make sure all repository dependency objects exist so that the appropriate repository dependency relationships can
    # be built.
    all_required_repo_info_dict = common_install_util.get_required_repo_info_dicts( trans, tool_shed_url, repo_info_dicts )
    all_repo_info_dicts = all_required_repo_info_dict.get( 'all_repo_info_dicts', [] )
    if not all_repo_info_dicts:
        # No repository dependencies were discovered so process the received repositories.
        all_repo_info_dicts = [ rid for rid in repo_info_dicts ]
    for repo_info_dict in all_repo_info_dicts:
        # If the user elected to install repository dependencies, all items in the all_repo_info_dicts list will be processed.  However, if
        # repository dependencies are not to be installed, only those items contained in the received repo_info_dicts list will be processed
        # but the the all_repo_info_dicts list will be used to create all defined repository dependency relationships.
        if is_in_repo_info_dicts( repo_info_dict, repo_info_dicts ) or install_repository_dependencies:
            for name, repo_info_tuple in repo_info_dict.items():
                can_update_db_record = False
                description, repository_clone_url, changeset_revision, ctx_rev, repository_owner, repository_dependencies, tool_dependencies = \
                    suc.get_repo_info_tuple_contents( repo_info_tuple )
                # See if the repository has an existing record in the database.
                repository_db_record, installed_changeset_revision = \
                    suc.repository_was_previously_installed( trans, tool_shed_url, name, repo_info_tuple )
                if repository_db_record:
                    if repository_db_record.status in [ trans.install_model.ToolShedRepository.installation_status.INSTALLED,
                                                        trans.install_model.ToolShedRepository.installation_status.CLONING,
                                                        trans.install_model.ToolShedRepository.installation_status.SETTING_TOOL_VERSIONS,
                                                        trans.install_model.ToolShedRepository.installation_status.INSTALLING_REPOSITORY_DEPENDENCIES,
                                                        trans.install_model.ToolShedRepository.installation_status.INSTALLING_TOOL_DEPENDENCIES,
                                                        trans.install_model.ToolShedRepository.installation_status.LOADING_PROPRIETARY_DATATYPES ]:
                        debug_msg = "Skipping installation of revision %s of repository '%s' because it was installed " % \
                            ( str( changeset_revision ), str( repository_db_record.name ) )
                        debug_msg += "with the (possibly updated) revision %s and it's current installation status is '%s'." % \
                            ( str( installed_changeset_revision ), str( repository_db_record.status ) )
                        log.debug( debug_msg )
                        can_update_db_record = False
                    else:
                        if repository_db_record.status in [ trans.install_model.ToolShedRepository.installation_status.ERROR,
                                                            trans.install_model.ToolShedRepository.installation_status.NEW,
                                                            trans.install_model.ToolShedRepository.installation_status.UNINSTALLED ]:
                            # The current tool shed repository is not currently installed, so we can update it's record in the database.
                            name = repository_db_record.name
                            installed_changeset_revision = repository_db_record.installed_changeset_revision
                            metadata_dict = repository_db_record.metadata
                            dist_to_shed = repository_db_record.dist_to_shed
                            can_update_db_record = True
                        elif repository_db_record.status in [ trans.install_model.ToolShedRepository.installation_status.DEACTIVATED ]:
                            # The current tool shed repository is deactivated, so updating it's database record is not necessary - just activate it.
                            log.debug( "Reactivating deactivated tool_shed_repository '%s'." % str( repository_db_record.name ) )
                            common_install_util.activate_repository( trans, repository_db_record )
                            # No additional updates to the database record are necessary.
                            can_update_db_record = False
                        elif repository_db_record.status not in [ trans.install_model.ToolShedRepository.installation_status.NEW ]:
                            # Set changeset_revision here so suc.create_or_update_tool_shed_repository will find the previously installed
                            # and uninstalled repository instead of creating a new record.
                            changeset_revision = repository_db_record.installed_changeset_revision
                            suc.reset_previously_installed_repository( trans, repository_db_record )
                            can_update_db_record = True
                else:
                    # No record exists in the database for the repository currently being processed.
                    installed_changeset_revision = changeset_revision
                    metadata_dict = {}
                    dist_to_shed = False
                    can_update_db_record = True
                if can_update_db_record:
                    # The database record for the tool shed repository currently being processed can be updated.  Get the repository metadata
                    # to see where it was previously located in the tool panel.
                    if repository_db_record and repository_db_record.metadata:
                        tool_section, tool_panel_section_key = \
                            tool_util.handle_tool_panel_selection( trans=trans,
                                                                   metadata=repository_db_record.metadata,
                                                                   no_changes_checked=no_changes_checked,
                                                                   tool_panel_section_id=tool_panel_section_id,
                                                                   new_tool_panel_section_label=new_tool_panel_section_label )
                    else:
                        # We're installing a new tool shed repository that does not yet have a database record.
                        tool_panel_section_key, tool_section = \
                            tool_util.handle_tool_panel_section( trans,
                                                                 tool_panel_section_id=tool_panel_section_id,
                                                                 new_tool_panel_section_label=new_tool_panel_section_label )
                    tool_shed_repository = \
                        suc.create_or_update_tool_shed_repository( app=trans.app,
                                                                   name=name,
                                                                   description=description,
                                                                   installed_changeset_revision=changeset_revision,
                                                                   ctx_rev=ctx_rev,
                                                                   repository_clone_url=repository_clone_url,
                                                                   metadata_dict={},
                                                                   status=trans.install_model.ToolShedRepository.installation_status.NEW,
                                                                   current_changeset_revision=changeset_revision,
                                                                   owner=repository_owner,
                                                                   dist_to_shed=False )
                    if tool_shed_repository not in all_created_or_updated_tool_shed_repositories:
                        all_created_or_updated_tool_shed_repositories.append( tool_shed_repository )
                    # Only append the tool shed repository to the list of created_or_updated_tool_shed_repositories if it is supposed to be installed.
                    if install_repository_dependencies or is_in_repo_info_dicts( repo_info_dict, repo_info_dicts ):
                        if tool_shed_repository not in created_or_updated_tool_shed_repositories:
                            # Keep the one-to-one mapping between items in 3 lists.
                            created_or_updated_tool_shed_repositories.append( tool_shed_repository )
                            tool_panel_section_keys.append( tool_panel_section_key )
                            filtered_repo_info_dicts.append( repo_info_dict )
    # Build repository dependency relationships even if the user chose to not install repository dependencies.
    build_repository_dependency_relationships( trans, all_repo_info_dicts, all_created_or_updated_tool_shed_repositories )
    return created_or_updated_tool_shed_repositories, tool_panel_section_keys, all_repo_info_dicts, filtered_repo_info_dicts

def generate_message_for_invalid_repository_dependencies( metadata_dict ):
    """Return the error message associated with an invalid repository dependency for display in the caller."""
    message = ''
    if metadata_dict:
        invalid_repository_dependencies_dict = metadata_dict.get( 'invalid_repository_dependencies', None )
        if invalid_repository_dependencies_dict:
            invalid_repository_dependencies = invalid_repository_dependencies_dict.get( 'invalid_repository_dependencies', [] )
            for repository_dependency_tup in invalid_repository_dependencies:
                toolshed, name, owner, changeset_revision, prior_installation_required, only_if_compiling_contained_td, error = \
                    common_util.parse_repository_dependency_tuple( repository_dependency_tup, contains_error=True )
                if error:
                    message = '%s  ' % str( error )
    return message

def get_key_for_repository_changeset_revision( trans, toolshed_base_url, repository, repository_metadata, all_repository_dependencies ):
    prior_installation_required, only_if_compiling_contained_td = \
        get_prior_installation_required_and_only_if_compiling_contained_td( trans, toolshed_base_url, repository, repository_metadata, all_repository_dependencies )
    # Create a key with the value of prior_installation_required defaulted to False.
    key = container_util.generate_repository_dependencies_key_for_repository( toolshed_base_url=toolshed_base_url,
                                                                              repository_name=repository.name,
                                                                              repository_owner=repository.user.username,
                                                                              changeset_revision=repository_metadata.changeset_revision,
                                                                              prior_installation_required=prior_installation_required,
                                                                              only_if_compiling_contained_td=only_if_compiling_contained_td )
    return key

def get_prior_installation_required_and_only_if_compiling_contained_td( trans, toolshed_base_url, repository, repository_metadata, all_repository_dependencies ):
    """
    This method is called from the tool shed and never Galaxy.  If all_repository_dependencies contains a repository dependency tuple that is associated with
    the received repository, return the value of the tuple's prior_installation_required component.
    """
    if all_repository_dependencies:
        for rd_key, rd_tups in all_repository_dependencies.items():
            if rd_key in [ 'root_key', 'description' ]:
                continue
            for rd_tup in rd_tups:
                rd_toolshed, rd_name, rd_owner, rd_changeset_revision, rd_prior_installation_required, rd_only_if_compiling_contained_td = \
                    common_util.parse_repository_dependency_tuple( rd_tup )
                if rd_toolshed == toolshed_base_url and \
                    rd_name == repository.name and \
                    rd_owner == repository.user.username and \
                    rd_changeset_revision == repository_metadata.changeset_revision:
                    return rd_prior_installation_required, rd_only_if_compiling_contained_td
    elif repository_metadata:
        # Get the list of changeset revisions from the tool shed to which the repository may be updated.
        metadata = repository_metadata.metadata
        current_changeset_revision = str( repository_metadata.changeset_revision )
        # Get the changeset revision to which the current value of required_repository_changeset_revision should be updated if it's not current.
        text = suc.get_updated_changeset_revisions( trans,
                                                    name=str( repository.name ),
                                                    owner=str( repository.user.username ),
                                                    changeset_revision=current_changeset_revision )
        if text:
            valid_changeset_revisions = listify( text )
            if current_changeset_revision not in valid_changeset_revisions:
                valid_changeset_revisions.append( current_changeset_revision )
        else:
            valid_changeset_revisions = [ current_changeset_revision ]
        repository_dependencies_dict = metadata[ 'repository_dependencies' ]
        rd_tups = repository_dependencies_dict.get( 'repository_dependencies', [] )
        for rd_tup in rd_tups:
            rd_toolshed, rd_name, rd_owner, rd_changeset_revision, rd_prior_installation_required, rd_only_if_compiling_contained_td = \
                common_util.parse_repository_dependency_tuple( rd_tup )
            if rd_toolshed == toolshed_base_url and \
                rd_name == repository.name and \
                rd_owner == repository.user.username and \
                rd_changeset_revision in valid_changeset_revisions:
                return rd_prior_installation_required, rd_only_if_compiling_contained_td
    # Default both prior_installation_required and only_if_compiling_contained_td to False.
    return 'False', 'False'

def get_repository_dependencies_for_installed_tool_shed_repository( trans, repository ):
    """
    Send a request to the appropriate tool shed to retrieve the dictionary of repository dependencies defined for the received repository which is
    installed into Galaxy.  This method is called only from Galaxy.
    """
    tool_shed_url = suc.get_url_from_tool_shed( trans.app, repository.tool_shed )
    url = suc.url_join( tool_shed_url,
                        'repository/get_repository_dependencies?name=%s&owner=%s&changeset_revision=%s' % \
                        ( str( repository.name ), str( repository.owner ), str( repository.changeset_revision ) ) )
    raw_text = common_util.tool_shed_get( trans.app, tool_shed_url, url )
    if len( raw_text ) > 2:
        encoded_text = json.from_json_string( raw_text )
        text = encoding_util.tool_shed_decode( encoded_text )
    else:
        text = ''
    return text

def get_repository_dependencies_for_changeset_revision( trans, repository, repository_metadata, toolshed_base_url,
                                                        key_rd_dicts_to_be_processed=None, all_repository_dependencies=None,
                                                        handled_key_rd_dicts=None, circular_repository_dependencies=None ):
    """
    Return a dictionary of all repositories upon which the contents of the received
    repository_metadata record depend.  The dictionary keys are name-spaced values
    consisting of:
    toolshed_base_url/repository_name/repository_owner/changeset_revision
    and the values are lists of repository_dependency tuples consisting of:
    ( toolshed_base_url, repository_name, repository_owner, changeset_revision ).
    This method ensures that all required repositories to the nth degree are returned.
    """
    if handled_key_rd_dicts is None:
        handled_key_rd_dicts = []
    if all_repository_dependencies is None:
        all_repository_dependencies = {}
    if key_rd_dicts_to_be_processed is None:
        key_rd_dicts_to_be_processed = []
    if circular_repository_dependencies is None:
        circular_repository_dependencies = []
    # Assume the current repository does not have repository dependencies defined for it.
    current_repository_key = None
    metadata = repository_metadata.metadata
    if metadata:
        if 'repository_dependencies' in metadata:
            current_repository_key = get_key_for_repository_changeset_revision( trans,
                                                                                toolshed_base_url,
                                                                                repository,
                                                                                repository_metadata,
                                                                                all_repository_dependencies )
            repository_dependencies_dict = metadata[ 'repository_dependencies' ]
            if not all_repository_dependencies:
                all_repository_dependencies = initialize_all_repository_dependencies( current_repository_key,
                                                                                      repository_dependencies_dict,
                                                                                      all_repository_dependencies )
            # Handle the repository dependencies defined in the current repository, if any, and populate
            # the various repository dependency objects for this round of processing.
            current_repository_key_rd_dicts, key_rd_dicts_to_be_processed, handled_key_rd_dicts, all_repository_dependencies = \
                populate_repository_dependency_objects_for_processing( trans,
                                                                       current_repository_key,
                                                                       repository_dependencies_dict,
                                                                       key_rd_dicts_to_be_processed,
                                                                       handled_key_rd_dicts,
                                                                       circular_repository_dependencies,
                                                                       all_repository_dependencies )
    if current_repository_key:
        if current_repository_key_rd_dicts:
            # There should be only a single current_repository_key_rd_dict in this list.
            current_repository_key_rd_dict = current_repository_key_rd_dicts[ 0 ]
            # Handle circular repository dependencies.
            if not in_circular_repository_dependencies( current_repository_key_rd_dict, circular_repository_dependencies ):
                if current_repository_key in all_repository_dependencies:
                    handle_current_repository_dependency( trans,
                                                          current_repository_key,
                                                          key_rd_dicts_to_be_processed,
                                                          all_repository_dependencies,
                                                          handled_key_rd_dicts,
                                                          circular_repository_dependencies )
            elif key_rd_dicts_to_be_processed:
                handle_next_repository_dependency( trans,
                                                   key_rd_dicts_to_be_processed,
                                                   all_repository_dependencies,
                                                   handled_key_rd_dicts,
                                                   circular_repository_dependencies )
        elif key_rd_dicts_to_be_processed:
            handle_next_repository_dependency( trans,
                                               key_rd_dicts_to_be_processed,
                                               all_repository_dependencies,
                                               handled_key_rd_dicts,
                                               circular_repository_dependencies )
    elif key_rd_dicts_to_be_processed:
        handle_next_repository_dependency( trans,
                                           key_rd_dicts_to_be_processed,
                                           all_repository_dependencies,
                                           handled_key_rd_dicts,
                                           circular_repository_dependencies )
    all_repository_dependencies = prune_invalid_repository_dependencies( all_repository_dependencies )
    return all_repository_dependencies

def get_repository_dependency_tups_from_repository_metadata( app, repository_metadata, deprecated_only=False ):
    """
    Return a list of of tuples defining repository objects required by the received repository.  The returned
    list defines the entire repository dependency tree.  This method is called only from the Tool Shed.
    """
    dependency_tups = []
    if repository_metadata is not None:
        metadata = repository_metadata.metadata
        if metadata:
            repository_dependencies_dict = metadata.get( 'repository_dependencies', None )
            if repository_dependencies_dict is not None:
                repository_dependency_tups = repository_dependencies_dict.get( 'repository_dependencies', None )
                if repository_dependency_tups is not None:
                    # The value of repository_dependency_tups is a list of repository dependency tuples like this:
                    # ['http://localhost:9009', 'package_samtools_0_1_18', 'devteam', 'ef37fc635cb9', 'False', 'False']
                    for repository_dependency_tup in repository_dependency_tups:
                        toolshed, name, owner, changeset_revision, pir, oicct = \
                        common_util.parse_repository_dependency_tuple( repository_dependency_tup )
                        repository = suc.get_repository_by_name_and_owner( app, name, owner )
                        if repository:
                            if deprecated_only:
                                if repository.deprecated:
                                    dependency_tups.append( repository_dependency_tup )
                            else:
                                dependency_tups.append( repository_dependency_tup )
                        else:
                            log.debug( "Cannot locate repository %s owned by %s for inclusion in repository dependency tups." % \
                                ( name, owner ) )
    return dependency_tups

def get_repository_dependency_tups_for_installed_repository( app, repository, dependency_tups=None, status=None ):
    """
    Return a list of of tuples defining tool_shed_repository objects (whose status can be anything) required by the
    received repository.  The returned list defines the entire repository dependency tree.  This method is called
    only from Galaxy.
    """
    if dependency_tups is None:
        dependency_tups = []
    repository_tup = get_repository_tuple_for_installed_repository_manager( repository )
    for rrda in repository.required_repositories:
        repository_dependency = rrda.repository_dependency
        required_repository = repository_dependency.repository
        if status is None or required_repository.status == status:
            required_repository_tup = get_repository_tuple_for_installed_repository_manager( required_repository )
            if required_repository_tup == repository_tup:
                # We have a circular repository dependency relationship, skip this entry.
                continue
            if required_repository_tup not in dependency_tups:
                dependency_tups.append( required_repository_tup )
                return get_repository_dependency_tups_for_installed_repository( app,
                                                                                required_repository,
                                                                                dependency_tups=dependency_tups )
    return dependency_tups

def get_repository_tuple_for_installed_repository_manager( repository ):
    return ( str( repository.tool_shed ),
             str( repository.name ),
             str( repository.owner ),
             str( repository.installed_changeset_revision ) )

def get_updated_changeset_revisions_for_repository_dependencies( trans, key_rd_dicts ):
    updated_key_rd_dicts = []
    for key_rd_dict in key_rd_dicts:
        key = key_rd_dict.keys()[ 0 ]
        repository_dependency = key_rd_dict[ key ]
        rd_toolshed, rd_name, rd_owner, rd_changeset_revision, rd_prior_installation_required, rd_only_if_compiling_contained_td = \
            common_util.parse_repository_dependency_tuple( repository_dependency )
        if suc.tool_shed_is_this_tool_shed( rd_toolshed ):
            repository = suc.get_repository_by_name_and_owner( trans.app, rd_name, rd_owner )
            if repository:
                repository_metadata = \
                    metadata_util.get_repository_metadata_by_repository_id_changeset_revision( trans,
                                                                                               trans.security.encode_id( repository.id ),
                                                                                               rd_changeset_revision )
                if repository_metadata:
                    # The repository changeset_revision is installable, so no updates are available.
                    new_key_rd_dict = {}
                    new_key_rd_dict[ key ] = repository_dependency
                    updated_key_rd_dicts.append( key_rd_dict )
                else:
                    # The repository changeset_revision is no longer installable, so see if there's been an update.
                    repo_dir = repository.repo_path( trans.app )
                    repo = hg.repository( suc.get_configured_ui(), repo_dir )
                    changeset_revision = suc.get_next_downloadable_changeset_revision( repository, repo, rd_changeset_revision )
                    repository_metadata = metadata_util.get_repository_metadata_by_repository_id_changeset_revision( trans,
                                                                                                                     trans.security.encode_id( repository.id ),
                                                                                                                     changeset_revision )
                    if repository_metadata:
                        new_key_rd_dict = {}
                        new_key_rd_dict[ key ] = \
                            [ rd_toolshed, rd_name, rd_owner, repository_metadata.changeset_revision, rd_prior_installation_required, rd_only_if_compiling_contained_td ]
                        # We have the updated changset revision.
                        updated_key_rd_dicts.append( new_key_rd_dict )
                    else:
                        repository_components_tuple = container_util.get_components_from_key( key )
                        components_list = suc.extract_components_from_tuple( repository_components_tuple )
                        toolshed, repository_name, repository_owner, repository_changeset_revision = components_list[ 0:4 ]
                        # For backward compatibility to the 12/20/12 Galaxy release.
                        if len( components_list ) == 4:
                            prior_installation_required = 'False'
                            rd_only_if_compiling_contained_td = 'False'
                        elif len( components_list ) == 5:
                            rd_only_if_compiling_contained_td = 'False'
                        message = "The revision %s defined for repository %s owned by %s is invalid, so repository dependencies defined for repository %s will be ignored." % \
                            ( str( rd_changeset_revision ), str( rd_name ), str( rd_owner ), str( repository_name ) )
                        log.debug( message )
            else:
                repository_components_tuple = container_util.get_components_from_key( key )
                components_list = suc.extract_components_from_tuple( repository_components_tuple )
                toolshed, repository_name, repository_owner, repository_changeset_revision = components_list[ 0:4 ]
                message = "The revision %s defined for repository %s owned by %s is invalid, so repository dependencies defined for repository %s will be ignored." % \
                    ( str( rd_changeset_revision ), str( rd_name ), str( rd_owner ), str( repository_name ) )
                log.debug( message )
    return updated_key_rd_dicts

def handle_circular_repository_dependency( repository_key, repository_dependency, circular_repository_dependencies, handled_key_rd_dicts, all_repository_dependencies ):
    all_repository_dependencies_root_key = all_repository_dependencies[ 'root_key' ]
    repository_dependency_as_key = get_repository_dependency_as_key( repository_dependency )
    repository_key_as_repository_dependency = repository_key.split( container_util.STRSEP )
    update_circular_repository_dependencies( repository_key,
                                             repository_dependency,
                                             all_repository_dependencies[ repository_dependency_as_key ],
                                             circular_repository_dependencies )
    if all_repository_dependencies_root_key != repository_dependency_as_key:
        all_repository_dependencies[ repository_key ] = [ repository_dependency ]
    return circular_repository_dependencies, handled_key_rd_dicts, all_repository_dependencies

def handle_current_repository_dependency( trans, current_repository_key, key_rd_dicts_to_be_processed, all_repository_dependencies, handled_key_rd_dicts,
                                          circular_repository_dependencies ):
    current_repository_key_rd_dicts = []
    for rd in all_repository_dependencies[ current_repository_key ]:
        rd_copy = [ str( item ) for item in rd ]
        new_key_rd_dict = {}
        new_key_rd_dict[ current_repository_key ] = rd_copy
        current_repository_key_rd_dicts.append( new_key_rd_dict )
    if current_repository_key_rd_dicts:
        toolshed, required_repository, required_repository_metadata, repository_key_rd_dicts, key_rd_dicts_to_be_processed, handled_key_rd_dicts = \
            handle_key_rd_dicts_for_repository( trans,
                                                current_repository_key,
                                                current_repository_key_rd_dicts,
                                                key_rd_dicts_to_be_processed,
                                                handled_key_rd_dicts,
                                                circular_repository_dependencies )
        return get_repository_dependencies_for_changeset_revision( trans=trans,
                                                                   repository=required_repository,
                                                                   repository_metadata=required_repository_metadata,
                                                                   toolshed_base_url=toolshed,
                                                                   key_rd_dicts_to_be_processed=key_rd_dicts_to_be_processed,
                                                                   all_repository_dependencies=all_repository_dependencies,
                                                                   handled_key_rd_dicts=handled_key_rd_dicts,
                                                                   circular_repository_dependencies=circular_repository_dependencies )

def handle_key_rd_dicts_for_repository( trans, current_repository_key, repository_key_rd_dicts, key_rd_dicts_to_be_processed, handled_key_rd_dicts, circular_repository_dependencies ):
    key_rd_dict = repository_key_rd_dicts.pop( 0 )
    repository_dependency = key_rd_dict[ current_repository_key ]
    toolshed, name, owner, changeset_revision, prior_installation_required, only_if_compiling_contained_td = \
        common_util.parse_repository_dependency_tuple( repository_dependency )
    if suc.tool_shed_is_this_tool_shed( toolshed ):
        required_repository = suc.get_repository_by_name_and_owner( trans.app, name, owner )
        required_repository_metadata = \
            metadata_util.get_repository_metadata_by_repository_id_changeset_revision( trans,
                                                                                       trans.security.encode_id( required_repository.id ),
                                                                                       changeset_revision )
        if required_repository_metadata:
            # The required_repository_metadata changeset_revision is installable.
            required_metadata = required_repository_metadata.metadata
            if required_metadata:
                for current_repository_key_rd_dict in repository_key_rd_dicts:
                    if not in_key_rd_dicts( current_repository_key_rd_dict, key_rd_dicts_to_be_processed ):
                        key_rd_dicts_to_be_processed.append( current_repository_key_rd_dict )
        # Mark the current repository_dependency as handled_key_rd_dicts.
        if not in_key_rd_dicts( key_rd_dict, handled_key_rd_dicts ):
            handled_key_rd_dicts.append( key_rd_dict )
        # Remove the current repository from the list of repository_dependencies to be processed.
        if in_key_rd_dicts( key_rd_dict, key_rd_dicts_to_be_processed ):
            key_rd_dicts_to_be_processed = remove_from_key_rd_dicts( key_rd_dict, key_rd_dicts_to_be_processed )
    else:
        # The repository is in a different tool shed, so build an url and send a request.
        error_message = "Repository dependencies are currently supported only within the same tool shed.  Ignoring repository dependency definition "
        error_message += "for tool shed %s, name %s, owner %s, changeset revision %s" % ( toolshed, name, owner, changeset_revision )
        log.debug( error_message )
    return toolshed, required_repository, required_repository_metadata, repository_key_rd_dicts, key_rd_dicts_to_be_processed, handled_key_rd_dicts

def handle_next_repository_dependency( trans, key_rd_dicts_to_be_processed, all_repository_dependencies, handled_key_rd_dicts, circular_repository_dependencies ):
    next_repository_key_rd_dict = key_rd_dicts_to_be_processed.pop( 0 )
    next_repository_key_rd_dicts = [ next_repository_key_rd_dict ]
    next_repository_key = next_repository_key_rd_dict.keys()[ 0 ]
    toolshed, required_repository, required_repository_metadata, repository_key_rd_dicts, key_rd_dicts_to_be_processed, handled_key_rd_dicts = \
        handle_key_rd_dicts_for_repository( trans,
                                            next_repository_key,
                                            next_repository_key_rd_dicts,
                                            key_rd_dicts_to_be_processed,
                                            handled_key_rd_dicts,
                                            circular_repository_dependencies )
    return get_repository_dependencies_for_changeset_revision( trans=trans,
                                                               repository=required_repository,
                                                               repository_metadata=required_repository_metadata,
                                                               toolshed_base_url=toolshed,
                                                               key_rd_dicts_to_be_processed=key_rd_dicts_to_be_processed,
                                                               all_repository_dependencies=all_repository_dependencies,
                                                               handled_key_rd_dicts=handled_key_rd_dicts,
                                                               circular_repository_dependencies=circular_repository_dependencies )

def in_all_repository_dependencies( repository_key, repository_dependency, all_repository_dependencies ):
    """Return True if { repository_key : repository_dependency } is in all_repository_dependencies."""
    for key, val in all_repository_dependencies.items():
        if key != repository_key:
            continue
        if repository_dependency in val:
            return True
    return False

def in_circular_repository_dependencies( repository_key_rd_dict, circular_repository_dependencies ):
    """
    Return True if any combination of a circular dependency tuple is the key : value pair defined in the received repository_key_rd_dict.  This
    means that each circular dependency tuple is converted into the key : value pair for comparison.
    """
    for tup in circular_repository_dependencies:
        rd_0, rd_1 = tup
        rd_0_as_key = get_repository_dependency_as_key( rd_0 )
        rd_1_as_key = get_repository_dependency_as_key( rd_1 )
        if rd_0_as_key in repository_key_rd_dict and repository_key_rd_dict[ rd_0_as_key ] == rd_1:
            return True
        if rd_1_as_key in repository_key_rd_dict and repository_key_rd_dict[ rd_1_as_key ] == rd_0:
            return True
    return False

def initialize_all_repository_dependencies( current_repository_key, repository_dependencies_dict, all_repository_dependencies ):
    """Initialize the all_repository_dependencies dictionary."""
    # It's safe to assume that current_repository_key in this case will have a value.
    all_repository_dependencies[ 'root_key' ] = current_repository_key
    all_repository_dependencies[ current_repository_key ] = []
    # Store the value of the 'description' key only once, the first time through this recursive method.
    description = repository_dependencies_dict.get( 'description', None )
    all_repository_dependencies[ 'description' ] = description
    return all_repository_dependencies

def in_key_rd_dicts( key_rd_dict, key_rd_dicts ):
    """Return True if key_rd_dict is contained in the list of key_rd_dicts."""
    k = key_rd_dict.keys()[ 0 ]
    v = key_rd_dict[ k ]
    for key_rd_dict in key_rd_dicts:
        for key, val in key_rd_dict.items():
            if key == k and val == v:
                return True
    return False

def is_circular_repository_dependency( repository_key, repository_dependency, all_repository_dependencies ):
    """
    Return True if the received repository_dependency is a key in all_repository_dependencies whose list of repository dependencies
    includes the received repository_key.
    """
    repository_dependency_as_key = get_repository_dependency_as_key( repository_dependency )
    repository_key_as_repository_dependency = repository_key.split( container_util.STRSEP )
    for key, val in all_repository_dependencies.items():
        if key != repository_dependency_as_key:
            continue
        if repository_key_as_repository_dependency in val:
            return True
    return False

def is_in_repo_info_dicts( repo_info_dict, repo_info_dicts ):
    """Return True if the received repo_info_dict is contained in the list of received repo_info_dicts."""
    for name, repo_info_tuple in repo_info_dict.items():
        for rid in repo_info_dicts:
            for rid_name, rid_repo_info_tuple in rid.items():
                if rid_name == name:
                    if len( rid_repo_info_tuple ) == len( repo_info_tuple ):
                        for item in rid_repo_info_tuple:
                            if item not in repo_info_tuple:
                                return False
                        return True
        return False

def filter_only_if_compiling_contained_td( key_rd_dict ):
    """
    Return a copy of the received key_rd_dict with repository dependencies that are needed only_if_compiling_contained_td filtered out
    of the list of repository dependencies for each rd_key.
    """
    filtered_key_rd_dict = {}
    for rd_key, required_rd_tup in key_rd_dict.items():
        tool_shed, name, owner, changeset_revision, prior_installation_required, only_if_compiling_contained_td = \
            common_util.parse_repository_dependency_tuple( required_rd_tup )
        if not asbool( only_if_compiling_contained_td ):
            filtered_key_rd_dict[ rd_key ] = required_rd_tup
    return filtered_key_rd_dict

def merge_missing_repository_dependencies_to_installed_container( containers_dict ):
    """Merge the list of missing repository dependencies into the list of installed repository dependencies."""
    missing_rd_container_root = containers_dict.get( 'missing_repository_dependencies', None )
    if missing_rd_container_root:
        # The missing_rd_container_root will be a root folder containing a single sub_folder.
        missing_rd_container = missing_rd_container_root.folders[ 0 ]
        installed_rd_container_root = containers_dict.get( 'repository_dependencies', None )
        # The installed_rd_container_root will be a root folder containing a single sub_folder.
        if installed_rd_container_root:
            installed_rd_container = installed_rd_container_root.folders[ 0 ]
            installed_rd_container.label = 'Repository dependencies'
            for index, rd in enumerate( missing_rd_container.repository_dependencies ):
                # Skip the header row.
                if index == 0:
                    continue
                installed_rd_container.repository_dependencies.append( rd )
            installed_rd_container_root.folders = [ installed_rd_container ]
            containers_dict[ 'repository_dependencies' ] = installed_rd_container_root
        else:
            # Change the folder label from 'Missing repository dependencies' to be 'Repository dependencies' for display.
            root_container = containers_dict[ 'missing_repository_dependencies' ]
            for sub_container in root_container.folders:
                # There should only be 1 sub-folder.
                sub_container.label = 'Repository dependencies'
            containers_dict[ 'repository_dependencies' ] = root_container
    containers_dict[ 'missing_repository_dependencies' ] = None
    return containers_dict

def populate_repository_dependency_objects_for_processing( trans, current_repository_key, repository_dependencies_dict,
                                                           key_rd_dicts_to_be_processed, handled_key_rd_dicts,
                                                           circular_repository_dependencies, all_repository_dependencies ):
    """
    The process that discovers all repository dependencies for a specified repository's
    changeset revision uses this method to populate the following items for the current
    processing loop: filtered_current_repository_key_rd_dicts, key_rd_dicts_to_be_processed,
    handled_key_rd_dicts, all_repository_dependencies.  Each processing loop may discover
    more repository dependencies, so this method is repeatedly called until all repository
    dependencies have been discovered.
    """
    current_repository_key_rd_dicts = []
    filtered_current_repository_key_rd_dicts = []
    for rd in repository_dependencies_dict[ 'repository_dependencies' ]:
        new_key_rd_dict = {}
        new_key_rd_dict[ current_repository_key ] = rd
        current_repository_key_rd_dicts.append( new_key_rd_dict )
    if current_repository_key_rd_dicts and current_repository_key:
        # Remove all repository dependencies that point to a revision within its own repository.
        current_repository_key_rd_dicts = remove_ropository_dependency_reference_to_self( current_repository_key_rd_dicts )
    current_repository_key_rd_dicts = get_updated_changeset_revisions_for_repository_dependencies( trans,
                                                                                                   current_repository_key_rd_dicts )
    for key_rd_dict in current_repository_key_rd_dicts:
        # Filter out repository dependencies that are required only if compiling the dependent repository's tool dependency.
        key_rd_dict = filter_only_if_compiling_contained_td( key_rd_dict )
        if key_rd_dict:
            is_circular = False
            if not in_key_rd_dicts( key_rd_dict, handled_key_rd_dicts ) and not in_key_rd_dicts( key_rd_dict,
                                                                                                 key_rd_dicts_to_be_processed ):
                filtered_current_repository_key_rd_dicts.append( key_rd_dict )
                repository_dependency = key_rd_dict[ current_repository_key ]
                if current_repository_key in all_repository_dependencies:
                    # Add all repository dependencies for the current repository into it's entry in all_repository_dependencies.
                    all_repository_dependencies_val = all_repository_dependencies[ current_repository_key ]
                    if repository_dependency not in all_repository_dependencies_val:
                        all_repository_dependencies_val.append( repository_dependency )
                        all_repository_dependencies[ current_repository_key ] = all_repository_dependencies_val
                elif not in_all_repository_dependencies( current_repository_key, repository_dependency, all_repository_dependencies ):
                    # Handle circular repository dependencies.
                    if is_circular_repository_dependency( current_repository_key, repository_dependency, all_repository_dependencies ):
                        is_circular = True
                        circular_repository_dependencies, handled_key_rd_dicts, all_repository_dependencies = \
                            handle_circular_repository_dependency( current_repository_key,
                                                                   repository_dependency,
                                                                   circular_repository_dependencies,
                                                                   handled_key_rd_dicts,
                                                                   all_repository_dependencies )
                    else:
                        all_repository_dependencies[ current_repository_key ] = [ repository_dependency ]
                if not is_circular and can_add_to_key_rd_dicts( key_rd_dict, key_rd_dicts_to_be_processed ):
                    new_key_rd_dict = {}
                    new_key_rd_dict[ current_repository_key ] = repository_dependency
                    key_rd_dicts_to_be_processed.append( new_key_rd_dict )
    return filtered_current_repository_key_rd_dicts, key_rd_dicts_to_be_processed, handled_key_rd_dicts, all_repository_dependencies

def prune_invalid_repository_dependencies( repository_dependencies ):
    """
    Eliminate all invalid entries in the received repository_dependencies dictionary.  An entry
    is invalid if the value_list of the key/value pair is empty.  This occurs when an invalid
    combination of tool shed, name , owner, changeset_revision is used and a repository_metadata
    record is not found.
    """
    valid_repository_dependencies = {}
    description = repository_dependencies.get( 'description', None )
    root_key = repository_dependencies.get( 'root_key', None )
    if root_key is None:
        return valid_repository_dependencies
    for key, value in repository_dependencies.items():
        if key in [ 'description', 'root_key' ]:
            continue
        if value:
            valid_repository_dependencies[ key ] = value
    if valid_repository_dependencies:
        valid_repository_dependencies[ 'description' ] = description
        valid_repository_dependencies[ 'root_key' ] = root_key
    return valid_repository_dependencies

def remove_from_key_rd_dicts( key_rd_dict, key_rd_dicts ):
    """Eliminate the key_rd_dict from the list of key_rd_dicts if it is contained in the list."""
    k = key_rd_dict.keys()[ 0 ]
    v = key_rd_dict[ k ]
    clean_key_rd_dicts = []
    for krd_dict in key_rd_dicts:
        key = krd_dict.keys()[ 0 ]
        val = krd_dict[ key ]
        if key == k and val == v:
            continue
        clean_key_rd_dicts.append( krd_dict )
    return clean_key_rd_dicts

def remove_ropository_dependency_reference_to_self( key_rd_dicts ):
    """Remove all repository dependencies that point to a revision within its own repository."""
    clean_key_rd_dicts = []
    key = key_rd_dicts[ 0 ].keys()[ 0 ]
    repository_tup = key.split( container_util.STRSEP )
    rd_toolshed, rd_name, rd_owner, rd_changeset_revision, rd_prior_installation_required, rd_only_if_compiling_contained_td = \
        common_util.parse_repository_dependency_tuple( repository_tup )
    for key_rd_dict in key_rd_dicts:
        k = key_rd_dict.keys()[ 0 ]
        repository_dependency = key_rd_dict[ k ]
        toolshed, name, owner, changeset_revision, prior_installation_required, only_if_compiling_contained_td = \
            common_util.parse_repository_dependency_tuple( repository_dependency )
        if rd_toolshed == toolshed and rd_name == name and rd_owner == owner:
            debug_msg = "Removing repository dependency for repository %s owned by %s " % ( name, owner )
            debug_msg += 'since it refers to a revision within itself.'
            log.debug( debug_msg )
        else:
            new_key_rd_dict = {}
            new_key_rd_dict[ key ] = repository_dependency
            clean_key_rd_dicts.append( new_key_rd_dict )
    return clean_key_rd_dicts

def get_repository_dependency_as_key( repository_dependency ):
    tool_shed, name, owner, changeset_revision, prior_installation_required, only_if_compiling_contained_td = \
        common_util.parse_repository_dependency_tuple( repository_dependency )
    return container_util.generate_repository_dependencies_key_for_repository( tool_shed,
                                                                               name,
                                                                               owner,
                                                                               changeset_revision,
                                                                               prior_installation_required,
                                                                               only_if_compiling_contained_td )

def get_repository_dependency_by_repository_id( trans, decoded_repository_id ):
    return trans.install_model.context.query( trans.install_model.RepositoryDependency ) \
                           .filter( trans.install_model.RepositoryDependency.table.c.tool_shed_repository_id == decoded_repository_id ) \
                           .first()

def update_circular_repository_dependencies( repository_key, repository_dependency, repository_dependencies, circular_repository_dependencies ):
    repository_dependency_as_key = get_repository_dependency_as_key( repository_dependency )
    repository_key_as_repository_dependency = repository_key.split( container_util.STRSEP )
    if repository_key_as_repository_dependency in repository_dependencies:
        found = False
        for tup in circular_repository_dependencies:
            if repository_dependency in tup and repository_key_as_repository_dependency in tup:
                # The circular dependency has already been included.
                found = True
        if not found:
            new_circular_tup = [ repository_dependency, repository_key_as_repository_dependency ]
            circular_repository_dependencies.append( new_circular_tup )
        return circular_repository_dependencies
