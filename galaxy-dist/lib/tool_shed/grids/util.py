import os, logging
import tool_shed.util.shed_util_common as suc
import tool_shed.util.metadata_util as metadata_util
from galaxy.web.form_builder import SelectField

def build_approved_select_field( trans, name, selected_value=None, for_component=True ):
    options = [ ( 'No', trans.model.ComponentReview.approved_states.NO ),
                ( 'Yes', trans.model.ComponentReview.approved_states.YES ) ]
    if for_component:
        options.append( ( 'Not applicable', trans.model.ComponentReview.approved_states.NA ) )
        if selected_value is None:
            selected_value = trans.model.ComponentReview.approved_states.NA
    select_field = SelectField( name=name )
    for option_tup in options:
        selected = selected_value and option_tup[ 1 ] == selected_value
        select_field.add_option( option_tup[ 0 ], option_tup[ 1 ], selected=selected )
    return select_field

def build_changeset_revision_select_field( trans, repository, selected_value=None, add_id_to_name=True,
                                           downloadable=False, reviewed=False, not_reviewed=False ):
    """Build a SelectField whose options are the changeset_rev strings of certain revisions of the received repository."""
    options = []
    changeset_tups = []
    refresh_on_change_values = []
    if downloadable:
        # Restrict the options to downloadable revisions.
        repository_metadata_revisions = repository.downloadable_revisions
    elif reviewed:
        # Restrict the options to revisions that have been reviewed.
        repository_metadata_revisions = []
        metadata_changeset_revision_hashes = []
        for metadata_revision in repository.metadata_revisions:
            metadata_changeset_revision_hashes.append( metadata_revision.changeset_revision )
        for review in repository.reviews:
            if review.changeset_revision in metadata_changeset_revision_hashes:
                repository_metadata_revisions.append( review.repository_metadata )
    elif not_reviewed:
        # Restrict the options to revisions that have not yet been reviewed.
        repository_metadata_revisions = []
        reviewed_metadata_changeset_revision_hashes = []
        for review in repository.reviews:
            reviewed_metadata_changeset_revision_hashes.append( review.changeset_revision )
        for metadata_revision in repository.metadata_revisions:
            if metadata_revision.changeset_revision not in reviewed_metadata_changeset_revision_hashes:
                repository_metadata_revisions.append( metadata_revision )
    else:
        # Restrict the options to all revisions that have associated metadata.
        repository_metadata_revisions = repository.metadata_revisions
    for repository_metadata in repository_metadata_revisions:
        rev, label, changeset_revision = \
            metadata_util.get_rev_label_changeset_revision_from_repository_metadata( trans,
                                                                                     repository_metadata,
                                                                                     repository=repository )
        changeset_tups.append( ( rev, label, changeset_revision ) )
        refresh_on_change_values.append( changeset_revision )
    # Sort options by the revision label.  Even though the downloadable_revisions query sorts by update_time,
    # the changeset revisions may not be sorted correctly because setting metadata over time will reset update_time.
    for changeset_tup in sorted( changeset_tups ):
        # Display the latest revision first.
        options.insert( 0, ( changeset_tup[ 1 ], changeset_tup[ 2 ] ) )
    if add_id_to_name:
        name = 'changeset_revision_%d' % repository.id
    else:
        name = 'changeset_revision'
    select_field = SelectField( name=name,
                                refresh_on_change=True,
                                refresh_on_change_values=refresh_on_change_values )
    for option_tup in options:
        selected = selected_value and option_tup[ 1 ] == selected_value
        select_field.add_option( option_tup[ 0 ], option_tup[ 1 ], selected=selected )
    return select_field
