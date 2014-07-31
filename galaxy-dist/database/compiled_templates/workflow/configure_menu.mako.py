# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404321848.113096
_template_filename='templates/webapps/galaxy/workflow/configure_menu.mako'
_template_uri='workflow/configure_menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['title']


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
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        ids_in_menu = context.get('ids_in_menu', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        util = context.get('util', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        message = context.get('message', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        if message:
            # SOURCE LINE 6

            try:
                messagetype
            except:
                messagetype = "done"
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['messagetype'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 11
            __M_writer(u'\n<p />\n<div class="')
            # SOURCE LINE 13
            __M_writer(unicode(messagetype))
            __M_writer(u'message">\n    ')
            # SOURCE LINE 14
            __M_writer(unicode(message))
            __M_writer(u'\n</div>\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\n<form action="')
        # SOURCE LINE 18
        __M_writer(unicode(h.url_for(controller='workflow', action='configure_menu')))
        __M_writer(u'" method="POST">\n\n<table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n    <tr class="header">\n        <th>Name</th>\n        <th>Owner</th>\n        <th># of Steps</th>\n')
        # SOURCE LINE 26
        __M_writer(u'        <th>Show in menu</th>\n    </tr>\n        \n')
        # SOURCE LINE 29
        if workflows:
            # SOURCE LINE 30
            __M_writer(u'\n')
            # SOURCE LINE 31
            for i, workflow in enumerate( workflows ):
                # SOURCE LINE 32
                __M_writer(u'            <tr>\n                <td>\n                    ')
                # SOURCE LINE 34
                __M_writer(unicode(util.unicodify( workflow.name )))
                __M_writer(u'\n                </td>\n                <td>You</td>\n                <td>')
                # SOURCE LINE 37
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n                <td>\n                    <input type="checkbox" name="workflow_ids" value="')
                # SOURCE LINE 39
                __M_writer(unicode(workflow.id))
                __M_writer(u'"\n')
                # SOURCE LINE 40
                if workflow.id in ids_in_menu:
                    # SOURCE LINE 41
                    __M_writer(u'                        checked\n')
                    pass
                # SOURCE LINE 43
                __M_writer(u'                    />\n                </td>\n            </tr>    \n')
                pass
            # SOURCE LINE 47
            __M_writer(u'\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'\n')
        # SOURCE LINE 50
        if shared_by_others:
            # SOURCE LINE 51
            __M_writer(u'\n')
            # SOURCE LINE 52
            for i, association in enumerate( shared_by_others ):
                # SOURCE LINE 53
                __M_writer(u'            ')
                workflow = association.stored_workflow 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['workflow'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n            <tr>\n                <td>\n                    ')
                # SOURCE LINE 56
                __M_writer(unicode(util.unicodify( workflow.name )))
                __M_writer(u'\n                </td>\n                <td>')
                # SOURCE LINE 58
                __M_writer(unicode(workflow.user.email))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 59
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n                <td>\n                    <input type="checkbox" name="workflow_ids" value="')
                # SOURCE LINE 61
                __M_writer(unicode(workflow.id))
                __M_writer(u'"\n')
                # SOURCE LINE 62
                if workflow.id in ids_in_menu:
                    # SOURCE LINE 63
                    __M_writer(u'                        checked\n')
                    pass
                # SOURCE LINE 65
                __M_writer(u'                    />\n                </td>\n            </tr>    \n')
                pass
            # SOURCE LINE 69
            __M_writer(u'\n')
            pass
        # SOURCE LINE 71
        __M_writer(u'\n</table>\n\n<p />\n<input type="Submit" />\n\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Configure workflow menu')
        return ''
    finally:
        context.caller_stack._pop_frame()


