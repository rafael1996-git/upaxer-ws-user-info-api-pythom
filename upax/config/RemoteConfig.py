'''
import boto3
import json
import upax.utils.properties as prop


class RemoteConfig:

    bucket = prop.bucket_name
    file = prop.file

    def __init__(self):
        self.client = boto3.client('s3')

    def get_config(self):
        return json.loads(self.client.get_object(Bucket=self.bucket, Key=self.file)['Body'].read().decode())
'''