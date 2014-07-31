jQuery(document).ready(function() {
	function show_image(src, width, height, alt) {
	    var img = document.createElement("img");
	    img.src = "images/unearned_basicRTutorialMastery.png";
	    img.width = 128;
	    img.height = 128;
	    img.alt = alt;
	    img.align = "middle";
	    img.id = "skBadge";
	    document.getElementById("dialog").appendChild(img);
	}
	
	$("#dialog").text("This is your profile page. Here you can view badges that you can earn in the form of a skill tree. You are not required to follow an order in skills. If you successfully completed the lessons in the tutorial, you should notice that the badges in the tutorial branch on the right are all filled in! Now, take a look as some of the other badges you can earn by completing our other lessons");
	$("#dialog").dialog({autoOpen: true});
	//show_image("images/unearned_basicRTutorialMastery.png", "Tutorial"); 
	
});