# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404321452.140103
_template_filename='templates/webapps/galaxy/workflow/import.mako'
_template_uri='workflow/import.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x1095de8d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1095de8d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095de8d0')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 20
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095de8d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(unicode(h.css( "workflow" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095de8d0')._populate(_import_ns, [u'render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="workflow"
        self.message_box_visible=False
        
        
        # SOURCE LINE 19
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095de8d0')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n    ')
        # SOURCE LINE 10
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095de8d0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        myexperiment_target_url = _import_ns.get('myexperiment_target_url', context.get('myexperiment_target_url', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        if message:
            # SOURCE LINE 26
            __M_writer(u'        ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 28
        __M_writer(u'    <div class="toolForm"> \n        <div class="toolFormTitle">Import Galaxy workflow</div>\n        <div class="toolFormBody">\n            <form name="import_workflow" id="import_workflow" action="')
        # SOURCE LINE 31
        __M_writer(unicode(h.url_for( controller='workflow', action='import_workflow' )))
        __M_writer(u'" enctype="multipart/form-data" method="POST">\n                <div class="form-row">\n                    <label>Galaxy workflow URL:</label> \n                    <input type="text" name="url" value="')
        # SOURCE LINE 34
        __M_writer(filters.html_escape(unicode(url )))
        __M_writer(u'" size="40">\n                    <div class="toolParamHelp" style="clear: both;">\n                        If the workflow is accessible via a URL, enter the URL above and click <b>Import</b>.\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <label>Galaxy workflow file:</label>\n                    <div class="form-row-input">\n                        <input type="file" name="file_data"/>\n                    </div>\n                    <div class="toolParamHelp" style="clear: both;">\n                        If the workflow is in a file on your computer, choose it and then click <b>Import</b>.\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="form-row">\n                    <input type="submit" class="primary-button" name="import_button" value="Import">\n                </div>\n            </form>\n            <hr/>\n            <div class="form-row">\n                <label>Import a Galaxy workflow from myExperiment:</label>\n                <div class="form-row-input">\n                    <a href="')
        # SOURCE LINE 58
        __M_writer(unicode(h.url_for( myexperiment_target_url )))
        __M_writer(u'">\n                        Visit myExperiment\n                    </a>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    Click the link above to visit myExperiment and browse for Galaxy workflows.\n                </div>\n                <div style="clear: both"></div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1095de8d0')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'Import Galaxy workflow')
        return ''
    finally:
        context.caller_stack._pop_frame()


