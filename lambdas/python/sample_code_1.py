# Built-in imports
import boto3


def list_buckets(s3_client):
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
            "error": "Error on the S3 list buckets operation {}".format(e)
        }
    return return_message


## ONLY FOR LOCAL TESTS! (OWN VALIDATIONS)
if __name__ == "__main__":
    s3_client = boto3.client("s3")
    print(list_buckets(s3_client))
