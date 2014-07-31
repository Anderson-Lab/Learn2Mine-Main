# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405696446.913996
_template_filename='templates/ind_share_base.mako'
_template_uri='/ind_share_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'body', 'init', 'center_panel']


# SOURCE LINE 5

def inherit(context):
    if context.get('use_panels'):
        if context.get('webapp'):
            webapp = context.get('webapp')
        else:
            webapp = 'galaxy'
        return '/webapps/%s/base_panels.mako' % webapp
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 18
    ns = runtime.TemplateNamespace('__anon_0x10a042f90', context._clean_inheritance_tokens(), templateuri=u'./display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x10a042f90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x10a042f90')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n    \n')
        # SOURCE LINE 52
        __M_writer(u'\n\n')
        # SOURCE LINE 109
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x10a042f90')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n    ')
        # SOURCE LINE 37
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style>\n')
        # SOURCE LINE 40
        if context.get('use_panels'):
            # SOURCE LINE 41
            __M_writer(u'        div#center\n        {\n            padding: 10px;\n        }\n')
            pass
        # SOURCE LINE 46
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x10a042f90')._populate(_import_ns, [u'*'])
        get_class_plural_display_name = _import_ns.get('get_class_plural_display_name', context.get('get_class_plural_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        messagetype = _import_ns.get('messagetype', context.get('messagetype', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        email = _import_ns.get('email', context.get('email', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\n')
        # SOURCE LINE 55
        if message:
            # SOURCE LINE 56
            __M_writer(u'    ')

            if messagetype is UNDEFINED:
                mt = "done"
            else:
                mt = messagetype
            
            
            # SOURCE LINE 61
            __M_writer(u'\n    <p />\n    <div class="')
            # SOURCE LINE 63
            __M_writer(unicode(mt))
            __M_writer(u'message">\n        ')
            # SOURCE LINE 64
            __M_writer(unicode(message))
            __M_writer(u'\n    </div>\n    <p />\n')
            pass
        # SOURCE LINE 68
        __M_writer(u'    \n    ')
        # SOURCE LINE 69

        #
        # Setup and variables needed for page.
        #
    
        # Get class name strings.
        item_class_name = get_class_display_name( item.__class__ ) 
        item_class_name_lc = item_class_name.lower()
        item_class_plural_name = get_class_plural_display_name( item.__class__ )
        item_class_plural_name_lc = item_class_plural_name.lower()
        item_controller = get_controller_name(item)
        
        # Get item name.
        item_name = get_item_name(item)
            
        
        # SOURCE LINE 83
        __M_writer(u'\n    \n    <div class="toolForm">\n        <div class="toolFormTitle">Share ')
        # SOURCE LINE 86
        __M_writer(unicode(item_class_name))
        __M_writer(u" '")
        __M_writer(unicode(item_name))
        __M_writer(u'\' with Another User</div>\n            <div class="toolFormBody">\n                <form action="')
        # SOURCE LINE 88
        __M_writer(unicode(h.url_for(controller=item_controller, action='share', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'" method="POST">\n                    <div class="form-row">\n                        <label>\n                            Email address of user to share with\n                        </label>\n                        <div style="float: left; width: 250px; margin-right: 10px;">\n                            <input type="text" name="email" value="')
        # SOURCE LINE 94
        __M_writer(unicode(email))
        __M_writer(u'" size="40">\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n                    <div class="form-row">\n                        <input type="submit" value="Share"></input>\n                    </div>\n                    <div class="form-row">\n                        <a href="')
        # SOURCE LINE 102
        __M_writer(unicode(h.url_for(controller=item_controller, action="sharing", id=trans.security.encode_id( item.id ) )))
        __M_writer(u'">Back to ')
        __M_writer(unicode(item_class_name))
        __M_writer(u"'s Sharing Home</a>\n                    </div>\n                    \n                </form>\n            </div>\n        </div>\n    </div>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x10a042f90')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.overlay_visible=False
        self.message_box_class=""
        self.active_view=""
        self.body_class=""
        
        
        # SOURCE LINE 33
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x10a042f90')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n    ')
        # SOURCE LINE 51
        __M_writer(unicode(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


