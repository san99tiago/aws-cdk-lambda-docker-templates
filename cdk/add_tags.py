#!/usr/bin/env python3

import aws_cdk as cdk

def add_tags_to_stack(stack, environment, main_resource_name):
    """
    Simple function to add custom tags to stack in a centralized (equal) approach.
    :param environment: str --> environment of the deployment (Example: "Development").
    :param main_resource_name: str --> resource name identifier for the deployment.
    """

    cdk.Tags.of(stack).add("Environment", environment)
    cdk.Tags.of(stack).add("MainResourceName", main_resource_name)
    cdk.Tags.of(stack).add("RepositoryUrl", "https://github.com/san99tiago/aws-cdk-lambda-docker-templates")
    cdk.Tags.of(stack).add("Source", "aws-cdk-lambda-docker-templates")
    cdk.Tags.of(stack).add("Owner", "Santiago Garcia Arango")
