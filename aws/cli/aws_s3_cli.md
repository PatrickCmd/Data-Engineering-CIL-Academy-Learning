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
