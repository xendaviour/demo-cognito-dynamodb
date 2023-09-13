#importing packages
import json
import boto3
#function definition
def lambda_handler(event,context):
	dynamodb = boto3.resource('dynamodb')
	#table name
	table = dynamodb.Table('dbserver')
	#inserting values into table
	user_attributes = event['request']['userAttributes']
	user_email = user_attributes['email']
	response = table.put_item(
	Item={
			'email':user_email ,
			
		}
	)
	return event

