import boto3
from botocore.config import Config

service_name = 's3'
access_key = '729184ca0f1e4e13852466b94e2cb2c0'
secret_key = 'b8e3e3417c6b47938d2e45c8bb9b80eb'
endpoint_url = 'http://storage.gscdn.com'
region_name = 'us-east-1'
my_config = Config(
        signature_version='s3v4')

if __name__ == "__main__":
        s3 = boto3.client(service_name, endpoint_url=endpoint_url, region_name=region_name, config=my_config, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

response = s3.list_buckets()

for bucket in response.get('Buckets', []):
        print(bucket.get('Name'))