import aws_cdk as core
import aws_cdk.assertions as assertions

from stacks.cdk_lambda_python_stack import CdkLambdaPythonStack

DEPLOYMENT_ENVIRONMENT = "dev"
NAME_PREFIX = "santi-{}-".format(DEPLOYMENT_ENVIRONMENT)
MAIN_RESOURCES_NAME = "lambda-docker-python-template"

app = core.App()

stack = CdkLambdaPythonStack(
    app,
    "{}-stack-compute-cdk".format(MAIN_RESOURCES_NAME),
    NAME_PREFIX,
    MAIN_RESOURCES_NAME,
    DEPLOYMENT_ENVIRONMENT,
)
template = assertions.Template.from_stack(stack)

def test_iam_policy_for_lambda_created():

    template.has_resource_properties(
        "AWS::IAM::Policy",
        {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Action":"s3:*",
                        "Effect": "Allow"
                    }
                ]
            },
            "PolicyName": "santi-dev-lambda-docker-python-template-Policy"
        }
    )


def test_iam_role_for_lambda_created():
    template.has_resource_properties(
        "AWS::IAM::Role",
        {
            "AssumeRolePolicyDocument": {
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    }
                }
            ],
            },
            "RoleName": "santi-dev-lambda-docker-python-template-Role",
        }
    )


def test_lambda_created():
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "FunctionName": "santi-dev-lambda-docker-python-template",
            "MemorySize": 128,
            "Timeout": 15
        }
    )


def test_lambda_alias_created():
    template.has_resource_properties(
        "AWS::Lambda::Alias",
        {
            "Name": "dev"
        }
    )

def test_mandatory_outputs():
    template.has_output(
        "DeploymentEnvironment",
        {
            "Value": "dev"
        })

    template.has_output("LambdaFunctionARN", {})
    template.has_output("LambdaFunctionRoleARN", {})
