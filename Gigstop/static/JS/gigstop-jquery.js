
$(document).ready(function()
	{
		var bool;
		// true = buy div ON screen i.e cant be moved further
		// false = buy div off screen (hidden) i.e can be moved on screen


	/*Pretty photo - in frame media player*/
		$("a[rel^='prettyPhoto']").prettyPhoto(
		{
			social_tools:false,
			// default_width:400,
			// default_height:300,
			theme: 'dark_rounded',
		});



	/*Masonry - wall tiling effect*/
		$('.wall').masonry(
		{
			itemSelector: ".wall-item",
			columnWidth: 300,
			rowHeight:300
		});



	/* side bar - scroll in animation */
	    $('#footer').click(function() 
	    {
	        $('#footer').animate({
	        'marginTop' : "+=600px" //moves left
	        });
	    });



	/* ANIMATE FLOAT IN BOXES*/
	    
	    /* buy tickets */

		window.onload = function() 
		{

			bool = false; /*initialise the boolean which declares that the buy-div is off the page*/

			// Buy button
			$(".buyticket").click(function() 
		    {
		    	if(bool == false) 
		    	{
		    		$('#footer').animate({'marginLeft' : "+=305px"});
		    		bool = true;

		    	} else 
		    	{
		    		$('#footer').animate({'width': "+="});
		    	}
		    });

			// Close button

			$("#footer-close").click(function() 
			{
		        $('#footer')
		        	.animate({'marginLeft' : "-=300px"});
		        bool = false;
		        // alert('boolean at end of close = '+bool);
		    });  
		};



    	/* I like this - save band button */

		    $(".likethis").click(function() {
		        $('#savedAlert')
		        .animate({'marginBottom': "+=110px"})
		        .fadeIn("slow")
		        .delay(1000)
		        .fadeOut("slow")
		        .animate({'marginBottom': "-=110px"});
		    });



	/*Main logo - pulse animation*/
		$(function () 
		{
		    $('#logo').textillate({ 
		    	loop:true, 
		    	in:{effect:'pulse', delay: 100, delayScale: 10, shuffle:true }, 
		    	reverse:true, 
		    	out:{effect:'pulse', delay: 100, delayScale: 10, shuffle:true } 
		    });
		});

}); /*End brackets*/



