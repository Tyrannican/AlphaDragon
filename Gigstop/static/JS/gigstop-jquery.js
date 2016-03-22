<script type="text/javascript" charset="utf-8">

			/*Pretty photo - in frame media player*/
				$(document).ready(function(){
				$("a[rel^='prettyPhoto']").prettyPhoto({
					social_tools:false,
					// default_width:400,
					// default_height:300,
					theme: 'dark_rounded',
					});
				});

			/*Masonry - wall tiling effect*/
				$('.wall').masonry({
	  				itemSelector: ".wall-item",
	  				columnWidth: 300,
	  				rowHeight:300,
				});

			/* side bar - scroll in animation */
				$(document).ready(function() {
			    $('#footer').click(function() {
			        $('#footer').animate({
			        'marginTop' : "+=600px" //moves left
			        });
			    });

			    $("#wall-action-save").click(function() {
			        $('#footer').animate({'marginLeft' : "+=300px"});
			    });

			    $("#footer-close").click(function() {
			        $('#footer').animate({'marginLeft' : "-=300px"});
			    });

			/*Main logo - pulse animation*/
		    $(function () {
			    $('#logo').textillate({ 
			    	loop:true, 
			    	in:{effect:'pulse', delay: 100, delayScale: 10, shuffle:true }, 
			    	reverse:true, 
			    	out:{effect:'pulse', delay: 100, delayScale: 10, shuffle:true } });
			})

			});
</script>