# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405607118.244941
_template_filename='templates/webapps/galaxy/workflow/run_complete.mako'
_template_uri='workflow/run_complete.mako'
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
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        util = context.get('util', UNDEFINED)
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        invocations = context.get('invocations', UNDEFINED)
        workflow = context.get('workflow', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<div class="donemessagelarge">\n    Successfully ran workflow "')
        # SOURCE LINE 4
        __M_writer(unicode(util.unicodify( workflow.name )))
        __M_writer(u'". The following datasets have been added to the queue:\n')
        # SOURCE LINE 5
        for invocation in invocations:
            # SOURCE LINE 6
            __M_writer(u'        <div class="workflow-invocation-complete">\n')
            # SOURCE LINE 7
            if invocation['new_history']:
                # SOURCE LINE 8
                __M_writer(u'                <p>These datasets will appear in a new history:\n                <a target=\'galaxy_history\' href="')
                # SOURCE LINE 9
                __M_writer(unicode(h.url_for( controller='history', action='list', operation="Switch", id=trans.security.encode_id(invocation['new_history'].id), use_panels=False, show_deleted=False )))
                __M_writer(u'">\n                    \'')
                # SOURCE LINE 10
                __M_writer(unicode(h.to_unicode(invocation['new_history'].name)))
                __M_writer(u"'.\n                </a></p>\n")
                pass
            # SOURCE LINE 13
            __M_writer(u'            <div style="padding-left: 10px;">\n')
            # SOURCE LINE 14
            for step_outputs in invocation['outputs'].itervalues():
                # SOURCE LINE 15
                for data in step_outputs.itervalues():
                    # SOURCE LINE 16
                    if not invocation['new_history'] or data.history == invocation['new_history']:
                        # SOURCE LINE 17
                        __M_writer(u'                            <p><strong>')
                        __M_writer(unicode(data.hid))
                        __M_writer(u'</strong>: ')
                        __M_writer(unicode(util.unicodify( data.name )))
                        __M_writer(u'</p>\n')
                        pass
                    pass
                pass
            # SOURCE LINE 21
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 24
        __M_writer(u'</div>\n\n<script type="text/javascript">\n    if( top.Galaxy && top.Galaxy.currHistoryPanel ){\n        top.Galaxy.currHistoryPanel.refreshHdas();\n    }\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


