import boto3


class datesns():
    client = boto3.client('sns', region_name='us-east-1')

    def sendtoSubscribe(self):
        TOPIC = 'arn:aws:sns:us-east-1:060013835473:datetips'
        URL = '<Body of Message in this example I used a url>'
        pub = self.client.publish(TopicArn=TOPIC, Message=URL)

    def subscribe1(self, email):
        TOPIC = 'arn:aws:sns:us-east-1:060013835473:datetips'
        URL = '<Body of Message in this example I used a url>'
        response = self.client.subscribe(
            TopicArn=TOPIC,
            Protocol='email',
            Endpoint=email
        )
        return response

    def subscribe1_phone(self, phone):
        TOPIC = 'arn:aws:sns:us-east-1:060013835473:datetips'
        URL = '<Body of Message in this example I used a url>'
        response = self.client.subscribe(
            TopicArn=TOPIC,
            Protocol='sms',
            Endpoint=phone
        )
        return response

# notification = datesns()
# notification.subscribe1("RanjithGangam1@gmail.com")
# notification.sendtoSubscribe()
