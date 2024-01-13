from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications ,
    aws_iam as _iam,
    aws_lambda_event_sources as eventsources,
    Stack
)
from constructs import Construct
import aws_cdk as core
import os

class S3TriggerStack(Stack):
    
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:

        env = os.environ.get('ENV')
        function_name = f"oversight-lambda-function-{env}"
        bucket_name = f"ovs-bigdata-{env}"


        super().__init__(scope, id, **kwargs)


        imported_role = _iam.Role.from_role_arn(
            self, "ImportedRole",
            role_arn=core.Fn.import_value("MyRoleExportName")
        )

        # create lambda function
        function = _lambda.Function(self, f"lambda_function-{env}",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    function_name=function_name,
                                    code=_lambda.Code.from_asset("./lambda"),
                                    role=imported_role)
                            
        # create s3 bucket
        s3 = _s3.Bucket(self, f"s3bucketforlamda-{env}",bucket_name=bucket_name)

    

        # s3 = _s3.Bucket.from_bucket_attributes(
        #     self, 'LambdaCodeBucket',
        #     bucket_name='mytestbucket-boomi'
        # )
        # bucket = _s3.Bucket.from_bucket_attributes(
        #     self, 'LambdaCodeBucket2',
        #     bucket_name='mytestbucket-boomi2'
        # )

        # function.add_event_source(eventsources.S3EventSource(bucket,
        # events=[_s3.EventType.OBJECT_CREATED]
        # ))
        # function2.add_event_source(eventsources.S3EventSource(bucket2,
        # events=[_s3.EventType.OBJECT_CREATED]
        # ))



 
        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)
 
        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
