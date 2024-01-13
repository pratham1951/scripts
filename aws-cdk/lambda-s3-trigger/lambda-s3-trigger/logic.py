if env == "prod":
  env = cdk.Environment(region="us-east-1",account="604474828993")
elif env == "dev":
  env = cdk.Environment(region="us-east-2",account="604474828993")
elif env == "qa":
  env = cdk.Environment(region="us-west-1",account="604474828993")  

S3TriggerStack(app, "S3TriggerStack",env=env)      
