# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405709939.160375
_template_filename='templates/webapps/galaxy/galaxy.panels.mako'
_template_uri='galaxy.panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['javascripts', 'late_javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace(u'masthead', context._clean_inheritance_tokens(), templateuri=u'/webapps/galaxy/galaxy.masthead.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'masthead')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        config = context.get('config', UNDEFINED)
        masthead = _mako_get_namespace(context, 'masthead')
        __M_writer = context.writer()
        __M_writer(u'\n\n<!DOCTYPE HTML>\n\n')
        # SOURCE LINE 6

    ## set defaults
        self.galaxy_config = {
            ## template options
            'title'         : '',
            'master'        : True,
            'left_panel'    : False,
            'right_panel'   : False,
            'message_box'   : False,
            
            ## root
            'root'          : h.url_for("/"),
            
            ## inject app specific configuration
            'app'           : config['app']
        }
        
        ## update configuration
        self.galaxy_config.update(config)
        
        
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 128
        __M_writer(u'\n\n')
        # SOURCE LINE 151
        __M_writer(u'\n\n')
        # SOURCE LINE 154
        __M_writer(u'<html>\n    <head>\n        <title></title>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        \n')
        # SOURCE LINE 160
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n        \n')
        # SOURCE LINE 163
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n \n')
        # SOURCE LINE 166
        __M_writer(u'        ')
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n    </head>\n    \n    <body scroll="no" class="full-content">\n        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n')
        # SOURCE LINE 172
        __M_writer(u'            <div id="background"></div>\n            \n')
        # SOURCE LINE 175
        if self.galaxy_config['master']:
            # SOURCE LINE 176
            __M_writer(u'                ')
            __M_writer(unicode(masthead.load()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 178
        __M_writer(u'            \n')
        # SOURCE LINE 180
        if self.galaxy_config['message_box']:
            # SOURCE LINE 181
            __M_writer(u'                <div id="messagebox" class="panel-message"></div>\n')
            pass
        # SOURCE LINE 184
        if self.galaxy_config['left_panel']:
            # SOURCE LINE 185
            __M_writer(u'                <div id="left">\n                    <div class="unified-panel-header" unselectable="on">\n                        <div class="unified-panel-header-inner">\n                            <div class="unified-panel-icons" style="float: right"></div>\n                            <div class="unified-panel-title"></div>\n                        </div>\n                    </div>\n                    <div class="unified-panel-body" style="overflow: auto;"></div>\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse right"></span></div>\n                        <div class="drag"></div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 199
        __M_writer(u'            \n')
        # SOURCE LINE 201
        __M_writer(u'            <div id="center">\n                <div class="unified-panel-header" unselectable="on">\n                    <div class="unified-panel-header-inner">\n                        <div class="unified-panel-title" style="float:left;"></div>\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n                <div class="unified-panel-body"></div>\n            </div>\n            \n')
        # SOURCE LINE 212
        if self.galaxy_config['right_panel']:
            # SOURCE LINE 213
            __M_writer(u'                <div id="right">\n                    <div class="unified-panel-header" unselectable="on">\n                        <div class="unified-panel-header-inner">\n                            <div class="unified-panel-icons" style="float: right"></div>\n                            <div class="unified-panel-title"></div>\n                        </div>\n                    </div>\n                    <div class="unified-panel-body" style="overflow: auto;"></div>\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse right"></span></div>\n                        <div class="drag"></div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 227
        __M_writer(u'        </div>\n    </body>\n')
        # SOURCE LINE 231
        __M_writer(u'    ')
        __M_writer(unicode(self.late_javascripts()))
        __M_writer(u'\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'    ')
        __M_writer(unicode(h.js(
        'libs/jquery/jquery',
        'libs/jquery/jquery-ui',
        'libs/bootstrap',
        'libs/underscore',
        'libs/backbone/backbone',
        'libs/require',
        'libs/d3',
        'galaxy.base',
        'galaxy.panels',
        'libs/handlebars.runtime'
    )))
        # SOURCE LINE 41
        __M_writer(u'\n\n    ')
        # SOURCE LINE 43
        __M_writer(unicode(h.js(
        "mvc/ui"
    )))
        # SOURCE LINE 45
        __M_writer(u'\n    \n')
        # SOURCE LINE 48
        if app.config.sentry_dsn:
            # SOURCE LINE 49
            __M_writer(u'        ')
            __M_writer(unicode(h.js( "libs/tracekit", "libs/raven" )))
            __M_writer(u"\n        <script>\n            Raven.config('")
            # SOURCE LINE 51
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            # SOURCE LINE 52
            if trans.user:
                # SOURCE LINE 53
                __M_writer(u'                Raven.setUser( { email: "')
                __M_writer(unicode(trans.user.email))
                __M_writer(u'" } );\n')
                pass
            # SOURCE LINE 55
            __M_writer(u'        </script>\n')
            pass
        # SOURCE LINE 57
        __M_writer(u'    \n')
        # SOURCE LINE 59
        __M_writer(u'    <script type="text/javascript">\n        // start a Galaxy namespace for objects created\n        window.Galaxy = window.Galaxy || {};\n\n        // console protection\n        window.console = window.console ||\n        {\n            log     : function(){},\n            debug   : function(){},\n            info    : function(){},\n            warn    : function(){},\n            error   : function(){},\n            assert  : function(){}\n        };\n    </script>\n\n')
        # SOURCE LINE 76
        __M_writer(u'    ')
        __M_writer(unicode(h.css("base")))
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'    <style type="text/css">\n    #center {\n')
        # SOURCE LINE 81
        if not self.galaxy_config['left_panel']:
            # SOURCE LINE 82
            __M_writer(u'            left: 0 !important;\n')
            pass
        # SOURCE LINE 84
        if not self.galaxy_config['right_panel']:
            # SOURCE LINE 85
            __M_writer(u'            right: 0 !important;\n')
            pass
        # SOURCE LINE 87
        __M_writer(u'    }\n')
        # SOURCE LINE 88
        if self.galaxy_config['message_box']:
            # SOURCE LINE 89
            __M_writer(u'        #left, #left-border, #center, #right-border, #right\n        {\n            top: 64px;\n        }\n')
            pass
        # SOURCE LINE 94
        __M_writer(u'    </style>\n    \n')
        # SOURCE LINE 97
        __M_writer(u'    <script type="text/javascript">\n')
        # SOURCE LINE 99
        __M_writer(u'        require.config({\n            baseUrl: "')
        # SOURCE LINE 100
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": { exports: "_" },\n                "libs/d3": { exports: "d3" },\n                "libs/backbone/backbone": { exports: "Backbone" },\n            }\n        });\n\n')
        # SOURCE LINE 109
        __M_writer(u'        var galaxy_config = ')
        __M_writer(unicode( h.to_json_string( self.galaxy_config ) ))
        __M_writer(u';\n\n')
        # SOURCE LINE 112
        __M_writer(u'        $(function()\n        {\n')
        # SOURCE LINE 115
        __M_writer(u'            var jscript = galaxy_config.app.jscript;\n            if (jscript)\n            {\n')
        # SOURCE LINE 119
        __M_writer(u'                require([jscript], function(js_lib)\n                {\n')
        # SOURCE LINE 122
        __M_writer(u'                    var module = new js_lib.GalaxyApp();\n                });\n            } else\n                console.log("\'galaxy_config.app.jscript\' missing.");\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 131
        __M_writer(u'\n')
        # SOURCE LINE 134
        __M_writer(u'    <script type="text/javascript">\n        \n        ensure_dd_helper();\n        \n')
        # SOURCE LINE 139
        if self.galaxy_config['left_panel']:
            # SOURCE LINE 140
            __M_writer(u'            var lp = new Panel( { panel: $("#left"), center: $("#center"), drag: $("#left > .unified-panel-footer > .drag" ), toggle: $("#left > .unified-panel-footer > .panel-collapse" ) } );\n            force_left_panel = function( x ) { lp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 143
        __M_writer(u'        \n')
        # SOURCE LINE 145
        if self.galaxy_config['right_panel']:
            # SOURCE LINE 146
            __M_writer(u'            var rp = new Panel( { panel: $("#right"), center: $("#center"), drag: $("#right > .unified-panel-footer > .drag" ), toggle: $("#right > .unified-panel-footer > .panel-collapse" ), right: true } );\n            window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };\n            force_right_panel = function( x ) { rp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 150
        __M_writer(u'    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


