#!/usr/bin/env python3
import aws_cdk as cdk

import add_tags
from stacks.cdk_lambda_python_stack import CdkLambdaPythonStack


DEPLOYMENT_ENVIRONMENT = "dev"
NAME_PREFIX = "santi-{}-".format(DEPLOYMENT_ENVIRONMENT)
MAIN_RESOURCES_NAME = "lambda-docker-python-template"


app = cdk.App()

stack = CdkLambdaPythonStack(
    app,
    "{}-stack-compute-cdk".format(MAIN_RESOURCES_NAME),
    NAME_PREFIX,
    MAIN_RESOURCES_NAME,
    DEPLOYMENT_ENVIRONMENT,
)

add_tags.add_tags_to_stack(stack)

app.synth()
