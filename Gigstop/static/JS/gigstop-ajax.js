			$(document).ready(function(){
			$('.likethis').click(function(){
                var eventid =this.value;
                alert(eventid);
                 $.get('/app/interested_band/', {event_id: eventid}, function(data){
                  $('#listobands').html(data);
                  $('.likethis').hide();
                });

    		});

			});