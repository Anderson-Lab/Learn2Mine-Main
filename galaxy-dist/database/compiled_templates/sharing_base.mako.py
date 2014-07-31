# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404321424.694313
_template_filename=u'templates/sharing_base.mako'
_template_uri=u'/sharing_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts']


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
    ns = runtime.TemplateNamespace('__anon_0x1093c8f50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1093c8f50')] = ns

    # SOURCE LINE 18
    ns = runtime.TemplateNamespace('__anon_0x1093c8850', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1093c8850')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
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
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 271
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        get_class_plural_display_name = _import_ns.get('get_class_plural_display_name', context.get('get_class_plural_display_name', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n')
        # SOURCE LINE 102
        __M_writer(u'    ')
        use_panels = context.get('use_panels', False)  
        
        __M_writer(u'\n    ')
        # SOURCE LINE 103
        controller_name = get_controller_name( item ) 
        
        __M_writer(u'\n\n')
        # SOURCE LINE 106
        if message:
            # SOURCE LINE 107
            __M_writer(u'        ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 109
        __M_writer(u'\n    ')
        # SOURCE LINE 110

        #
        # Setup and variables needed for page.
        #
    
        # Get class name strings.
        item_class_name = get_class_display_name( item.__class__ ) 
        item_class_name_lc = item_class_name.lower()
        item_class_plural_name = get_class_plural_display_name( item.__class__ )
        item_class_plural_name_lc = item_class_plural_name.lower()
        
        # Get item name.
        item_name = get_item_name(item)
            
        
        # SOURCE LINE 123
        __M_writer(u'\n\n    <h2>Share or Publish ')
        # SOURCE LINE 125
        __M_writer(unicode(item_class_name))
        __M_writer(u" '")
        __M_writer(unicode(item_name))
        __M_writer(u"'</h2>\n\n")
        # SOURCE LINE 128
        if trans.get_user().username is None or trans.get_user().username is "":
            # SOURCE LINE 129
            __M_writer(u'        <p>To make a ')
            __M_writer(unicode(item_class_name_lc))
            __M_writer(u' accessible via link or publish it, you must create a public username:</p>\n        \n        <form action="')
            # SOURCE LINE 131
            __M_writer(unicode(h.url_for( controller=controller_name, action='set_public_username', id=trans.security.encode_id( item.id ) )))
            __M_writer(u'"     \n                method="POST">\n            <div class="form-row">\n                <label>Public Username:</label>\n                <div class="form-row-input">\n                    <input type="text" name="username" size="40"/>\n                </div>\n            </div>\n            <div style="clear: both"></div>\n            <div class="form-row">\n                <input class="action-button" type="submit" name="Set Username" value="Set Username"/>\n            </div>\n        </form>\n')
            # SOURCE LINE 144
        else:
            # SOURCE LINE 146
            __M_writer(u'        <h3>Make ')
            __M_writer(unicode(item_class_name))
            __M_writer(u' Accessible via Link and Publish It</h3>\n    \n            <div>\n')
            # SOURCE LINE 149
            if item.importable:
                # SOURCE LINE 150
                __M_writer(u'                    ')
 
                item_status = "accessible via link" 
                if item.published:
                    item_status = item_status + " and published"    
                                    
                
                # SOURCE LINE 154
                __M_writer(u'\n                    This ')
                # SOURCE LINE 155
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' is currently <strong>')
                __M_writer(unicode(item_status))
                __M_writer(u'</strong>. \n                    <div>\n                        <p>Anyone can view and import this ')
                # SOURCE LINE 157
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' by visiting the following URL:\n\n                        <blockquote>\n                            ')
                # SOURCE LINE 160
 
                url = h.url_for( controller=controller_name, action='display_by_username_and_slug', username=trans.get_user().username, slug=item.slug, qualified=True ) 
                url_parts = url.split("/")
                                            
                
                # SOURCE LINE 163
                __M_writer(u'\n                            <a id="item-url" href="')
                # SOURCE LINE 164
                __M_writer(unicode(url))
                __M_writer(u'" target="_top">')
                __M_writer(unicode(url))
                __M_writer(u'</a>\n                            <span id="item-url-text" style="display: none">\n                                ')
                # SOURCE LINE 166
                __M_writer(unicode("/".join( url_parts[:-1] )))
                __M_writer(u"/<span id='item-identifier'>")
                __M_writer(unicode(url_parts[-1]))
                __M_writer(u'</span>\n                            </span>\n                            \n                            <a href="#" id="edit-identifier"><img src="')
                # SOURCE LINE 169
                __M_writer(unicode(h.url_for('/static/images/fugue/pencil.png')))
                __M_writer(u'"/></a>\n                        </blockquote>\n        \n')
                # SOURCE LINE 172
                if item.published:
                    # SOURCE LINE 173
                    __M_writer(u'                            This ')
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" is publicly listed and searchable in Galaxy's <a href='")
                    __M_writer(unicode(h.url_for( controller=controller_name, action='list_published' )))
                    __M_writer(u'\' target="_top">Published ')
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section.\n')
                    pass
                # SOURCE LINE 175
                __M_writer(u'                    </div>\n        \n                    <p>You can:\n                    <div>\n                    <form action="')
                # SOURCE LINE 179
                __M_writer(unicode(h.url_for( controller=controller_name, action='sharing', id=trans.security.encode_id( item.id ) )))
                __M_writer(u'" method="POST">\n')
                # SOURCE LINE 180
                if not item.published:
                    # SOURCE LINE 182
                    __M_writer(u'                            <input class="action-button" type="submit" name="disable_link_access" value="Disable Access to ')
                    __M_writer(unicode(item_class_name))
                    __M_writer(u' Link">\n                            <div class="toolParamHelp">Disables ')
                    # SOURCE LINE 183
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u'\'s link so that it is not accessible.</div>\n                            <br />\n                            <input class="action-button" type="submit" name="publish" value="Publish ')
                    # SOURCE LINE 185
                    __M_writer(unicode(item_class_name))
                    __M_writer(u'" method="POST">\n                            <div class="toolParamHelp">Publishes the ')
                    # SOURCE LINE 186
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" to Galaxy's <a href='")
                    __M_writer(unicode(h.url_for( controller=controller_name, action='list_published' )))
                    __M_writer(u'\' target="_top">Published ')
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section, where it is publicly listed and searchable.</div>\n\n                        <br />\n')
                    # SOURCE LINE 189
                else: ## item.published == True
                    # SOURCE LINE 191
                    __M_writer(u'                            <input class="action-button" type="submit" name="unpublish" value="Unpublish ')
                    __M_writer(unicode(item_class_name))
                    __M_writer(u'">\n                            <div class="toolParamHelp">Removes this ')
                    # SOURCE LINE 192
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" from Galaxy's <a href='")
                    __M_writer(unicode(h.url_for(controller=controller_name, action='list_published' )))
                    __M_writer(u'\' target="_top">Published ')
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section so that it is not publicly listed or searchable.</div>\n                            <br />\n                            <input class="action-button" type="submit" name="disable_link_access_and_unpublish" value="Disable Access to ')
                    # SOURCE LINE 194
                    __M_writer(unicode(item_class_name))
                    __M_writer(u' via Link and Unpublish">\n                            <div class="toolParamHelp">Disables this ')
                    # SOURCE LINE 195
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u"'s link so that it is not accessible and removes ")
                    __M_writer(unicode(item_class_name_lc))
                    __M_writer(u" from Galaxy's <a href='")
                    __M_writer(unicode(h.url_for(controller=controller_name, action='list_published' )))
                    __M_writer(u"' target='_top'>Published ")
                    __M_writer(unicode(item_class_plural_name))
                    __M_writer(u'</a> section so that it is not publicly listed or searchable.</div>\n')
                    pass
                # SOURCE LINE 197
                __M_writer(u'                    </form>\n                    </div>\n   \n')
                # SOURCE LINE 200
            else:
                # SOURCE LINE 201
                __M_writer(u'   \n                    <p>This ')
                # SOURCE LINE 202
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' is currently restricted so that only you and the users listed below can access it. You can:</p>\n                    \n                    <form action="')
                # SOURCE LINE 204
                __M_writer(unicode(h.url_for(controller=controller_name, action='sharing', id=trans.security.encode_id(item.id) )))
                __M_writer(u'" method="POST">\n                        <input class="action-button" type="submit" name="make_accessible_via_link" value="Make ')
                # SOURCE LINE 205
                __M_writer(unicode(item_class_name))
                __M_writer(u' Accessible via Link">\n                        <div class="toolParamHelp">Generates a web link that you can share with other people so that they can view and import the ')
                # SOURCE LINE 206
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u'.</div>\n        \n                        <br />\n                        <input class="action-button" type="submit" name="make_accessible_and_publish" value="Make ')
                # SOURCE LINE 209
                __M_writer(unicode(item_class_name))
                __M_writer(u' Accessible and Publish" method="POST">\n                        <div class="toolParamHelp">Makes the ')
                # SOURCE LINE 210
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' accessible via link (see above) and publishes the ')
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u" to Galaxy's <a href='")
                __M_writer(unicode(h.url_for(controller=controller_name, action='list_published' )))
                __M_writer(u"' target='_top'>Published ")
                __M_writer(unicode(item_class_plural_name))
                __M_writer(u'</a> section, where it is publicly listed and searchable.</div>\n                    </form>\n       \n')
                pass
            # SOURCE LINE 214
            __M_writer(u'\n')
            # SOURCE LINE 218
            __M_writer(u'        <h3>Share ')
            __M_writer(unicode(item_class_name))
            __M_writer(u' with Individual Users</h3>\n\n            <div>\n')
            # SOURCE LINE 221
            if item.users_shared_with:
                # SOURCE LINE 222
                __M_writer(u'\n                    <p>\n                        The following users will see this ')
                # SOURCE LINE 224
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' in their ')
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' list and will be\n                        able to view, import, and run it.\n                    </p>\n            \n                    <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n                        <tr class="header">\n                            <th>Email</th>\n                            <th></th>\n                        </tr>\n')
                # SOURCE LINE 233
                for i, association in enumerate( item.users_shared_with ):
                    # SOURCE LINE 234
                    __M_writer(u'                            ')
                    user = association.user 
                    
                    __M_writer(u'\n                            <tr>\n                                <td>\n                                    <div class="menubutton popup" id="user-')
                    # SOURCE LINE 237
                    __M_writer(unicode(i))
                    __M_writer(u'-popup">')
                    __M_writer(unicode(user.email))
                    __M_writer(u'</div>\n                                </td>\n                                <td>\n                                    <div popupmenu="user-')
                    # SOURCE LINE 240
                    __M_writer(unicode(i))
                    __M_writer(u'-popup">\n                                    <a class="action-button" href="')
                    # SOURCE LINE 241
                    __M_writer(unicode(h.url_for(controller=controller_name, action='sharing', id=trans.security.encode_id( item.id ), unshare_user=trans.security.encode_id( user.id ), use_panels=use_panels )))
                    __M_writer(u'">Unshare</a>\n                                    </div>\n                                </td>\n                            </tr>    \n')
                    pass
                # SOURCE LINE 246
                __M_writer(u'                    </table>\n    \n                    <p>\n                    <a class="action-button" \n                       href="')
                # SOURCE LINE 250
                __M_writer(unicode(h.url_for(controller=controller_name, action='share', id=trans.security.encode_id(item.id), use_panels=use_panels )))
                __M_writer(u'">\n                        <span>Share with another user</span>\n                    </a>\n\n')
                # SOURCE LINE 254
            else:
                # SOURCE LINE 255
                __M_writer(u'\n                    <p>You have not shared this ')
                # SOURCE LINE 256
                __M_writer(unicode(item_class_name_lc))
                __M_writer(u' with any users.</p>\n    \n                    <a class="action-button" \n                       href="')
                # SOURCE LINE 259
                __M_writer(unicode(h.url_for(controller=controller_name, action='share', id=trans.security.encode_id(item.id), use_panels=use_panels )))
                __M_writer(u'">\n                        <span>Share with a user</span>\n                    </a>\n                    <br />\n    \n')
                pass
            # SOURCE LINE 265
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 268
        __M_writer(u'\n    <br /><br />\n    <a href="')
        # SOURCE LINE 270
        __M_writer(unicode(h.url_for(controller=controller_name, action="list" )))
        __M_writer(u'">Back to ')
        __M_writer(unicode(item_class_plural_name))
        __M_writer(u' List</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n    Sharing and Publishing ')
        # SOURCE LINE 38
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u" '")
        __M_writer(unicode(get_item_name( item )))
        __M_writer(u"'\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n    ')
        # SOURCE LINE 97
        __M_writer(unicode(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n    ')
        # SOURCE LINE 78
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style>\n')
        # SOURCE LINE 81
        __M_writer(u'        h3 {\n            margin-top: 2em;\n        }\n        input.action-button {\n            margin-left: 0;\n        }\n')
        # SOURCE LINE 88
        if context.get('use_panels'):
            # SOURCE LINE 89
            __M_writer(u'            div#center {\n                padding: 10px;\n            }\n')
            pass
        # SOURCE LINE 93
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
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
        
        
        # SOURCE LINE 34
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1093c8f50')._populate(_import_ns, [u'render_msg'])
        _mako_get_namespace(context, '__anon_0x1093c8850')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n    ')
        # SOURCE LINE 42
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    $(document).ready( function() {\n        //\n        // Set up slug-editing functionality.\n        //\n        var on_start = function( text_elt ) {\n            // Replace URL with URL text.\n            $(\'#item-url\').hide();\n            $(\'#item-url-text\').show();\n            \n            // Allow only lowercase alphanumeric and \'-\' characters in slug.\n            text_elt.keyup(function(){\n                text_elt.val( $(this).val().replace(/\\s+/g,\'-\').replace(/[^a-zA-Z0-9\\-]/g,\'\').toLowerCase() )\n            });\n        };\n        \n        var on_finish = function( text_elt ) {\n            // Replace URL text with URL.\n            $(\'#item-url-text\').hide();\n            $(\'#item-url\').show();\n            \n            // Set URL to new value.\n            var new_url = $(\'#item-url-text\').text();\n            var item_url_obj = $(\'#item-url\');\n            item_url_obj.attr( "href", new_url );\n            item_url_obj.text( new_url );\n        };\n        \n        ')
        # SOURCE LINE 71
        controller_name = get_controller_name( item ) 
        
        __M_writer(u'\n        async_save_text("edit-identifier", "item-identifier", "')
        # SOURCE LINE 72
        __M_writer(unicode(h.url_for( controller=controller_name, action='set_slug_async', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'", "new_slug", null, false, 0, on_start, on_finish); \n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


