# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404321368.481781
_template_filename='templates/webapps/galaxy/workflow/export.mako'
_template_uri='/workflow/export.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'render_export_to_myexp', 'center_panel', 'render_more']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x1095251d0', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1095251d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/export_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095251d0')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095251d0')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style>\n        .toolForm {\n            max-width: 350px;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095251d0')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6

        parent.init()
        self.active_view="workflow"
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_export_to_myexp(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095251d0')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'    <h3>Export to myExperiment</h3>\n    \n    <div class="toolForm"> \n        <form action="')
        # SOURCE LINE 28
        __M_writer(unicode(h.url_for(controller='workflow', action='export_to_myexp', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'" \n                method="POST">\n            <div class="form-row"> \n                <label>myExperiment username:</label> \n                <input type="text" name="myexp_username" value="" size="40"/> \n            </div> \n            <div class="form-row"> \n                <label>myExperiment password:</label> \n                <input type="password" name="myexp_password" value="" size="40"/> \n            </div> \n            <div class="form-row"> \n                <input type="submit" value="Export"/> \n            </div> \n        </form> \n    </div>    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095251d0')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n    ')
        # SOURCE LINE 58
        __M_writer(unicode(parent.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_more(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095251d0')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n')
        # SOURCE LINE 47
        __M_writer(u'    ')
        __M_writer(unicode(self.render_export_to_myexp(item)))
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        __M_writer(u'    <h3>Create Image</h3>\n    \n    <a href="')
        # SOURCE LINE 52
        __M_writer(unicode(h.url_for(controller='workflow', action='gen_image', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'">\n        Create image of ')
        # SOURCE LINE 53
        __M_writer(unicode(get_class_display_name( item.__class__ ).lower()))
        __M_writer(u' in SVG format\n    </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


