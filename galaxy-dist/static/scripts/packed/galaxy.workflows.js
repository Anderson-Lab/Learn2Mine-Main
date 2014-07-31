$(function(){if(window.lt_ie_7){show_modal("Browser not supported","Sorry, the workflow editor is not supported for IE6 and below.");return}$("#tool-search-query").click(function(){$(this).focus();$(this).select()}).keyup(function(){$(this).css("font-style","normal");if(this.value.length<3){reset_tool_search(false)}else{if(this.value!=this.lastValue){$(this).addClass("search_active");var g=this.value+"*";if(this.timer){clearTimeout(this.timer)}$("#search-spinner").show();this.timer=setTimeout(function(){$.get(tool_search_url,{query:g},function(i){$("#search-no-results").hide();$(".toolSectionWrapper").hide();$(".toolSectionWrapper").find(".toolTitle").hide();if(i.length!=0){var h=$.map(i,function(k,j){return"link-"+k});$(h).each(function(j,k){$("[id='"+k+"']").parent().addClass("search_match");$("[id='"+k+"']").parent().show().parent().parent().show().parent().show()});$(".toolPanelLabel").each(function(){var l=$(this);var k=l.next();var j=true;while(k.length!==0&&k.hasClass("toolTitle")){if(k.is(":visible")){j=false;break}else{k=k.next()}}if(j){l.hide()}})}else{$("#search-no-results").show()}$("#search-spinner").hide()},"json")},200)}}this.lastValue=this.value});canvas_manager=new CanvasManager($("#canvas-viewport"),$("#overview"));reset();$.ajax({url:get_datatypes_url,dataType:"json",cache:false,success:function(g){populate_datatype_info(g);$.ajax({url:load_workflow_url,data:{id:workflow_id,_:"true"},dataType:"json",cache:false,success:function(h){reset();workflow.from_simple(h);workflow.has_changes=false;workflow.fit_canvas_to_nodes();scroll_to_nodes();canvas_manager.draw_overview();upgrade_message="";$.each(h.upgrade_messages,function(j,i){upgrade_message+=("<li>Step "+(parseInt(j,10)+1)+": "+workflow.nodes[j].name+"<ul>");$.each(i,function(k,l){upgrade_message+="<li>"+l+"</li>"});upgrade_message+="</ul></li>"});if(upgrade_message){show_modal("Workflow loaded with changes","Problems were encountered loading this workflow (possibly a result of tool upgrades). Please review the following parameters and then save.<ul>"+upgrade_message+"</ul>",{Continue:hide_modal})}else{hide_modal()}show_workflow_parameters()},beforeSubmit:function(h){show_message("Loading workflow","progress")}})}});$(document).ajaxStart(function(){active_ajax_call=true;$(document).bind("ajaxStop.global",function(){active_ajax_call=false})});$(document).ajaxError(function(i,g){var h=g.responseText||g.statusText||"Could not connect to server";show_modal("Server error",h,{"Ignore error":hide_modal});return false});make_popupmenu($("#workflow-options-button"),{Save:save_current_workflow,Run:function(){window.location=run_workflow_url},"Edit Attributes":c,"Auto Re-layout":f,Close:close_editor});function b(){workflow.clear_active_node();$(".right-content").hide();var j="";for(var h in workflow.nodes){var i=workflow.nodes[h];if(i.type=="tool"){j+="<div class='toolForm' style='margin-bottom:5px;'><div class='toolFormTitle'>Step "+i.id+" - "+i.name+"</div>";for(var k in i.output_terminals){var g=i.output_terminals[k];if($.inArray(g.name,i.workflow_outputs)!=-1){j+="<p>"+g.name+"<input type='checkbox' name='"+i.id+"|"+g.name+"' checked /></p>"}else{j+="<p>"+g.name+"<input type='checkbox' name='"+i.id+"|"+g.name+"' /></p>"}}j+="</div>"}}$("#output-fill-area").html(j);$("#output-fill-area input").bind("click",function(){var n=this.name.split("|")[0];var l=this.name.split("|")[1];if(this.checked){if($.inArray(l,workflow.nodes[n].workflow_outputs)==-1){workflow.nodes[n].workflow_outputs.push(l)}}else{while($.inArray(l,workflow.nodes[n].workflow_outputs)!=-1){var m=$.inArray(l,workflow.nodes[n].workflow_outputs);workflow.nodes[n].workflow_outputs=workflow.nodes[n].workflow_outputs.slice(0,m).concat(workflow.nodes[n].workflow_outputs.slice(m+1))}}workflow.has_changes=true});$("#workflow-output-area").show()}function f(){workflow.layout();workflow.fit_canvas_to_nodes();scroll_to_nodes();canvas_manager.draw_overview()}function c(){workflow.clear_active_node();$(".right-content").hide();$("#edit-attributes").show()}overview_size=$.jStorage.get("overview-size");if(overview_size!==undefined){$("#overview-border").css({width:overview_size,height:overview_size})}if($.jStorage.get("overview-off")){d()}else{e()}$("#overview-border").bind("dragend",function(h,j){var k=$(this).offsetParent();var i=k.offset();var g=Math.max(k.width()-(j.offsetX-i.left),k.height()-(j.offsetY-i.top));$.jStorage.set("overview-size",g+"px")});function e(){$.jStorage.set("overview-off",false);$("#overview-border").css("right","0px");$("#close-viewport").css("background-position","0px 0px")}function d(){$.jStorage.set("overview-off",true);$("#overview-border").css("right","20000px");$("#close-viewport").css("background-position","12px 0px")}$("#close-viewport").click(function(){if($("#overview-border").css("right")==="0px"){d()}else{e()}});window.onbeforeunload=function(){if(workflow&&workflow.has_changes){return"There are unsaved changes to your workflow which will be lost."}};$("div.toolSectionBody").hide();$("div.toolSectionTitle > span").wrap("<a href='#'></a>");var a=null;$("div.toolSectionTitle").each(function(){var g=$(this).next("div.toolSectionBody");$(this).click(function(){if(g.is(":hidden")){if(a){a.slideUp("fast")}a=g;g.slideDown("fast")}else{g.slideUp("fast");a=null}})});async_save_text("workflow-name","workflow-name",rename_async_url,"new_name");$("#workflow-tag").click(function(){$(".tag-area").click();return false});async_save_text("workflow-annotation","workflow-annotation",annotate_async_url,"new_annotation",25,true,4)});function reset(){if(workflow){workflow.remove_all()}workflow=new Workflow($("#canvas-container"))}function scroll_to_nodes(){var a=$("#canvas-viewport");var d=$("#canvas-container");var c,b;if(d.width()<a.width()){b=(a.width()-d.width())/2}else{b=0}if(d.height()<a.height()){c=(a.height()-d.height())/2}else{c=0}d.css({left:b,top:c})}function add_node_for_tool(c,b){var a=prebuild_node("tool",b,c);workflow.add_node(a);workflow.fit_canvas_to_nodes();canvas_manager.draw_overview();workflow.activate_node(a);$.ajax({url:get_new_module_info_url,data:{type:"tool",tool_id:c,_:"true"},global:false,dataType:"json",success:function(d){a.init_field_data(d)},error:function(f,g){var d="error loading field data";if(f.status===0){d+=", server unavailable"}a.error(d)}})}function add_node_for_module(a,b){node=prebuild_node(a,b);workflow.add_node(node);workflow.fit_canvas_to_nodes();canvas_manager.draw_overview();workflow.activate_node(node);$.ajax({url:get_new_module_info_url,data:{type:a,_:"true"},dataType:"json",success:function(c){node.init_field_data(c)},error:function(d,f){var c="error loading field data";if(d.status==0){c+=", server unavailable"}node.error(c)}})}function display_pja(b,a){$("#pja_container").append(get_pja_form(b));$("#pja_container>.toolForm:last>.toolFormTitle>.buttons").click(function(){action_to_rem=$(this).closest(".toolForm",".action_tag").children(".action_tag:first").text();$(this).closest(".toolForm").remove();delete workflow.active_node.post_job_actions[action_to_rem];workflow.active_form_has_changes=true})}function display_pja_list(){return pja_list}function display_file_list(b){addlist="<select id='node_data_list' name='node_data_list'>";for(var a in b.output_terminals){addlist+="<option value='"+a+"'>"+a+"</option>"}addlist+="</select>";return addlist}function new_pja(d,b,a){if(a.post_job_actions===undefined){a.post_job_actions={}}if(a.post_job_actions[d+b]===undefined){var c={};c.action_type=d;c.output_name=b;a.post_job_actions[d+b]=null;a.post_job_actions[d+b]=c;display_pja(c,a);workflow.active_form_has_changes=true;return true}else{return false}}function show_workflow_parameters(){var c=/\$\{.+?\}/g;var b=[];var f=$("#workflow-parameters-container");var e=$("#workflow-parameters-box");var a="";var d=[];$.each(workflow.nodes,function(g,h){var i=h.form_html.match(c);if(i){d=d.concat(i)}if(h.post_job_actions){$.each(h.post_job_actions,function(j,l){if(l.action_arguments){$.each(l.action_arguments,function(m,n){var o=n.match(c);if(o){d=d.concat(o)}})}});if(d){$.each(d,function(j,l){if($.inArray(l,b)===-1){b.push(l)}})}}});if(b&&b.length!==0){$.each(b,function(g,h){a+="<div>"+h.substring(2,h.length-1)+"</div>"});f.html(a);e.show()}else{f.html(a);e.hide()}}function show_form_for_tool(c,b){$(".right-content").hide();$("#right-content").show().html(c);if(b){$("#right-content").find(".toolForm:first").after("<p><div class='metadataForm'>             <div class='metadataFormTitle'>Edit Step Attributes</div>             <div class='form-row'>             <label>Annotation / Notes:</label>                     <div style='margin-right: 10px;'>                     <textarea name='annotation' rows='3' style='width: 100%'>"+b.annotation+"</textarea>                         <div class='toolParamHelp'>Add an annotation or notes to this step; annotations are available when a workflow is viewed.</div>                     </div>             </div>             </div>")}if(b&&b.type=="tool"){pjastr="<p><div class='metadataForm'><div class='metadataFormTitle'>Edit Step Actions</div><div class='form-row'>             "+display_pja_list()+" <br/> "+display_file_list(b)+" <div class='action-button' style='border:1px solid black;display:inline;' id='add_pja'>Create</div>            </div><div class='form-row'>            <div style='margin-right: 10px;'><span id='pja_container'></span>";pjastr+="<div class='toolParamHelp'>Add actions to this step; actions are applied when this workflow step completes.</div></div></div></div>";$("#right-content").find(".toolForm").after(pjastr);for(var a in b.post_job_actions){if(a!="undefined"){display_pja(b.post_job_actions[a],b)}}$("#add_pja").click(function(){new_pja($("#new_pja_list").val(),$("#node_data_list").val(),b)})}$("#right-content").find("form").ajaxForm({type:"POST",dataType:"json",success:function(d){workflow.active_form_has_changes=false;b.update_field_data(d);show_workflow_parameters()},beforeSubmit:function(d){d.push({name:"tool_state",value:b.tool_state});d.push({name:"_",value:"true"})}}).each(function(){var d=this;$(this).find("select[refresh_on_change='true']").change(function(){$(d).submit()});$(this).find(".popupmenu").each(function(){var g=$(this).parents("div.form-row").attr("id");var e=$('<a class="popup-arrow" id="popup-arrow-for-'+g+'">&#9660;</a>');var f={};$(this).find("button").each(function(){var h=$(this).attr("name");var i=$(this).attr("value");f[$(this).text()]=function(){$(d).append("<input type='hidden' name='"+h+"' value='"+i+"' />").submit()}});e.insertAfter(this);$(this).remove();make_popupmenu(e,f)});$(this).find("input,textarea,select").each(function(){$(this).bind("focus click",function(){workflow.active_form_has_changes=true})})})}var close_editor=function(){workflow.check_changes_in_active_form();if(workflow&&workflow.has_changes){do_close=function(){window.onbeforeunload=undefined;window.document.location=workflow_index_url};show_modal("Close workflow editor","There are unsaved changes to your workflow which will be lost.",{Cancel:hide_modal,"Save Changes":function(){save_current_workflow(null,do_close)}},{"Don't Save":do_close})}else{window.document.location=workflow_index_url}};var save_current_workflow=function(b,c){show_message("Saving workflow","progress");workflow.check_changes_in_active_form();if(!workflow.has_changes){hide_modal();if(c){c()}return}workflow.rectify_workflow_outputs();var a=function(d){$.ajax({url:save_workflow_url,type:"POST",data:{id:workflow_id,workflow_data:function(){return JSON.stringify(workflow.to_simple())},_:"true"},dataType:"json",success:function(g){var e=$("<div></div>").text(g.message);if(g.errors){e.addClass("warningmark");var f=$("<ul/>");$.each(g.errors,function(j,h){$("<li></li>").text(h).appendTo(f)});e.append(f)}else{e.addClass("donemark")}workflow.name=g.name;workflow.has_changes=false;workflow.stored=true;show_workflow_parameters();if(g.errors){show_modal("Saving workflow",e,{Ok:hide_modal})}else{if(d){d()}hide_modal()}}})};if(active_ajax_call){$(document).bind("ajaxStop.save_workflow",function(){$(document).unbind("ajaxStop.save_workflow");a();$(document).unbind("ajaxStop.save_workflow");active_ajax_call=false})}else{a(c)}};