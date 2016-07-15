# P2dating
Cloud Computing CS6065 P2 project
The project is a simple dating website(dateapp).  In this dateapp users can register and get the matching people based on their interests. User can chat and message with the interested people. They can subscribe for mail and mobile alerts about the site tips. If subscribed users will get alerts about dating tips. Chat system doesn't save chat message for security reasons and since we used pubnub who is giving realtime chat service socket help.

python Flask REST framework is used for webservices. And to deploy in Amazon eservices Tornado is implemented in p2dateapp.py and deployed in ec2.

##Application URL:

http://ec2-54-152-106-134.compute-1.amazonaws.com

##Services used:

Amazon EC2 --> hosting website in cloud.

Amazon Dynamo DB --> User data is stored in Dynamo DB database.

Pub Nub --> This service is used implementing chat system.

Amazon SNS --> This service is used to send notification service.

##Architecture
Click below link to view the architecture of the project

https://github.uc.edu/raw/bollara/p2dating/master/static/arch.PNG?token=AAAH_eCSxQBvaRxsaKvQKyUME84A70EJks5W9chSwA%3D%3D

##Future Scope: 

Most of the below services are almost implemented as libraries and need some adjustments to make it work effectively.

•	Email to interested people using Amazon SES service. 

• Amazon S3  -->This service is used for storing user profile pictures.

•	Amazon SQS --> This service is used for messaging between users.

•	Email and phone number verification while registering

•	Refine interested people by age, location and mutual interests.

##Limitations or Things not fixed:

• Html validations and UI mistakes are not taken care for this application.

• Chat service implemented is currenly handling only one user.
