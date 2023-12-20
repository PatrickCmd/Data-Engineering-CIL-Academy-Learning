# Getting Started with Amazon Simple Storage Service(Amazon S3)
## Storage Fundamentals
Amazon S3 is storage for the Internet that makes web-scale computing easier for developers and users alike.  Amazon S3 is an object storage platform that allows you to store and retrieve any amount of data, at any time, from anywhere on the web.  If you are new to storage, you may not be aware that there are different types of storage. 

Amazon S3 is an object storage based service. However, to better understand object storage and how it differs from the other storage types, take a moment to review the underlying differences between storage types. 

### Block storage
A block is a range of bytes or bits on a storage device. Block storage files, are divided into blocks and written directly to empty blocks on a physical drive. Each block is assigned a unique identifier and then written to the disk in the most efficient manner possible. Since blocks are assigned identifiers, they do not need to be stored in adjacent sections of the disk. Indeed they can be spread across multiple disks or environments. You can retrieve the individual blocks separately from the rest of the file, which makes block storage excellent for technology like relational databases.

With relational databases, you might only need to retrieve a single piece of a file, such as an inventory tracking number, or one specific employee ID, rather than retrieving the entire inventory listing or whole employee repository.

![block storage](images/Fundamentals/aws-block-storage.png)

### File Storage

Historically, operating systems save data in hierarchical file systems organized in the form of directories, sub-directories and files, or folders, sub-folders, and files depending on the operating system.

For example, if you are troubleshooting an issue on a Linux distribution, you may need to look in /var/log or /etc/config. Once inside of these directories, you need to identify which file to explore and open. When using a file-based system, you must know the exact path and location of the files you need to work with or have a way to search the entire structure to find the file you need.  

![file storage](images/Fundamentals/file-storage.jpeg)

### Object Storage

Unlike the hierarchical structure used in file-based storage, object storage is a flat structure where the data, called an object, is located in a single repository known as a bucket. Object can be organized to imitate a hierarchy by attaching key name prefixes and delimiters. Prefixes and delimiters allow you to group similar items to help visually organize and easily retrieve your data. In the user interface, these prefixes give the appearance of a folder and subfolder structure but in reality, the storage is still a flat structure.

![object storage](images/Fundamentals/s3-object-storage.png)

## Amazon S3 Fundamentals

Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. It is intentionally built with a minimal feature set that focuses on simplicity and robustness. You have access to the same highly scalable, reliable, fast, inexpensive data storage infrastructure that Amazon uses to run its own global network of web sites. The service aims to maximize benefits of scale and to pass those benefits on to the you, the customer. 

### Object storage in Amazon S3
We learned that object storage is a flat storage structure where objects are stored in buckets. Objects are any piece of data stored within a bucket. You also learned that you can create a pseudo folder structure using prefixes. In Amazon S3 object storage, you can organize objects to imitate a hierarchy by using key name prefixes and delimiters. Prefixes and delimiters allow you to group similar items to help visually organize and easily retrieve your data. In the user interface, these prefixes give the appearance of a folder/ subfolder structure but in reality, the storage is still a flat structure. 

In the image below, you have a bucket called `getting-started-with-s3`. Inside the bucket there is an object called `dolphins.jpg`. To organize and group the oceanography data for the external vendor you created a logical hierarchy using the prefix `ocean`. Ocean looks like a subfolder but this is only to help make the structure readable.

In reality, the key name of the dolphin object is a little longer, allowing us to locate the `ocean/dolphin.jpg` object. The object still sits in one single flat-storage structure.

![s3 object](images/Fundamentals/s3-object.png)

[**Using a Prefix and Delimiter**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)

### Bucket overview

Buckets are permanent containers that hold objects. You can create between 1 and 100 buckets in each AWS account. You can increase the bucket limit to a maximum of 1,000 buckets by submitting a service limit increase. Bucket sizes are virtually unlimited so you don't have to allocate a predetermined bucket size the way you would when creating a storage volume or partition. 

> An Amazon S3 bucket is a versatile storage option with the ability to: host a static web site, retain version information on objects, and employ life-cycle management policies to balance version retention with bucket size and cost.

### Bucket limitations

Prior to creating an Amazon S3 bucket, there are some important restrictions and limitations that you should know.

#### Bucket owner
Amazon S3 buckets are owned by the account that creates them and cannot be transferred to other accounts

#### Bucket names
Bucket names are globally unique.  There can be no duplicate names within the entire S3 infrastructure.

#### Bucket renaming
Once created, you cannot change a bucket name. 

#### Permanent entities
Buckets are permanent storage entities and only removable when they are empty. After deleting a bucket, the name becomes available for reuse by any account after 24 hours if not taken by another account.

#### Object storage limits
There’s no limit to the number of objects you can store in a bucket. You can store all of your objects in a single bucket, or organize them across several buckets. However, you can't create a bucket from within another bucket, also known as nesting buckets.

#### Bucket creation limits
By default, you can create up to 100 buckets in each of your AWS accounts. If you need additional buckets, you can increase your account bucket limit to a maximum of 1,000 buckets by submitting a service limit increase.

### Naming buckets

![naming buckets](images/Fundamentals/naming-buckets.png) 
> This identifies the bucket URL in the format of bucket name/ region endpoint.

When naming buckets, carefully determine how you want to structure your bucket names and how they will function. Will you use them only for data storage or hosting a static website? Your bucket names matter to S3, and based on how you use the bucket, your bucket names and characters will vary. Bucket names are globally viewable and need to be DNS-compliant. 

Here are the rules to follow when naming your buckets. Bucket names must:
- Be unique across all of Amazon S3
- Be between 3-63 characters long
- Consist only of lowercase letters, numbers, dots (.), and hyphens (-)
- Start with a lowercase letter or number
- Not begin with xn-- (beginning February 2020)
- Not be formatted as an IP address. (i.e. 198.68.10.2)
- Use a dot (.) in the name only if the bucket's intended purpose is to host an Amazon S3 static website; otherwise do not use a dot (.) in the bucket name

### Object Overview
To begin using Amazon S3, you should be familiar with the terminology used for creating, accessing, and securing the data in your buckets.

#### Amazon S3 Object Introduction

![Object introduction](images/Fundamentals/s3-object-intro.png)

Amazon S3 is an object store that uses unique key-values to store as many objects as you want. You store these objects in one or more buckets, and each object can be up to 5 TB in size. 

An object consists of the following: `Key, version ID, value, metadata, and access control information`. The object `key (or key name)` uniquely identifies the object in a bucket. Object metadata is a set of name-value pairs. You can set object metadata at the time you upload it. After you upload the object, you cannot modify object metadata. The only way to modify object metadata is to make a copy of the object and set the metadata. 

#### What is an object?

![Object](images/Fundamentals/object.png)

An object is a file and any optional metadata that describes the file. To store a file in Amazon S3, you upload it to a bucket. When you upload a file as an object, you can set permissions on the object and any metadata.

#### What is a Key?

![object key](images/Fundamentals/object-key.png)

When you create an object, you specify the key name. The key name uniquely identifies the object in the bucket. It is the full path to the object in the bucket.

In Amazon S3, there is no hierarchy, as you would see in a file system. However, by using prefixes and delimiters in an object key name, the Amazon S3 console and the AWS SDKs can infer hierarchy and introduce the concept of folders. You do not get actual folders, what you get is a very long key name.

#### Version ID

![object version id](images/Fundamentals/object-version-id.png)

Versioning is a means of keeping multiple variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. You can easily recover from both unintended user actions and application failures. If Amazon S3 receives multiple write requests for the same object simultaneously; it stores all of the objects.

If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object being stored. In one bucket, for example, you can have two objects with the same key, but different version IDs, such as the latest version of dolphins.jpg `(version qNTCxBvI7p0pR39sw1sJhHyc59jx75HB)` and the previous version of dolphins.jpg `(version KWdgdZCncMiiPNs5LGHDz7zmf1QImseb)`.

#### Value

![object value](images/Fundamentals/object-value.png)

**Value (or size)** is the actual content that you are storing. An object value can be any sequence of bytes, meaning it can be the whole object or a range of bytes within an object that an application needs to retrieve. Objects can range in size from zero to 5 TB.

#### Metadata

![Object metadata](images/Fundamentals/object-metadata.png)

For each object stored in a bucket, Amazon S3 maintains a set of system metadata. Amazon S3 processes this system metadata as needed. For example, Amazon S3 maintains object creation date and size metadata and uses this information as part of object management.

There are two categories of system metadata:
1. Metadata such as object creation date is system controlled, where only Amazon S3 can modify the value.
2. Other system metadata, such as the storage class configured for the object and whether the object has server-side encryption enabled, are examples of system metadata whose values you control.

#### Access control information

![access control info](images/Fundamentals/object-access-control-info.png)

You can control access to the objects you store in Amazon S3. S3 supports both resource-based and user-based access controls. Access control lists (ACLs) and bucket policies are both examples of resource-based access control. 

### Organizing data using tags

**A tag** is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define to suit your company's requirements. Tags enable you to categorize your AWS resources or data in different ways. 

For example, you could define a set of tags for your objects that help you track project data or owner. Amazon S3 tags are key-value pairs and apply to a whole bucket or to individual objects to help with identification, searches, and data classification. Using tags for your objects allows you to effectively manage your storage and provide valuable insight on how your data is used. Newly created tags assigned to a bucket, are not retroactively applied to its existing child objects. 

You can use two types of tags: `Bucket tags` and `Object tags`

#### Bucket tags

Bucket tags allow you to track storage cost, or other criteria, by labeling your Amazon S3 buckets using cost allocation tags. A cost allocation tag is a key-value pair that you associate with an S3 bucket. After you activate cost allocation tags, AWS uses the tags to organize your resource costs on your cost allocation report. You can only use cost allocation tags on buckets and not on individual objects.

AWS provides two types of cost allocation tags, an AWS-generated tag and user-defined tag. AWS defines, creates, and applies the AWS-generated tag, createdBy, for you after an S3 CreateBucket event. You define, create, and apply user-defined tags to your S3 bucket. 

Once you have created and applied the user-defined tags, you can activate them by using the Billing and Cost Management console for cost allocation tracking. Cost Allocation Tags appear on the console after enabling AWS Cost Explorer, AWS Budgets, AWS Cost and Usage reports, or legacy reports. 

After you activate the AWS services, they appear on your cost allocation report. You can then use the tags on your cost allocation report to track your AWS costs.

![aws cost allocation report](images/Fundamentals/aws-cost-allocation-report.png)

#### Bucket tag set
Each S3 bucket has a tag set. A tag set contains all of the tags that are assigned to that bucket and can contain as many as 50 tags, or it can be empty.

Keys must be unique within a tag set but values don't.  In the image below the Value: ocean-life is listed twice in tag sets named `project/ocean-life` and `topic/ocean-life`. Since values don't need to be unique these entries are fine. However, when attempting to add a second Key called "items" an error occurs because the key must be unique within the tag set.

![bucket tag set](images/Fundamentals/bucket-tag-set.png)

#### Object tags
Object tagging gives you a way to categorize and query your storage. You can add tags to an Amazon S3 object during the upload or after the upload. Each tag is a key-value pair that adheres to the following rules:
- You can associate up to 10 tags with an object they must have unique tag keys.
- Tag keys can be up to 128 characters in length
- Tag values can be up to 255 characters in length
- Key and tag values are case sensitive

#### Additional benefits
Adding tags to your objects offer benefits such as the following:
- Object tags enable fine-grained access control of permissions. For example, you could grant an IAM user permission to read-only objects with specific tags.
- Object tags enable fine-grained object lifecycle management in which you can specify a tag-based filter, in addition to a key name prefix, in a lifecycle rule.
- When using Amazon S3 analytics, you can configure filters to group objects together for analysis by object tags, key name prefix, or both prefix and tags.
- You can also customize Amazon CloudWatch metrics to display information by specific tag filters.

#### Object API operations for tagging
With Amazon S3 tagging, if you want to add or replace a tag in a tag set (all the tags associated with an object or bucket), you must download all the tags, modify the tags, and then replace all the tags at once.

For more information, see the 'API operations related to object tagging' section in the following link:  https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html

### Region location
Amazon S3 is a globally viewable service. This means that in the AWS Management Console you do not have to specify a region in order to view the buckets. Remember that when you initially create the bucket, you must choose a region to indicate where you want the bucket data to reside. The region you choose should be local to your users or consumers to optimize latency, minimize costs, or to address regulatory requirements. 

For example, if you reside in Europe, you will want to create buckets in the Europe (Ireland) or Europe (Frankfurt) regions rather than creating your buckets in Asia Pacific (Sydney) or South America (Sao Paulo). This way the data is closer to your users and consumers, reducing latency and ensuring regulatory and meets country legal requirements.

#### Cross-Region Replication (CRR)

If you need data stored in multiple regions, you can replicate your bucket to other regions using cross-region replication. This enables you to automatically copy objects from a  bucket in one region to different bucket in a another, separate region. You can replicate the entire bucket or you can use tags to replicate only the objects with the tags you choose.

![CRR](images/Fundamentals/cross-region-replication.jpeg)

#### Same-Region Replication (SRR)

Amazon S3 supports automatic and asynchronous replication of newly uploaded S3 objects to a destination bucket in the same AWS Region. 

SRR makes another copy of S3 objects within the same AWS Region, with the same redundancy as the destination storage class. This allows you to automatically aggregate logs from different S3 buckets for in-region processing, or configure live replication between test and development environments. SRR helps you address data sovereignty and compliance requirements by keeping a copy of your objects in the same AWS Region as the original.

![SRR](images/Fundamentals/same-region-replication.png)

### Amazon S3 static websites 

You can use Amazon S3 to host a static website. With a static website, the individual web pages include only static content that does not change frequently. This is different from using a dynamic website, where the content is constantly changing and constantly updated. From the AWS Management Console, you can easily configure your bucket for static website hosting without needing to write any code. 

![static web hosting](images/Fundamentals/static-webhosting.jpeg)

To host a static website on Amazon S3, you configure a bucket for website hosting and then upload your content. When you configure a bucket as a static website, you must enable website hosting, set public read permissions, and create and add an index document. 

Depending on your website requirements, you can also configure redirects, web traffic logging, and a custom error document. If you prefer not to use the AWS Management Console, you can create, update, and delete the website configuration programmatically by using the AWS SDKs. 

For the best compatibility, we recommend that you avoid using dots (.) in bucket names, except when using buckets for static website hosting. If you include dots in a bucket name that is not a static website, you can't use virtual-host-style addressing over HTTPS, unless you perform your own certificate validation. This is because the security certificates used for virtual hosting of buckets don't work for buckets with dots in their names. 

**Virtual hosting** is the practice of serving multiple websites from a single web server. 

For more information on virtual hosting or using buckets as a static website, follow the link listed below

- [**Virtual hosting**](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html)

## Interfacing with Amazon S3

Once you have a bucket created, there are multiple ways to add, overwrite, or retrieve objects in your Amazon S3 bucket. The three primary tools for interacting with buckets are the AWS Console, the AWS Command Line Interface (CLI), and using the AWS Software Development Kit (SDK).  Each tool enables you to work with the data based on your role and preferences.

### AWS Management Console
The AWS Management Console provides a simple web interface to interact with AWS Services. You can log in using your AWS account name and password. If you’ve enabled AWS Multi-Factor Authentication, you will be prompted for your device’s authentication code. 

Using the AWS Management Console for Amazon S3, you can view your buckets and objects, upload and download data, and manage permissions and security through the graphical user interface. You can also perform almost all bucket operations without having to write any code. 

When uploading data via the AWS Management Console, the maximum file that you can upload is `160GB`. To upload a file larger than 160 GB, use the AWS CLI, AWS SDK, or Amazon S3 REST API. 

### AWS CLI
The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. The AWS CLI is used to manage your Amazon S3 data, buckets, and objects for users who prefer or require the functionality of the command line. You can manually upload, download, and manage your objects using the AWS CLI commands, or automate your processes using scripts.

For more information on the AWS CLI follow this link:

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

### AWS SDK
AWS SDK helps take the complexity out of coding by providing language specific groups of tools for building in AWS. You can simplify using Amazon S3 in your application with an API tailored to your programming language or platform. You can send authenticated requests to Amazon S3 either by using the AWS SDK or by making the REST API calls directly from your application. 

 

You can easily develop applications on AWS in the programming language of your choice with familiar tools. There are a variety of SDKs to choose from to help you build solutions you need for your Amazon S3.

For more information on available AWS SDKs, follow this link:

https://aws.amazon.com/getting-started/tools-sdks/

## Amazon S3 and REST API

The REST API is an HTTP interface to Amazon S3. Using REST API, you use standard HTTP requests to create, fetch, and delete buckets and objects. You can use any toolkit that supports HTTP for use with the REST API. You can even use a browser to fetch objects, as long as they are anonymously readable.  

Amazon S3 supports the REST API, which means that objects and buckets are resources, each with a URL that uniquely identifies the resource.

Addressing models are URLs that define how to locate data within an S3 bucket. Amazon S3 supports two types of addressing models: `Path-style URLs` and `Virtual hosted style URLs`.

### Path-style URLs

With path-style URLs, the bucket name comes after the global or region-specific endpoint. In the image below, notice that the formatting of the URL: `https:/region-specific endpoint/bucket/object`.  The bucket is always a subdomain of `s3.amazonaws.com` and when DNS resolves this URL the endpoint will always be a subdomain of `s3.amazonaws.com`.

In addition, with path-style URLs, multiple accounts for different companies and owners map to this single subdomain, s3.amazonaws.com. If you need a customized URL then you should choose virtual hosted URLs, which are discussed next.

![path style urls](images/Fundamentals/path-style-urls.jpeg)

> Path-style URLS are formatted as a /region-specific-endpoint/bucket/object. This style of URL is deprecated as of September 2020.

### Amazon S3 path-style URL deprecation plan

It is important to note that there is a deprecation plan in the works for path-style URLs on newly created buckets. Support will continue for any path-style URLs previously created; however, once this feature is deprecated you will no longer be able to create new path-style URLs.  This information is important for you to consider when planning for the future of your environment. 

### Virtual hosted-style URLs

Virtual hosting is the practice of serving multiple websites from a single web server. One way to differentiate sites is by using the host name (bucket name) of the request. In a virtual-hosted–style URL, the bucket name is part of the domain name in the URL, which makes the URL easier to read, and more end-user friendly.

![virtual hosted-style urls](images/Fundamentals/virtual-hosted-style-urls.jpeg)

> With Virtual hosted-style URLs the bucket name is listed first, creating a unique subdomain and making the URL easier to remember.

Virtual hosting also has other benefits. You can completely customize the URL of your Amazon S3 resources by naming your bucket after your registered domain name and making that name a DNS alias for Amazon S3.

For example, a customized URL for this Getting Started Course could look like: http://getting-started-with-s3.net/. Virtual hosting also allows you to publish to the "root directory" of your bucket's virtual server which is an important feature that allows applications to search for files in the standardized root directory location. 

When using virtual hosted–style buckets with SSL, the SSL wild-card certificate only matches buckets that do not contain dots (.). To work around this, don't use dots (.) in bucket names, or use HTTP to write your own certificate verification logic.

### How a DNS request is routed

Amazon S3 uses the Domain Name System (DNS) to route requests to facilities that can process them. This system works effectively, but temporary routing errors can occur. If a request arrives at the wrong Amazon S3 location, it responds with a temporary redirect that tells the requester to resend the request to a new endpoint. If a request forms incorrectly, Amazon S3 uses permanent redirects to provide direction on how to perform the request correctly. 

Take a moment to review the diagram below.  The client is making a request to retrieve the dolphins.jpg object, read each step to ensure you understand how to route a DNS request.

#### DNS request step-by-step:

![DNS request](images/Fundamentals/dns-request.jpeg)

1. The client wants to view the `dolphins.jpg` object stored on Amazon S3. The client makes a DNS request to get the address of s3.amazonaws.com. 
2. The client receives one or more IP addresses for facilities that can process the request. In this example, the IP address is for Facility B.
3. The client makes a request to Amazon S3 Facility B.
4. Facility B returns a copy of the dolphin.jpg object to the client.

### DNS temporary redirects

One of the design requirements of Amazon S3 is extremely high availability. One of the ways we meet this requirement is by updating the IP addresses associated with the Amazon S3 endpoint in DNS as needed.  

Due to the distributed nature of Amazon S3, requests could temporarily route to the wrong Region. This is most likely to occur immediately after the creation or deletion of buckets. A temporary redirect is a type of error response that signals to the requester that they should resend the request to a different endpoint. 

For example, if you create a new bucket and immediately make a request to the bucket, you might receive a temporary redirect, depending on the location constraint of the bucket. If you created the bucket in the US East (N. Virginia) AWS Region, you will not see the redirect because this is also the default Amazon S3 endpoint.

However, if the created bucket is in any other AWS Region, any requests for the bucket go to the default endpoint while the bucket's DNS entry is propagated. The default endpoint redirects the request to the correct endpoint with an HTTP 302 response. Temporary redirects contain a URI to the correct Region, which you can immediately resend the request.

Review the diagram below that illustrates a temporary request redirection and then review the steps to ensure you understand the process.

#### Temporary request redirection steps

![DNS temporary redirects](images/Fundamentals/dns-temporary-redirects.png)

1. The client makes a DNS request to get the dolphin.jpg object stored on Amazon S3.
2. The client receives an IP address for a Region that can process the request. In this example the IP that is returned is `192.168.7.52`.
3. The client makes a request to Amazon S3 Region B, located at 192.168.7.52.
4. Region B returns a redirect indicating the object is available from Location D, at `192.168.7.54`.
5. The client resends the request to Region D, at 192.168.7.54.
6. Region D returns a copy of the requested object.

- [**DNS For S3**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingRouting.html)

## Amazon S3 Data Management
Amazon S3 gives you robust capabilities to manage access to your data.  In this lesson, the focus is on how to get data into and out of Amazon S3 from both the AWS Management Console and the CLI. It is important to become familiar with using both tools due to file upload limitations in the AWS Management Console. 

The first topic to explore is the new Amazon S3 data consistency model used when adding or modifying data to an S3 bucket. 

### S3 Strong data consistency model
Amazon S3 now delivers strong read-after-write consistency for any storage request, without changes to performance or availability, without sacrificing regional isolation for applications, and at no additional cost.  Any request for S3 storage is now strongly consistent.

After a successful write of a new object or overwrite of an existing object, any subsequent read request immediately receives the latest version of the object. Amazon S3 also provides strong consistency for list operations, so after a write, you can immediately perform a listing of the objects in a bucket with any changes reflected.

Why is this important? Previously, the Amazon S3 consistency model was strongly consistent for new objects and eventually consistent for modified or recently queried objects.  However, with the increased usage of high process analytics engines, applications and users need to have access to update data immediately after written. The strong read-after-write consistency model addresses the needs of large data lakes and applications that require immediate access to changed data.

There is no charge for this feature and it is available for all GET, PUT, LIST, HEAD requests, as well as Access Control Lists, object tags, and other metadata. For bucket operations such as reading a bucket policy or metadata, the consistency model remains eventually consistent.

### AWS Management Console
The AWS Management Console is a graphical user interface that allows you to enable or disable versioning, view access logs, permissions and encryption, and manage all aspects of your buckets and objects though a friendly user interface. It provides you a secure login and management capabilities using your AWS or AWS Identity and Access Management (Identity and Access Management) account credentials, and allows you to enable AWS Multi-Factor Authentication for additional security.

You can personalize your AWS Management Console experience by creating shortcuts to the services you visit most often, like Amazon S3, by dragging and dropping the links onto the console’s top-level toolbar to create your shortcuts.

In addition to this, any login session that is not closed automatically expires after 12 hours. The console supports the three latest versions of Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari, as well as, Microsoft Internet Explorer 11. The AWS Management Console has a mobile app as well. With the mobile app, you can easily view your existing buckets and objects. The app also allows you to perform operational tasks. 

### Getting started with Amazon S3

Learning Amazon S3 by using the console gives you the opportunity to visualize buckets and objects, and explore all of the configuration options available to you. You can manage and maintain most of your Amazon S3 storage via the console but some restrictions will prompt you to use the command line.

For example, the largest file you can upload via the AWS Management Console is 160 GB. Any larger files will need to be uploaded programmatically either at the command line or from within your applications.

![S3 bucket](images/Fundamentals/amazon-s3-bucket.jpeg)

#### Versioning

Versioning is a means of keeping multiple variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. With versioning, you can easily recover from both unintended user actions and application failures. If Amazon S3 receives multiple write requests for the same object simultaneously, and you enable versioning, it will store all of the object write requests.

If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object being stored. In one bucket, for example, you can have two objects with the same key, but different version IDs, such as dolphins.jpg (version 111111) and dolphins.jpg (version 222222). 

Versioning-enabled buckets enable you to recover objects from accidental deletion or overwrite. For example:
- If you delete an object, instead of removing it permanently, Amazon S3 inserts a delete marker, which becomes the current object version. You can always restore the previous version. 
- If you overwrite an object, it results in a new object version in the bucket. You can always restore the previous version.

### Using the command line

In Amazon S3 there are two types of commands you can use from the CLI: high-level commands and low-level commands.  In this topic, you will cover both types of commands and resource links provided for additional reading material.

#### High-level commands

High-level commands simplify managing Amazon S3 objects from a command line. These commands enable you to manage the contents of Amazon S3 within itself and with local directories. You can identify the high-level commands because they begin with aws s3.

#### Example of using high-level commands
The following example uses the aws s3 command to make a bucket called demo-oceanlife, then the example shows how to copy a file called into the bucket, then list the Amazon S3 buckets available, and finally list the individual objects within the buckets.

**Make a bucket**

```sh
aws s3 mb s3://demo-oceanlife-cmd
```

```
make_bucket: demo-oceanlife-cmd
```

Here you use the aws `s3 mb` or make bucket command to make a bucket called "demo-oceanlife". 

The output, listed on the second line, `make_bucket: demo-oceanlife` indicates a successful bucket creation.

**Copy files to a bucket**

```sh
aws s3 cp ~/Downloads/whale.jpg s3://demo-oceanlife-cmd
```

In this command, you use the `aws s3 cp` command to copy the `whale.jpg` file from the client local machine in `~/Downloads` to the demo-oceanlife-cmd bucket. 

The output on the second line, `upload: Downloads/whale.jpg to s3://demo-oceanlife-cmd/whale.jpg` appears while the file copies.

**Viewing the list of Amazon S3 buckets**

```sh
aws s3 ls
```

```
2023-12-19 16:25:21 demo-oceanlife-cmd
```

In order to list all of the buckets in your account, you use the `aws s3 ls` command. 

The output on the second line lists the one bucket you created in the first step called `demo-oceanlife-cmd`. If you had more buckets in your account you would see all of the buckets listed here.

**Viewing objects in the bucket**

```sh
aws s3 ls s3://demo-oceanlife-cmd
```

```
2023-12-19 16:34:55 whale.jpg
```

Additionally, to view all objects in a specific bucket, in this case the `demo-oceanlife-cmd` bucket, you can use the `aws s3 ls *bucketname*` to see all of the files in the bucket.

The output on the second line shows the one file, **whale.jpg**, that was uploaded.

**Delete objects**

```sh
aws s3 rm s3://demo-oceanlife-cmd/whale.jpg
```

```
delete: s3://demo-oceanlife-cmd/whale.jpg
```

The following example deletes `whale.jpg` from `s3://demo-oceanlife-cmd`. The output on the second line shows the one file, **whale.jpg**, that was deleted.

**Delete buckets**

```sh
aws s3 rb s3://demo-oceanlife-cmd
```

```
remove_bucket: demo-oceanlife-cmd
```

The following example removes the `s3://demo-oceanlife-cmd` bucket. The output on the second line shows that the bucket **demo-oceanlife-cmd** was removed.

High-level commands allow you to functionally manage and work with your Amazon S3 buckets.

- [**S3 High level commands**](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)

#### Low Level Commands
Low-level commands use the s3api command-set and provide direct access to the Amazon S3 APIs, enabling operations not exposed in the high-level s3 commands. Most of the the s3api commands are generated from JSON models that directly imitate the APIs of other AWS services that provide API-level access.

The **s3api list-objects** and **s3api make-bucket** commands share a similar operation name, input, and output as the corresponding operation in the Amazon S3 API. As a result, these commands allow a significantly more granular amount of control over your buckets when using the CLI. 

- [**Amazon S3 documentation: Using s3api commands**](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-apicommands.html)
- [**s3api**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html)

### PUT operations

Use the PUT request operation to add an object to a bucket. You must have **WRITE** permissions on a bucket in order to add an object. Amazon S3 never adds partial objects; if you receive a success response, you can be confident that the entire object was stored durably. 

If the object already exists in the bucket, the new object overwrites the existing object. Amazon S3 orders all of the requests that it receives but it is possible that if you send two requests nearly simultaneously, the received requests will be in a different order than sent.

The last request received is the one which is stored. This means that if multiple parties are simultaneously writing to the same object, they may all get a success response even though only the last write wins. This is because Amazon S3 is a distributed system and it may take a few moments for one part of the system to communicate that another part has received an object update. 

#### Multipart Upload API
You can upload or copy objects of up to **5 GB** in a single PUT operation. For objects, up to **5 TB** you must use the multipart upload API. The multipart upload API allows you to upload a single object as a set of parts. Each part is a contiguous portion of the object's data. You can upload these object parts independently and in any order.

![multipart upload](images/Fundamentals/mutlipart-upload.png)

If transmission of any part fails, you can re-transmit just that part without having to re-transmit all the parts. After all parts of your object upload, Amazon S3 assembles these pieces and creates the object. In general, when your object size reaches **100 MB**, you should consider using multipart uploads instead of uploading the object in a single operation. 

Using multipart upload provides the following advantages:
- Improved throughput - You can upload parts in parallel to improve throughput.
- Quick recovery from any network issues - Smaller part size minimizes the impact of restarting a failed upload due to a network error.
- Pause and resume object uploads - You can upload object parts over time. Once you initiate a multipart upload there is no expiry; you must explicitly complete or abort the multipart upload.
- Begin an upload before you know the final object size - You can upload an object as you are creating it.

[**Uploading and copying objects using multipart upload**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

#### Object lifecycle management

When using multipart uploads, Amazon S3 retains all the parts on the server until you complete or discontinue the upload. To avoid unnecessary storage costs related to incomplete uploads, make sure to complete or discontinue an upload. Use lifecycle rules to clean up incomplete multipart uploads automatically.

An Amazon S3 Lifecycle configuration is an XML file that consists of a set of rules with predefined actions that you want Amazon S3 to perform on objects during their lifetime. As a best practice, we recommend you configure a lifecycle rule using the **AbortIncompleteMultipartUpload** action to minimize your storage costs.

It is recommended that you enable the ability to clean incomplete multipart uploads in the lifecycle settings even if you are not sure whether you are going to perform multipart uploads. Some applications default to multipart uploads when uploading files over a particular application-dependent size and failed or incomplete uploads will result in increased storage costs.

[**Object Lifecycle**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html)

### GET operations

You can use the GET operation to retrieve a whole object or parts of an object directly from Amazon S3. 

If you need to retrieve the object in parts, use the Range HTTP header in a GET request. Doing this allows you to retrieve a specific range of bytes from an object stored in Amazon S3. You can then resume fetching other parts of the object whenever you or your application is ready. This resumeable download is useful if you only need portions of your object data, in cases where network connectivity is poor, or if your application must process only subsets of object data.

### Delete operations

With a delete operation, you can delete either a single object or multiple objects in a single delete request. Multiple outcomes are possible when you issue a DELETE request, depending on whether you enable versioning or disable it on your bucket.

The images listed below illustrate the delete operations on versioning enabled and non-versioning enabled buckets.

![Delete operations](images/Fundamentals/delete-operations.png)

#### Versioning not enabled

If a bucket is not versioning-enabled, you can permanently delete an object by specifying the key name of the object. The DELETE request will permanently remove the object from the bucket, making it unrecoverable.

#### Permanent deletes

If a bucket is versioning-enabled, you can either permanently delete an object or have Amazon S3 create a delete marker for the object, which allows the object to be recoverable.

You can permanently delete individual versions of an object by invoking a DELETE request with the object's key and version ID. To completely remove the object from your bucket, you must delete each individual version.

![Object deletions](images/Fundamentals/object-deletions-1.png)

#### Recoverable deletes

If your DELETE request specifies only the object's key name, Amazon S3 inserts a delete marker that becomes the current version of the object. If you try to retrieve an object that has a delete marker, Amazon S3 returns a **404 NOT FOUND** error. You can recover the object by removing the delete marker from the current version of the object, making the object available for retrieval.

![Object deletions](images/Fundamentals/object-deletions-2.png)

## Cloud Data Migration Services
Data is a cornerstone of successful application deployments, analytics workflows, and machine learning innovations. When moving data to the cloud, you need to understand your different use cases, the types of data you are moving, and the network resources available. AWS offers a wide variety of services and partner tools to help you migrate your data sets, whether they are files, databases, machine images, block volumes, or even tape backups. 

The portfolio of data transfer services provides the ideal solution for any data migration project. The level of online connectivity is a major factor in data migration, and AWS has offerings that can address your hybrid cloud storage, online data transfer, and offline data transfer needs.  In this lesson, we cover a high-level overview of the available migration tools.

### Online data transfer services

Online data transfer services are a group of offerings that allows you to move your data into and out of the AWS Cloud and Amazon S3 via online, internet based, connections.

#### AWS DataSync
AWS DataSync makes it simple and fast to move large amounts of data online between on-premises storage and Amazon S3. DataSync manages many of the tasks related to data transfers that can slow down migrations. You can also reduce the burden of your IT operations, including running your own instances, handling encryption, managing scripts, network optimization, and data integrity validation.

DataSync can transfer hundreds of terabytes and millions of files at speeds up to 10 times faster than open-source tools. You can use it to migrate active data sets or archives to AWS, transfer data to the cloud for timely analysis and processing, or replicate data to AWS for business continuity. 

For additional information on AWS Data Sync, select the following link:

https://aws.amazon.com/datasync/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc

#### AWS Transfer Family
The AWS Transfer Family provides fully managed support for file transfers directly into and out of Amazon S3. The AWS Transfer Family helps you seamlessly migrate your file transfer workflows to AWS by integrating with existing authentication systems, and providing DNS routing with Amazon Route 53 so nothing changes for your customers and partners, or their applications. With your data in Amazon S3, you can use it with AWS services for processing, analytics, machine learning, and archiving. 

For additional information on AWS Transfer Family, select the following link:

https://aws.amazon.com/aws-transfer-family/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc 

#### Amazon S3 Transfer Acceleration
You can use Amazon S3 Transfer Acceleration for fast, easy, and secure transfers of files over long distances. It takes advantage of Amazon CloudFront globally distributed edge locations, routing data to Amazon S3 over an optimized network path.

Transfer Acceleration is best suited for scenarios in which you want to transfer data to a central location from all over the world or transfer significant amounts of data across continents regularly. It can also help you use your available bandwidth when uploading to Amazon S3.

For additional information on Amazon S3 Transfer Acceleration, select the following link:

https://aws.amazon.com/s3/transfer-acceleration/

#### Amazon Kinesis Data Firehose
You can also stream data into Amazon S3 by using Amazon Kinesis Data Firehose, a fully managed streaming service. Because it captures and automatically loads streaming data in Amazon S3 and Amazon Redshift, you get near-real-time analytics with the business intelligence tools that you already use.

For additional information on Amazon Kinesis Data Firehose select the following link:

https://aws.amazon.com/kinesis/data-firehose/?kinesis-blogs.sort-by=item.additionalFields.createdDate&kinesis-blogs.sort-order=desc

#### Amazon Kinesis Data Streams
Amazon Kinesis Data Streams (KDS) enables you to build custom applications that process or analyze streaming data for specialized needs. Kinesis Data Streams can continuously capture and store terabytes of data per hour from hundreds of thousands of sources, such as website clickstreams, financial transactions, social media feeds, IT logs, and location -tracking events. You can also emit data from Kinesis Data Streams to other AWS services, such as Amazon S3, Amazon Redshift, Amazon EMR, and AWS Lambda.

For additional information on Amazon Kinesis Data Streams, select the following link:

For additional information on Amazon Kinesis Data Streams select the following link:

https://aws.amazon.com/kinesis/data-streams/

#### Amazon Partner Network
You can use third-party connectors from the Amazon Partner Network for additional Amazon transfer service support. Amazon partners can help you move your data to the cloud. The simplest way to do that is through an embedded connection in your backup software. Using this approach, your backup catalog stays consistent so that you maintain visibility and controls across jobs that span disk, tape, and the cloud.

For additional information on Amazon Partner Network select the following link:

https://aws.amazon.com/partners/

### Offline data transfer services

Offline data transfer services use an alternate, physical storage method to move your data from remote locations to AWS. AWS Snowcone, AWS Snowball, and AWS Snowmobile are offline transfer services designed to transfer various quantities of data based on your business need.

#### AWS Snowcone
AWS Snowcone is the smallest member of the AWS Snow Family of edge computing, edge storage, and data transfer devices, weighing in at 4.5 pounds (2.1 kg) with 8 terabytes of usable storage. You can run compute applications at the edge, and ship the device with data to AWS for offline data transfer, or you can transfer data online with AWS DataSync from edge locations.

Snowcone has multiple layers of security and encryption. You can use it to collect, process, and transfer data to Amazon S3. Snowcone is designed for data migration needs up to dozens of terabytes (with up to 8 terabytes per device) and from space-constrained environments where AWS Snowball devices will not fit.

For additional information on AWS Snowcone select the following link:

https://aws.amazon.com/snowcone

#### AWS Snowball
AWS Snowball is an edge computing, data migration, and edge storage device that comes in two options: Snowball Edge Storage Optimized and Snowball Edge Compute optimized.

Snowball Edge Storage Optimized devices provides both block storage and Amazon S3-compatible object storage, along with 40 vCPUs. Snowball Edge Compute Optimized devices provide 52 vCPUs, block and object storage, and an optional GPU for use cases like advanced machine learning and full motion video analysis in disconnected environments.

You can use these devices for data collection, machine learning and processing, and storage in environments with intermittent connectivity (like manufacturing, industrial, and transportation) or in extremely remote locations (like military or maritime operations) before shipping back to AWS. These devices may also be rack mounted and clustered together to build larger temporary installations.

For additional information on AWS Snowball select the following link:

https://aws.amazon.com/snowball/

#### AWS Snowmobile
AWS Snowmobile is an Exabyte-scale data transfer service used to move extremely large amounts of data to AWS. You can transfer up to 100PB per Snowmobile, a 45-foot long ruggedized shipping container, pulled by a semi-trailer truck. 

Snowmobile uses multiple layers of security to help protect your data including dedicated security personnel, GPS tracking, alarm monitoring, 24/7 video surveillance, and an optional escort security vehicle while in transit. All data is encrypted with 256-bit encryption keys you manage through the AWS Key Management Service (KMS) and designed for security and full chain-of-custody of your data.

For additional information on AWS Snowmobile select the following link:

https://aws.amazon.com/snowmobile/

### Hybrid cloud storage services

If you want to take advantage of the benefits of cloud storage but have applications running on-premises that require low-latency access to their data, or you need rapid data transfer to the cloud; then you can use AWS hybrid cloud storage architectures. 

A hybrid storage strategy allows you to connect your on-premises applications and systems to cloud storage. This helps you reduce costs, minimize management burden, and innovate with your data.

#### AWS Direct Connect
AWS Direct Connect is a dedicated network connection from your on-premise data center to AWS. It provides a dedicated connection for higher throughput and secure data transfer without passing through the internet. Using industry standard 802.1q VLANs, this dedicated connection can be partitioned into multiple virtual interfaces. 

For additional information on AWS Direct Connect select the following link:

https://aws.amazon.com/directconnect/

#### AWS Storage Gateway
You can use the AWS Storage Gateway, in File Gateway mode, to store your on premises data in an existing Amazon S3 bucket. You can deploy AWS Storage Gateway as a virtual appliance or purchase a hardware appliance version.

AWS Storage Gateway configured as a File Gateway enables you to connect your Amazon S3 bucket using either the Network File System (NFS) or Server Message Block (SMB) protocol with local caching. You can transfer your data using an AWS File Storage Gateway over the internet or over an AWS Direct Connect connection.

For additional information on AWS File Storage Gateway select the following link:

https://aws.amazon.com/storagegateway/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc

### Unmanaged cloud data migration tools

AWS also offers easy script or CLI tools to move data from your site into AWS cloud storage. 

#### rsync and 3rd party tools
Depending your needs, you have the option to use rsync, an open source tool, along with other third-party file system tools to copy data directly into Amazon S3 buckets.

#### Amazon S3 and the AWS CLI
You can use the Amazon S3 and the AWS CLI to write commands and scripts that help you to move data directly into Amazon S3 buckets.

[**Cloud Data Migration**](https://aws.amazon.com/cloud-data-migration/)

## Securing Data Access
As with all of the AWS services, security exists in all layers of Amazon S3. By default, all Amazon S3 resources are private and accessible by the resource owner or account administrator. By implementing a strict security stance, Amazon S3 allows you to work backwards, configure, and finely-tune your access policies. This helps to align your organizational, governance, security, and compliance requirements. One of AWS Security best practices is to design your environment based on the principle of least privilege.

### Principle of least privilege

Least privilege is a security design strategy where granted permissions allow only the minimum necessary rights required to accomplish the task. With least privilege, you start with a strict set of minimum permissions and grant additional permissions only when necessary. Starting with tight restrictions and adding new ones when required is more secure. Starting with open permissions too lenient and then trying to tighten them later is less secure.

When working with Amazon S3, identify what each user, role, and application needs to accomplish within your buckets and then create policies that allow them to perform only those specific tasks. When granting permissions, you decide who gets permissions and into which Amazon S3 resources. You enable specific actions that you want to allow on those resources. Therefore, you should grant only the permissions that are required to perform a task. Implementing least privilege access is fundamental in reducing security vulnerabilities.

### Security mechanisms

A newly created bucket can only be accessed by the user who created it or by the account owner. You must grant access to other users by using one or a combination of the following access management features.

#### AWS Identity and Access Management(IAM)
IAM is used to create users and manage their respective access to resources, including buckets and objects.

#### Bucket policies
Bucket policies are used to configure permissions for all or a subset of objects using tags and prefixes.

#### Pre-Signed URLS
Pre-Signed URLs are used to grant time-limited access to others with temporary URLs.

#### Access control lists
Access Control List (ACLs) to make individual objects accessible to authorized users.
> Note: Amazon S3 ACLs are a legacy access control mechanism that predates IAM. AWS recommends using Amazon S3 bucket policies or IAM policies for access control.

### Block Public Access

AWS introduced the S3 Block Public Access feature to help you avoid inadvertent data exposure. With Block Public Access, you can manage public access of your Amazon S3 resources at both the AWS account level and the bucket level, which helps ensure that your data is not publicly available. Any new bucket created has block all public access enabled by default. 

What does this mean for you? If you want to grant public access on any resources managed by Block Public Access, you will have to adjust your Block Public Access configuration. 

![Block public access](images/Fundamentals/block-public-access.jpeg)

### Amazon S3 Block Public Access settings

Review each of the available Block Public Access (BPA) options, which are either enabled at the account level or the bucket level. If enabled at the account level, the BPA settings override any settings on the individual buckets.

#### Block all public access
Sometimes, you want to make sure that a bucket will never allow public access. By enabling this one click option, you can prevent public access to your bucket. This overrides any configured ACLs and bucket polices that would normally grant public access. Choosing to enable this option equates to enabling all of the other options listed here.

Any new bucket you create will have this option enabled by default. You need to disable this option if you want to allow public access to your bucket or objects.

![Block all public access](images/Fundamentals/block-all-public-access.jpeg)

#### Block public access granted through new ACLs
This option prevents you from creating any new ACL, either for a bucket or object, which grants public access permissions. This option only affects the creation of new public ACLs; it does not alter any existing ACLs or policies. Any existing ACLs or policies granting public access will not affect permissions and public access to those resources will remain intact.

After you enable this option, you should then review your ACLs to evaluate any existing public access permissions and assess whether or not those permissions should stay the same.

Remember, with this option enabled, if you have any bucket policies or existing ACLs granting public access to buckets and objects, those resources will remain publicly accessible. If you wish to block all public access to buckets and objects, choose the block all public access option.

![BPA new acls](images/Fundamentals/bpa-new-acls.jpeg)

#### Block public access granted through any ACLs
This option only affects how you evaluate ACL public permissions. When you enable this option, it ignores any existing ACLs that grant public permission on buckets and objects. This does not alter the existing ACLs themselves, but any resources configured with existing public ACLs will no longer be publicly accessible. 

It can be confusing because it does not prevent you from creating new ACLs that would normally grant public access. You can still create them, but those ACLs will not become effective, resulting in the bucket or object not being publicly accessible. 

You should take the time to review your ACLs once enabled and remove any public ACLs to prevent any possible future mistakes. Any existing public ACLs, will no longer be ignored, if the block public access granted through any ACLs option is later disabled.

Remember, with this option enabled, if you have any bucket policies granting public access to buckets and objects, those buckets or objects will remain publicly accessible. If you wish to block all public access to buckets and objects, choose the block all public access option.

![BPA any ACLs](images/Fundamentals/bpa-any-acls.jpeg)

#### Block public access granted through new public bucket policies
This option only prevents the creation of new bucket policies that grant public access. Any existing bucket policies are not affected. If you currently have any bucket policies configured that grant public access, those buckets or objects will remain publicly accessible. 

To use this setting effectively, you should apply it at the AWS account level. A bucket policy can allow users to alter a bucket's Block Public Access settings. Therefore, users who have permission to change a bucket policy could insert a policy that allows them to disable the Block Public Access settings for the bucket. If enabling this setting for the entire account, rather than for a specific bucket, Amazon S3 blocks public policies even if a user alters the bucket policy to disable this setting. 

Remember, with this option enabled, if you have any existing bucket policies or ACLs granting public access to buckets and objects, those buckets or objects will remain publicly accessible. If you wish to block all public access to buckets and objects, choose the block all public access option.

![bpa new public bucket policies](images/Fundamentals/bpa-new-public-bucket-policies.jpeg)

#### Block public and cross-account access granted through any public bucket policies
This option only affects how you evaluate bucket policy permissions. When you enable this option, it ignores any buckets or objects that have public permissions granted through bucket policies. This option, when enabled, restricts access to a bucket with a public policy to only AWS services and authorized users within the bucket owner's account. This setting blocks all cross-account access to the bucket with a public policy (except by AWS services), while still allowing users within the account to manage the bucket. 

This does not alter existing bucket policies, but ignores any existing bucket policies that grant public access, blocking public access and any cross-account access configurations. 

Remember, with this option enabled, if you have any ACLs granting public access to buckets and objects will remain publicly accessible. If you wish to block all public access to buckets and objects, choose the block all public access option

![bpa cross account access](images/Fundamentals/bpa-cross-account-access.jpeg)

> Unless you need to make your bucket or objects publicly available, it is strongly recommended enabling the block all public access option.

### Access policies

Access policy describes who has access to what resources. They attach to your resources, such as buckets and objects, and are also called resource policies. For example, bucket policies and access control lists are resource based policies because you attach them directly to buckets and objects.

User policies or IAM policies are access policies attached to users in your account. You may choose to use one type of policy or a combination of both, to manage permissions with your Amazon S3 resources.

Examine the example of access policies in the image below. Both the bucket and user policies are written in JSON format. Just by looking at the code, it may not be immediately apparent which policy is for a user and which is for a bucket. However, by looking at what the policy is attached to, you can quickly determine which type of policy it is. If you are not familiar with JSON, AWS has a policy generator tool to assist you. 

![Access policies](images/Fundamentals/access-policies.png)

[**AWS Policy Generator**](https://awspolicygen.s3.amazonaws.com/policygen.html)

### Bucket policies

In order to grant other AWS accounts or IAM users access to the bucket and the objects in it, you need to attach a bucket policy. Because you are granting access to a user or account, a bucket policy must define a PRINCIPAL (which is an account, user, role, or service) entity within the policy. You will notice that the "Principal" statement is listed in the policy. Consult the image below as an example.

When using bucket policies, Amazon S3 is managing the security. Bucket policies supplement, and in many cases, replace legacy ACL-based access policies. Amazon S3 supports a bucket policy size limit of up 20 kb.

![bucket policies](images/Fundamentals/bucket-policies.png)

> Because bucket policies grant access to another AWS account or IAM user, you must specify the principal, or the user to whom you are granting access, as a "Principal" in the bucket policy.

#### When to use a bucket policy

Use a bucket policy if:

- You need to grant cross-account permissions to other AWS accounts or users in another account, without using IAM roles.
- Your IAM policies reach the size limits for users, groups, roles. 
- You prefer to keep access control policies in the Amazon S3 environment.
- Although both bucket and user policies support granting permission for all Amazon S3 operations, the user policies are for managing permissions for users in your account. 

### IAM policies

You can use IAM to manage access to your Amazon S3 resources. You can create IAM users, groups, and roles in your account and attach access policies to them granting them access to AWS resources, including Amazon S3. 

There are maximum size limitations for IAM policies for users, groups, and roles. IAM policies have a 2 kb size limit for users, 5 kb for groups, and a 10 kb for roles. Also note that there is no principal stanza listed in the User policy as the principal is whichever user the policy is applied to.

![IAM policies](images/Fundamentals/iam-policies.png)

In this example, you grant your IAM user access to your buckets, `ocean-life-bucket`, and allow the user to `Put*, Get*, Delete*` objects. The policy also grants the `s3:ListAllMyBuckets`, `s3:GetBucketLocation`,  `s3:ListBucket`, `s3:PutObjectAcl`, and `s3:GetObjectAcl` permissions which are additional permissions required by the AWS console. This example also shows each permission applied to different resources. In the top permission, the resource is all buckets (*). In the middle the permission is applied to one specific bucket, called `ocean-life-bucket`. The bottom permission applies to only objects within the `ocean-life-bucket`.

#### When to use IAM user policies

Use IAM policies if:

- You need to control access to AWS services other than Amazon S3. IAM policies allow for easier centralized management all of your permissions.
- You have numerous Amazon S3 buckets each with different permissions requirements. IAM policies will be easier to manage than having to define a large number of Amazon S3 bucket policies. This way you can focus on having fewer, more detailed IAM policies.
- You prefer to keep access control policies in the IAM environment.

### Query string authentication 

You can use a query string to express a request entirely in a URL. To do this, you use query parameters to provide request information, including the authentication information. Because the request signature is part of the URL, this referred to as a **presigned URL**. 

### Presigned URLs

All objects and buckets by default are private and only the object owner has permission to access these objects. However, the object owner can share their objects with others who do not have AWS credentials. They can create a presigned URL to grant time-limited permission to download the objects. 

The main purpose of a pre-signed URL is to grant temporary access to the required object. When you create a presigned URL, you must provide your security credentials and then specify a bucket name, an object key, an HTTP method (PUT for uploading objects), and an expiration date and time. Anyone who receives the presigned URL can then access the object. For example, if you have a video in your bucket and both the bucket and the object are private, you can share the video with others by generating a presigned URL. A presigned URL remains valid for a limited period of time, which is specified when the URL generates. You can use presigned URLs to embed clickable links, which can be valid for up to seven days, in HTML.

A use case scenario for presigned URLs is that you can grant temporary access to your Amazon S3 resources. For example, you can embed a presigned URL on your website or alternatively use it in command line client (such as Curl) to download objects. You could also programmatically generate a presigned URL to allow a user to an upload an object to a bucket. 

### How to create a presigned URL
This demonstration shows you how to create a presigned URL for a non-public object called `whale.jpg`.

Imagine that you need to share this image with an external vendor who is creating an informational brochure on ocean life. The external vendor does not have an AWS account and has no access to your private bucket to view objects.

#### Verify the location of the object
![Step 1](images/Fundamentals/presigned-url-step1.jpeg)

First, you must locate the bucket with the correct image. In this step, you identify the necessary bucket as `getting-started-s3-demo-bucket` and the object, `whale.jpg`, as the object you need to share with the external vendor.

Select the image to enlarge it.

#### Use AWS CLI to view the command

![Step 2](images/Fundamentals/presigned-url-step2.jpeg)

Using the AWS CLI, you view the command help to determine which options are required to generate the presigned url. 

#### Specifying the default Signature Version

```sh
aws configure set default.s3.signature_version s3v4
```

Amazon S3 supports only AWS Signature Version 4 in most AWS Regions. You must set the default Signature Version for your AWS CLI connection. This step shows how to configure Signature Version 4 as default.

#### Generate the presigned URL

```sh
aws s3 presign s3://getting-started-s3-demo-bucket/whale.jpg --expires 3600 --region us-east-1
```

In this step you run the command to generate the presigned URL indicating the correct bucket, `getting-started-s3-demo-bucket` and the object to share as `whale.jpg`.

```sh
aws s3 presign s3://test-presigned-url-cmd/whale.jpeg --expires 3600 --region us-east-1
```

#### Presigned URL

**Output**

```
https://test-presigned-url-cmd.s3.us-east-1.amazonaws.com/whale.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAY362MTJFBPCRGWWZ%2F20231220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231220T144508Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=c153ba09b5042cc33f659733f155cd464457b49a0465c8fb5928a93f00a981c7
```

This output shows you what the presigned URL looks like after the command is run to generate it. You can now copy and send this URL to your external vendor so that they may access the `whale.jpeg` image. This URL contains a short time limit, `Amz-Expires=3600` which means this particular URL will expire in `60 minutes`.

#### Viewing the image

![whale.jpeg](images/Fundamentals/whale.jpeg)

Finally, once you have sent the presigned URL to your external vendor, they will be able to paste the URL into a browser to view the image within the allotted time. Once that time has expired, they will lose access to view the image.

### Additional considerations
#### Permissions to the object
Anyone with valid security credentials can create a presigned URL. However, to successfully access an object, someone who has permission to perform the operation must create the presigned URL.

#### Credentials
The credentials that you can use to create a presigned URL include:
- **IAM instance profile**: Valid up to 6 hours
- **AWS Security Token Service**: Valid up to 36 hours when signed with permanent credentials, such as the credentials of the AWS account root user or an IAM user
- **IAM user**: Valid up to 7 days when using AWS Signature Version 4

To create a presigned URL that's valid for up to 7 days, first designate IAM user credentials (the access key and secret access key) to the SDK that you're using. Then, generate a presigned URL using AWS Signature Version 4.

#### Token expiration
If you created a presigned URL using a temporary token, then the URL expires when the token expires, even if you created the URL with a later expiration time. 

[**How to generate presigned URLs**](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-presigned-urls.html)

### Amazon S3 Object Ownership 

Prior to the addition of Amazon S3 Object Ownership, an S3 object was owned by the AWS account that uploaded the object. If a bucket owner uploads an object, the bucket owner remains the owner of that object. If another AWS account uploads objects to your bucket, the objects remain owned by the other AWS account that uploaded the object. 

AWS has released a new feature that allows all objects written to a bucket to be owned by the bucket owner.  With Amazon S3 Object Ownership, the bucket owner, now has full control of the objects, and may own any new objects written by other accounts automatically.

Amazon S3 Object Ownership has two modes: (see image below)
1. **Object writer** – The account that is writing the object owns the object.
2. **Bucket owner preferred** – The bucket owner will own the object if uploaded with the bucket-owner-full-control canned ACL. Without this setting and canned ACL, the object is uploaded to the bucket but remains owned by the uploading account.

![Object ownership](images/Fundamentals/object-ownership.png)

### Enforcing S3 Object Ownership

After setting S3 Object Ownership to bucket owner preferred, you can add a bucket policy to require all Amazon S3 PUT operations to include the bucket-owner-full-control canned ACL. This ACL grants the bucket owner full control of new objects, and with the S3 Object Ownership setting it transfers object ownership to the bucket owner. If the uploader fails to meet the ACL requirement in their upload, the request will fail. This enables bucket owners to enforce uniform object ownership across all newly uploaded objects in their buckets. 

For additional information on Amazon S3 Object Ownership choose this [link](https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html)

### Access Analyzer

On the Amazon S3 console, you can use Access Analyzer for Amazon S3 to review all buckets that have bucket access control lists (ACLs), bucket policies, or access point policies that grant public or shared access.

Access Analyzer for Amazon S3 alerts you to buckets configured to allow access to anyone on the internet or other AWS accounts, including AWS accounts outside of your organization. For each public or shared bucket, you receive findings that report the source and level of public or shared access.

[**Security in Amazon S3**](https://aws.amazon.com/s3/security/)

## Encrypting Data

### Data in-transit and data at-rest

Data protection refers to protecting data while in-transit (data traveling to and from Amazon S3) and while at rest (while stored on disks in Amazon S3 data centers). You can protect data in transit using Secure Socket Layer/Transport Layer Security (SSL/TLS) or client-side encryption. By providing the appropriate level of protection for your data in transit, you protect the confidentiality and integrity of your workload’s data from any bad actor who may intercept the data while in transit. Because the AWS API is a REST service that supports SSL/TLS connections, all official AWS SDKs and CLI tools connect to the AWS API using SSL/TLS by default. 

For data at rest (data already stored on disk), Amazon S3 provides you with two options: **Server-side encryption**, and **client-side encryption**.

### Server-side encryption

When you use server-side encryption, Amazon S3 encrypts an object before saving it to disk and decrypts it when you download it. As long as you authenticate and have access permissions, there is no difference in how you access encrypted or unencrypted objects. For example, if you share your objects using a presigned URL, that URL works the same way for both encrypted and unencrypted objects. Additionally, when you list objects in your bucket, the list API returns a list of all objects, regardless of their encryption. 

### Three server-side encryption options

You have three mutually exclusive options, depending on how you choose to manage the encryption keys. 

#### SSE-S3
Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3)

When you use Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3), each object encrypts with a unique key. As an additional safeguard, it encrypts the key itself with a master key that it regularly rotates. Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data. 

For additional information: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

#### SSE-KMS
Server-Side Encryption with Customer Master Keys (CMKs) Stored in AWS Key Management Service (SSE-KMS)

Server-Side Encryption with Customer Master Keys (CMKs) Stored in AWS Key Management Service (SSE-KMS) is similar to SSE-S3, but with some additional benefits and charges for using this service. There are separate permissions for the use of a CMK that provides added protection against unauthorized access of your objects in Amazon S3. SSE-KMS also provides you with an audit trail showing when and who used the CMK. Additionally, you can choose to create and manage customer managed CMKs, or use AWS managed CMKs that are unique to you, your service, and your Region. 

For more information:

link: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html

#### SSE-C
Server-Side Encryption with Customer-Provided Keys (SSE-C)

With Server-Side Encryption with Customer-Provided Keys (SSE-C), you manage the encryption keys and Amazon S3 manages the encryption, as it writes to disks, and decryption, when you access your objects. With this option, the customer is responsible for managing and rotating the keys, and without access to these keys the Amazon S3 data can not be decrypted.

For more information: https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html

### Client-side encryption

Client-side encryption is the act of encrypting sensitive data before sending it to Amazon S3. When using client-side encryption, the encryption performs locally and your data never leaves the run environment unencrypted. You maintain possession of your master encryption keys, and they are never sent to AWS therefore, it is important that you safely store them (i.e., as a file or using a separate key management system) and load them when uploading or downloading objects. This ensures that no one outside of your environment has access to your master keys and without access to the master keys; your data cannot be decrypted. If your master encryption keys are lost, you will not be able to decrypt your own data, therefore it is essential that if you use client-side encryption, that you store your keys safely.

To enable client-side encryption, you have the following options:

- Use a customer master key (CMK) stored in AWS Key Management Service (AWS KMS). With this option, you use an AWS KMS CMK for client-side encryption when uploading or downloading data in Amazon S3. 
- Use a master key that you store within your application. With this option, you provide a client-side master key to the Amazon S3 encryption client. The client uses the master key only to encrypt the data encryption key that it generates randomly. 

[**Protecting data using client-side encryption**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html)


## Amazon S3 Service Integration
As organizations are collecting and analyzing increasing amounts of data, traditional on-premises solutions for data storage, data management, and analytics can no longer keep pace. Data siloes that aren’t built to work well together make it difficult to consolidate storage so that you can perform comprehensive and efficient analytics. This limits an organization’s agility, and ability to derive more insights and value from its data. It also limits the capability to adopt more sophisticated analytics tools and processes as its needs evolve.

Amazon S3 has a broad integration with a variety of services and use cases. In this section we use data lakes and high performance computing as two such examples.

### A data lake

A data lake is a centralized repository that allows you to migrate, store, and manage all structured and unstructured data at an unlimited scale. Once the data is centralized, you can extract value and gain insights from your data through analytics and machine learning.

A data lake makes the data and the analytics tools available to more of your users, across more lines of business enabling them to get the business insights they need, whenever they need them.

### Amazon S3 as a data lake      

The Amazon S3-based data lake solution uses Amazon S3 as its primary storage platform. Amazon S3 provides an optimal foundation for a data lake because of its virtually unlimited scalability. You can nondisruptively increase storage from gigabytes to petabytes of content.

Amazon S3 is designed for 99.999999999% (11 9s) of durability. It has scalable performance, ease-of-use features, native encryption, and access control capabilities. It also integrates with a broad portfolio of AWS and third party ISV data processing tools. 

Amazon Web Services (AWS) has developed a data lake architecture that allows you to build data lake solutions cost-effectively using Amazon Simple Storage Service and other services. 

#### Decoupling storage from compute
In traditional Hadoop and data warehouse solutions, storage and compute remain tightly coupled, making it difficult to optimize costs and data processing workflows. With Amazon S3, you can cost-effectively store all data types in their native formats. Then, you can launch as many or as few virtual servers as you need using Amazon Elastic Compute Cloud (EC2), and use AWS analytics tools to process your data. You can also optimize your EC2 instances to provide the right ratios of CPU, memory, and bandwidth for best performance. 

#### Centralized data architecture
Amazon S3 makes it easy to build a multi-tenant environment, where many users can bring their own data analytics tools to a common set of data. This improves both cost and data governance over that of traditional solutions, which require multiple copies of data to be distributed across multiple processing platforms.

#### Integration with clusterless and serverless AWS services
You can use Amazon S3 with Amazon Athena, Amazon Redshift Spectrum, Amazon Rekognition, and AWS Glue to query and process data. Amazon S3 also integrates with AWS Lambda serverless computing to run code without provisioning or managing servers. With all of these capabilities, you only pay for the actual amounts of data you process or for the compute time consumed. 

#### Standardized APIs
Amazon S3 REST APIs are easy to use, and supported by most major third-party independent software vendors (ISVs), including leading Apache Hadoop and analytics tool vendors. This allows customers to bring the tools they are comfortable and knowledgeable about to help them perform analytics on data in Amazon S3.

### Data cataloging

The earliest challenges that inhibited building a data lake were keeping track of all of the raw assets, as they were loaded into the data lake. Then, keeping track of all of the new data assets and versions created by data transformation, data processing, and analytics.

Thus, an essential component of an Amazon S3-based data lake is the data catalog. The data catalog provides a query-able interface of all assets stored in the data lake’s S3 buckets. The design of the data catalog is to provide a single source of truth about the contents of the data lake. 

![Data catalog](images/Fundamentals/data-cataloging.png)

You can create the comprehensive data catalog by using standard AWS services like AWS Lambda, Amazon DynamoDB, and Amazon Elasticsearch Service (Amazon ES). At a high level, you can use Lambda triggers to populate DynamoDB tables with object names and metadata. When those objects are put into Amazon S3 then Amazon ES is used to search for specific assets, related metadata, and data classifications.

### AWS Glue
AWS Glue is a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data. You can use AWS Glue to organize, cleanse, validate, and format data for storage in a data warehouse or data lake. The AWS Glue Data Catalog is an index to the location, schema, and runtime metrics of your data. In order to create your data warehouse or data lake, you must catalog this data.

### In-Place data querying

One of the most important capabilities of a data lake built into AWS is the ability to do in-place transformation and querying of data assets, without having to provision and manage clusters. This allows you to run sophisticated analytic queries directly on your data stored in Amazon S3. You don’t have to copy and load data into separate analytics platforms or data warehouses.

This makes the ability to analyze vast amounts of unstructured data accessible to any data lake user who can use SQL. In addition, it makes it more cost effective than the traditional method of performing an ETL process, creating a Hadoop cluster or data warehouse, loading the transformed data into these environments, and then running query jobs.

Amazon Athena and Amazon Redshift Spectrum provide the in-place querying capabilities of an Amazon S3 data lake. 

### Amazon Athena

Amazon Athena is an interactive query service that makes it easy for you to analyze data directly in Amazon S3, using standard SQL. You can get results in a matter of seconds. 

Athena is serverless, so there is no infrastructure to set up or manage. You only pay for the volume of data assets scanned during the queries you run.

You can use Athena to process unstructured, semi-structured, and structured data sets. It integrates with Amazon QuickSight for easy visualization. It can also be used with third-party reporting and business intelligence tools by connecting these tools to Athena with a JDBC driver.

### Amazon Redshift Spectrum

A second way to perform in-place querying of data assets in an Amazon S3-based data lake is to use Amazon Redshift Spectrum. Amazon Redshift is a large-scale, managed data warehouse service used with data assets in Amazon S3. However, data assets must be loaded into Amazon Redshift before queries run. 

Amazon Redshift Spectrum enables you to run Amazon Redshift SQL queries directly against data stored in an Amazon S3-based data lake.

Amazon Redshift Spectrum applies sophisticated query optimization, scaling processing across thousands of nodes so results are fast—even with large data sets and complex queries. You can directly query a wide variety of data assets stored in the data lake, including CSV, TSV, Parquet, Sequence, and RCFile.

Because Amazon Athena and Amazon Redshift share a common data catalog and data formats, you can use both Athena and Redshift Spectrum against the same data assets.

You would typically use Athena for ad hoc data discovery and SQL querying, and then use Redshift Spectrum for more complex queries and scenarios where a large number of data lake users want to run concurrent BI and reporting workloads.

### Amazon FSx for Lustre and Amazon S3 data lakes

Amazon FSx for Lustre, is a fully managed file system that is optimized for compute-intensive workloads, such as high performance computing, machine learning, and media data processing workflows.

With Amazon FSx for Lustre, you can launch and run a Lustre file system that can process massive data sets at up to hundreds of gigabytes per second of throughput, millions of IOPS, and sub-millisecond latencies.  Amazon FSx for Lustre file systems can link to Amazon S3 buckets, allowing you to access and process data concurrently from a high-performance file system.

![Amazon Fsx](images/Fundamentals/amazon-fsx.png)

Amazon FSx for Lustre can use Amazon S3 as a raw data repository as well as a repository for processed data. It makes it easy to process your cloud datasets in Amazon S3. 

When linked to an S3 bucket, FSx for Lustre transparently presents objects as files, allowing you to run your workload without managing data transfer from S3. As the contents of your S3 bucket change, FSx for Lustre automatically updates your file system with the latest data available to run your workload.
