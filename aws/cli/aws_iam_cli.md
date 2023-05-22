# Using AWS Identity and Access Management from the AWS CLI

You can access the features of AWS Identity and Access Management (IAM) using the AWS Command Line Interface (AWS CLI). To list the AWS CLI commands for IAM, use the following command.

```sh
aws iam help
```

## [Creating IAM users and groups](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam-new-user-group.html)

This topic describes how to use AWS Command Line Interface (AWS CLI) commands to create an AWS Identity and Access Management (IAM) group and a new user, and then add the user to the group. For more information on the IAM service, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

### To create a group and add a new user to it
1. Use the [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-group.html) command to create the group.

```sh
aws iam create-group --group-name MyIamGroup
```

```sh
group_name=DataEngineersGroup
aws iam create-group --group-name $group_name
```

2. Use the [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html) command to create the user.

```sh
aws iam create-user --user-name MyUser
```

```sh
user_name=DataEngineer
aws iam create-user --user-name $user_name
```

3. Use the [add-user-to-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-user-to-group.html) command to add the user to the group.

```sh
aws iam add-user-to-group --user-name MyUser --group-name MyIamGroup
```

```sh
aws iam add-user-to-group --user-name $user_name --group-name $group_name
```

4. To verify that the `MyIamGroup` group contains the `MyUser`, use the [get-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group.html) command.

```sh
aws iam get-group --group-name MyIamGroup
```

```sh
aws iam get-group --group-name $group_name
```

## [Attaching an IAM managed policy to a user](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam-policy.html)

This topic describes how to use AWS Command Line Interface (AWS CLI) commands to attach an AWS Identity and Access Management (IAM) policy to a user. The policy in this example provides the user with "Power User Access". For more information on the IAM service, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

### To attach an IAM managed policy to a user

1. Determine the Amazon Resource Name (ARN) of the policy to attach. The following command uses `list-policies` to find the ARN of the policy with the name `PowerUserAccess`. It then stores that ARN in an environment variable.

The `PowerUserAccess` policy in AWS Identity and Access Management (IAM) is a predefined policy that grants a broad range of permissions to perform most AWS service actions, except for management of IAM users and groups, account management, and access to AWS Identity and Access Management (IAM) service-related actions.

The `PowerUserAccess` policy is designed to provide users with elevated permissions beyond what is available with the basic AWS managed policy, such as `ReadOnlyAccess`, while still restricting access to critical account-level actions. Users with the `PowerUserAccess` policy can perform a wide range of tasks within AWS services, including creating and managing resources like EC2 instances, S3 buckets, and RDS databases, among others.

The `PowerUserAccess` policy grants permissions across multiple AWS services but does not provide full administrative access to an AWS account. It strikes a balance between granting significant privileges to perform common operational tasks and maintaining restrictions on critical account-level actions to prevent accidental or unauthorized changes.

It's important to note that the `PowerUserAccess` policy should be carefully assigned to trusted users who require elevated permissions within specific AWS services but do not need administrative access to manage IAM users, groups, roles, or policies, or perform account management actions.

```sh
export POLICYARN=$(aws iam list-policies --query 'Policies[?PolicyName==`PowerUserAccess`].{ARN:Arn}' --output text)
echo $POLICYARN
```

2. To attach the policy, use the [attach-user-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html) command, and reference the environment variable that holds the policy ARN.

```sh
aws iam attach-user-policy --user-name MyUser --policy-arn $POLICYARN
```

```sh
aws iam attach-user-policy --user-name $user_name --policy-arn $POLICYARN
```

3. Verify that the policy is attached to the user by running the [list-attached-user-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-user-policies.html) command.

```sh
aws iam list-attached-user-policies --user-name MyUser
```

```sh
aws iam list-attached-user-policies --user-name $user_name
```

For more information, see [Access Management Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-additional-resources.html). This topic provides links to an overview of permissions and policies, and links to examples of policies for accessing Amazon S3, Amazon EC2, and other services.


## [Setting an initial password for an IAM user](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam-set-pw.html)

This topic describes how to use AWS Command Line Interface (AWS CLI) commands to set an initial password for an AWS Identity and Access Management( IAM) user. For more information on the IAM service, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

The following command uses [create-login-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html) to set an initial password on the specified user. When the user signs in for the first time, the user is required to change the password to something that only the user knows.

```sh
aws iam create-login-profile --user-name MyUser --password My!User1Login8P@ssword --password-reset-required
```

```sh
aws iam create-login-profile --user-name $user_name --password MyUser1Login8P@ssword --password-reset-required
```

You can use the `update-login-profile` command to change the password for a user.

```sh
aws iam update-login-profile --user-name MyUser --password My!User1ADifferentP@ssword
```

### [Create an access key for an IAM user](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam-create-creds.html)

This topic describes how to use AWS Command Line Interface (AWS CLI) commands to create a set of access keys for an AWS Identity and Access Management (IAM) user. For more information on the IAM service, see the AWS Identity and Access Management User Guide.

You can use the [create-access-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-access-key.html) command to create an access key for a user. An access key is a set of security credentials that consists of an access key ID and a secret key.

A user can create only two access keys at one time. If you try to create a third set, the command returns a `LimitExceeded` error.

```sh
aws iam create-access-key --user-name MyUser
```

```sh
aws iam create-access-key --user-name $user_name
```

Use the [delete-access-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html) command to delete an access key for a user. Specify which access key to delete by using the access key ID.

```sh
aws iam delete-access-key --user-name MyUser --access-key-id AKIAIOSFODNN7EXAMPLE
```
