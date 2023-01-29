# SAMPLE PYTHON LAMBDA FUNCTION FOR DOCKER IMAGE
# Santiago Garcia Arango

# Built-in imports
import boto3
import json

# Own imports
import sample_code_1
import sample_code_2

s3_client = boto3.client("s3")


def handler(event, context):
    print("Event: ", event)
    print("Context: ", context)

    try:
        github_username = event["github_user"]
    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "you did not specify your GitHub user 'github_user' in the JSON event. {}".format(e)}, indent=2, default=str)
        }

    response_1 = sample_code_1.list_buckets(s3_client)
    response_2 = sample_code_2.get_github_information_from_user(github_username)

    response_body = {
        "response_1_list_buckets": response_1,
        "response_2_github_bio": response_2,
    }

    print(json.dumps(response_body, indent=2, default=str))

    return {
        "statusCode": 200,
        "body": json.dumps(response_body, indent=2, default=str)
    }


## ONLY FOR LOCAL TESTS! (OWN VALIDATIONS)
if __name__ == "__main__":
    response = handler(
        {
            "github_user": "san99tiago"
        },
        None
    )
    print("statusCode: {}".format(response["statusCode"]))
    print("body: {}".format(json.loads(response["body"])))
