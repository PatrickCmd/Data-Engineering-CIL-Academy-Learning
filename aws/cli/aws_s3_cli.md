# [Using Amazon S3 with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html)

You can access the features of Amazon Simple Storage Service (Amazon S3) using the AWS Command Line Interface (AWS CLI). The AWS CLI provides two tiers of commands for accessing Amazon S3:

- **s3** – High-level commands that simplify performing common tasks, such as creating, manipulating, and deleting objects and buckets.

- **s3api** – Exposes direct access to all Amazon S3 API operations which enables you to carry out advanced operations. 

## Using high-level (s3) commands with the AWS CLI

This topic describes some of the commands you can use to manage Amazon S3 buckets and objects using the [aws s3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html) commands in the AWS CLI. For commands not covered in this topic and additional command examples, see the [aws s3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html) commands in the AWS CLI Reference.

The high-level `aws s3` commands simplify managing Amazon S3 objects. These commands enable you to manage the contents of Amazon S3 within itself and with local directories.

### Understand these Amazon S3 terms:

- **Bucket** – A top-level Amazon S3 folder.

- **Prefix** – An Amazon S3 folder in a bucket.

- **Object** – Any item that's hosted in an Amazon S3 bucket.

### Create a bucket

Use the [s3 mb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mb.html) command to make a bucket. Bucket names must be **globally** unique (unique across all of Amazon S3) and should be DNS compliant.

Bucket names can contain lowercase letters, numbers, hyphens, and periods. Bucket names can start and end only with a letter or number, and cannot contain a period next to a hyphen or another period.

**Syntax**

```sh
aws s3 mb <target> [--options]
```

The following example creates the `s3://bucket-name` bucket.

```sh
aws s3 mb s3://bucket-name
```

```sh
BUCKETNAME=data-engineering-102
aws s3 mb s3://$BUCKETNAME
```

### List buckets and objects
To list your buckets, folders, or objects, use the [s3 ls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html) command. Using the command without a target or options lists all buckets.

**Syntax**

```sh
aws s3 ls <target> [--options]
```

For a few common options to use with this command, and examples, see [Frequently used options for s3](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-param) commands. For a complete list of available options, see [s3 ls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html) in the AWS CLI Command Reference.


**s3 ls Examples**

The following example lists all of your Amazon S3 buckets.

```sh
aws s3 ls
```

The following command lists all objects and prefixes in a bucket.

```sh
aws s3 ls s3://$BUCKETNAME
```

You can filter the output to a specific prefix by including it in the command. The following command lists the objects in `bucket-name/example/` (that is, objects in `bucket-name` filtered by the prefix `example/`).

```sh
aws s3 ls s3://bucket-name/example/
```

### Delete buckets
To delete a bucket, use the [s3 rb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rb.html) command.

**Syntax**

```sh
aws s3 rb <target> [--options]
```

The following example removes the `s3://bucket-name` bucket.

```sh
aws s3 rb s3://bucket-name
```

```sh
aws s3 rb s3://$BUCKETNAME
```

By default, the bucket must be empty for the operation to succeed. To remove a bucket that's not empty, you need to include the --force option. If you're using a versioned bucket that contains previously deleted—but retained—objects, this command does not allow you to remove the bucket. You must first remove all of the content.

The following example deletes all objects and prefixes in the bucket, and then deletes the bucket.

```sh
aws s3 rb s3://bucket-name --force
```

### Delete objects

To delete objects in a bucket or your local directory, use the [s3 rm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html) command.

**Syntax**

```sh
aws s3 rm  <target> [--options]
```

For a few common options to use with this command, and examples, see [Frequently used options for s3](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-param) commands.


**s3 rm examples**

The following example deletes `filename.txt` from `s3://bucket-name/example`.

```sh
aws s3 rm s3://bucket-name/example/filename.txt
```

The following example deletes all objects from `s3://bucket-name/example` using the `--recursive` option.

```sh
aws s3 rm s3://bucket-name/example --recursive
```

### Move objects

Use the [s3 mv](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html) command to move objects from a bucket or a local directory.

**Syntax**

```sh
aws s3 mv <source> <target> [--options]
```

**s3 mv examples**

The following example moves all objects from `s3://bucket-name/example` to `s3://my-bucket/`.

```sh
aws s3 mv s3://bucket-name/example s3://my-bucket/
```

The following example moves a local file from your current working directory to the Amazon S3 bucket with the `s3 mv` command.

```sh
aws s3 mv filename.txt s3://bucket-name
```

The following example moves a file from your Amazon S3 bucket to your current working directory, where `./` specifies your current working directory.

```sh
aws s3 mv s3://bucket-name/filename.txt ./
```

### Copy objects

Use the [s3 cp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html) command to copy objects from a bucket or a local directory.

**Syntax**

```sh
aws s3 cp <source> <target> [--options]
```

You can use the dash parameter for file streaming to standard input (`stdin`) or standard output (`stdout`).

The `s3 cp` command uses the following syntax to upload a file stream from stdin to a specified bucket.

**Syntax**

```sh
aws s3 cp - <target> [--options]
```

The `s3 cp` command uses the following syntax to download an Amazon S3 file stream for stdout.

**Syntax**

```sh
aws s3 cp <target> [--options] -
```

**s3 cp examples**

The following example copies all objects from `s3://bucket-name/example` to `s3://my-bucket/`.

```sh
aws s3 cp s3://bucket-name/example s3://my-bucket/
```

The following example copies a local file from your current working directory to the Amazon S3 bucket with the `s3 cp` command.

```sh
aws s3 cp filename.txt s3://bucket-name
```

```sh
aws s3 cp aws-overview.pdf s3://$BUCKETNAME
```

The following example copies a file from your Amazon S3 bucket to your current working directory, where `./` specifies your current working directory.

```sh
aws s3 cp s3://bucket-name/filename.txt ./
```

The following example uses echo to stream the text "hello world" to the `s3://bucket-name/filename.txt` file.

```sh
echo "hello world" | aws s3 cp - s3://bucket-name/filename.txt
```

```sh
echo "hello world" | aws s3 cp - s3://${BUCKETNAME}/filename.txt
```

The following example streams the `s3://bucket-name/filename.txt` file to `stdout` and prints the contents to the console.

```sh
aws s3 cp s3://bucket-name/filename.txt -
```

```sh
aws s3 cp s3://${BUCKETNAME}/filename.txt -
```

The following example streams the contents of `s3://bucket-name/pre` to `stdout`, uses the `bzip2` command to compress the files, and uploads the new compressed file named `key.bz2` to `s3://bucket-name`.

```sh
aws s3 cp s3://bucket-name/pre - | bzip2 --best | aws s3 cp - s3://bucket-name/key.bz2
```

### Sync objects

The [s3 sync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html) command synchronizes the contents of a bucket and a directory, or the contents of two buckets. Typically, `s3 sync` copies missing or outdated files or objects between the source and target. However, you can also supply the `--delete` option to remove files or objects from the target that are not present in the source.

**Syntax**

```sh
aws s3 sync <source> <target> [--options]
```

**s3 sync examples**

The following example synchronizes the contents of an Amazon S3 prefix named path in the bucket named my-bucket with the current working directory.

`s3 sync` updates any files that have a size or modified time that are different from files with the same name at the destination. The output displays specific operations performed during the sync. Notice that the operation recursively synchronizes the subdirectory `MySubdirectory` and its contents with `s3://my-bucket/path/MySubdirectory`.

```sh
aws s3 sync . s3://my-bucket/path
upload: MySubdirectory\MyFile3.txt to s3://my-bucket/path/MySubdirectory/MyFile3.txt
upload: MyFile2.txt to s3://my-bucket/path/MyFile2.txt
upload: MyFile1.txt to s3://my-bucket/path/MyFile1.txt
```

```sh
LOCALPATH='aws/employee-directory-app-hosting/images/'
aws s3 sync $LOCALPATH s3://${BUCKETNAME}/aws_images
```

The following example, which extends the previous one, shows how to use the `--delete` option.

```sh
// Delete local file
rm ./MyFile1.txt

// Attempt sync without --delete option - nothing happens
aws s3 sync . s3://my-bucket/path

// Sync with deletion - object is deleted from bucket
aws s3 sync . s3://my-bucket/path --delete
delete: s3://my-bucket/path/MyFile1.txt

// Delete object from bucket
aws s3 rm s3://my-bucket/path/MySubdirectory/MyFile3.txt
delete: s3://my-bucket/path/MySubdirectory/MyFile3.txt

// Sync with deletion - local file is deleted
aws s3 sync s3://my-bucket/path . --delete
delete: MySubdirectory\MyFile3.txt

// Sync with Infrequent Access storage class
$ aws s3 sync . s3://my-bucket/path --storage-class STANDARD_IA
```

When using the `--delete` option, the `--exclude` and `--include` options can filter files or objects to delete during an `s3 sync` operation. In this case, the parameter string must specify files to exclude from, or include for, deletion in the context of the target directory or bucket. The following shows an example.

```sh
Assume local directory and s3://my-bucket/path currently in sync and each contains 3 files:
MyFile1.txt
MyFile2.rtf
MyFile88.txt
'''

// Sync with delete, excluding files that match a pattern. MyFile88.txt is deleted, while remote MyFile1.txt is not.
aws s3 sync . s3://my-bucket/path --delete --exclude "path/MyFile?.txt"
delete: s3://my-bucket/path/MyFile88.txt
'''

// Sync with delete, excluding MyFile2.rtf - local file is NOT deleted
aws s3 sync s3://my-bucket/path . --delete --exclude "./MyFile2.rtf"
download: s3://my-bucket/path/MyFile1.txt to MyFile1.txt
'''

// Sync with delete, local copy of MyFile2.rtf is deleted
aws s3 sync s3://my-bucket/path . --delete
delete: MyFile2.rtf
```

## Frequently used options for s3 commands

The following options are frequently used for the commands described in this topic. For a complete list of options you can use on a command, see the specific command in the [AWS CLI version 2 reference guide](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).

### acl
`s3 sync` and `s3 cp` can use the `--acl` option. This enables you to set the access permissions for files copied to Amazon S3. The `--acl` option accepts `private`, `public-read`, and `public-read-write` values. For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) in the Amazon Simple Storage Service User Guide.

```sh
aws s3 sync . s3://my-bucket/path --acl public-read
```

### exclude
When you use the `s3 cp`, `s3 mv`, `s3 sync`, or `s3 rm` command, you can filter the results by using the `--exclude` or `--include` option. The `--exclude` option sets rules to only exclude objects from the command, and the options apply in the order specified. This is shown in the following example.

```sh
Local directory contains 3 files:
MyFile1.txt
MyFile2.rtf
MyFile88.txt

// Exclude all .txt files, resulting in only MyFile2.rtf being copied
aws s3 cp . s3://my-bucket/path --exclude "*.txt"

// Exclude all .txt files but include all files with the "MyFile*.txt" format, resulting in, MyFile1.txt, MyFile2.rtf, MyFile88.txt being copied
aws s3 cp . s3://my-bucket/path --exclude "*.txt" --include "MyFile*.txt"

// Exclude all .txt files, but include all files with the "MyFile*.txt" format, but exclude all files with the "MyFile?.txt" format resulting in, MyFile2.rtf and MyFile88.txt being copied
aws s3 cp . s3://my-bucket/path --exclude "*.txt" --include "MyFile*.txt" --exclude "MyFile?.txt"
```

### include
When you use the `s3 cp`, `s3 mv`, `s3 sync`, or `s3 rm` command, you can filter the results using the `--exclude` or `--include` option. The `--include` option sets rules to only include objects specified for the command, and the options apply in the order specified. This is shown in the following example.

```sh
Local directory contains 3 files:
MyFile1.txt
MyFile2.rtf
MyFile88.txt

// Include all .txt files, resulting in MyFile1.txt and MyFile88.txt being copied
aws s3 cp . s3://my-bucket/path --include "*.txt"

// Include all .txt files but exclude all files with the "MyFile*.txt" format, resulting in no files being copied
aws s3 cp . s3://my-bucket/path --include "*.txt" --exclude "MyFile*.txt"

// Include all .txt files, but exclude all files with the "MyFile*.txt" format, but include all files with the "MyFile?.txt" format resulting in MyFile1.txt being copied

aws s3 cp . s3://my-bucket/path --include "*.txt" --exclude "MyFile*.txt" --include "MyFile?.txt"
```

### grant
The `s3 cp`, `s3 mv`, and `s3 sync` commands include a `--grants` option that you can use to grant permissions on the object to specified users or groups. Set the `--grants` option to a list of permissions using the following syntax. Replace Permission, `Grantee_Type`, and `Grantee_ID` with your own values.

**Syntax**

```sh
--grants Permission=Grantee_Type=Grantee_ID
         [Permission=Grantee_Type=Grantee_ID ...]
```

Each value contains the following elements:

- `Permission` – Specifies the granted permissions. Can be set to `read`, `readacl`, `writeacl`, or `full`.

- `Grantee_Type` – Specifies how to identify the grantee. Can be set to `uri`, `emailaddress`, or `id`.

- `Grantee_ID` – Specifies the grantee based on `Grantee_Type`.

    - `uri` – The group's URI. For more information, see [Who is a grantee](https://docs.aws.amazon.com/AmazonS3/latest/dev/ACLOverview.html#SpecifyingGrantee)?

    - `emailaddress` – The account's email address.

    - `id` – The account's canonical ID.

For more information about Amazon S3 access control, see [Access control](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAuthAccess.html).


The following example copies an object into a bucket. It grants `read` permissions on the object to everyone, and `full` permissions (`read`, `readacl`, and `writeacl`) 
to the account associated with `user@example.com`.

```sh
aws s3 cp file.txt s3://my-bucket/ --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers full=emailaddress=user@example.com
```

You can also specify a nondefault storage class (`REDUCED_REDUNDANCY` or `STANDARD_IA`) for objects that you upload to Amazon S3. To do this, use the `--storage-class` option.

```sh
aws s3 cp file.txt s3://my-bucket/ --storage-class REDUCED_REDUNDANCY
```

### recursive
When you use this option, the command is performed on all files or objects under the specified directory or prefix. 
The following example deletes `s3://my-bucket/path` and all of its contents.

```sh
aws s3 rm s3://my-bucket/path --recursive
```

```sh
aws s3 rm s3://${BUCKETNAME}/aws_images --recursive
```

## Using API-Level (s3api) commands with the AWS CLI

The API-level commands (contained in the `s3api` command set) provide direct access to the Amazon Simple Storage Service (Amazon S3) APIs, and enable some operations that are not exposed in the high-level `s3` commands. These commands are the equivalent of the other AWS services that provide API-level access to the services' functionality. 

This topic provides examples that demonstrate how to use the lower-level commands that map to the Amazon S3 APIs. In addition, you can find examples for each S3 API command in the `s3api` section of the [AWS CLI version 2 reference guide](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html).

### Apply a custom ACL

With high-level commands, you can use the `--acl` option to apply predefined access control lists (ACLs) to Amazon S3 objects. But you can't use that command to set bucket-wide ACLs. However, you can do this by using the [put-bucket-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-acl.html) API-level command.

The following example shows how to grant full control to two AWS users (`user1@example.com` and `user2@example.com`) and read permission to everyone. The identifier for "everyone" comes from a special URI that you pass as a parameter.

```sh
aws s3api put-bucket-acl --bucket MyBucket --grant-full-control 'emailaddress="user1@example.com",emailaddress="user2@example.com"' --grant-read 'uri="http://acs.amazonaws.com/groups/global/AllUsers"'
```

For details about how to construct the ACLs, see [PUT Bucket acl](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTacl.html) in the Amazon Simple Storage Service API Reference. The `s3api` ACL commands in the CLI, such as `put-bucket-acl`, use the same [shorthand argument notation](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html).

### Configure a logging policy

The API command `put-bucket-logging` configures a bucket logging policy.

In the following example, the AWS user `user@example.com` is granted full control over the log files, and all users have read access to them. Notice that the `put-bucket-acl` command is also required to grant the Amazon S3 log delivery system (specified by a URI) the permissions needed to read and write the logs to the bucket.

```sh
aws s3api put-bucket-acl --bucket MyBucket --grant-read-acp 'URI="http://acs.amazonaws.com/groups/s3/LogDelivery"' --grant-write 'URI="http://acs.amazonaws.com/groups/s3/LogDelivery"'
aws s3api put-bucket-logging --bucket MyBucket --bucket-logging-status file://logging.json
```

The `logging.json` file in the previous command has the following content.

```json
{
  "LoggingEnabled": {
    "TargetBucket": "MyBucket",
    "TargetPrefix": "MyBucketLogs/",
    "TargetGrants": [
      {
        "Grantee": {
          "Type": "AmazonCustomerByEmail",
          "EmailAddress": "user@example.com"
        },
        "Permission": "FULL_CONTROL"
      },
      {
        "Grantee": {
          "Type": "Group",
          "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
        },
        "Permission": "READ"
      }
    ]
  }
}
```

### Amazon S3 bucket lifecycle operations scripting example

This topic uses a bash scripting example for Amazon S3 bucket lifecycle operations using the AWS Command Line Interface (AWS CLI). 
This scripting example uses the [aws s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html) set of commands. Shell scripts are programs designed to run in a command line interface.

**About this example**

This example demonstrates how to interact with some of the basic Amazon S3 operations using a set of functions in shell script files. The functions are located in the shell script file named `bucket-operations.sh`. You can call these functions in another file. Each script file contains comments describing each of the functions.

To see the intermediate results of each step, run the script with a `-i` parameter. You can view the current status of the bucket or its contents using the Amazon S3 console. The script only proceeds to the next step when you press enter at the prompt.

For the full example and downloadable script files, see [Amazon S3 Bucket Lifecycle Operations](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/s3/bucket-lifecycle-operations) in the AWS Code Examples Repository on GitHub.

### Files
The example contains the following files:

**bucket-operations.sh**
This main script file can be sourced from another file. It includes functions that perform the following tasks:

- Creating a bucket and verifying that it exists

- Copying a file from the local computer to a bucket

- Copying a file from one bucket location to a different bucket location

- Listing the contents of a bucket

- Deleting a file from a bucket

- Deleting a bucket

**test-bucket-operations.sh**

The shell script file `test-bucket-operations.sh` demonstrates how to call the functions by sourcing the `bucket-operations.sh` file and calling each of the functions. After calling functions, the test script removes all resources that it created.

**awsdocs-general.sh**

The script file `awsdocs-general.sh` holds general purpose functions used across advanced code examples for the AWS CLI.
