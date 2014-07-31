// Additional dependencies: jQuery, underscore.
define([], function() {

/**
 * Dataset metedata.
 */
var DatasetMetadata = Backbone.Model.extend({});

/**
 * A dataset. In Galaxy, datasets are associated with a history, so
 * this object is also known as a HistoryDatasetAssociation.
 */
var Dataset = Backbone.Model.extend({
    defaults: {
        id: '',
        type: '',
        name: '',
        hda_ldda: 'hda',
        metadata: null
    },

    initialize: function() {
        this._set_metadata();
        
        // Update metadata on change.
        this.on('change', this._set_metadata, this);
    },

    _set_metadata: function() {
        var metadata = new DatasetMetadata();

        // Move metadata from dataset attributes to metadata object.
        _.each(_.keys(this.attributes), function(k) { 
            if (k.indexOf('metadata_') === 0) {
                // Found metadata.
                var new_key = k.split('metadata_')[1];
                metadata.set(new_key, this.attributes[k]);
                delete this.attributes[k];
            }
        }, this);

        // Because this is an internal change, silence it.
        this.set('metadata', metadata, { 'silent': true });
    },

    /**
     * Returns dataset metadata for a given attribute.
     */
    get_metadata: function(attribute) {
        return this.attributes.metadata.get(attribute);
    },

    urlRoot: galaxy_config.root + "api/datasets"
});

/**
 * A tabular dataset. This object extends dataset to provide incremental chunked data.
 */
var TabularDataset = Dataset.extend({
    defaults: _.extend({}, Dataset.prototype.defaults, {
        chunk_url: null,
        first_data_chunk: null,
        chunk_index: -1,
        at_eof: false
    }),

    initialize: function(options) {
        Dataset.prototype.initialize.call(this);

        // If first data chunk is available, next chunk is 1.
        this.attributes.chunk_index = (this.attributes.first_data_chunk ? 1 : 0);
    },

    /**
     * Returns a jQuery Deferred object that resolves to the next data chunk or null if at EOF.
     */
    get_next_chunk: function() {
        // If already at end of file, do nothing.
        if (this.attributes.at_eof) {
            return null;
        }

        // Get next chunk.
        var self = this,
            next_chunk = $.Deferred();
        $.getJSON(this.attributes.chunk_url, {
            chunk: self.attributes.chunk_index++
        }).success(function(chunk) {
            var rval;
            if (chunk.ck_data !== '') {
                // Found chunk.
                rval = chunk;
            }
            else {
                // At EOF.
                self.attributes.at_eof = true;
                rval = null;
            }
            next_chunk.resolve(rval);
        });

        return next_chunk;
    }
});

var DatasetCollection = Backbone.Collection.extend({
    model: Dataset
});

/**
 * Provides table-based, dynamic view of a tabular dataset. 
 * NOTE: view's el must be in DOM already and provided when 
 * createing the view so that scrolling event can be attached
 * to the correct container.
 */
var TabularDatasetChunkedView = Backbone.View.extend({

    initialize: function(options)
    {
        // load trackster button
        new TabularButtonTracksterView(options);
    },

    render: function()
    {
        // Add data table and header.
        var data_table = $('<table/>').attr({
            id: 'content_table',
            cellpadding: 0
        });
        this.$el.append(data_table);
        var column_names = this.model.get_metadata('column_names');
        if (column_names) {
            data_table.append('<tr><th>' + column_names.join('</th><th>') + '</th></tr>');
        }

        // Add first chunk.
        var first_chunk = this.model.get('first_data_chunk');
        if (first_chunk) {
            this._renderChunk(first_chunk);
        }

        // -- Show new chunks during scrolling. --
        
        var self = this,
            // Element that does the scrolling.
            scroll_elt = _.find(this.$el.parents(), function(p) {
                return $(p).css('overflow') === 'auto';
            }),
            // Flag to ensure that only one chunk is loaded at a time.
            loading_chunk = false;

        // If no scrolling element found, use window.
        if (!scroll_elt) { scroll_elt = window; }

        // Wrap scrolling element for easy access.
        scroll_elt = $(scroll_elt);

        // Set up chunk loading when scrolling using the scrolling element.
        scroll_elt.scroll(function() {
            // If not already loading a chunk and have scrolled to the bottom of this element, get next chunk.
            if ( !loading_chunk && (self.$el.height() - scroll_elt.scrollTop() - scroll_elt.height() <= 0) ) {
                loading_chunk = true;
                $.when(self.model.get_next_chunk()).then(function(result) {
                    if (result) {
                        self._renderChunk(result);
                        loading_chunk = false;
                    }
                });
            }
        });
        $('#loading_indicator').ajaxStart(function(){
           $(this).show();
        }).ajaxStop(function(){
           $(this).hide();
        });
    },

    // -- Helper functions. --

    _renderCell: function(cell_contents, index, colspan) {
        var $cell = $('<td>').text(cell_contents);
        var column_types = this.model.get_metadata('column_types');
        if (colspan !== undefined) {
            $cell.attr('colspan', colspan).addClass('stringalign');
        } else if (column_types) {
            if (index < column_types.length) {
                if (column_types[index] === 'str' || column_types === 'list') {
                    /* Left align all str columns, right align the rest */
                    $cell.addClass('stringalign');
                }
            }
        }
        return $cell;
    },

    _renderRow: function(line) {
        // Check length of cells to ensure this is a complete row.
        var cells = line.split('\t'),
            row = $('<tr>'),
            num_columns = this.model.get_metadata('columns');
        if (cells.length === num_columns) {
            _.each(cells, function(cell_contents, index) {
                row.append(this._renderCell(cell_contents, index));
            }, this);
        }
        else if (cells.length > num_columns) {
            // SAM file or like format with optional metadata included.
            _.each(cells.slice(0, num_columns - 1), function(cell_contents, index) {
                row.append(this._renderCell(cell_contents, index));
            }, this);
            row.append(this._renderCell(cells.slice(num_columns - 1).join('\t'), num_columns - 1));
        }
        else if (num_columns > 5 && cells.length === num_columns - 1 ) {
            // SAM file or like format with optional metadata missing.
            _.each(cells, function(cell_contents, index) {
                row.append(this._renderCell(cell_contents, index));
            }, this);
            row.append($('<td>'));
        }
        else {
            // Comment line, just return the one cell.
            row.append(this._renderCell(line, 0, num_columns));
        }
        return row;
    },

    _renderChunk: function(chunk) {
        var data_table = this.$el.find('table');
        _.each(chunk.ck_data.split('\n'), function(line, index) {
            data_table.append(this._renderRow(line));
        }, this);
    }
});

// button for trackster visualization
var TabularButtonTracksterView = Backbone.View.extend(
{
    // gene region columns
    col: {
        chrom   : null,
        start   : null,
        end     : null
    },

    // url for trackster
    url_viz     : null,

    // dataset id
    dataset_id  : null,

    // database key
    genome_build: null,

    // data type
    data_type: null,

    // backbone initialize
    initialize: function (options)
    {
        // get options
        var attributes  = options.model.attributes;
        var metadata    = options.model.attributes.metadata.attributes;

        // check for datatype
        if (typeof attributes.data_type !== "undefined")
            this.data_type = attributes.data_type;
        else
            console.log("TabularButtonTrackster : Data type missing.");

        // check for bed-file format
        if (this.data_type == "bed")
        {
            // verify that metadata exists
            if (typeof metadata.chromCol !== "undefined" || typeof metadata.startCol !== "undefined" || typeof metadata.endCol !== "undefined")
            {
                // read in columns
                this.col.chrom   = metadata.chromCol - 1;
                this.col.start   = metadata.startCol - 1;
                this.col.end     = metadata.endCol - 1;
            } else
                console.log("TabularButtonTrackster : Bed-file metadata incomplete.");
        }

        // check for vcf-file format
        if (this.data_type == "vcf")
        {
            // search array
            function search (str, array)
            {
                for (var j = 0; j < array.length; j++)
                    if (array[j].match(str)) return j;
                return -1;
            };

            // load
            this.col.chrom = search("Chrom", metadata.column_names);
            this.col.start = search("Pos", metadata.column_names);
            this.col.end   = null;

            // verify that metadata exists
            if (this.col.chrom == -1 || this.col.start == -1)
                console.log("TabularButtonTrackster : VCF-file metadata incomplete.");
        }

        // check
        if(this.col.chrom === null) {
            return;
        }

        // get dataset id
        if (typeof options.model.attributes.id === "undefined") {
            console.log("TabularButtonTrackster : Dataset identification is missing.");
        } else {
            this.dataset_id = options.model.attributes.id;
        }
        
        // get url
        if (typeof options.model.attributes.url_viz === "undefined") {
            console.log("TabularButtonTrackster : Url for visualization controller is missing.");
        } else {
            this.url_viz = options.model.attributes.url_viz;
        }

        // get genome_build / database key
        if (typeof options.model.attributes.genome_build !== "undefined") {
            this.genome_build = options.model.attributes.genome_build;
        }

        // render the icon from template
        var btn_viz = new IconButtonView({ model : new IconButton({
            title       : 'Visualize',
            icon_class  : 'chart_curve',
            id          : 'btn_viz'
        })});
        
        // add it to the screen
        this.$el.append(btn_viz.render().$el);

        // hide the button
        $('#btn_viz').hide();
    },

    // backbone events
    events:
    {
        'mouseover tr'  : 'btn_viz_show',
        'mouseleave'    : 'btn_viz_hide'
    },
    
    // show button
    btn_viz_show: function (e)
    {
        // is numeric
        function is_numeric(n)
        {
            return !isNaN(parseFloat(n)) && isFinite(n);
        };

        // check
        if(this.col.chrom === null)
            return;

        // get selected data line
        var row = $(e.target).parent();

        // verify that location has been found
        var chrom = row.children().eq(this.col.chrom).html();
        var start = row.children().eq(this.col.start).html();

        // end is optional
        var end = this.col.end ? row.children().eq(this.col.end).html() : start;

        // double check location
        if (!chrom.match("^#") && chrom !== "" && is_numeric(start))
        {
            // get target gene region
            var btn_viz_pars = {
                dataset_id  : this.dataset_id,
                gene_region : chrom + ":" + start + "-" + end
            };

            // get button position
            var offset  = row.offset();
            var left    = offset.left - 10;
            var top     = offset.top - $(window).scrollTop();

            // update css
            $('#btn_viz').css({'position': 'fixed', 'top': top + 'px', 'left': left + 'px'});
            $('#btn_viz').off('click');
            $('#btn_viz').click(this.create_trackster_action(this.url_viz, btn_viz_pars, this.genome_build));

            // show the button
            $('#btn_viz').show();
        } else {
            // hide the button
            $('#btn_viz').hide();
        }
    },
    
    // hide button
    btn_viz_hide: function ()
    {
        // hide button from screen
        $('#btn_viz').hide();
    },
    
    // create action
    create_trackster_action : function (vis_url, dataset_params, dbkey) {
        return function() {
            var listTracksParams = {};
            if (dbkey){
                // list_tracks seems to use 'f-dbkey' (??)
                listTracksParams[ 'f-dbkey' ] = dbkey;
            }
            $.ajax({
                url: vis_url + '/list_tracks?' + $.param( listTracksParams ),
                dataType: "html",
                error: function() { alert( ( "Could not add this dataset to browser" ) + '.' ); },
                success: function(table_html) {
                    var parent = window.parent;
                    parent.Galaxy.modal.show({
                        title   : "View Data in a New or Saved Visualization",
                        buttons :{
                            "Cancel": function(){
                                parent.Galaxy.modal.hide();
                            },
                            "View in saved visualization": function(){
                                // Show new modal with saved visualizations.
                                parent.Galaxy.modal.show(
                                {
                                    title: "Add Data to Saved Visualization",
                                    body: table_html,
                                    buttons :{
                                        "Cancel": function(){
                                            parent.Galaxy.modal.hide();
                                        },
                                        "Add to visualization": function(){
                                            $(parent.document).find('input[name=id]:checked').each(function(){
                                                // hide
                                                parent.Galaxy.modal.hide();
                                                
                                                var vis_id = $(this).val();
                                                dataset_params.id = vis_id;
                                        
                                                // add widget
                                                parent.Galaxy.frame.add({
                                                    title    : "Trackster",
                                                    type     : "url",
                                                    content  : vis_url + "/trackster?" + $.param(dataset_params)
                                                });
                                            });
                                        }
                                    }
                                });
                            },
                            "View in new visualization": function(){
                                // hide
                                parent.Galaxy.modal.hide();
                                
                                var url = vis_url + "/trackster?" + $.param(dataset_params);

                                // add widget
                                parent.Galaxy.frame.add({
                                    title    : "Trackster",
                                    type     : "url",
                                    content  : url
                                });
                            }
                        }
                    });
                }
            });
            return false;
        };
    }
});

// -- Utility functions. --

/**
 * Create a model, attach it to a view, render view, and attach it to a parent element.
 */
var createModelAndView = function(model, view, model_config, parent_elt) {
    // Create model, view.
    var a_view = new view({
        model: new model(model_config)
    });

    // Render view and add to parent element.
    a_view.render();
    if (parent_elt) {
        parent_elt.append(a_view.$el);
    }

    return a_view;
};

/**
 * Create a tabular dataset chunked view (and requisite tabular dataset model)
 * and appends to parent_elt.
 */
var createTabularDatasetChunkedView = function(dataset_config, parent_elt) {
    // Create view element and add to parent.
    var view_div = $('<div/>').appendTo(parent_elt);

    // default viewer
    return new TabularDatasetChunkedView({
        el: view_div,
        model: new TabularDataset(dataset_config)
    }).render();
};

return {
	Dataset: Dataset,
    TabularDataset: TabularDataset,
	DatasetCollection: DatasetCollection,
    TabularDatasetChunkedView: TabularDatasetChunkedView,
    createTabularDatasetChunkedView: createTabularDatasetChunkedView
};

});
