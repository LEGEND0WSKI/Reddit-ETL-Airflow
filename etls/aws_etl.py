import boto3
from botocore.exceptions import ClientError
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY

# 1.conenct to s3
def connect_to_s3():
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_ACCESS_KEY)
        return s3
    except ClientError as e:
        print(e)

# 2.create s3 bucket
def create_bucket_if_not_exist(s3, bucket):
    try:
        response = s3.head_bucket(Bucket=bucket)
        print("Bucket already exists")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            s3.create_bucket(Bucket=bucket)
            print("Bucket is created")
        else:
            print(e)

# 3.upload to s3
def upload_to_s3(s3, file_path, bucket, s3_file_name):
    try:
        s3.upload_file(file_path, bucket, 'raw/' + s3_file_name)
        print('File uploaded to S3')
    except ClientError as e:
        print(e)
