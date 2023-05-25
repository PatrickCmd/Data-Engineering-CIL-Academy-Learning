"""Working with IAM policies
This Python example shows you how to create and get IAM policies and attach and detach IAM policies from roles.

The scenario
You grant permissions to a user by creating a policy, which is a document that lists the actions that a user can 
perform and the resources those actions can affect. Any actions or resources that are not explicitly allowed are 
denied by default. Policies can be created and attached to users, groups of users, roles assumed by users, and resources.

In this example, Python code used to manage policies in IAM. The code uses the Amazon Web Services (AWS) SDK for Python 
to create and delete policies as well as attaching and detaching role policies using these methods of the IAM client class:

- create_policy.
- get_policy.
- attach_role_policy.
- detach_role_policy.

Resources
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/iam-example-policies.html
https://www.learnaws.org/2021/05/12/aws-iam-boto3-guide/#how-to-create-an-iam-role
https://medium.com/geekculture/automating-aws-iam-using-lambda-and-boto3-part-3-3100088a4454
"""

import os
import json
import boto3

iam = boto3.client("iam")


# Create an IAM policy
def create_policy():
    """Create a new managed policy for your AWS account
    This operation creates a policy version with a version identifier of v1 and sets v1 as the policy’s default version.

    The example below shows how to:
    - Create a new managed policy using create_policy.
    """

    REGION = os.environ.get("AWS_DEFAULT_REGION")
    ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")
    LOGS_RESOURCE_ARN = f"arn:aws:logs:{REGION}:{ACCOUNT_ID}:log-group:*"
    DYNAMODB_RESOURCE_ARN = f"arn:aws:dynamodb:{REGION}:{ACCOUNT_ID}:table/*"
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": LOGS_RESOURCE_ARN,
            },
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Scan",
                    "dynamodb:UpdateItem",
                ],
                "Resource": DYNAMODB_RESOURCE_ARN,
            },
        ],
    }
    response = iam.create_policy(
        PolicyName="myDynamoDBPolicy", PolicyDocument=json.dumps(my_managed_policy)
    )
    # print(response)
    policy = response["Policy"]
    policy = {
        "policy_name": policy["PolicyName"],
        "policy_id": policy["PolicyId"],
        "policy_arn": policy["Arn"],
        "create_date": policy["CreateDate"].strftime("%Y-%m-%d"),
    }
    print(json.dumps(policy, indent=2))

    return policy


# Get an IAM policy
def get_iam_policy(policy_arn):
    """Get information about the specified managed policy, including the policy’s default version and the total number of IAM users,
    groups, and roles to which the policy is attached. To get the list of the specific users, groups, and roles that the policy is
    attached to, use the list_entities_for_policy API. This API returns metadata about the policy. To get the actual policy document
    for a specific version of the policy, use get_policy_version API.

    This API gets information about managed policies. To get information about an inline policy that is embedded with an IAM user, group, or role,
    use the get_user_policy, get_group_policy, or get_role_policy API.

    The example below shows how to:
    - Get information about a managed policy using get_policy
    """

    # Get a policy
    response = iam.get_policy(PolicyArn=policy_arn)
    # print(json.dumps(response["Policy"], indent=2))
    print(response)


# Attach a managed role policy
def attach_role_policy():
    """When you attach a managed policy to a role, the managed policy becomes part of the role’s permission (access) policy.
    You cannot use a managed policy as the role’s trust policy. The role’s trust policy is created at the same time as the role,
    using create_role. You can update a role’s trust policy using update_assume_role_policy.

    Use this API to attach a managed policy to a role. To embed an inline policy in a role, use put_role_policy.

    The example below shows how to:
    - Attach a managed policy to an IAM role. using attach_role_policy.
    """

    # Create a temporary role
    # We also need to provide a trust relationship policy as part of the IAM role. 
    # This policy grants an entity (like AWS EC2 in our example) the permission to assume the role. - https://www.learnaws.org/2021/05/12/aws-iam-boto3-guide/#how-to-create-an-iam-role
    # Principal — defines the entity which can assume this role.
    assume_role_policy_document = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "ec2.amazonaws.com"},
                    "Action": "sts:AssumeRole",
                }
            ],
        }
    )
    _ = iam.create_role(
        AssumeRolePolicyDocument=assume_role_policy_document,
        Path="/",
        RoleName="AmazonDynamoDBFullAccess",
    )
    # Attach a role policy
    iam.attach_role_policy(
        PolicyArn="arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
        RoleName="AmazonDynamoDBFullAccess",
    )


# Detach a managed role policy
def detach_role_policy():
    """Detach the specified managed policy from the specified role.

    A role can also have inline policies embedded with it. To delete an inline policy, use the delete_role_policy

    The example below shows how to:
    - Detach a managed role policy using detach_role_policy.
    """

    # Detach a role policy
    iam.detach_role_policy(
        PolicyArn="arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
        RoleName="AmazonDynamoDBFullAccess",
    )

    # Just doing a clean up for my previously created temporary role (AmazonDynamoDBFullAccess).
    _ = iam.delete_role(RoleName="AmazonDynamoDBFullAccess")


if __name__ == "__main__":
    print("Create a new managed policy for your AWS account")
    policy = create_policy()

    print("Get an IAM policy")
    get_iam_policy(policy["policy_arn"])

    print("Attach a role policy")
    attach_role_policy()

    print("Detach a role policy")
    detach_role_policy()
