# Sample lambda function

import boto3


def handler(event, context):
    print("Event: ", event)
    print("Context: ", context)
    return {
        "statusCode": 200,
        "body": "Sample response"
    }
