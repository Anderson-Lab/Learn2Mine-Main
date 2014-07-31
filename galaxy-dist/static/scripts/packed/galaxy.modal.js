define([],function(){var a=Backbone.View.extend({elMain:"#everything",optionsDefault:{title:"galaxy-modal",body:"",backdrop:true,height:null,width:null,closing_events:false},buttonList:{},initialize:function(b){if(b){this._create(b)}},show:function(b){this.initialize(b);if(this.options.height){this.$body.css("height",this.options.height);this.$body.css("overflow","hidden")}else{this.$body.css("max-height",$(window).height()/2)}if(this.options.width){this.$dialog.css("width",this.options.width)}if(this.visible){this.$el.show()}else{this.$el.fadeIn("fast")}this.visible=true},hide:function(){this.visible=false;this.$el.fadeOut("fast")},enableButton:function(b){var c=this.buttonList[b];this.$buttons.find("#"+c).prop("disabled",false)},disableButton:function(b){var c=this.buttonList[b];this.$buttons.find("#"+c).prop("disabled",true)},showButton:function(b){var c=this.buttonList[b];this.$buttons.find("#"+c).show()},hideButton:function(b){var c=this.buttonList[b];this.$buttons.find("#"+c).hide()},getButton:function(b){var c=this.buttonList[b];return this.$buttons.find("#"+c)},scrollTop:function(){return this.$body.scrollTop()},_create:function(d){var c=this;this.options=_.defaults(d,this.optionsDefault);if(this.options.body=="progress"){this.options.body=$('<div class="progress progress-striped active"><div class="progress-bar progress-bar-info" style="width:100%"></div></div>')}if(this.$el){this.$el.remove();$(document).off("keyup")}this.setElement(this._template(this.options.title));this.$dialog=(this.$el).find(".modal-dialog");this.$body=(this.$el).find(".modal-body");this.$footer=(this.$el).find(".modal-footer");this.$buttons=(this.$el).find(".buttons");this.$backdrop=(this.$el).find(".modal-backdrop");this.$body.html(this.options.body);if(!this.options.backdrop){this.$backdrop.removeClass("in")}if(this.options.buttons){this.buttonList={};var b=0;$.each(this.options.buttons,function(e,g){var f="button-"+b++;c.$buttons.append($('<button id="'+f+'"></button>').text(e).click(g)).append(" ");c.buttonList[e]=f})}else{this.$footer.hide()}$(this.elMain).append($(this.el));if(this.options.closing_events){if(!this.options.buttons.Pause){$(document).on("keyup",function(f){if(f.keyCode==27){c.hide()}})}this.$el.find(".modal-backdrop").on("click",function(){c.hide()})}},_template:function(b){return'<div class="modal"><div class="modal-backdrop fade in" style="z-index: -1;"></div><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" style="display: none;">&times;</button><h4 class="title">'+b+'</h4></div><div class="modal-body" style="position: static;"></div><div class="modal-footer"><div class="buttons" style="float: right;"></div></div></div</div></div>'}});return{GalaxyModal:a}});