"""Amazon S3 buckets
An Amazon S3 bucket is a storage location to hold files. S3 files are referred to as objects.

This section describes how to use the AWS SDK for Python to perform common operations on S3 buckets.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
"""

import os
import logging
import boto3
from botocore.exceptions import ClientError

ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")
REGION = os.environ.get("AWS_DEFAULT_REGION")


# Create an Amazon S3 bucket
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region
    The name of an Amazon S3 bucket must be unique across all regions of the AWS platform.
    The bucket can be located in a specific region to minimize latency or to address regulatory requirements.

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None or region == "us-east-1":
            s3_client = boto3.client("s3")
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client("s3", region_name=region)
            location = {"LocationConstraint": region}
            s3_client.create_bucket(
                Bucket=bucket_name, CreateBucketConfiguration=location
            )
    except ClientError as e:
        logging.error(e)
        return False
    return True


# List existing buckets
def list_buckets():
    """List all the existing buckets for the AWS account"""
    # Retrieve the list of existing buckets
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    # Output the bucket names
    print("Existing buckets:")
    for bucket in response["Buckets"]:
        print(f'  {bucket["Name"]}')


if __name__ == "__main__":
    print("Create bucket")
    bucket_name = f"boto3-test-{ACCOUNT_ID}"
    create_bucket(bucket_name, region=REGION)

    print("List all the existing buckets for the AWS account")
    list_buckets()
