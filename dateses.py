# -*- coding: utf-8 -*-
import boto3

client = boto3.client('ses', region_name='us-east-1')

body = "test body"
body = body.encode('UTF-8')
response = client.send_email(
    Source='rtr.ravitejareddy@gmail.com',
    Destination={
        'ToAddresses': [
        "aamerm21@gmail.com",
        ]
    },
    Message={
        'Subject': {
        'Data': 'Testme',
        'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': body ,
                'Charset': 'UTF-8'
            }
        }
    }
)