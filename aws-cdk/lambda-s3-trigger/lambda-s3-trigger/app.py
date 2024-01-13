#!/usr/bin/env python3

from aws_cdk import App
import aws_cdk as cdk
import os

from lambda_s3_trigger.lambda_s3_trigger_stack import S3TriggerStack
from lambda_s3_trigger.iam_role_stack import IamRoleStack
from lambda_s3_trigger.custom_s3_bucket import CustomS3ResourcePolicyStack
from lambda_s3_trigger.s3_stack import S3Stack


app = App()

env = os.environ.get('ENV')

IamRoleStack(app, "IamRoleStack")
CustomS3ResourcePolicyStack(app,"CustomS3ResourcePolicyStack")
S3Stack(app,"S3Stack")

env_prod_us = cdk.Environment(region="us-east-1",account="604474828993")
env_dev_us = cdk.Environment(region="us-east-1",account="604474828993")
env_qa_us = cdk.Environment(region="us-west-1",account="604474828993")

if env == "prod":
 S3TriggerStack(app, f"S3TriggerStack-{env}" , env=env_prod_us)   
elif env == "dev":
 S3TriggerStack(app, f"S3TriggerStack-{env}" , env=env_dev_us)   
elif env == "qa":
 S3TriggerStack(app, f"S3TriggerStack-{env}" , env=env_qa_us)   
  

app.synth()
