# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404321368.562492
_template_filename=u'templates/export_base.mako'
_template_uri=u'/export_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'render_more', 'render_download_to_file', 'title', 'render_url_for_importing', 'center_panel', 'stylesheets', 'init', 'render_footer']


# SOURCE LINE 5

def inherit(context):
    if context.get('use_panels', False) == True:
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
    # SOURCE LINE 19
    ns = runtime.TemplateNamespace('__anon_0x1095a18d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1095a18d0')] = ns

    # SOURCE LINE 18
    ns = runtime.TemplateNamespace('__anon_0x109518d10', context._clean_inheritance_tokens(), templateuri=u'./display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x109518d10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'\n\n')
        # SOURCE LINE 87
        __M_writer(u'\n\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 103
        __M_writer(u'\n\n')
        # SOURCE LINE 118
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 105
        __M_writer(u'\n    ')
        # SOURCE LINE 106

        item_name = get_item_name(item)
            
        
        # SOURCE LINE 108
        __M_writer(u'\n    <h2>Download or Export ')
        # SOURCE LINE 109
        __M_writer(unicode(self.item_class_name))
        __M_writer(u" '")
        __M_writer(unicode(item_name))
        __M_writer(u"'</h2>\n    \n    ")
        # SOURCE LINE 111
        __M_writer(unicode(self.render_download_to_file(item)))
        __M_writer(u'\n    \n    ')
        # SOURCE LINE 113
        __M_writer(unicode(self.render_url_for_importing(item)))
        __M_writer(u'\n    \n    ')
        # SOURCE LINE 115
        __M_writer(unicode(self.render_more(item)))
        __M_writer(u'\n    \n    ')
        # SOURCE LINE 117
        __M_writer(unicode(self.render_footer()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_more(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_download_to_file(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 89
        __M_writer(u'\n    <h3>Download to File</h3>\n    \n    <a href="')
        # SOURCE LINE 92
        __M_writer(unicode(h.url_for(controller=self.controller, action='export_to_file', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'">\n        Download ')
        # SOURCE LINE 93
        __M_writer(unicode(get_class_display_name( item.__class__ ).lower()))
        __M_writer(u' to file so that it can be saved or imported into another Galaxy server.</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n    Export ')
        # SOURCE LINE 45
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u" '")
        __M_writer(unicode(get_item_name( item )))
        __M_writer(u"'\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_url_for_importing(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 75
        __M_writer(u'\n    <h3>URL for Importing to Another Galaxy</h3>\n    \n')
        # SOURCE LINE 78
        if item.importable:
            # SOURCE LINE 79
            __M_writer(u'        Use this URL to import the ')
            __M_writer(unicode(get_class_display_name( item.__class__ ).lower()))
            __M_writer(u' directly into another Galaxy server: \n        <div class="display-url">\n            ')
            # SOURCE LINE 81
            __M_writer(unicode(h.url_for(controller=self.controller, action='for_direct_import', id=trans.security.encode_id( item.id ), qualified=True )))
            __M_writer(u"\n        </div>\n        (Copy this URL into the box titled 'Workflow URL' in the Import Workflow page.)\n")
            # SOURCE LINE 84
        else:
            # SOURCE LINE 85
            __M_writer(u'        <a href="')
            __M_writer(unicode(h.url_for(controller=self.controller, action='sharing', id=trans.security.encode_id( item.id ) )))
            __M_writer(u'">This  ')
            __M_writer(unicode(get_class_display_name( item.__class__ ).lower()))
            __M_writer(u' must be accessible before it can be imported into another Galaxy.</a>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n    ')
        # SOURCE LINE 72
        __M_writer(unicode(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n    ')
        # SOURCE LINE 49
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style>\n')
        # SOURCE LINE 52
        __M_writer(u'        h3 {\n            margin-top: 1.5em;\n        }\n        input.action-button {\n            margin-left: 0;\n        }\n')
        # SOURCE LINE 59
        if context.get('use_panels'):
            # SOURCE LINE 60
            __M_writer(u'        div#center {\n            padding: 10px;\n        }\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'        .display-url {\n            margin: 0.5em 0em 0.5em 0.5em;\n            font-weight: bold;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_class_plural_display_name = _import_ns.get('get_class_plural_display_name', context.get('get_class_plural_display_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.overlay_visible=False
        self.message_box_class=""
        self.active_view=""
        self.body_class=""
        
        # Get class name strings.
        self.item_class_name = get_class_display_name( item.__class__ ) 
        self.item_class_name_lc = self.item_class_name.lower()
        self.item_class_plural_name = get_class_plural_display_name( item.__class__ )
        self.item_class_plural_name_lc = self.item_class_plural_name.lower()
        self.controller = get_controller_name(item)
        
        
        # SOURCE LINE 41
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_footer(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095a18d0')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x109518d10')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n    <p><br><br>\n    <a href="')
        # SOURCE LINE 102
        __M_writer(unicode(h.url_for(controller=self.controller, action="list" )))
        __M_writer(u'">Back to ')
        __M_writer(unicode(self.item_class_plural_name))
        __M_writer(u' List</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


