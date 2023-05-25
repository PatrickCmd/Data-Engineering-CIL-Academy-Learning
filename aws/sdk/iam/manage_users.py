"""Managing IAM users
This Python example shows you how to create a user, list users, update a user name and delete a user.

The scenario
In this example Python code is used to create and manage users in IAM. The code uses the Amazon Web 
Services (AWS) SDK for Python to manage users using these methods of the IAM client class:

- create_user
- get_paginator(‘list_users’).
- update_user.
- delete_user.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/iam-example-managing-users.html
"""

import json
import boto3

# Create IAM client
iam = boto3.client("iam")


# Create a user
def create_user(username):
    """Create a new IAM user for your AWS account.
    The example below shows how to:
    - Create a new IAM user using create_user.
    """

    # Create user
    response = iam.create_user(UserName=username)

    # print(response)
    user = {
        "username": response["User"]["UserName"],
        "user_id": response["User"]["UserId"],
        "create_date": response["User"]["CreateDate"].strftime("%Y-%m-%d"),
    }
    print(json.dumps(user, indent=2))


# List users in your account
def list_account_users():
    """List the IAM users.
    The example below shows how to:
    - List the IAM users using get_paginator(‘list_users’).
    """
    users = []
    # List users with the pagination interface
    paginator = iam.get_paginator("list_users")
    for response in paginator.paginate():
        # print(response)
        for user in response["Users"]:
            user = {
                "username": user["UserName"],
                "user_id": user["UserId"],
                "create_date": user["CreateDate"].strftime("%Y-%m-%d"),
            }
            users.append(user)

    print(json.dumps(users, indent=2))


# Update a user’s name
def update_user(username):
    """The example below shows how to:
    Update an IAM user name using update_user.
    """
    # Update a user name
    iam.update_user(UserName=username, NewUserName="NEW_IAM_USER_NAME")
    print(f"User {username} updated")


# Delete a user
def delete_user(username):
    """Delete the specified IAM user. The user must not belong to any groups or have any access keys,
    signing certificates, or attached policies.

    The example below shows how to:
    - Delete an IAM user name using delete_user.
    """
    # Delete a user
    iam.delete_user(UserName=username)
    print(f"User {username} deleted")


if __name__ == "__main__":
    print("Create a new IAM user for your AWS account")
    username = "IAM_USER_NAME"
    create_user(username)

    print("List users in your account")
    list_account_users()

    print("Update a user’s name")
    update_user(username)

    print("Delete a user")
    username = "NEW_IAM_USER_NAME"
    delete_user(username)
