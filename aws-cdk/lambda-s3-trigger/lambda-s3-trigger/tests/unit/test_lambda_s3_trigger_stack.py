import aws_cdk as core
import aws_cdk.assertions as assertions
from lambda_s3_trigger.lambda_s3_trigger_stack import LambdaS3TriggerStack


def test_sqs_queue_created():
    app = core.App()
    stack = LambdaS3TriggerStack(app, "lambda-s3-trigger")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = LambdaS3TriggerStack(app, "lambda-s3-trigger")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
