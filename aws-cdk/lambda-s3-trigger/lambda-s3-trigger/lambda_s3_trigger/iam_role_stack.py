from constructs import Construct
from aws_cdk import (
    aws_iam as _iam,
    Stack
)
import aws_cdk as core


class IamRoleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        custom_iam_role = _iam.Role(
            self,
            'customRole',
            # assumed_by=_iam.AccountPrincipal(f"{core.Aws.ACCOUNT_ID}"),
            assumed_by=_iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="custom_iam_role"
        )   


        custom_iam_role.add_managed_policy(_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")) 


        #  Create Managed Policy & Attach to Role
        list_ec2_policy = _iam.ManagedPolicy(
            self,
            "listEc2Instances",
            description="list ec2 isntances in the account",
            managed_policy_name="list_ec2_policy",
            statements=[
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    actions=[
                        "ec2:Describe*",
                        "cloudwatch:Describe*",
                        "cloudwatch:Get*"
                    ],
                    resources=["*"]
                )
            ],
            roles=[
                custom_iam_role
            ]
        )

        core.CfnOutput(
            self, "MyRoleOutput",
            value=custom_iam_role.role_arn,
            export_name="MyRoleExportName"
        )


