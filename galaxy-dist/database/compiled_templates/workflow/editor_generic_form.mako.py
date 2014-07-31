# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404256372.442218
_template_filename='templates/webapps/galaxy/workflow/editor_generic_form.mako'
_template_uri='workflow/editor_generic_form.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        module = context.get('module', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<form name="')
        __M_writer(unicode(form.name))
        __M_writer(u'" action="')
        __M_writer(unicode(h.url_for( controller='workflow', action='editor_form_post' )))
        __M_writer(u'" method="post">\n    <div class="toolForm">\n        <div class="toolFormTitle">')
        # SOURCE LINE 3
        __M_writer(unicode(form.title))
        __M_writer(u'</div>\n        <div class="toolFormBody">\n            <input type="hidden" name="type" value="')
        # SOURCE LINE 5
        __M_writer(unicode(module.type))
        __M_writer(u'" />\n')
        # SOURCE LINE 6
        if form.inputs:
            # SOURCE LINE 7
            for input in form.inputs:
                # SOURCE LINE 8
                __M_writer(u'                  ')

                cls = "form-row"
                if input.error:
                    cls += " form-row-error"
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cls'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 12
                __M_writer(u'\n                  <div class="')
                # SOURCE LINE 13
                __M_writer(unicode(cls))
                __M_writer(u'">\n                    <label>\n                        ')
                # SOURCE LINE 15
                __M_writer(unicode(input.label))
                __M_writer(u':\n                    </label>\n                    <div style="float: left; width: 250px; margin-right: 10px;">\n                        <input type="')
                # SOURCE LINE 18
                __M_writer(unicode(input.type))
                __M_writer(u'" name="')
                __M_writer(filters.html_escape(unicode(input.name )))
                __M_writer(u'" value="')
                __M_writer(filters.html_escape(unicode(input.value )))
                __M_writer(u'" size="30">\n                    </div>\n')
                # SOURCE LINE 20
                if input.error:
                    # SOURCE LINE 21
                    __M_writer(u'                    <div style="float: left; color: red; font-weight: bold; padding-top: 1px; padding-bottom: 3px;">\n                        <div style="width: 300px;"><img style="vertical-align: middle;" src="')
                    # SOURCE LINE 22
                    __M_writer(unicode(h.url_for('/static/style/error_small.png')))
                    __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
                    __M_writer(unicode(input.error))
                    __M_writer(u'</span></div>\n                    </div>\n')
                    pass
                # SOURCE LINE 25
                __M_writer(u'  \n')
                # SOURCE LINE 26
                if input.help:
                    # SOURCE LINE 27
                    __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        ')
                    # SOURCE LINE 28
                    __M_writer(unicode(input.help))
                    __M_writer(u'\n                    </div>\n')
                    pass
                # SOURCE LINE 31
                __M_writer(u'  \n                    <div style="clear: both"></div>\n  \n                  </div>\n')
                pass
            # SOURCE LINE 36
        else:
            # SOURCE LINE 37
            __M_writer(u'              <div class="form-row"><i>No options</i></div>\n')
            pass
        # SOURCE LINE 39
        __M_writer(u'            </table>\n        </div>\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


