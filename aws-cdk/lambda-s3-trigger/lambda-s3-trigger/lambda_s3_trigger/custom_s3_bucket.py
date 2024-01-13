import aws_cdk as core
from constructs import Construct
from aws_cdk import (
    aws_s3 as _s3,
    aws_s3_notifications ,
    aws_iam as _iam,
    Stack
)


class CustomS3ResourcePolicyStack(Stack):

    def __init__(self, scope: Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 Bucket):
        resource_bucket = _s3.Bucket(self,
                                  "resource_bucket",
                                  versioned=False,
                                  bucket_name="big-data-ovs",
                                  removal_policy=core.RemovalPolicy.DESTROY
                                  )

        # Add Bucket Resource policy
        # resource_bucket.add_to_resource_policy(
        #     _iam.PolicyStatement(
        #         effect=_iam.Effect.ALLOW,
        #         actions=["s3:GetObject"],
        #         resources=[resource_bucket.arn_for_objects("*")],
        #         principals=[_iam.AnyPrincipal()]
        #     )
        # )

        # resource_bucket.add_to_resource_policy(
        #     _iam.PolicyStatement(
        #         effect=_iam.Effect.DENY,
        #         actions=["s3:*"],
        #         resources=[f"{resource_bucket.bucket_arn}/*"],
        #         principals=[_iam.AnyPrincipal()],
        #         conditions={
        #             "Bool": {"aws:SecureTransport": False}
        #         }
        #     )
        # )