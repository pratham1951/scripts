from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3,
)
import aws_cdk as core
import json


class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         # Read values from the JSON file
        with open('config.json') as json_file:
            config_data = json.load(json_file)

          # Create S3 buckets
        for bucket_info in config_data.get('buckets', []):
            bucket_name = bucket_info.get('bucket_name')
            self.create_s3_bucket(bucket_name)


        #  # Create S3 folders
        # for folder_path in config_data.get('folders', []):
        #     self.create_s3_folder(folder_path)    

    def create_s3_bucket(self, bucket_name: str) -> None:
        # Create an S3 bucket
        s3.Bucket(self, f'S3Bucket-{bucket_name}',
               bucket_name=bucket_name,
               removal_policy=core.RemovalPolicy.DESTROY)   

    # def create_s3_folder(self, folder_path: str) -> None:
    #     # Extract bucket name and folder path
    #     bucket_name, folder_key = folder_path.split('/', 1)

    #     # Create an S3 object (mimicking a folder)
    #     bucket = s3.Bucket.from_bucket_name(self, f'S3Object-{bucket_name}', bucket_name)
    #     bucket.add_object(folder_key + '/', content='')
              


        


       
