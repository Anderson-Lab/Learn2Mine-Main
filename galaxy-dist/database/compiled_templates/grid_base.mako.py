# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402425550.581367
_template_filename=u'templates/grid_base.mako'
_template_uri=u'/history/../grid_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['load', 'body', 'init', 'center_panel', 'title']


# SOURCE LINE 1

from galaxy.web.framework.helpers.grids import TextColumn
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
    # SOURCE LINE 16
    ns = runtime.TemplateNamespace('__anon_0x1097a8e50', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1097a8e50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1097a8e50')._populate(_import_ns, [u'get_class_plural'])
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 234
        __M_writer(u'\n\n')
        # SOURCE LINE 239
        __M_writer(u'\n')
        # SOURCE LINE 241
        __M_writer(u'\n\n')
        # SOURCE LINE 246
        __M_writer(u'\n\n')
        # SOURCE LINE 251
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,embedded=False,insert=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1097a8e50')._populate(_import_ns, [u'get_class_plural'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'    ')
        __M_writer(unicode(self.init(embedded, insert)))
        __M_writer(u'\n    \n')
        # SOURCE LINE 25
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "autocomplete_tagging", "jquery.rating" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(h.js("libs/jquery/jquery.autocomplete", "galaxy.autocom_tagging", "libs/jquery/jquery.rating" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'    <div id="grid-container"><div>\n\n')
        # SOURCE LINE 32
        __M_writer(u'    <script type="text/javascript">\n        var gridView = null;\n        function add_tag_to_grid_filter (tag_name, tag_value)\n        {\n')
        # SOURCE LINE 37
        __M_writer(u'            var tag = tag_name + (tag_value !== undefined && tag_value !== "" ? ":" + tag_value : "");\n            var advanced_search = $(\'#advanced-search\').is(":visible");\n            if (!advanced_search)\n            {\n                $(\'#standard-search\').slideToggle(\'fast\');\n                $(\'#advanced-search\').slideToggle(\'fast\');\n            }\n            gridView.add_filter_condition("tags", tag);\n        };\n\n')
        # SOURCE LINE 48
        __M_writer(u"        $(function() {\n            require(['mvc/grid/grid-view'], function(GridView) {\n                gridView = new GridView(")
        # SOURCE LINE 50
        __M_writer(unicode(h.to_json_string(self.grid_config)))
        __M_writer(u');\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1097a8e50')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 249
        __M_writer(u'\n    ')
        # SOURCE LINE 250
        __M_writer(unicode(self.load()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context,embedded=False,insert=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1097a8e50')._populate(_import_ns, [u'get_class_plural'])
        cur_page_num = _import_ns.get('cur_page_num', context.get('cur_page_num', UNDEFINED))
        unicode = _import_ns.get('unicode', context.get('unicode', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        sort_key = _import_ns.get('sort_key', context.get('sort_key', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        num_page_links = _import_ns.get('num_page_links', context.get('num_page_links', UNDEFINED))
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        advanced_search = _import_ns.get('advanced_search', context.get('advanced_search', UNDEFINED))
        endfor = _import_ns.get('endfor', context.get('endfor', UNDEFINED))
        default_filter_dict = _import_ns.get('default_filter_dict', context.get('default_filter_dict', UNDEFINED))
        get_class_plural = _import_ns.get('get_class_plural', context.get('get_class_plural', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        refresh_frames = _import_ns.get('refresh_frames', context.get('refresh_frames', UNDEFINED))
        num_pages = _import_ns.get('num_pages', context.get('num_pages', UNDEFINED))
        cur_filter_dict = _import_ns.get('cur_filter_dict', context.get('cur_filter_dict', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        current_item = _import_ns.get('current_item', context.get('current_item', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        endif = _import_ns.get('endif', context.get('endif', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n')
        # SOURCE LINE 58

        self.has_left_panel         = False
        self.has_right_panel        = False
        self.message_box_visible    = False
        self.overlay_visible        = False
        self.active_view            = 'user'
        
        self.grid_config = {
            'title'                         : grid.title,
            'url_base'                      : trans.request.path_url,
            'async'                         : grid.use_async,
            'async_ops'                     : [],
            'categorical_filters'           : {},
            'filters'                       : cur_filter_dict,
            'sort_key'                      : sort_key,
            'show_item_checkboxes'          : context.get('show_item_checkboxes', False),
            'cur_page_num'                  : cur_page_num,
            'num_pages'                     : num_pages,
            'num_page_links'                : num_page_links,
            'history_tag_autocomplete_url'  : url( controller='tag', action='tag_autocomplete_data', item_class='History' ),
            'history_name_autocomplete_url' : url( controller='history', action='name_autocomplete_data' ),
            'status'                        : status,
            'message'                       : util.restore_text(message),
            'global_actions'                : [],
            'operations'                    : [],
            'items'                         : [],
            'columns'                       : [],
            'get_class_plural'              : get_class_plural( grid.model_class ).lower(),
            'use_paging'                    : grid.use_paging,
            'legend'                        : grid.legend,
            'current_item_id'               : False,
            'use_panels'                    : context.get('use_panels'),
            'use_hide_message'              : grid.use_hide_message,
            'insert'                        : insert,
            'default_filter_dict'           : default_filter_dict,
            'advanced_search'               : advanced_search,
            'refresh_frames'                : [],
            'embedded'                      : embedded,
            'info_text'                     : grid.info_text,
            'url'                           : url(dict())
        }
        
        ## add refresh frames
        if refresh_frames:
            self.grid_config['refresh_frames'] = refresh_frames
        
        ## add current item if exists
        if current_item:
            self.grid_config['current_item_id'] = current_item.id
        endif
        
        ## column
        for column in grid.columns:
            
            ## add column sort links
            href = None
            extra = ''
            if column.sortable:
                if sort_key.endswith(column.key):
                    if not sort_key.startswith("-"):
                        href = url( sort=( "-" + column.key ) )
                        extra = "&darr;"
                    else:
                        href = url( sort=( column.key ) )
                        extra = "&uarr;"
                else:
                    href = url( sort=column.key )
        
            ## add to configuration
            self.grid_config['columns'].append({
                'key'               : column.key,
                'visible'           : column.visible,
                'nowrap'            : column.nowrap,
                'attach_popup'      : column.attach_popup,
                'label_id_prefix'   : column.label_id_prefix,
                'sortable'          : column.sortable,
                'label'             : column.label,
                'filterable'        : column.filterable,
                'is_text'           : isinstance(column, TextColumn),
                'href'              : href,
                'extra'             : extra
            })
        endfor
        
        ## operations
        for operation in grid.operations:
            self.grid_config['operations'].append({
                'allow_multiple'        : operation.allow_multiple,
                'allow_popup'           : operation.allow_popup,
                'target'                : operation.target,
                'label'                 : operation.label,
                'confirm'               : operation.confirm,
                'inbound'               : operation.inbound,
                'global_operation'      : False
            })
            if operation.allow_multiple:
                self.grid_config['show_item_checkboxes'] = True
                
            if operation.global_operation:
                self.grid_config['global_operation'] = url( ** (operation.global_operation()) )
        endfor
        
        ## global actions
        for action in grid.global_actions:
            self.grid_config['global_actions'].append({
                'url_args'  : url(**action.url_args),
                'label'     : action.label,
                'inbound'   : action.inbound
            })
        endfor
        
        ## Operations that are async (AJAX) compatible.
        for operation in [op for op in grid.operations if op.async_compatible]:
            self.grid_config['async_ops'].append(operation.label.lower());
        endfor
        
        ## Filter values for categorical filters.
        for column in grid.columns:
            if column.filterable is not None and not isinstance( column, TextColumn ):
                self.grid_config['categorical_filters'][column.key] = dict([ (filter.label, filter.args) for filter in column.get_accepted_filters() ])
            endif
        endfor
        
        # items
        for i, item in enumerate( query ):
            item_dict = {
                'id'                    : item.id,
                'encode_id'             : trans.security.encode_id(item.id),
                'link'                  : [],
                'operation_config'      : {},
                'column_config'         : {}
            }
        
            ## data columns
            for column in grid.columns:
                if column.visible:
                    ## get link
                    link = column.get_link(trans, grid, item)
                    if link:
                        link = url(**link)
                    else:
                        link = None
                    endif
        
                    ## inbound
                    inbound = column.inbound
        
                    ## get value
                    value = column.get_value( trans, grid, item )
        
                    # Handle non-ascii chars.
                    if isinstance(value, str):
                        value = unicode(value, 'utf-8')
                        value = value.replace('/', '//')
                    endif
        
                    ## Item dictionary
                    item_dict['column_config'][column.label] = {
                        'link'      : link,
                        'value'     : value,
                        'inbound'   : inbound
                    }
                endif
            endfor
            ## add operation details to item
            for operation in grid.operations:
                item_dict['operation_config'][operation.label] = {
                    'allowed'   : operation.allowed(item),
                    'url_args'  : url( **operation.get_url_args( item ) )
                }
            endfor
        
            ## add item to list
            self.grid_config['items'].append(item_dict)
        endfor
        
        
        # SOURCE LINE 233
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1097a8e50')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 244
        __M_writer(u'\n    ')
        # SOURCE LINE 245
        __M_writer(unicode(self.load()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1097a8e50')._populate(_import_ns, [u'get_class_plural'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 241
        __M_writer(unicode(self.grid_config['title']))
        return ''
    finally:
        context.caller_stack._pop_frame()


