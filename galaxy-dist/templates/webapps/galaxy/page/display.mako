<%inherit file="/display_base.mako"/>

<%def name="javascripts()">
    ${parent.javascripts()}
    <script type="text/javascript">
    
        $(function() {

            // Setup embedded content:
            //  (a) toggles for showing/hiding embedded content;
            //  (b) ...
            $('.embedded-item').each( function() {
                var container = $(this);
            
                // Show embedded item.
                var show_embedded_item = function() {
                    var ajax_url = container.find("input[type=hidden]").val();
                    // Only get item content if it's not already there.
                    var item_content = $.trim(container.find(".item-content").text());
                    if (!item_content) {
                        $.ajax({
                            type: "GET",
                            url: ajax_url,
                            error: function() { alert("Getting item content failed."); },
                            success: function( item_content ) {
                                container.find(".summary-content").hide("fast");
                                container.find(".item-content").html(item_content);
                                container.find(".expanded-content").show("fast");
                                container.find(".toggle-expand").hide();
                                container.find(".toggle").show();

                                // Init needed for history items.
                                init_history_items( container.find("div.historyItemWrapper"), "noinit", "nochanges" ); 
                                container.find( "div.historyItemBody:visible" ).each( function() {
                                    if ( $.browser.mozilla ) {
                                        $(this).find( "pre.peek" ).css( "overflow", "hidden" );
                                    }
                                    $(this).hide();
                                });
                                make_popup_menus();
                            }
                        });
                    } else {
                        container.find(".summary-content").hide("fast");
                        container.find(".expanded-content").show("fast");
                        container.find(".toggle-expand").hide();
                        container.find(".toggle").show();
                    }
                };
            
                // Hide embedded item.
                var hide_embedded_item = function() {
                    container.find(".expanded-content").hide("fast");
                    container.find(".summary-content").show("fast");
                    container.find(".toggle").hide();
                    container.find(".toggle-expand").show();
                };
            
                // Setup toggle expand.
                var toggle_expand = $(this).find('.toggle-expand');
                toggle_expand.click( function() {
                    show_embedded_item();
                    return false;
                });
            
                // Setup toggle contract.
                var toggle_contract = $(this).find('.toggle');
                toggle_contract.click( function() {
                    hide_embedded_item();
                    return false;
                });
            
                // Setup toggle embed.
                var toggle_embed = $(this).find('.toggle-embed');
                toggle_embed.click( function() {
                    if (container.find(".expanded-content").is(":visible")) {
                        hide_embedded_item();
                    } else {
                        show_embedded_item();
                    }
                    return false;
                });
            });
        });
    
    </script>
</%def>

<%def name="stylesheets()">
    ${parent.stylesheets()}
    ${h.css( "base", "history", "autocomplete_tagging" )}
    <style type="text/css">
        .toggle { display: none; }
        .embedded-item h4 {
            margin: 0px;
        }
        ## Format tables in pages so that they look like they do in the page editor.
        .page-body > table {
            padding: 8px 5px 5px;
            min-width: 500px; 
            border: none;
            margin-top: 1em;
            margin-bottom: 1em;
        }
        .page-body caption { 
            text-align: left;
            background: #E4E4B0; 
            padding: 5px; 
            font-weight: bold; 
        }
        .page-body > table td {
            width: 25%;
            padding: 0.2em 0.8em;
        }
        ## HACKs to get Trackster navigation controls to display.
        .embedded-item .trackster-nav-container {
            height: inherit;
        }
        .embedded-item .trackster-nav {
            position: inherit;
        }
    </style>
</%def>

<%def name="render_item_header( item )">
    ## No header for pages.
</%def>

<%def name="render_item_links( page )">
</%def>

<%def name="render_item( page, page_data=None )">
    ${page_data}
</%def>