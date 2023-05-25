"""Uploading files
The AWS SDK for Python provides a pair of methods to upload a file to an S3 bucket.

The `upload_file` method accepts a file name, a bucket name, and an object name. The method handles 
large files by splitting them into smaller chunks and uploading each chunk in parallel.

The `upload_fileobj` method accepts a readable file-like object. The file object must be opened in binary mode, not text mode.

s3 = boto3.client('s3')
with open("FILE_NAME", "rb") as f:
    s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")

The `upload_file` and `upload_fileobj` methods are provided by the S3 Client, Bucket, and Object classes. 
The method functionality provided by each class is identical. No benefits are gained by calling one class’s 
method over another’s. Use whichever class is most convenient.

The ExtraArgs parameter
Both upload_file and upload_fileobj accept an optional ExtraArgs parameter that can be used for various purposes. 
The list of valid ExtraArgs settings is specified in the ALLOWED_UPLOAD_ARGS attribute of the S3Transfer object at boto3.s3.transfer.S3Transfer.ALLOWED_UPLOAD_ARGS.

The following ExtraArgs setting specifies metadata to attach to the S3 object.

s3.upload_file(
    'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME',
    ExtraArgs={'Metadata': {'mykey': 'myvalue'}}
)

The following ExtraArgs setting assigns the canned ACL (access control list) value ‘public-read’ to the S3 object.

s3.upload_file(
    'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME',
    ExtraArgs={'ACL': 'public-read'}
)

The ExtraArgs parameter can also be used to set custom or multiple ACLs.

s3.upload_file(
    'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME',
    ExtraArgs={
        'GrantRead': 'uri="http://acs.amazonaws.com/groups/global/AllUsers"',
        'GrantFullControl': 'id="01234567890abcdefg"',
    }
)

The Callback parameter
Both upload_file and upload_fileobj accept an optional Callback parameter. 
The parameter references a class that the Python SDK invokes intermittently during the transfer operation.

Invoking a Python class executes the class’s __call__ method. For each invocation, the class is passed the number of 
bytes transferred up to that point. This information can be used to implement a progress monitor.

The following Callback setting instructs the Python SDK to create an instance of the ProgressPercentage class. 
During the upload, the instance’s __call__ method will be invoked intermittently.

s3.upload_file(
    'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME',
    Callback=ProgressPercentage('FILE_NAME')
)

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
"""

import os
import sys
import threading
import logging
import boto3
from botocore.exceptions import ClientError


# An example implementation of the ProcessPercentage class
class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)\n"
                % (self._filename, self._seen_so_far, self._size, percentage)
            )
            sys.stdout.flush()


def upload_file_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(
            file_name, bucket, object_name, Callback=ProgressPercentage(file_name)
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")
    file_name = "../../networking/images/vpc-2.png"
    bucket_name = f"boto3-test-{ACCOUNT_ID}"
    print(f"Upload a file {file_name} to an S3 bucket")
    upload_file_s3(file_name, bucket_name)
