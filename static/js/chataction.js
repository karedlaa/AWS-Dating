$(document).ready(function(){

	$('.msg_head').click(function(){
		$('.msg_wrap').slideToggle('slow');
	});

	$('.close').click(function(){
		$('.msg_box').hide();
	});

	$('.userchat').click(function(){
		$('.msg_wrap').show();
		$('.msg_box').show();
	});

	$('textarea').keypress(
    function(e){
        if (e.keyCode == 13) {
            var msg = $(this).val();
            var sender = $('#myusername').val();
            var receiver = $('#mylikeduser').val();
			$(this).val('');
			if(msg!='')
            $('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
			$.ajax({
              type: "POST",
              url:$('#myusername').val(),
              data: {
              "myusername":sender,
              "liked_user":receiver,
              "msg":msg
              }

            });
            var channel = $('#mychannel').val()
            var msg_to_publish = {
            channel: channel,
            message:{
            user_name: sender,
            content: msg
            }
            };
            PUBNUB.publish(msg_to_publish);
        }
    });

    $(function() {
        var sender = $('#myusername').val();
        var receiver = $('#mylikeduser').val();
        var channel = $('#mychannel').val();
        var subscription_setup = {
            channel: channel,
            callback: function(new_message) {
                $('<div class="msg_b">'+new_message.content+'</div>').insertBefore('.msg_push');
            }
        };
        PUBNUB.subscribe(subscription_setup);
    });

});