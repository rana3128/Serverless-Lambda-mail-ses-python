import boto3
import json

region_name = "us-west-2"
aws_access_key_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
aws_secret_access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def sendEmailHandler(event, context):
    data = event['body']
    name = data['name']
    source = data['source']
    subject = data['subject']
    message = data['message']
    destination = data['destination']
    _message = "Message from: " + name + "\nEmail: " + source + "\nMessage content: " + message

    client = boto3.client('ses')

    response = client.send_email(
        Destination={
            'ToAddresses': [destination]
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': _message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source=source,
    )
    return {
        "mesg":_message,
        "region": str(region_name),
        "response": response
    }
