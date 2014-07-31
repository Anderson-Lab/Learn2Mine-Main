# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402425443.876375
_template_filename='templates/webapps/galaxy/user/api_keys.mako'
_template_uri='webapps/galaxy/user/api_keys.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x1092bbe50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1092bbe50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1092bbe50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n<br/><br/>\n<ul class="manage-table-actions">\n    <li>\n        <a class="action-button"  href="')
        # SOURCE LINE 7
        __M_writer(unicode(h.url_for( controller='user', action='index', cntrller=cntrller )))
        __M_writer(u'">User preferences</a>\n    </li>\n</ul>\n\n')
        # SOURCE LINE 11
        if message:
            # SOURCE LINE 12
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Web API Key</div>\n    <div class="toolFormBody">\n        <form name="user_api_keys" id="user_api_keys" action="')
        # SOURCE LINE 18
        __M_writer(unicode(h.url_for( controller='user', action='api_keys', cntrller=cntrller )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Current API key:</label>\n')
        # SOURCE LINE 21
        if user.api_keys:
            # SOURCE LINE 22
            __M_writer(u'                    ')
            __M_writer(unicode(user.api_keys[0].key))
            __M_writer(u'\n')
            # SOURCE LINE 23
        else:
            # SOURCE LINE 24
            __M_writer(u'                    none set\n')
            pass
        # SOURCE LINE 26
        __M_writer(u'            </div>\n            <div class="form-row">\n                <input type="submit" name="new_api_key_button" value="Generate a new key now"/>\n')
        # SOURCE LINE 29
        if user.api_keys:
            # SOURCE LINE 30
            __M_writer(u'                    (invalidates old key)\n')
            pass
        # SOURCE LINE 32
        __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    ')
        # SOURCE LINE 33

        if trans.webapp.name == 'galaxy':
            webapp_str = 'Galaxy'
        else:
            webapp_str = 'the Tool Shed'
                            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['webapp_str'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 38
        __M_writer(u'\n                    An API key will allow you to access ')
        # SOURCE LINE 39
        __M_writer(unicode(webapp_str))
        __M_writer(u' via its web API.  Please note that <strong>this key acts as an alternate means \n                    to access your account and should be treated with the same care as your login password</strong>.\n                </div>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


