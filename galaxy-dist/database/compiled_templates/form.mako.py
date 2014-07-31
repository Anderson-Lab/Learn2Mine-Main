# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402424490.964311
_template_filename='templates/form.mako'
_template_uri='form.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts', 'render_form']


# SOURCE LINE 1

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
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        def render_form():
            return render_render_form(context)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n    ')
        # SOURCE LINE 47
        __M_writer(unicode(render_form( )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(unicode(form.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        def render_form():
            return render_render_form(context)
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n    ')
        # SOURCE LINE 43
        __M_writer(unicode(render_form( )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n    ')
        # SOURCE LINE 38
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 39
        __M_writer(unicode(h.css("autocomplete_tagging")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        active_view = context.get('active_view', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view=active_view
        self.message_box_visible=False
        
        
        # SOURCE LINE 21
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n    ')
        # SOURCE LINE 28
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 29
        __M_writer(unicode(h.js("libs/jquery/jquery.autocomplete")))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("input:text:first").focus();\n        })\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_form(context):
    context.caller_stack._push_frame()
    try:
        util = context.get('util', UNDEFINED)
        header = context.get('header', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        if header:
            # SOURCE LINE 52
            __M_writer(u'        ')
            __M_writer(unicode(header))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 54
        __M_writer(u'    \n    <div class="form" style="margin: 1em">\n        <div class="form-title">')
        # SOURCE LINE 56
        __M_writer(unicode(util.unicodify( form.title )))
        __M_writer(u'</div>\n        <div class="form-body">\n        ')
        # SOURCE LINE 58

        has_file_input = False
        for input in form.inputs:
            if input.type == 'file':
                has_file_input = True
                break
                
        
        # SOURCE LINE 64
        __M_writer(u'\n        <form name="')
        # SOURCE LINE 65
        __M_writer(unicode(form.name))
        __M_writer(u'" action="')
        __M_writer(unicode(form.action))
        __M_writer(u'" method="post" \n')
        # SOURCE LINE 66
        if has_file_input:
            # SOURCE LINE 67
            __M_writer(u'             enctype="multipart/form-data"\n')
            pass
        # SOURCE LINE 69
        __M_writer(u'        >\n')
        # SOURCE LINE 70
        for input in form.inputs:
            # SOURCE LINE 71
            __M_writer(u'                ')

            cls = "form-row"
            if input.error:
                cls += " form-row-error"
            
            
            # SOURCE LINE 75
            __M_writer(u'\n                <div class="')
            # SOURCE LINE 76
            __M_writer(unicode(cls))
            __M_writer(u'">\n')
            # SOURCE LINE 77
            if input.use_label:
                # SOURCE LINE 78
                __M_writer(u'                  <label>\n                      ')
                # SOURCE LINE 79
                __M_writer(unicode(_(input.label)))
                __M_writer(u':\n                  </label>\n')
                pass
            # SOURCE LINE 82
            __M_writer(u'                <div class="form-row-input">\n')
            # SOURCE LINE 83
            if input.type == 'textarea':
                # SOURCE LINE 84
                __M_writer(u'                        <textarea name="')
                __M_writer(unicode(input.name))
                __M_writer(u'">')
                __M_writer(unicode(input.value))
                __M_writer(u'</textarea>\n')
                # SOURCE LINE 85
            elif input.type == 'select':
                # SOURCE LINE 86
                __M_writer(u'                        <select name="')
                __M_writer(unicode(input.name))
                __M_writer(u'">\n')
                # SOURCE LINE 87
                for (name, value) in input.options:
                    # SOURCE LINE 88
                    __M_writer(u'                                <option value="')
                    __M_writer(unicode(value))
                    __M_writer(u'">')
                    __M_writer(unicode(name))
                    __M_writer(u'</option>\n')
                    pass
                # SOURCE LINE 90
                __M_writer(u'                        </select>\n')
                # SOURCE LINE 91
            else:
                # SOURCE LINE 92
                __M_writer(u'                        <input type="')
                __M_writer(unicode(input.type))
                __M_writer(u'" name="')
                __M_writer(unicode(input.name))
                __M_writer(u'" value="')
                __M_writer(unicode(input.value))
                __M_writer(u'">\n')
                pass
            # SOURCE LINE 94
            __M_writer(u'                </div>\n')
            # SOURCE LINE 95
            if input.error:
                # SOURCE LINE 96
                __M_writer(u'                    <div class="form-row-error-message">')
                __M_writer(unicode(input.error))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 98
            if input.help:
                # SOURCE LINE 99
                __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        ')
                # SOURCE LINE 100
                __M_writer(unicode(input.help))
                __M_writer(u'\n                    </div>\n')
                pass
            # SOURCE LINE 103
            __M_writer(u'                <div style="clear: both"></div>\n        </div>\n')
            pass
        # SOURCE LINE 106
        __M_writer(u'        <div class="form-row"><input type="submit" value="')
        __M_writer(unicode(form.submit_text))
        __M_writer(u'"></div>\n        </form>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


