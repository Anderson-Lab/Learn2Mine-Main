# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402424483.025867
_template_filename='templates/webapps/galaxy/workflow/list.mako'
_template_uri='workflow/list.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['init', 'center_panel', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 123
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="workflow"
        self.message_box_visible=False
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        h = context.get('h', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        message = context.get('message', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    <div style="overflow: auto; height: 100%;">\n        <div class="page-container" style="padding: 10px;">\n')
        # SOURCE LINE 17
        if message:
            # SOURCE LINE 18
            __M_writer(u'                ')

            try:
                status
            except:
                status = "done"
                            
            
            # SOURCE LINE 23
            __M_writer(u'\n                <p />\n                <div class="')
            # SOURCE LINE 25
            __M_writer(unicode(status))
            __M_writer(u'message">\n                    ')
            # SOURCE LINE 26
            __M_writer(unicode(h.to_unicode( message )))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'\n            <h2>Your workflows</h2>\n\n            <ul class="manage-table-actions">\n                <li>\n                    <a class="action-button" href="')
        # SOURCE LINE 34
        __M_writer(unicode(h.url_for( controller='workflow', action='create' )))
        __M_writer(u'">\n                        <img src="')
        # SOURCE LINE 35
        __M_writer(unicode(h.url_for('/static/images/silk/add.png')))
        __M_writer(u'" />\n                        <span>Create new workflow</span>\n                    </a>\n                </li>\n                <li>\n                    <a class="action-button" href="')
        # SOURCE LINE 40
        __M_writer(unicode(h.url_for( controller='workflow', action='import_workflow' )))
        __M_writer(u'">\n                        <img src="')
        # SOURCE LINE 41
        __M_writer(unicode(h.url_for('/static/images/fugue/arrow-090.png')))
        __M_writer(u'" />\n                        <span>Upload or import workflow</span>\n                    </a>\n                </li>\n            </ul>\n\n')
        # SOURCE LINE 47
        if workflows:
            # SOURCE LINE 48
            __M_writer(u'                <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" style="width:100%;">\n                    <tr class="header">\n                        <th>Name</th>\n                        <th># of Steps</th>\n')
            # SOURCE LINE 53
            __M_writer(u'                        <th></th>\n                    </tr>\n')
            # SOURCE LINE 55
            for i, workflow in enumerate( workflows ):
                # SOURCE LINE 56
                __M_writer(u'                        <tr>\n                            <td>\n                                <div class="menubutton" style="float: left;" id="wf-')
                # SOURCE LINE 58
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                ')
                # SOURCE LINE 59
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'\n                                </div>\n                            </td>\n                            <td>')
                # SOURCE LINE 62
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n')
                # SOURCE LINE 64
                __M_writer(u'                            <td>\n                                <div popupmenu="wf-')
                # SOURCE LINE 65
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                <a class="action-button" href="')
                # SOURCE LINE 66
                __M_writer(unicode(h.url_for( controller='workflow', action='editor', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'" target="_parent">Edit</a>\n                                <a class="action-button" href="')
                # SOURCE LINE 67
                __M_writer(unicode(h.url_for( controller='root', action='index', workflow_id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'" target="_parent">Run</a>\n                                <a class="action-button" href="')
                # SOURCE LINE 68
                __M_writer(unicode(h.url_for( controller='workflow', action='sharing', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Share or Publish</a>\n                                <a class="action-button" href="')
                # SOURCE LINE 69
                __M_writer(unicode(h.url_for( controller='workflow', action='export', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Download or Export</a>\n                                <a class="action-button" href="')
                # SOURCE LINE 70
                __M_writer(unicode(h.url_for( controller='workflow', action='copy', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Copy</a>\n                                <a class="action-button" href="')
                # SOURCE LINE 71
                __M_writer(unicode(h.url_for( controller='workflow', action='rename', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Rename</a>\n                                <a class="action-button" href="')
                # SOURCE LINE 72
                __M_writer(unicode(h.url_for( controller='workflow', action='display_by_id', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'" target="_top">View</a>\n                                <a class="action-button" confirm="Are you sure you want to delete workflow \'')
                # SOURCE LINE 73
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'\'?" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='delete', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Delete</a>\n                                </div>\n                            </td>\n                        </tr>\n')
                pass
            # SOURCE LINE 78
            __M_writer(u'                </table>\n')
            # SOURCE LINE 79
        else:
            # SOURCE LINE 80
            __M_writer(u'                You have no workflows.\n')
            pass
        # SOURCE LINE 82
        __M_writer(u'\n            <h2>Workflows shared with you by others</h2>\n\n')
        # SOURCE LINE 85
        if shared_by_others:
            # SOURCE LINE 86
            __M_writer(u'                <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n                    <tr class="header">\n                        <th>Name</th>\n                        <th>Owner</th>\n                        <th># of Steps</th>\n                        <th></th>\n                    </tr>\n')
            # SOURCE LINE 93
            for i, association in enumerate( shared_by_others ):
                # SOURCE LINE 94
                __M_writer(u'                        ')
                workflow = association.stored_workflow 
                
                __M_writer(u'\n                        <tr>\n                            <td>\n                                <a class="menubutton" id="shared-')
                # SOURCE LINE 97
                __M_writer(unicode(i))
                __M_writer(u'-popup" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id(workflow.id) )))
                __M_writer(u'">')
                __M_writer(unicode(h.to_unicode( workflow.name )))
                __M_writer(u'</a>\n                            </td>\n                            <td>')
                # SOURCE LINE 99
                __M_writer(unicode(workflow.user.email))
                __M_writer(u'</td>\n                            <td>')
                # SOURCE LINE 100
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n                            <td>\n                                <div popupmenu="shared-')
                # SOURCE LINE 102
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                    <a class="action-button" href="')
                # SOURCE LINE 103
                __M_writer(unicode(h.url_for( controller='workflow', action='display_by_username_and_slug', username=workflow.user.username, slug=workflow.slug )))
                __M_writer(u'" target="_top">View</a>\n                                    <a class="action-button" href="')
                # SOURCE LINE 104
                __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Run</a>\n                                    <a class="action-button" href="')
                # SOURCE LINE 105
                __M_writer(unicode(h.url_for( controller='workflow', action='copy', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Copy</a>\n                                    <a class="action-button" confirm="Are you sure you want to remove the shared workflow \'')
                # SOURCE LINE 106
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'\'?" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='sharing', unshare_me=True, id=trans.security.encode_id( workflow.id ))))
                __M_writer(u'">Remove</a>\n                                </div>\n                            </td>\n                        </tr>\n')
                pass
            # SOURCE LINE 111
            __M_writer(u'                </table>\n')
            # SOURCE LINE 112
        else:
            # SOURCE LINE 113
            __M_writer(u'                No workflows have been shared with you.\n')
            pass
        # SOURCE LINE 115
        __M_writer(u'\n            <h2>Other options</h2>\n\n            <a class="action-button" href="')
        # SOURCE LINE 118
        __M_writer(unicode(h.url_for( controller='workflow', action='configure_menu' )))
        __M_writer(u'">\n                <span>Configure your workflow menu</span>\n            </a>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'Workflow home')
        return ''
    finally:
        context.caller_stack._pop_frame()


