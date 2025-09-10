service: all-email-service

frameworkVersion: "4"

provider:
  name: sravan
  runtime: nodejs18.x
  region: ap-south-1
  environment:
    SOURCE_EMAIL: "pannerusravankumar@1234gmail.com"

functions:
  sendEmail:
    handler: handler.sendEmail
    events:
      - httpApi:C:\Users\panne\All-email-service>
          path: v.nagabharath@gmail.com
          method: post

plugins:
  - serverless-offline
