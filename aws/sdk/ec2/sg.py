"""The scenario
An Amazon EC2 security group acts as a virtual firewall that controls the traffic for one or more instances. 
You add rules to each security group to allow traffic to or from its associated instances. You can modify the 
rules for a security group at any time; the new rules are automatically applied to all instances that are associated with the security group.

In this example, Python code is used to perform several Amazon EC2 operations involving security groups. 
The code uses the AWS SDK for Python to manage IAM access keys using these methods of the EC2 client class:

- describe_security_groups.
- authorize_security_group_ingress.
- create_security_group.
- delete_security_group.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-security-group.html
https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code
"""

import json
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")


# Describe security groups
def describe_security_groups(SECURITY_GROUP_ID):
    """Describe one or more of your security groups."""
    try:
        response = ec2.describe_security_groups(GroupIds=[SECURITY_GROUP_ID])
        # print(json.dumps(response, indent=2))
        security_group_id = response["SecurityGroups"][0]["GroupId"]
        print(json.dumps({"Security group id": security_group_id}, indent=2))
    except ClientError as e:
        print(e)


# Create a security group and rules
def create_security_group():
    """
    - Create a security group.
    - Add one or more ingress rules to a security group.

    Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

    The example below shows how to:

    - Create a Security Group using create_security_group.
    - Add an ingress rule to a security group using authorize_security_group_ingress.
    """

    response = ec2.describe_vpcs()
    vpc_id = response.get("Vpcs", [{}])[0].get("VpcId", "")
    print(f"VPC Id: {vpc_id}")

    try:
        response = ec2.create_security_group(
            GroupName="SECURITY_GROUP_NAME", Description="DESCRIPTION", VpcId=vpc_id
        )
        security_group_id = response["GroupId"]
        print("Security Group Created %s in vpc %s." % (security_group_id, vpc_id))

        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    "IpProtocol": "tcp",
                    "FromPort": 80,
                    "ToPort": 80,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                },
                {
                    "IpProtocol": "tcp",
                    "FromPort": 22,
                    "ToPort": 22,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                },
            ],
        )
        print("Ingress Successfully Set %s" % data)
    except ClientError as e:
        print(e)

    return security_group_id


# Delete a security group
def delete_security_group(SECURITY_GROUP_ID):
    """If you attempt to delete a security group that is associated with an instance,
    or is referenced by another security group, the operation fails with InvalidGroup.InUse
    in EC2-Classic or DependencyViolation in EC2-VPC.

    The example below shows how to:
    - Delete a security group using delete_security_group.
    """
    # Delete security group
    try:
        response = ec2.delete_security_group(GroupId=SECURITY_GROUP_ID)
        print("Security Group Deleted")
    except ClientError as e:
        print(e)


if __name__ == "__main__":
    print("Describe one or more of your security groups.")
    security_group_id = "sg-05fb8cc9e5dbafedb"
    describe_security_groups(security_group_id)

    print(
        """
        - Create a security group.
        - Add one or more ingress rules to a security group.
        """
    )
    security_group_id_2 = create_security_group()
    print(json.dumps({"Security group id": security_group_id_2}, indent=2))

    print(f"Delete a security group: {security_group_id_2}")
    delete_security_group(security_group_id_2)
