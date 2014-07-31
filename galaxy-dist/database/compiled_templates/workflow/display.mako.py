# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404329585.862642
_template_filename='templates/webapps/galaxy/workflow/display.mako'
_template_uri='workflow/display.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'render_item', 'do_inputs', 'render_item_links', 'row_for_param']


# SOURCE LINE 4

from galaxy.tools.parameters import DataToolParameter, RuntimeValue
from galaxy.web import form_builder


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x109773ed0', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x109773ed0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/display_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x109773ed0')._populate(_import_ns, [u'render_message'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 77
        __M_writer(u'\n\n')
        # SOURCE LINE 122
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x109773ed0')._populate(_import_ns, [u'render_message'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n    ')
        # SOURCE LINE 10
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,workflow,steps):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x109773ed0')._populate(_import_ns, [u'render_message'])
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def do_inputs(inputs,values,prefix,step,other_values=None):
            return render_do_inputs(context,inputs,values,prefix,step,other_values)
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n    ')
        # SOURCE LINE 80

        # HACK: Rendering workflow steps requires that trans have a history; however, if it's  user's first visit to Galaxy is here, he won't have a history
        # and an error will occur. To prevent this error, make sure user has a history. 
        trans.get_history( create=True ) 
            
        
        # SOURCE LINE 84
        __M_writer(u'\n    <table class="annotated-item">\n        <tr><th>Step</th><th class="annotation">Annotation</th></tr>\n')
        # SOURCE LINE 87
        for i, step in enumerate( steps ):
            # SOURCE LINE 88
            __M_writer(u'            <tr><td>\n')
            # SOURCE LINE 89
            if step.type == 'tool' or step.type is None:
                # SOURCE LINE 90
                __M_writer(u'              ')
 
                tool = trans.app.toolbox.get_tool( step.tool_id )
                              
                
                # SOURCE LINE 92
                __M_writer(u'\n              <div class="toolForm">\n')
                # SOURCE LINE 94
                if tool:
                    # SOURCE LINE 95
                    __M_writer(u'                  <div class="toolFormTitle">Step ')
                    __M_writer(unicode(int(step.order_index)+1))
                    __M_writer(u': ')
                    __M_writer(unicode(tool.name))
                    __M_writer(u'</div>\n                  <div class="toolFormBody">\n                    ')
                    # SOURCE LINE 97
                    __M_writer(unicode(do_inputs( tool.inputs, step.state.inputs, "", step )))
                    __M_writer(u'\n                  </div>\n')
                    # SOURCE LINE 99
                else:
                    # SOURCE LINE 100
                    __M_writer(u'                  <div class="toolFormTitle">Step ')
                    __M_writer(unicode(int(step.order_index)+1))
                    __M_writer(u": Unknown Tool with id '")
                    __M_writer(unicode(step.tool_id))
                    __M_writer(u"'</div>\n")
                    pass
                # SOURCE LINE 102
                __M_writer(u'              </div>\n')
                # SOURCE LINE 103
            else:
                # SOURCE LINE 105
                __M_writer(u'            ')
                module = step.module 
                
                __M_writer(u'\n              <div class="toolForm">\n                  <div class="toolFormTitle">Step ')
                # SOURCE LINE 107
                __M_writer(unicode(int(step.order_index)+1))
                __M_writer(u': ')
                __M_writer(unicode(module.name))
                __M_writer(u'</div>\n                  <div class="toolFormBody">\n                    ')
                # SOURCE LINE 109
                __M_writer(unicode(do_inputs( module.get_runtime_inputs(), step.state.inputs, "", step )))
                __M_writer(u'\n                  </div>\n              </div>\n')
                pass
            # SOURCE LINE 113
            __M_writer(u'            </td>\n            <td class="annotation">\n')
            # SOURCE LINE 115
            if hasattr( step, "annotation") and step.annotation is not None:
                # SOURCE LINE 116
                __M_writer(u'                    ')
                __M_writer(unicode(step.annotation))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 118
            __M_writer(u'            </td>\n            </tr>\n')
            pass
        # SOURCE LINE 121
        __M_writer(u'    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,values,prefix,step,other_values=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x109773ed0')._populate(_import_ns, [u'render_message'])
        def row_for_param(param,value,other_values,prefix,step):
            return render_row_for_param(context,param,value,other_values,prefix,step)
        def do_inputs(inputs,values,prefix,step,other_values=None):
            return render_do_inputs(context,inputs,values,prefix,step,other_values)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        for input_index, input in enumerate( inputs.itervalues() ):
            # SOURCE LINE 15
            if input.type == "repeat":
                # SOURCE LINE 16
                __M_writer(u'      <div class="repeat-group">\n          <div class="form-title-row"><b>')
                # SOURCE LINE 17
                __M_writer(unicode(input.title_plural))
                __M_writer(u'</b></div>\n          ')
                # SOURCE LINE 18
                repeat_values = values[input.name] 
                
                __M_writer(u'\n')
                # SOURCE LINE 19
                for i in range( len( repeat_values ) ):
                    # SOURCE LINE 20
                    __M_writer(u'            <div class="repeat-group-item">\n                ')
                    # SOURCE LINE 21
                    index = repeat_values[i]['__index__'] 
                    
                    __M_writer(u'\n                <div class="form-title-row"><b>')
                    # SOURCE LINE 22
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</b></div>\n                ')
                    # SOURCE LINE 23
                    __M_writer(unicode(do_inputs( input.inputs, repeat_values[ i ], prefix + input.name + "_" + str(index) + "|", step, other_values )))
                    __M_writer(u'\n            </div> \n')
                    pass
                # SOURCE LINE 26
                __M_writer(u'      </div>\n')
                # SOURCE LINE 27
            elif input.type == "conditional":
                # SOURCE LINE 28
                __M_writer(u'      ')
                group_values = values[input.name] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 29
                current_case = group_values['__current_case__'] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 30
                new_prefix = prefix + input.name + "|" 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 31
                __M_writer(unicode(row_for_param( input.test_param, group_values[ input.test_param.name ], other_values, prefix, step )))
                __M_writer(u'\n      ')
                # SOURCE LINE 32
                __M_writer(unicode(do_inputs( input.cases[ current_case ].inputs, group_values, new_prefix, step, other_values )))
                __M_writer(u'\n')
                # SOURCE LINE 33
            else:
                # SOURCE LINE 34
                __M_writer(u'      ')
                __M_writer(unicode(row_for_param( input, values[ input.name ], other_values, prefix, step )))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,workflow):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x109773ed0')._populate(_import_ns, [u'render_message'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 66
        __M_writer(u'\n')
        # SOURCE LINE 67
        if workflow.importable:
            # SOURCE LINE 68
            __M_writer(u'    <a\n        href="')
            # SOURCE LINE 69
            __M_writer(unicode(h.url_for( controller='/workflow', action='imp', id=trans.security.encode_id(workflow.id) )))
            __M_writer(u'"\n        class="icon-button import"\n        title="Import workflow"></a>\n    <a\n        href="')
            # SOURCE LINE 73
            __M_writer(unicode(h.url_for( controller='/workflow', action='export_to_file', id=trans.security.encode_id(workflow.id) )))
            __M_writer(u'"\n        class="icon-button disk"\n        title="Save workflow"></a>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,param,value,other_values,prefix,step):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x109773ed0')._populate(_import_ns, [u'render_message'])
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        list = _import_ns.get('list', context.get('list', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        render_message = _import_ns.get('render_message', context.get('render_message', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n    ')
        # SOURCE LINE 40
        cls = "form-row" 
        
        __M_writer(u'\n    <div class="')
        # SOURCE LINE 41
        __M_writer(unicode(cls))
        __M_writer(u'">\n        <label>')
        # SOURCE LINE 42
        __M_writer(unicode(param.get_label()))
        __M_writer(u'</label>\n        <div>\n')
        # SOURCE LINE 44
        if isinstance( param, DataToolParameter ):
            # SOURCE LINE 45
            if ( prefix + param.name ) in step.input_connections_by_name:
                # SOURCE LINE 46
                __M_writer(u'                    ')

                conns = step.input_connections_by_name[ prefix + param.name ]
                if not isinstance(conns, list):
                    conns = [conns]
                vals = ["Output dataset '%s' from step %d" % (conn.output_name, int(conn.output_step.order_index)+1) for conn in conns]
                                    
                
                # SOURCE LINE 51
                __M_writer(u'\n                    ')
                # SOURCE LINE 52
                __M_writer(unicode(",".join(vals)))
                __M_writer(u'\n')
                # SOURCE LINE 53
            else:
                # SOURCE LINE 54
                __M_writer(u'                    <i>select at runtime</i>\n')
                pass
            # SOURCE LINE 56
        else:
            # SOURCE LINE 57
            __M_writer(u'                ')
            __M_writer(unicode(param.value_to_display_text( value, app )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 59
        __M_writer(u'        </div>\n')
        # SOURCE LINE 60
        if hasattr( step, 'upgrade_messages' ) and step.upgrade_messages and param.name in step.upgrade_messages:
            # SOURCE LINE 61
            __M_writer(u'            ')
            __M_writer(unicode(render_message( step.upgrade_messages[param.name], "info" )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 63
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


