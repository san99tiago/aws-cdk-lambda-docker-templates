import os

from aws_cdk import (
    Stack,
    CfnOutput,
    aws_iam,
    aws_lambda,
    Duration,
    aws_logs,
)
from constructs import Construct


class CdkLambdaPythonStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        name_prefix: str,
        main_resources_name: str,
        deployment_environment: str,
        **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.construct_id = construct_id
        self.name_prefix = name_prefix
        self.main_resources_name = main_resources_name
        self.deployment_environment = deployment_environment


        # Lambda function creation
        self.create_policy_statement_for_lambda()
        self.create_lambda_role_policy()
        self.create_lambda_role()
        self.create_docker_lambda_function()

        # Relevant CloudFormation outputs
        self.show_cloudformation_outputs()


    def create_policy_statement_for_lambda(self):
        """
        Method to create IAM policy statement for Lambda execution.
        """
        self.s3_access_policy_statement = aws_iam.PolicyStatement(
            actions=[
                "s3:*"
            ],
            effect=aws_iam.Effect.ALLOW,
            resources=[
                "*",
            ],
        )


    def create_lambda_role_policy(self):
        """
        Method to create IAM Policy based on all policy statements.
        """
        self.lambda_role_policy = aws_iam.Policy(
            self,
            id="{}-Policy".format(self.construct_id),
            policy_name="{}{}-Policy".format(self.name_prefix, self.main_resources_name),
            statements=[
                self.s3_access_policy_statement,
            ],
        )


    def create_lambda_role(self):
        """
        Method that creates the role for Lambda function execution.
        """
        self.lambda_role = aws_iam.Role(
            self,
            id="{}-Role".format(self.construct_id),
            role_name="{}{}-Role".format(self.name_prefix, self.main_resources_name),
            description="Role for {}".format(self.main_resources_name),
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")],
        )

        self.lambda_role.attach_inline_policy(self.lambda_role_policy)


    def create_docker_lambda_function(self):
        """
        Method that creates the main Lambda function based on a Docker image.
        """
        # Get relative path for folder that contains Lambda function sources
        # ! Note--> we must obtain parent dirs to create path (that's why there is "os.path.dirname()")
        PATH_TO_FUNCTION_FOLDER = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "lambdas",
            "python",
        )
        print("Source code for lambda function obtained from: ", PATH_TO_FUNCTION_FOLDER)

        self.docker_lambda_function = aws_lambda.DockerImageFunction(
            self,
            id="{}-Lambda".format(self.construct_id),
            code=aws_lambda.DockerImageCode.from_image_asset(PATH_TO_FUNCTION_FOLDER),
            function_name="{}{}".format(self.name_prefix, self.main_resources_name),
            environment={"ENVIRONMENT": self.environment, "OWNER": "Santiago Garcia Arango"},
            description="Simple example of Docker-Python image for Lambda Functions",
            role=self.lambda_role,
            timeout=Duration.seconds(15),
            memory_size=128,
            log_retention=aws_logs.RetentionDays.ONE_WEEK,
        )

        self.docker_lambda_function.add_alias(self.deployment_environment)


    def show_cloudformation_outputs(self):
        """
        Method to create/add the relevant CloudFormation outputs.
        """

        CfnOutput(
            self,
            "DeploymentEnvironment",
            value=self.deployment_environment,
            description="Deployment environment",
        )

        CfnOutput(
            self,
            "LambdaFunctionARN",
            value=self.docker_lambda_function.function_arn,
            description="ARN of the created Lambda function",
        )

        CfnOutput(
            self,
            "LambdaFunctionRoleARN",
            value=self.docker_lambda_function.role.role_arn,
            description="Role for the created Lambda function",
        )
