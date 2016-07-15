var channel_name = 'user2_tester4';

$(function() {
  var subscription_setup = {
    channel: channel_name,
    callback: function(new_message) {
      var sent_at = new Date(new_message.sent_at);
      var date = sent_at.getDate(),
          month = sent_at.getMonth(),
          year = sent_at.getFullYear(),
          hour = sent_at.getHours(),
          minutes = sent_at.getMinutes();
      var sent_at_formatted = month + '/' + date + '/' + year
        + ' ' + hour + ':' + minutes;
      var message_html = $("<div class='message'>"
        + sent_at_formatted + ' -- '
        + new_message.user_name +
        " says: " + new_message.content + "</div>");
      $('#messages').prepend(message_html);
    }
  };
  PUBNUB.subscribe(subscription_setup);
});

function send_message() {
  var name = $('#name').val();
  var message_text = $('#message').val();
  var message_to_publish = {
    channel: channel_name,
    message: {
      user_name: name,
      content: message_text
    }
  };
  PUBNUB.publish(message_to_publish);
  return false;
}