var Galaxy={ITEM_HISTORY:"item_history",ITEM_DATASET:"item_dataset",ITEM_WORKFLOW:"item_workflow",ITEM_PAGE:"item_page",ITEM_VISUALIZATION:"item_visualization",DIALOG_HISTORY_LINK:"link_history",DIALOG_DATASET_LINK:"link_dataset",DIALOG_WORKFLOW_LINK:"link_workflow",DIALOG_PAGE_LINK:"link_page",DIALOG_VISUALIZATION_LINK:"link_visualization",DIALOG_EMBED_HISTORY:"embed_history",DIALOG_EMBED_DATASET:"embed_dataset",DIALOG_EMBED_WORKFLOW:"embed_workflow",DIALOG_EMBED_PAGE:"embed_page",DIALOG_EMBED_VISUALIZATION:"embed_visualization",DIALOG_HISTORY_ANNOTATE:"history_annotate",};function init_galaxy_elts(a){$(".annotation",a._doc.body).each(function(){$(this).click(function(){var b=a._doc.createRange();b.selectNodeContents(this);var d=window.getSelection();d.removeAllRanges();d.addRange(b);var c=""})})}function get_item_info(d){var f,c,b;switch(d){case (Galaxy.ITEM_HISTORY):f="History";c="Histories";b="history";item_class="History";break;case (Galaxy.ITEM_DATASET):f="Dataset";c="Datasets";b="dataset";item_class="HistoryDatasetAssociation";break;case (Galaxy.ITEM_WORKFLOW):f="Workflow";c="Workflows";b="workflow";item_class="StoredWorkflow";break;case (Galaxy.ITEM_PAGE):f="Page";c="Pages";b="page";item_class="Page";break;case (Galaxy.ITEM_VISUALIZATION):f="Visualization";c="Visualizations";b="visualization";item_class="Visualization";break}var e="list_"+c.toLowerCase()+"_for_selection";var a=list_objects_url.replace("LIST_ACTION",e);return{singular:f,plural:c,controller:b,iclass:item_class,list_ajax_url:a}}function make_item_importable(a,c,b){ajax_url=set_accessible_url.replace("ITEM_CONTROLLER",a);$.ajax({type:"POST",url:ajax_url,data:{id:c,accessible:"True"},error:function(){alert("Making "+b+" accessible failed")}})}WYMeditor.editor.prototype.dialog=function(i,e,g){var a=this;var b=a.uniqueStamp();var f=a.selected();function h(){$("#set_link_id").click(function(){$("#link_attribute_label").text("ID/Name");var k=$(".wym_href");k.addClass("wym_id").removeClass("wym_href");if(f){k.val($(f).attr("id"))}$(this).remove()})}if(i==WYMeditor.DIALOG_LINK){if(f){$(a._options.hrefSelector).val($(f).attr(WYMeditor.HREF));$(a._options.srcSelector).val($(f).attr(WYMeditor.SRC));$(a._options.titleSelector).val($(f).attr(WYMeditor.TITLE));$(a._options.altSelector).val($(f).attr(WYMeditor.ALT))}var c,d;if(f){c=$(f).attr("href");if(c==undefined){c=""}d=$(f).attr("title");if(d==undefined){d=""}}show_modal("Create Link","<div><div><label id='link_attribute_label'>URL <span style='float: right; font-size: 90%'><a href='#' id='set_link_id'>Create in-page anchor</a></span></label><br><input type='text' class='wym_href' value='"+c+"' size='40' /></div><div><label>Title</label><br><input type='text' class='wym_title' value='"+d+"' size='40' /></div><div>",{"Make link":function(){var m=$(a._options.hrefSelector).val()||"",k=$(".wym_id").val()||"",n=$(a._options.titleSelector).val()||"";if(m||k){a._exec(WYMeditor.CREATE_LINK,b);var l=$("a[href="+b+"]",a._doc.body);l.attr(WYMeditor.HREF,m).attr(WYMeditor.TITLE,n).attr("id",k);if(l.text().indexOf("wym-")===0){l.text(n)}}hide_modal()},Cancel:function(){hide_modal()}},{},h)}if(i==WYMeditor.DIALOG_IMAGE){if(a._selected_image){$(a._options.dialogImageSelector+" "+a._options.srcSelector).val($(a._selected_image).attr(WYMeditor.SRC));$(a._options.dialogImageSelector+" "+a._options.titleSelector).val($(a._selected_image).attr(WYMeditor.TITLE));$(a._options.dialogImageSelector+" "+a._options.altSelector).val($(a._selected_image).attr(WYMeditor.ALT))}show_modal("Image","<div class='row'><label>URL</label><br><input type='text' class='wym_src' value='' size='40' /></div><div class='row'><label>Alt text</label><br><input type='text' class='wym_alt' value='' size='40' /></div><div class='row'><label>Title</label><br><input type='text' class='wym_title' value='' size='40' /></div>",{Insert:function(){var k=$(a._options.srcSelector).val();if(k.length>0){a._exec(WYMeditor.INSERT_IMAGE,b);$("img[src$="+b+"]",a._doc.body).attr(WYMeditor.SRC,k).attr(WYMeditor.TITLE,$(a._options.titleSelector).val()).attr(WYMeditor.ALT,$(a._options.altSelector).val())}hide_modal()},Cancel:function(){hide_modal()}});return}if(i==WYMeditor.DIALOG_TABLE){show_modal("Table","<div class='row'><label>Caption</label><br><input type='text' class='wym_caption' value='' size='40' /></div><div class='row'><label>Summary</label><br><input type='text' class='wym_summary' value='' size='40' /></div><div class='row'><label>Number Of Rows<br></label><input type='text' class='wym_rows' value='3' size='3' /></div><div class='row'><label>Number Of Cols<br></label><input type='text' class='wym_cols' value='2' size='3' /></div>",{Insert:function(){var o=$(a._options.rowsSelector).val();var r=$(a._options.colsSelector).val();if(o>0&&r>0){var n=a._doc.createElement(WYMeditor.TABLE);var l=null;var q=null;var k=$(a._options.captionSelector).val();var p=n.createCaption();p.innerHTML=k;for(x=0;x<o;x++){l=n.insertRow(x);for(y=0;y<r;y++){l.insertCell(y)}}$(n).attr("summary",$(a._options.summarySelector).val());var m=$(a.findUp(a.container(),WYMeditor.MAIN_CONTAINERS)).get(0);if(!m||!m.parentNode){$(a._doc.body).append(n)}else{$(m).after(n)}}hide_modal()},Cancel:function(){hide_modal()}})}if(i==Galaxy.DIALOG_HISTORY_LINK||i==Galaxy.DIALOG_DATASET_LINK||i==Galaxy.DIALOG_WORKFLOW_LINK||i==Galaxy.DIALOG_PAGE_LINK||i==Galaxy.DIALOG_VISUALIZATION_LINK){var j;switch(i){case (Galaxy.DIALOG_HISTORY_LINK):j=get_item_info(Galaxy.ITEM_HISTORY);break;case (Galaxy.DIALOG_DATASET_LINK):j=get_item_info(Galaxy.ITEM_DATASET);break;case (Galaxy.DIALOG_WORKFLOW_LINK):j=get_item_info(Galaxy.ITEM_WORKFLOW);break;case (Galaxy.DIALOG_PAGE_LINK):j=get_item_info(Galaxy.ITEM_PAGE);break;case (Galaxy.DIALOG_VISUALIZATION_LINK):j=get_item_info(Galaxy.ITEM_VISUALIZATION);break}$.ajax({url:j.list_ajax_url,data:{},error:function(){alert("Failed to list "+j.plural.toLowerCase()+" for selection")},success:function(k){show_modal("Insert Link to "+j.singular,k+"<div><input id='make-importable' type='checkbox' checked/>Make the selected "+j.plural.toLowerCase()+" accessible so that they can viewed by everyone.</div>",{Insert:function(){var m=false;if($("#make-importable:checked").val()!==null){m=true}var l=new Array();$("input[name=id]:checked").each(function(){var n=$(this).val();if(m){make_item_importable(j.controller,n,j.singular)}url_template=get_name_and_link_url+n;ajax_url=url_template.replace("ITEM_CONTROLLER",j.controller);$.getJSON(ajax_url,function(p){a._exec(WYMeditor.CREATE_LINK,b);var o=$("a[href="+b+"]",a._doc.body).text();if(o==""||o==b){a.insert("<a href='"+p.link+"'>"+j.singular+" '"+p.name+"'</a>")}else{$("a[href="+b+"]",a._doc.body).attr(WYMeditor.HREF,p.link).attr(WYMeditor.TITLE,j.singular+n)}})});hide_modal()},Cancel:function(){hide_modal()}})}})}if(i==Galaxy.DIALOG_EMBED_HISTORY||i==Galaxy.DIALOG_EMBED_DATASET||i==Galaxy.DIALOG_EMBED_WORKFLOW||i==Galaxy.DIALOG_EMBED_PAGE||i==Galaxy.DIALOG_EMBED_VISUALIZATION){var j;switch(i){case (Galaxy.DIALOG_EMBED_HISTORY):j=get_item_info(Galaxy.ITEM_HISTORY);break;case (Galaxy.DIALOG_EMBED_DATASET):j=get_item_info(Galaxy.ITEM_DATASET);break;case (Galaxy.DIALOG_EMBED_WORKFLOW):j=get_item_info(Galaxy.ITEM_WORKFLOW);break;case (Galaxy.DIALOG_EMBED_PAGE):j=get_item_info(Galaxy.ITEM_PAGE);break;case (Galaxy.DIALOG_EMBED_VISUALIZATION):j=get_item_info(Galaxy.ITEM_VISUALIZATION);break}$.ajax({url:j.list_ajax_url,data:{},error:function(){alert("Failed to list "+j.plural.toLowerCase()+" for selection")},success:function(k){if(i==Galaxy.DIALOG_EMBED_HISTORY||i==Galaxy.DIALOG_EMBED_WORKFLOW||i==Galaxy.DIALOG_EMBED_VISUALIZATION){k=k+"<div><input id='make-importable' type='checkbox' checked/>Make the selected "+j.plural.toLowerCase()+" accessible so that they can viewed by everyone.</div>"}show_modal("Embed "+j.plural,k,{Embed:function(){var l=false;if($("#make-importable:checked").val()!=null){l=true}$("input[name=id]:checked").each(function(){var m=$(this).val();var p=$("label[for='"+m+"']:first").text();if(l){make_item_importable(j.controller,m,j.singular)}var n=j.iclass+"-"+m;var o="<p><div id='"+n+"' class='embedded-item "+j.singular.toLowerCase()+" placeholder'>                                         <p class='title'>Embedded Galaxy "+j.singular+" '"+p+"'</p>                                         <p class='content'>                                             [Do not edit this block; Galaxy will fill it in with the annotated "+j.singular.toLowerCase()+" when it is displayed.]                                         </p>                                     </div></p>";a.insert("&nbsp;");a.insert(o);$("#"+n,a._doc.body).each(function(){var q=true;while(q){var r=$(this).prev();if(r.length!=0&&jQuery.trim(r.text())==""){r.remove()}else{q=false}}})});hide_modal()},Cancel:function(){hide_modal()}})}})}if(i==Galaxy.DIALOG_ANNOTATE_HISTORY){$.ajax({url:list_histories_for_selection_url,data:{},error:function(){alert("Grid refresh failed")},success:function(k){show_modal("Insert Link to History",k,{Annotate:function(){var l=new Array();$("input[name=id]:checked").each(function(){var m=$(this).val();$.ajax({url:get_history_annotation_table_url,data:{id:m},error:function(){alert("Grid refresh failed")},success:function(n){a.insert(n);init_galaxy_elts(a)}})});hide_modal()},Cancel:function(){hide_modal()}})}})}};$(function(){$(document).ajaxError(function(i,g){var h=g.responseText||g.statusText||"Could not connect to server";show_modal("Server error",h,{"Ignore error":hide_modal});return false});$("[name=page_content]").wymeditor({skin:"galaxy",basePath:editor_base_path,iframeBasePath:iframe_base_path,boxHtml:"<table class='wym_box' width='100%' height='100%'><tr><td><div class='wym_area_top'>"+WYMeditor.TOOLS+"</div></td></tr><tr height='100%'><td><div class='wym_area_main' style='height: 100%;'>"+WYMeditor.IFRAME+WYMeditor.STATUS+"</div></div></td></tr></table>",toolsItems:[{name:"Bold",title:"Strong",css:"wym_tools_strong"},{name:"Italic",title:"Emphasis",css:"wym_tools_emphasis"},{name:"Superscript",title:"Superscript",css:"wym_tools_superscript"},{name:"Subscript",title:"Subscript",css:"wym_tools_subscript"},{name:"InsertOrderedList",title:"Ordered_List",css:"wym_tools_ordered_list"},{name:"InsertUnorderedList",title:"Unordered_List",css:"wym_tools_unordered_list"},{name:"Indent",title:"Indent",css:"wym_tools_indent"},{name:"Outdent",title:"Outdent",css:"wym_tools_outdent"},{name:"Undo",title:"Undo",css:"wym_tools_undo"},{name:"Redo",title:"Redo",css:"wym_tools_redo"},{name:"CreateLink",title:"Link",css:"wym_tools_link"},{name:"Unlink",title:"Unlink",css:"wym_tools_unlink"},{name:"InsertImage",title:"Image",css:"wym_tools_image"},{name:"InsertTable",title:"Table",css:"wym_tools_table"},]});var d=$.wymeditors(0);var f=function(g){show_modal("Saving page","progress");$.ajax({url:save_url,type:"POST",data:{id:page_id,content:d.xhtml(),annotations:JSON.stringify(new Object()),_:"true"},success:function(){g()}})};$("#save-button").click(function(){f(function(){hide_modal()})});$("#close-button").click(function(){var h=false;if(h){var g=function(){window.onbeforeunload=undefined;window.document.location=page_list_url};show_modal("Close editor","There are unsaved changes to your page which will be lost.",{Cancel:hide_modal,"Save Changes":function(){f(g)}},{"Don't Save":g})}else{window.document.location=page_list_url}});var a=$("<div class='galaxy-page-editor-button'><a id='insert-galaxy-link' class='action-button popup' href='#'>Paragraph type</a></div>");$(".wym_area_top").append(a);var b={};$.each(d._options.containersItems,function(h,g){var i=g.name;b[g.title.replace("_"," ")]=function(){d.container(i)}});make_popupmenu(a,b);var c=$("<div><a id='insert-galaxy-link' class='action-button popup' href='#'>Insert Link to Galaxy Object</a></div>").addClass("galaxy-page-editor-button");$(".wym_area_top").append(c);make_popupmenu(c,{"Insert History Link":function(){d.dialog(Galaxy.DIALOG_HISTORY_LINK)},"Insert Dataset Link":function(){d.dialog(Galaxy.DIALOG_DATASET_LINK)},"Insert Workflow Link":function(){d.dialog(Galaxy.DIALOG_WORKFLOW_LINK)},"Insert Page Link":function(){d.dialog(Galaxy.DIALOG_PAGE_LINK)},"Insert Visualization Link":function(){d.dialog(Galaxy.DIALOG_VISUALIZATION_LINK)},});var e=$("<div><a id='embed-galaxy-object' class='action-button popup' href='#'>Embed Galaxy Object</a></div>").addClass("galaxy-page-editor-button");$(".wym_area_top").append(e);make_popupmenu(e,{"Embed History":function(){d.dialog(Galaxy.DIALOG_EMBED_HISTORY)},"Embed Dataset":function(){d.dialog(Galaxy.DIALOG_EMBED_DATASET)},"Embed Workflow":function(){d.dialog(Galaxy.DIALOG_EMBED_WORKFLOW)},"Embed Visualization":function(){d.dialog(Galaxy.DIALOG_EMBED_VISUALIZATION)},})});