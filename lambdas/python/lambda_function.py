# SAMPLE PYTHON LAMBDA FUNCTION FOR DOCKER IMAGE
# Santiago Garcia Arango

# Built-in imports
import boto3
import json


s3_client = boto3.client("s3")


def handler(event, context):
    print("Event: ", event)
    print("Context: ", context)

    try:
        response = s3_client.list_buckets()
        buckets = []
        for bucket in response["Buckets"]:
            buckets.append(bucket["Name"])
        return_message = {
            "buckets": buckets
        }
    except Exception as e:
        return_message = {
            "message": "Error on the S3 list buckets operation {}".format(e)
        }

    print(json.dumps(return_message, indent=2, default=str))

    return {
        "statusCode": 200,
        "body": json.dumps(return_message, indent=2, default=str)
    }
