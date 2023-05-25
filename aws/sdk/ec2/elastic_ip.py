"""Using Elastic IP addresses in Amazon EC2

The scenario
An Elastic IP address is a static IP address designed for dynamic cloud computing. 
An Elastic IP address is associated with your AWS account. It is a public IP address, 
which is reachable from the Internet. If your instance does not have a public IP address, 
you can associate an Elastic IP address with your instance to enable communication with the Internet.

In this example, Python code performs several Amazon EC2 operations involving Elastic IP addresses. 
The code uses the AWS SDK for Python to manage IAM access keys using these methods of the EC2 client class:

- describe_addresses.
- allocate_address.
- release_address.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-elastic-ip-addresses.html
"""

import json
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")


# Describe Elastic IP addresses
def describe_addresses():
    """The example below shows how to:
    - Describe Elastic IP addresses using describe_addresses.
    """
    filters = [{"Name": "domain", "Values": ["vpc"]}]
    response = ec2.describe_addresses(Filters=filters)
    addresses = response["Addresses"]
    print(json.dumps({"Addresses": addresses}, indent=2))


# Allocate and associate an Elastic IP address with an Amazon EC2 instance
def allocate_address(INSTANCE_ID):
    """he example below shows how to:
    - Acquire an Elastic IP address using allocate_address.
    """
    try:
        allocation = ec2.allocate_address(Domain="vpc")
        # print(json.dumps(allocation, indent=2))
        AllocationId = allocation["AllocationId"]
        print(json.dumps({"allocation id": AllocationId}, indent=2))
        response = ec2.associate_address(
            AllocationId=AllocationId, InstanceId=INSTANCE_ID
        )
        AssociationId = response["AssociationId"]
        print(json.dumps({"AssociationId": AssociationId}, indent=2))
        describe_addresses()
    except ClientError as e:
        print(e)

    return AllocationId, AssociationId


# Release an Elastic IP address
def release_address(ALLOCATION_ID, ASSOCIATION_ID):
    """After releasing an Elastic IP address, it is released to the IP address pool and might be unavailable to you.
    Be sure to update your DNS records and any servers or devices that communicate with the address.
    If you attempt to release an Elastic IP address that you already released, you’ll get an AuthFailure error
    if the address is already allocated to another AWS account.

    The example below shows how to:
    - Release the specified Elastic IP address using release_address.
    """
    try:
        _ = ec2.disassociate_address(
            AssociationId=ASSOCIATION_ID,
        )
        print(f"Address {ALLOCATION_ID} disassociated")
        response = ec2.release_address(AllocationId=ALLOCATION_ID)
        print(f"Address {ALLOCATION_ID} released")
    except ClientError as e:
        print(e)


if __name__ == "__main__":
    print("Describe Elastic IP addresses")
    describe_addresses()

    print("Allocate and associate an Elastic IP address with an Amazon EC2 instance")
    instance_id = "i-07a258fcf34fae482"
    allocation_id, association_id = allocate_address(instance_id)

    print("Release an Elastic IP address")
    release_address(allocation_id, association_id)
