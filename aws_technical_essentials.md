# AWS Technical Essentials

## What is AWS
- Cloud computing is the on-demand delivery of IT resources with primarily pay-as-you-go pricing.

## Cloud computing deployment models

Cloud computing provides developers and IT departments with the ability to focus on what matters most by avoiding work like procurement, maintenance, and capacity planning. As cloud computing has grown in popularity, several deployment strategies have emerged to help meet specific needs of different users. Each type of deployment method provides you with different levels of control, flexibility, and management. Understanding the differences between these deployment strategies can help you decide what set of services is right for your needs. 

### On-premises

Before the cloud, companies and organizations hosted and maintained hardware such as compute, storage, and networking equipment in their own data centers. They often allocated entire infrastructure departments to take care of their data centers, which resulted in costly operations that made some workloads and experimentation impossible. 

As internet use became more widespread, the demand for compute, storage, and networking equipment increased. For some companies and organizations, the cost of maintaining a large physical presence was unsustainable. To solve this problem, cloud computing emerged.

### Cloud

Cloud computing is the on-demand delivery of IT resources over the internet with primarily pay-as-you-go pricing. With cloud computing, companies do not have to manage and maintain their own hardware and data centers. Instead, companies like Amazon Web Services (AWS) own and maintain data centers and provide virtual data center technologies and services to companies and users over the internet.

### Hybrid

A third option is a hybrid deployment. This type of deployment is a way to connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud. The most common method of hybrid deployment between the cloud and existing on-premises infrastructure connects cloud resources to internal systems to extend and grow an organization's infrastructure into the cloud.

## Six advantages of cloud computing

- Pay as you go
    - The cloud computing model is based on paying only for the resources that you use. This is in contrast to on-premises models of investing in data centers and hardware that might not be fully used.

- Benefit from massive economies of scale
    - By using cloud computing, you can achieve a lower cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.

- Stop guessing capacity
    - Stop guessing on your infrastructure capacity needs. When you make a capacity decision before deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With cloud computing, these problems go away. You can access as much or as little capacity as you need, and scale up and down as required with only a few minutes notice.

- Increase speed and agility
    - IT resources are only a click away, which means that you reduce the time to make resources available to developers from weeks to minutes. This results in a dramatic increase in agility for the organization, because the cost and time it takes to experiment and develop is significantly lower.

- Realize cost savings
    - Companies can focus on projects that differentiate their business and remove the "undifferentiated heavy lifting", instead of maintaining data centers. With cloud computing, you can focus on your customers, rather than racking, stacking, and powering physical infrastructure.

- Go global in minutes
    - Applications can be deployed in multiple Regions around the world with a few clicks. This means that you can provide lower latency and a better experience for your customers at a minimal cost.

### Resources 

For more information, see the following resources:

- AWS website: [What Is Cloud Computing?](https://aws.amazon.com/what-is-cloud-computing/)
- AWS whitepaper: [Types of Cloud Computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/types-of-cloud-computing.html)
- AWS website: [Cloud Computing with AWS](https://aws.amazon.com/what-is-aws/)
- AWS whitepaper: [Overview of Amazon Web Services](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-overview/aws-overview.pdf)

## AWS Global Infrastructure
- Infrastructure, like data centers and networking connectivity, still exists as the foundation of every cloud application. In AWS, this physical infrastructure makes up the AWS Global Infrastructure, in the form of Regions and Availability Zones.

### Regions
- Regions are geographic locations worldwide where AWS hosts its data centers. AWS Regions are named after the location where they reside. For example, in the United States, the Region in Northern Virginia is called the Northern Virginia Region, and the Region in Oregon is called the Oregon Region. AWS has Regions in Asia Pacific, China, Europe, the Middle East, North America, and South America. And we continue to expand to meet our customers' needs.

Each AWS Region is associated with a geographical name and a Region code.

Here are examples of Region codes:

- **us-east-1** is the first Region created in the eastern US area. The geographical name for this Region is N. Virginia.
- **ap-northeast-1** is the first Region created in the northeast Asia Pacific area. The geographical name for this Region is Tokyo.

![AWS Region Codes](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/Tzl3mXlbnlvQJdVt_UB1vzpgv31Y9lgIX.jpg)

### Factors to consider Choosing the right AWS Region
- Latency
    - If your application is sensitive to latency (the delay between a request for data and the response), choose a Region that is close to your user base. This helps prevent long wait times for your customers. Synchronous applications such as gaming, telephony, WebSockets, and Internet of Things (IoT) are significantly affected by high latency. Asynchronous workloads, such as ecommerce applications, can also suffer from user connectivity delays.
- Pricing
    - Due to the local economy and the physical nature of operating data centers, prices vary from one Region to another. Internet connectivity, imported equipment costs, customs, real estate, and other factors impact a Region's pricing. Instead of charging a flat rate worldwide, AWS charges based on the financial factors specific to each Region.
- Service Availability
    - Some services might not be available in some Regions. The AWS documentation provides a table that shows the services available in each Region.
- Data Compliance
    - Enterprise companies often must comply with regulations that require customer data to be stored in a specific geographic territory. If applicable, choose a Region that meets your compliance requirements.

### Availability Zones

Inside every Region is a cluster of Availability Zones. An Availability Zone consists of one or more data centers with redundant power, networking, and connectivity. These data centers operate in discrete facilities in undisclosed locations. They are connected using redundant high-speed and low-latency links.

Availability Zones also have code names. Because they are located inside Regions, they can be addressed by appending a letter to the end of the Region code name. Here are examples of Availability Zone codes:

- **us-east-1a** is an Availability Zone in us-east-1 (N. Virginia Region).
- **sa-east-1b** is an Availability Zone in sa-east-1 (São Paulo Region).

Therefore, if you see that a resource exists in us-east-1c, you can infer that the resource is located in Availability Zone c of the us-east-1 Region.

### Edge locations

Edge locations are global locations where content is cached. For example, if your media content is in London and you want to share video files with your customers in Sydney, you could have the videos cached in an edge location closest to Sydney. This would make it possible for your customers to access the cached videos more quickly than accessing them from London. Currently, there are over 400+ edge locations globally.

Amazon CloudFront delivers your content through a worldwide network of edge locations. When a user requests content that is being served with CloudFront, the request is routed to the location that provides the lowest latency. So that content is delivered with the best possible performance. CloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content.

### Resources 

For more information, see the following resources:

- AWS website: [Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
AWS whitepaper: [AWS Global Infrastructure Documentation](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html)
- AWS website: [AWS Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- AWS reference guide: [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html)
- AWS website: [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
- AWS developer guide: [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

## Interacting with AWS

Every action that you make in AWS is an API call that is authenticated and authorized. In AWS, you can make API calls to services and resources through the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

### AWS Management Console

One way to manage cloud resources is through the web-based console, where you log in and choose the desired service. This can be the easiest way to create and manage resources when you first begin working with the cloud. The following is a screenshot that shows the landing page when you first log in to the console. 

![AWS Console](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/iKfcrjkTN_KM0b5m_kACdFvNejWudvMNP.jpg)

### AWS CLI

Consider the scenario where you run many servers on AWS for your application’s frontend. You want to run a report to collect data from all the servers. You need to do this programmatically every day because the server details might change. Instead of manually logging in to the console and then copying and pasting information, you can schedule an AWS CLI script with an API call to pull this data for you.

The AWS CLI is a unified tool that you can use to manage AWS services. You can download and configure one tool that you can use to control multiple AWS services from the command line, and automate them with scripts. The AWS CLI is open source, and installers are available for Windows, Linux, and macOS.

For example, you run the following API call against a service, using the AWS CLI:

```sh
aws s3api list-buckets
```

You will get a response similar to the following one, listing the buckets in your AWS accounts:

```json
{
    "Owner": {
        "DisplayName": "tech-essentials", 
        "ID": "d9881f40b83adh2896eb276f44ffch53677faec805422c83dfk60cc335a7da92"
    }, 
    "Buckets": [
        {
            "CreationDate": "2023-01-10T15:50:20.000Z", 
            "Name": "aws-tech-essentials"
        }, 
        {
            "CreationDate": "2023-01-10T16:04:15.000Z", 
            "Name": "aws-tech-essentials-employee-directory-app"
        } 
    ]
}
```

### AWS SDKs

API calls to AWS can also be performed by running code with programming languages. You can do this by using AWS SDKs. SDKs are open source and maintained by AWS for the most popular programming languages, such as C++, Go, Java, JavaScript, .NET, Node.js, PHP, Python, Ruby, Rust, and Swift.

Developers commonly use AWS SDKs to integrate their application source code with AWS services. For example, consider an application with a frontend that runs in Python. Every time the application receives a photo, it uploads the file to a storage service. This action can be achieved in the source code by using the AWS SDK for Python (Boto3). Here is an example of code that you can implement to work with AWS resources using the SDK for Python.

```python
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
```

#### Resources 

For more information, see the following resources:

- AWS getting started guide: [What Is the AWS Management Console?](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/)
- AWS website: [AWS Command Line Interface](https://aws.amazon.com/cli/)
- AWS website: [Tools to Build on AWS](https://aws.amazon.com/developer/tools/)

## Security and the AWS Shared Responsibility Model
- Security and compliance are a shared responsibility between AWS and you.

When you work with the AWS Cloud, managing security and compliance is a shared responsibility between AWS and you. To depict this shared responsibility, AWS created the shared responsibility model. The distinction of responsibility is commonly referred to as security of the cloud as compared to security in the cloud. 

![Shared Responsibility](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/rRoHGMS1atgXXnXn_VQj8P7tpf4Xy4mAS.png)

### AWS responsibility

AWS is responsible for **security of the cloud**. This means that AWS protects and secures the infrastructure that runs the services offered in the AWS Cloud. AWS is responsible for the following:

- Protecting and securing AWS Regions, Availability Zones, and data centers, down to the physical security of the buildings
- Managing the hardware, software, and networking components that run AWS services, such as the physical servers, host operating systems, virtualization layers, and AWS networking components

The level of responsibility that AWS has depends on the service.

### Customer responsibility

Customers are responsible for security in the cloud. When using any AWS service, the customer is responsible for properly configuring the service and their applications, in addition to ensuring that their data is secure.

The customers' level of responsibility depends on the AWS service. Some services require the customer to perform all the necessary security configuration and management tasks. Other more abstracted services require customers to only manage the data and control access to their resources. Using the two categories of AWS services, customers can determine their level of responsibility for each AWS service that they use.

Due to the varying levels of effort, customers must consider which AWS services they use and review the level of responsibility required to secure each service. They must also review how the AWS shared responsibility model aligns with the security standards in their IT environment in addition to any applicable laws and regulations.

A key concept is that customers maintain complete control of their data and are responsible for managing the security related to their content. For example, you are responsible for the following:

- Choosing a Region for AWS resources in accordance with data sovereignty regulations
- Implementing data-protection mechanisms, such as encryption and scheduled backups
- Using access control to limit who can access your data and AWS resources

#### Resources

For more information, see the following resource:

- AWS website: [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

## Protecting the AWS Root User
- When you first access AWS, you begin with a **single sign-in identity** known as the **root user**.

### AWS root user

When you first create an AWS account, you begin with a single sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the **AWS root user** and is accessed by signing in with the email address and password that were used to create the account. 

### AWS root user credentials

The AWS root user has two sets of credentials associated with it. One set of credentials is the email address and password that were used to create the account. This allows you to access the AWS Management Console. The second set of credentials is called access keys, which allow you to make programmatic requests from the AWS Command Line Interface (AWS CLI) or AWS API.

Access keys consist of two parts:

- **Access key ID**: for example, **A2lAl5EXAMPLE**
- **Secret access key**: for example, **wJalrFE/KbEKxE**

Similar to a user name and password combination, you need both the access key ID and secret access key to authenticate your requests through the AWS CLI or AWS API. Access keys should be managed with the same security as an email address and password.

> Delete your access keys to stay safe!

> If you don't have an access key for your AWS account root user, don't create one unless you absolutely need to. If you have an access key for your AWS account root user and want to delete the key, follow these steps:

    1. In the AWS Management Console, navigate to your username in the upper right section of the navigation bar. From the dropdown menu, go to the **My Security Credentials** page, and sign in with the root user’s email address and password.
    2. Open the **Access keys** section.
    3. Under **Actions**, choose **Delete**.
    4. Choose **Yes**.

### AWS root user best practices

The root user has complete access to all AWS services and resources in your account, including your billing and personal information. Therefore, you should securely lock away the credentials associated with the root user and not use the root user for everyday tasks. Visit the links at the end of this lesson to learn more about when to use the AWS root user.

To ensure the safety of the root user, follow these best practices:
- Choose a strong password for the root user.
- Enable multi-factor authentication (MFA) for the root user.
- Never share your root user password or access keys with anyone.
- Disable or delete the access keys associated with the root user.
- Create an Identity and Access Management (IAM) user for administrative tasks or everyday tasks.

![Root User protection](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/gRYm5CSkPkIqEr9B_YD5J2pBrmA9lGqT-.png)

### Multi-factor authentication

When you create an AWS account and first log in to the account, you use single-factor authentication. Single-factor authentication is the simplest and most common form of authentication. It only requires one authentication method. In this case, you use a user name and password to authenticate as the AWS root user. Other forms of single-factor authentication include a security pin or a security token.

However, sometimes a user’s password is easy to guess. For example, your coworker Bob’s password, IloveCats222, might be easy for someone who knows Bob personally to guess, because it’s a combination of information that is easy to remember and includes certain facts about Bob (Bob loves cats, and his birthday is February 22). If a bad actor guessed or cracked Bob’s password through social engineering, bots, or scripts, Bob might lose control of his account. Unfortunately, this is a common scenario that users of any website often face. This is why using multi-factor authentication (MFA) is important in preventing unwanted account access.

![MFA](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/DVzNXQ-mMCu1I-q7_ae3D9Goxf5poTU_J.png)

MFA requires two or more authentication methods to verify an identity. 

With a combination of this information, systems can provide a layered approach to account access. So even if the first method of authentication, like Bob’s password, is cracked by a malicious actor, the second method of authentication, such as a fingerprint, provides another level of security. This extra layer of security can help protect your most important accounts, which is why you should activate MFA on your AWS root user.

### MFA on AWS

If you activate MFA on your root user, you must present a piece of identifying information from both the something you know category and the something you have category. The first piece of identifying information the user enters is an email and password combination. The second piece of information is a temporary numeric code provided by an MFA device.

Using MFA adds an additional layer of security because it requires users to use a supported MFA mechanism in addition to their regular sign-in credentials. Activating MFA on the AWS root user account is an AWS best practice.

### Supported MFA devices

AWS supports a variety of MFA mechanisms, such as virtual MFA devices, hardware time-based one-time password (TOTP) tokens, and FIDO security keys.

|Device	|Description	|Supported Devices|
|:-----:|:-------------:|:---------------:|
|Virtual MFA	|A software app that runs on a phone or other device that provides a one-time passcode. These applications can run on unsecured mobile devices, and because of that, they might not provide the same level of security as hardware or FIDO security keys.	|Twilio Authy Authenticator, Duo Mobile, LastPass Authenticator, Microsoft Authenticator, Google Authenticator, Symantec VIP|
|Hardware TOTP token	|A hardware device, generally a key fob or display card device, that generates a one-time, six-digit numeric code based on the time-based one-time password (TOTP) algorithm.	|Key fob, display card|
|FIDO security keys|FIDO-certified hardware security keys are provided by third-party providers such as Yubico. You can plug your FIDO security key into a USB port on your computer and enable it using the instructions that follow.|[FIDO Certified products](https://fidoalliance.org/certification/fido-certified-products)|

#### Resources 

For more information, see the following resources:

- AWS user guide: [Enabling a Hardware TOTP token (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html)
- AWS user guide: [Enabling a FIDO Security Key (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_fido.html)
- AWS user guide: [Enabling a Virtual Multi-Factor Authentication (MFA) Device (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)
- AWS website: [Multi-Factor Authentication for IAM](https://aws.amazon.com/iam/features/mfa/)
- AWS reference guide: [Tasks That Require Root User Credentials](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html)

## AWS Identity and Access Management(AWS IAM)

- Authentication answers the question, "Are you who you say you are?" Authorization answers the question, "What actions can you perform?"

### Authentication and authorization

When you configure access to any account, two terms come up frequently: **authentication** and **authorization**. Although these terms might seem basic, you must fully understand them to properly configure access management on AWS.

### Authentication

When you create your AWS account, you use the combination of an email address and a password to verify your identity. If a user types in the correct email address and password, the system assumes the user is allowed to enter and grants them access. This is the process of authentication.

Authentication ensures that the user is who they say they are. User names and passwords are the most common types of authentication. But you might also work with other forms, such as token-based authentication or biometric data, like a fingerprint. Authentication simply answers the question, “Are you who you say you are?”

### Authorization

After you’re authenticated and in your AWS account, you might be curious about what actions you can take. This is where authorization comes in. Authorization is the process of giving users permission to access AWS resources and services. Authorization determines whether a user can perform certain actions, such as read, edit, delete, or create resources. Authorization answers the question, “What actions can you perform?” 

### What is IAM?

AWS Identity and Access Management (IAM) is an AWS service that helps you manage access to your AWS account and resources. It also provides a centralized view of who and what are allowed inside your AWS account (authentication), and who and what have permissions to use and work with your AWS resources (authorization).

With IAM, you can share access to an AWS account and resources without sharing your set of access keys or password. You can also provide granular access to those working in your account, so people and services only have permissions to the resources that they need. For example, to provide a user of your AWS account with read-only access to a particular AWS service, you can granularly select which actions and which resources in that service that they can access.

### IAM features

To help control access and manage identities in your AWS account, IAM offers many features to ensure security.

- Global
    - IAM is global and not specific to any one Region. You can see and use your IAM configurations from any Region in the AWS Management Console.
- Integrated with AWS services
    - IAM is integrated with many AWS services by default.
- Shared access
    - You can grant other identities permission to administer and use resources in your AWS account without having to share your password and key.
- Multi-factor authentication
    - IAM supports MFA. You can add MFA to your account and to individual users for extra security.
- Identity federation
    - IAM supports identity federation, which allows users with passwords elsewhere—like your corporate network or internet identity provider—to get temporary access to your AWS account. 
- Free to use
    - Any AWS customer can use IAM; the service is offered at no additional charge.

### IAM user

An IAM user represents a person or service that interacts with AWS. You define the user in your AWS account. Any activity done by that user is billed to your account. When you create a user, that user can sign in to gain access to the AWS resources inside your account.

### IAM user credentials

An IAM user consists of a name and a set of credentials. When you create a user, you can provide them with the following types of access:

- Access to the AWS Management Console
- Programmatic access to the AWS CLI and AWS API

To access the console, provide the user with a user name and password. For programmatic access, AWS generates a set of access keys that can be used with the AWS CLI and AWS API. IAM user credentials are considered permanent, which means that they stay with the user until there’s a forced rotation by admins.

When you create an IAM user, you can grant permissions directly at the user level. This can seem like a good idea if you have only one or a few users. However, as the number of users increases, keeping up with permissions can become more complicated. For example, if you have 3,000 users in your AWS account, administering access and getting a top-level view of who can perform what actions on which resources can be challenging.

Fortunately, you can group IAM users and attach permissions at the group level.

### IAM groups

An IAM group is a collection of users. All users in the group inherit the permissions assigned to the group. This makes it possible to give permissions to multiple users at once. It’s a more convenient and scalable way of managing permissions for users in your AWS account. This is why using IAM groups is a best practice.

If you have an application that you’re trying to build and you have multiple users in one account working on the application, you might organize the users by job function. For example, you might organize your IAM groups by developers, security, and admins. You could then place all your IAM users into their respective groups.

This provides a way to see who has what permissions in your organization. It also helps you scale when new people join, leave, and change roles in your organization.

![IAM groups](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/4LldeceBXuorYhtB_WXZ1hMonELN5HDwI.png)

Consider the following examples:

- A new developer joins your AWS account to help with your application. You create a new user and add them to the developer group, without thinking about which permissions they need.
- A developer changes jobs and becomes a security engineer. Instead of editing the user’s permissions directly, you remove them from the old group and add them to the new group that already has the correct level of access.

Keep in mind the following features of groups:

- Groups can have many users.
- Users can belong to many groups.
- Groups cannot belong to groups.

The root user can perform all actions on all resources inside an AWS account by default. This is in contrast to creating new IAM users, new groups, or new roles. To allow an IAM identity to perform specific actions in AWS, such as implement resources, you must grant the IAM user the necessary permissions.

The way you grant permissions in IAM is by using IAM policies.

### IAM policies

To manage access and provide permissions to AWS services and resources, you create IAM policies and attach them to an IAM identity. Whenever an IAM identity makes a request, AWS evaluates the policies associated with them. For example, if you have a developer inside the developers group who makes a request to an AWS service, AWS evaluates any policies attached to the developers group and any policies attached to the developer user to determine if the request should be allowed or denied.

### IAM policy examples

Most policies are stored in AWS as JSON documents with several policy elements. The following example provides admin access through an IAM identity-based policy.

```json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": "*",
        "Resource": "*"
    }]
}
```

This policy has four major JSON elements: **Version**, **Effect**, **Action**, and **Resource**.

- The **Version** element defines the version of the policy language. It specifies the language syntax rules that are needed by AWS to process a policy. To use all the available policy features, include **"Version": "2012-10-17"** before the **"Statement"** element in your policies.
- The **Effect** element specifies whether the policy will allow or deny access. In this policy, the Effect is **"Allow"**, which means you’re providing access to a particular resource.
- The **Action** element describes the type of action that should be allowed or denied. In the example policy, the action is "*". This is called a wildcard, and it is used to symbolize every action inside your AWS account.
- The **Resource** element specifies the object or objects that the policy statement covers. In the policy example, the resource is the wildcard "*". This represents all resources inside your AWS console.

Putting this information together, you have a policy that allows you to perform all actions on all resources in your AWS account. This is what we refer to as **an administrator policy**.

The next example shows a more granular IAM policy.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyS3AccessOutsideMyBoundary",
      "Effect": "Deny",
      "Action": [
        "s3:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceAccount": [
            "222222222222"
          ]
        }
      }
    }
  ]
}
```

This policy uses a Deny effect to block access to Amazon S3 actions, unless the Amazon S3 resource that's being accessed is in account 222222222222. This ensures that any Amazon S3 principals are accessing only the resources that are inside of a trusted AWS account.

### IAM roles



### AM best practices

This section summarizes some of the most important IAM best practices that you must be familiar with before building solutions in AWS.

- Lock down the AWS root user

    - The root user is an all-powerful and all-knowing identity in your AWS account. If a malicious user were to gain control of root-user credentials, they would be able to access every resource in your account, including personal and billing information. To lock down the root user, you can do the following:

        - Don’t share the credentials associated with the root user.
        - Consider deleting the root user access keys.
        - Activate MFA on the root account.

- Follow the principle of least privilege

    - Least privilege is a standard security principle that advises you to grant only the necessary permissions to do a particular job and nothing more. To implement least privilege for access control, start with the minimum set of permissions in an IAM policy and then grant additional permissions as necessary for a user, group, or role.

- Use IAM appropriately

    - IAM is used to secure access to your AWS account and resources. It provides a way to create and manage users, groups, and roles to access resources in a single AWS account. IAM is not used for website authentication and authorization, such as providing users of a website with sign-in and sign-up functionality. IAM also does not support security controls for protecting operating systems and networks.

- Use IAM roles when possible
    - Maintaining roles is more efficient than maintaining users. When you assume a role, IAM dynamically provides temporary credentials that expire after a defined period of time, between 15 minutes and 36 hours. Users, on the other hand, have long-term credentials in the form of user name and password combinations or a set of access keys.
    - User access keys only expire when you or the account admin rotates the keys. User login credentials expire if you applied a password policy to your account that forces users to rotate their passwords.

- Consider using an identity provider
    - If you decide to make your cat photo application into a business and begin to have more than a handful of people working on it, consider managing employee identity information through an identity provider (IdP). Using an IdP, whether it's with an AWS service such as AWS IAM Identity Center (successor to AWS Single Sign-On) or a third-party identity provider, provides a single source of truth for all identities in your organization.

    - You no longer have to create separate IAM users in AWS. You can instead use IAM roles to provide permissions to identities that are federated from your IdP. Being federated is a process that allows for the transfer of identity and authentication information across a set of networked systems. 

    - For example, your employee Martha has access to multiple AWS accounts. Instead of creating and managing multiple IAM users named Martha in each of those AWS accounts, you could manage Martha in your company’s IdP. If Martha moves in the company or leaves the company, Martha can be updated in the IdP rather than in every AWS account in the company.

- Regularly review and remove unused users, roles, and other credentials
    - You might have IAM users, roles, permissions, policies, or credentials that you are no longer using in your account. IAM provides last accessed information to help you identify irrelevant credentials that you no longer need so that you can remove them. This helps you reduce the number of users, roles, permissions, policies, and credentials that you have to monitor.

#### Resources 

For more information, see the following resources:
- AWS user guide: [What Is IAM?](https://docs.aws.amazon.com/en_us/IAM/latest/UserGuide/introduction.html)
- AWS user guide: [IAM Identities (User, User Groups, and Roles)](https://docs.aws.amazon.com/en_us/IAM/latest/UserGuide/id.html)
- AWS user guide: [Access Management for AWS Resources](https://docs.aws.amazon.com/en_us/IAM/latest/UserGuide/access.html)
- AWS user guide: [Security Best Practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- AWS blog: [How to Create and Manage Users within AWS IAM Identity Center](https://aws.amazon.com/blogs/security/how-to-create-and-manage-users-within-aws-sso/)