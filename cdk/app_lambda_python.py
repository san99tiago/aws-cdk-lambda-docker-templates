#!/usr/bin/env python3

import os

import aws_cdk as cdk

import add_tags
from stacks.cdk_lambda_python_stack import CdkLambdaPythonStack


DEPLOYMENT_ENVIRONMENT = "dev"
NAME_PREFIX = "santi-{}-".format(DEPLOYMENT_ENVIRONMENT)
MAIN_RESOURCES_NAME = "lambda-docker-python-template"


app = cdk.App()

stack = CdkLambdaPythonStack(
    app,
    "{}-stack-cdk".format(MAIN_RESOURCES_NAME),
    NAME_PREFIX,
    MAIN_RESOURCES_NAME,
    DEPLOYMENT_ENVIRONMENT,
    env={
        "account": os.getenv("CDK_DEFAULT_ACCOUNT"),
        "region": os.getenv("CDK_DEFAULT_REGION"),
    },
    description="Stack for {} infrastructure in {} environment".format(MAIN_RESOURCES_NAME, DEPLOYMENT_ENVIRONMENT),
)

add_tags.add_tags_to_stack(stack, DEPLOYMENT_ENVIRONMENT, MAIN_RESOURCES_NAME)

app.synth()
