# AWS SDK

## Resources
- [What is an SDK](https://aws.amazon.com/what-is/sdk/)
- [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)

### Using Boto3

To use Boto3, you must first import it and indicate which service or services you’re going to use:

```python
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
```

Now that you have an `s3` resource, you can make send requests to the service. The following code uses the buckets collection to print out all `bucket` names:

```python
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
```

You can also upload and download binary data. For example, the following uploads a new file to S3, assuming that the bucket `my-bucket` already exists:

```sh
# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)
```

[Resources](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html#guide-resources) and [Collections](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html#guide-collections) are covered in more detail in the following sections.


### Code Examples
- [AWS SDK Code Examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/examples.html)
