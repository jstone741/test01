import boto3
from botocore.config import Config

service_name = 's3'
access_key = 'a1a59c6954024fe9ab45b7faa52d1e29'
secret_key = 'edd0189cab4b47a09e92149da237ecd0'
endpoint_url = 'http://storage.gscdn.com'
region_name = 'us-east-1'

my_config = Config(
        signature_version='s3v4'
)

if __name__ == "__main__":
        s3 = boto3.client(service_name, endpoint_url=endpoint_url, region_name=region_name, config=my_config, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        bucket_name = 'test'

        # list all in the bucket
        max_keys = 300
        response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys)

        print('list all in the bucket')

        while True:
                print('IsTruncated=%r' % response.get('IsTruncated'))
                print('Marker=%s' % response.get('Marker'))
                print('NextMarker=%s' % response.get('NextMarker'))

                print('Object List')
                for content in response.get('Contents'):
                        print(' Name=%s, Size=%d, Owner=%s' % (content.get('Key'), content.get('Size'), content.get('Owner').get('ID')))

                if response.get('IsTruncated'):
                        response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys,
                        Marker=response.get('NextMarker'))
                else:
                        break

        # top level folders and files in the bucket
        delimiter = '/'
        max_keys = 300

        response = s3.list_objects(Bucket=bucket_name, Delimiter=delimiter, MaxKeys=max_keys)

        print('top level folders and files in the bucket')

        while True:
                print('IsTruncated=%r' % response.get('IsTruncated'))
                print('Marker=%s' % response.get('Marker'))
                print('NextMarker=%s' % response.get('NextMarker'))

                if response.get('CommonPrefixes') is not None:
                        print('Folder List')
                        for folder in response.get('CommonPrefixes'):
                                print(' Name=%s' % folder.get('Prefix'))

                if response.get('Contents') is not None:
                        print('File List')
                        for content in response.get('Contents'):
                                print(' Name=%s, Size=%d, Owner=%s' % (content.get('Key'), content.get('Size'), content.get('Owner').get('ID')))

                if response.get('IsTruncated'):
                        response = s3.list_objects(Bucket=bucket_name, Delimiter=delimiter, MaxKeys=max_keys, Marker=response.get('NextMarker'))

                else:
                        break