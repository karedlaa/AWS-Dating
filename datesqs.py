from urlparse import urlparse

from boto3 import resource


class datesqs():
    sqs = resource('sqs', region_name='us-east-1')

    def createq(self, qname):
        res = self.sqs.create_queue(
            QueueName=qname,
            Attributes={
                'DelaySeconds': '0',
                'MaximumMessageSize': '262144',
                'MessageRetentionPeriod': '172800',
                'ReceiveMessageWaitTimeSeconds': '0',
                'VisibilityTimeout': '43200'
            }
        )
        return res

    def getq(self, qname):
        res = self.sqs.get_queue_by_name(QueueName=qname)
        return res

    def get_all_qs(self):
        qs = self.sqs.queues.all()
        return qs

    def get_uname(self, eachqurl):
        parsed = urlparse(eachqurl)
        user = parsed.path.split('/')[2]
        return user

    def get_all_qnames(self):
        qs = self.get_all_qs()
        qsurls = [q.url for q in qs]
        unames = [self.get_uname(eachurl) for eachurl in qsurls]
        return unames

    def check_q(self, qname):
        unames = self.get_all_qnames()
        if qname in unames:
            return True
        return False

    def send_mes(self, sender, receiver, mes):
        qname = sender + "_" + receiver
        if self.check_q(qname):
            queue = self.getq(qname)
        else:
            queue = self.createq(qname)
        res = queue.send_message(MessageBody=mes)
        if res.get('ResponseMetadata')['HTTPStatusCode'] == 200:
            return True
        else:
            print res
        return False

    def get_mes(self, receiver, sender):
        qname = sender + "_" + receiver
        msgs = []
        if self.check_q(qname):
            queue = self.getq(qname)
            msgs_inq = queue.receive_messages(
                MaxNumberOfMessages=10,
                VisibilityTimeout=123,
                WaitTimeSeconds=12
            )
            for msg in msgs_inq:
                msgs.append(msg.body)
        return msgs

        # sqs=datesqs()
        # print sqs.get_mes("tester4", "user2")
