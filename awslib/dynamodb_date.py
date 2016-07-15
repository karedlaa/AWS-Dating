import json

import boto3
from boto3.dynamodb.conditions import Key, Attr


class dynamodb_date():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('dateappusers')

    def insert_user(self, name, pwd, email, phone, dob,
                    addrline1, addrline2, addrCity, addrState,
                    addrCountry, gender, interestedIn):
        self.table.put_item(
            Item={
                'uname': name,
                'password': pwd,
                'email': email,
                'phone': phone,
                'dob': dob,
                'address':{
                    'line1': addrline1,
                    'line2': addrline2,
                    'city': addrCity,
                    'state': addrState,
                    'country': addrCountry
                },
                'gender':gender,
                'interestedIn':interestedIn,
                'active':0
            }
        )

    def get_user(self, uname):
        response = self.table.get_item(
            Key={
                'uname': uname
            }
        )
        item = response['Item']
        return(item)

    def get_users(self):
        response = self.table.get_item(
            Key={
                'uname': 'tester1'
            }
        )
        item = response['Item']
        print(json.dumps(item))

    def delete_user(self, uname):
        self.table.delete_item(
            Key={
                'uname': uname
            }
        )

    def db_query(self, name):
        response = self.table.query(
            KeyConditionExpression=Key('uname').eq(name)
        )
        items = response['Items']
        print(json.dumps(items))

    def get_all(self, gender):
        response = self.table.scan(
            FilterExpression=Attr('gender').eq(gender)
        )
        items = response['Items']
        for each in items:
            print json.dumps(each)

    def get_intereseted(self, uname, gender, interested_in):
        response = self.table.scan(
            FilterExpression=Attr('gender').eq(gender) & Attr('interestedIn').eq(interested_in) & Attr('uname').ne(uname)
        )
        items = response['Items']
        return items

    def get_people_in_city(self, city):
        response = self.table.scan(
            FilterExpression=Attr('address.state').eq(city)
        )
        items = response['Items']
        print(items)


        # name = "tester5"
        # pwd = "minceme"
        ##email = "tester1@gmail.com"
        # phone = "998998998"
        # dob="2/3/1989"
        # addrline1="27 MLK"
        # addrline2="Apt#1"
        # addrCity = "newyork"
        # addrState = "DC"
        # addrCountry="US"
        # gender="M"
        # interestedIn="F"

#db = dynamodb_date()
#print(db.table.creation_date_time)
#db.insert_user(name, pwd, email, phone, dob, addrline1, addrline2, addrCity, addrState, addrCountry, gender, interestedIn)
#print db.get_user("user2")
#db.delete_user("tester2")
#db.db_query("tester2")
#db.get_all("M")
#db.get_all("F")
#db.get_intereseted("F","M")
#db.get_people_in_city("DC")