jQuery(document).ready(function() {
	function show_image(src, width, height, alt) {
	    var img = document.createElement("img");
	    img.src = src;
	    img.width = 128;
	    img.height = 128;
	    img.alt = alt;
	    img.align = "middle";
	    img.id = "skBadge";
	    document.getElementById("dialog").appendChild(img);
	}

	$("#org").jOrgChart();
	
	$selected = "none"
	    $("div#skpattern").click(function(){
		$("#dialog").text("Pattern Recognition");
		$("#dialog").dialog("open");
	});
	    $("div#skclustering").click(function(){
		$("#dialog").text("Clustering");
		$("#dialog").dialog("open");
	});
	    $("div#skkmeans").click(function(){
		$("#dialog").text("K-Means");
		$("#dialog").dialog("open");
	});
	    $("div#skhc").click(function(){
		$("#dialog").text("Hierarchical Clustering");
		$("#dialog").dialog("open");
	});
	    $("div#skclassification").click(function(){
		$("#dialog").text("Classification");
		$("#dialog").dialog("open");
	});
	    $("div#skknn").click(function(){
		$("#dialog").text("K-Nearest Neighbors");
		$("#dialog").dialog("open");
	});
	    $("div#skregression").click(function(){
		$("#dialog").text("Regression");
		$("#dialog").dialog("open");
	});
	    $("div#sknn").click(function(){
		$("#dialog").text("Neural Networks");
		$("#dialog").dialog("open");
	});
	    $("div#sksvm").click(function(){
		$("#dialog").text("Support Vector Machines");
		$("#dialog").dialog("open");
	});
	    $("div#skdtree").click(function(){
		$("#dialog").text("Decision Trees");
		$("#dialog").dialog("open");
	});
	    $("div#sknb").click(function(){
		$("#dialog").text("Naive Bayes");
		$("#dialog").dialog("open");
	});
	    $("div#skmarkbask").click(function(){
		$("#dialog").text("Market Basket Analysis");
		$("#dialog").dialog("open");
	});
	    $("div#skother").click(function(){
		$("#dialog").text("Other Techniques");
		$("#dialog").dialog("open");
	});
	    $("div#skscalefilter").click(function(){
		$("#dialog").text("Scale 'N Filter");
		$("#dialog").dialog("open");
	});
	    $("div#skpca").click(function(){
		$("#dialog").text("Principal Component Analysis");
		$("#dialog").dialog("open");
	});
	    $("div#skcase").click(function(){
		$("#dialog").text("Case Studies");
		$("#dialog").dialog("open");
	});
	    $("div#skcase1").click(function(){
		$("#dialog").text("Algae Case Study");
		$("#dialog").dialog("open");
	});
	    $("div#skcase2").click(function(){
		$("#dialog").text("Stock Market Case Study");
		$("#dialog").dialog("open");
	});
	    $("div#skcase3").click(function(){
		$("#dialog").text("Fraud Detection Case Study");
		$("#dialog").dialog("open");
	});
	    $(".locked").click(function(){
		$("#dialog").append("<br /><br />This skill is locked. Learn the prerequisite skills to unlock these lessons<br/>");
	});
	    $(".stillneedswork").click(function(){
		$("#dialog").append("<br /><br />This skill still needs work. In order to achieve the learned status for this skill, complete the corresponding lesson.<br/>");
	});
	    $(".learned").click(function(){
		$("#dialog").append("<br /><br />This skill is learned. In order to achieve skill mastery, complete the advanced lesson for this skill.<br/>");
	});
	    $(".mastered").click(function(){
		$("#dialog").append("<br /><br />Congratulations! You have mastered this skill!<br/>");
	});
	    $("div#skknn").click(function(){
		show_image("images/knnMastery.png", "KNN Badge"); 
		$("#dialog").append("<br/>Mastering this skill will allow you to earn the above badge");
	});
	    $("div#skcase1").click(function(){
		show_image("images/algaeMastery.png", "Algae Case Study Badge"); 
		$("#dialog").append("<br/>Mastering this skill will allow you to earn the above badge");
	});
	    $("div#skcase2").click(function(){
		show_image("images/stocksMastery.png", "Stocks Case Study Badge"); 
		$("#dialog").append("<br/>Mastering this skill will allow you to earn the above badge");
	});
	    $("div#skcase3").click(function(){
		show_image("images/fraudMastery.png", "Fraud Detection Case Study Badge"); 
		$("#dialog").append("<br/>Mastering this skill will allow you to earn the above badge");
	});

	$("#dialog").dialog({autoOpen: false});
	
});
