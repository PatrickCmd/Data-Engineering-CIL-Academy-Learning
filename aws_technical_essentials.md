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


## Compute as a Service
- At a fundamental level, three types of compute options are available: virtual machines (VMs), container services, and serverless.

### Servers

The first building block that you need to host an application is a server. Servers can usually handle HTTP requests and send responses to clients following the client-server model. Although any API-based communication also falls under this model. 

![client-server](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/0Z2Ge4DWal9Lg4oC_pTtbd7zybSuD-m3K.png)

- A client is a person or computer that sends a request. 
- A server handling the requests is a computer, or collection of computers, connected to the internet serving websites to internet users. Servers power your application by providing CPU, memory, and networking capacity to process users’ requests and transform them into responses. For context, common HTTP servers include the following:

    - Windows options, such as Internet Information Services (IIS)
    - Linux options, such as Apache HTTP Server, Nginx, and Apache Tomcat

### Choosing the right compute option

If you’re responsible for setting up servers on AWS to run your infrastructure, you have many compute options. First, you need to know which compute service to use for each use case. At a fundamental level, three types of compute options are available: virtual machines (VMs), container services, and serverless.

![compute options](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/9bC0T62_VgZWJ5Hv_RnozzfcimAtzGYe6.png)

If you have prior infrastructure knowledge, a virtual machine will often be the easiest compute option to understand. This is because a virtual machine emulates a physical server and allows you to install an HTTP server to run your applications, for example. To run virtual machines, you install a hypervisor on a host machine. In its simplest form, a hypervisor is software or firmware that makes it possible to share physical hardware resources across one or more virtual machines. The hypervisor provisions the resources to create and run your VMs.

In AWS, Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure and resizable compute capacity in the cloud. You can provision virtual servers called EC2 instances. Behind the scenes, AWS operates and manages the host machines and the hypervisor layer. AWS also installs the virtual machine operating system, called the guest operating system.

Beneath the surface, some AWS compute services use Amazon EC2 or use virtualization concepts. You should understand this service before advancing to container services and serverless compute.

#### Resources

For more information, see the following resources:

- AWS whitepaper: Compute Services(https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)
- AWS website: Compute for Any Workload(https://aws.amazon.com/products/compute/)

### Amazon EC2

Amazon EC2 is a web service that provides secure, resizable compute capacity in the cloud. With this service, you can provision virtual servers called EC2 instances. 

![Amazon EC2](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/chYg2z1i3WOig7a7_r79kCL5ArAFFb0im.jpg)

With Amazon EC2, you can do the following:
- Provision and launch one or more EC2 instances in minutes.
- Stop or shut down EC2 instances when you finish running a workload.
- Pay by the hour or second for each instance type (minimum of 60 seconds).

You can create and manage EC2 instances through the AWS Management Console, AWS CLI, AWS SDKs, automation tools, and infrastructure orchestration services.

To create an EC2 instance, you must define the following:
- Hardware specifications: CPU, memory, network, and storage
- Logical configurations: Networking location, firewall rules, authentication, and the operating system of your choice

### Amazon Machine Image

When launching an EC2 instance, the first setting you configure is which operating system you want by selecting an Amazon Machine Image (AMI).

In the traditional infrastructure world, spinning up a server consists of installing an operating system from installation disks, drives, or wizards over the network. In the AWS Cloud, the operating system installation is not your responsibility. Instead, it's built into the AMI that you choose.

An AMI includes the operating system, storage mapping, architecture type, launch permissions, and any additional preinstalled software applications.

### Relationship between AMIs and EC2 instances

EC2 instances are live instantiations (or versions) of what is defined in an AMI, as a cake is a live instantiation of a cake recipe. If you are familiar with software development, you can also see this kind of relationship between a class and an object. In this case, the AMI is how you model and define your instance. The EC2 instance is the entity you interact with, where you can install your web server and serve your content to users.

When you launch a new instance, AWS allocates a virtual machine that runs on a hypervisor. Then the AMI that you selected is copied to the root device volume, which contains the image that is used to boot the volume. In the end, you get a server that you can connect to and install packages and additional software on. In the example, you install a web server along with the properly configured source code of your employee directory application.

![AMI](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/H6rwy-73WJHIzF8T_b1oUsgei4V-I5ioF.png)

One advantage of using AMIs is that they are reusable. You might choose a Linux-based AMI and configure the HTTP server, application packages, and additional software that you need to run your application. If you want to create another EC2 instance with the same configurations, you could create and configure a new EC2 instance to match the first instance. Or you could create an AMI from your running instance and use the AMI to start a new instance. That way, your new instance would have the same configurations as your current instance because the configurations set in the AMIs are the same.


![AMI](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/XQZZ5lTxRTtBYTB0_jKOXSf3jjyOMxyyo.png)

### Finding AMIs

There are multiple ways to select an AMI. To learn more, expand each of the following five categories.

- Quick Start AMIs
    - Quick Start AMIs are commonly used AMIs created by AWS that you can select to get started quickly. 

- AWS Marketplace AMIs
    - AWS Marketplace AMIs provide popular open-source and commercial software from third-party vendors.

- My AMIs
    - My AMIs are created from your EC2 instances.

- Community AMIs
    - Community AMIs are provided by the AWS user community.

- Custom image
    - Build your own custom image with EC2 Image Builder.

Each AMI in the AWS Management Console has an AMI ID, which is prefixed by ami-, followed by a random hash of numbers and letters. The IDs are unique to each AWS Region.

![AMIs](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/OHe7BHzYomOG7z49_wStnc1Mz27U8c_r2.png)

An AMI includes the operating system, storage mapping, architecture type, launch permissions, and any additional preinstalled software applications.

### Amazon EC2 instance types

EC2 instances are a combination of virtual processors (vCPUs), memory, network, and, in some cases, instance storage and graphics processing units (GPUs). When you create an EC2 instance, you need to choose how much you need of each of these components.

![EC2 instance types](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/KLtuC4QMp7CGJvX6_z8A9aBSkVQf0MwmJ.png)

AWS offers a variety of instances that differ based on performance. Some instances provide more capacity than others. To get an overview of the capacity details for a particular instance, you should look at the instance type. Instance types consist of a prefix identifying the type of workloads they’re optimized for, followed by a size. For example, the instance type c5n.xlarge can be broken down as follows:

- **First position** – The first position, **c**, indicates the instance family. This indicates that this instance belongs to the compute optimized family.
- **Second position** – The second position, **5**, indicates the generation of the instance. This instance belongs to the fifth generation of instances.
- **Remaining letters before the period** – In this case, **n** indicates additional attributes, such as local NVMe storage.
- **After the period** – After the period, **xlarge** indicates the instance size. In this example, it's xlarge.

![c5n.xlarge](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/Gs9fkNp49iZLvDvJ_TOY_r5g2WQYpD6O5.jpg)

### Instance families

Each instance family is optimized to fit different use cases. The following table describes instance families and some typical workloads.

|Instance |family Description |Use Cases|
|:-------:|:------------------|:--------|
|General purpose|General purpose instances provide a balance of compute, memory, and networking resources, and can be used for a variety of workloads.|Ideal for applications that use these resources in equal proportions, such as web servers and code repositories|
|Compute optimized|Compute optimized instances are ideal for compute-bound applications that benefit from high-performance processors.|Well-suited for batch processing workloads, media transcoding, high performance web servers, high performance computing (HPC), scientific modeling, dedicated gaming servers and ad server engines, machine learning inference, and other compute intensive applications|
|Memory optimized|Memory optimized instances are designed to deliver fast performance for workloads that process large datasets in memory.|Memory-intensive applications, such as high-performance databases, distributed web-scale in-memory caches, mid-size in-memory databases, real-time big-data analytics, and other enterprise applications|
|Accelerated computing|Accelerated computing instances use hardware accelerators or co-processors to perform functions such as floating-point number calculations, graphics processing, or data pattern matching more efficiently than is possible in software running on CPUs|Machine learning, HPC, computational fluid dynamics, computational finance, seismic analysis, speech recognition, autonomous vehicles, and drug discovery|
|Storage optimized|Storage optimized instances are designed for workloads that require high sequential read and write access to large datasets on local storage. They are optimized to deliver tens of thousands of low-latency random I/O operations per second (IOPS) to applications that replicate their data across different instances.|NoSQL databases (Cassandra, MongoDB and Redis), in-memory databases, scale-out transactional databases, data warehousing, Elasticsearch, and analytics|
|HPC optimized|High performance computing (HPC) instances are purpose built to offer the best price performance for running HPC workloads at scale on AWS.|Ideal for applications that benefit from high-performance processors, such as large, complex simulations and deep learning workloads|

### EC2 instance locations

Unless otherwise specified, when you launch EC2 instances, they are placed in a default virtual private cloud (VPC). The default VPC is suitable for getting started quickly and launching public EC2 instances without having to create and configure your own VPC.

Any resource that you put inside the default VPC will be public and accessible by the internet, so you shouldn’t place any customer data or private information in it.

When you get more comfortable with networking on AWS, you should change this default setting to choose your own custom VPCs and restrict access with additional routing and connectivity mechanisms.

### Architecting for high availability

In the network, your instance resides in an Availability Zone of your choice. As you learned previously, AWS services that are scoped at the Availability Zone level must be architected with high availability in mind.

Although EC2 instances are typically reliable, two are better than one, and three are better than two. Specifying the instance size gives you an advantage when designing your architecture because you can use more smaller instances rather than a few larger ones.

If your frontend only has a single instance and the instance fails, your application goes down. Alternatively, if your workload is distributed across 10 instances and one fails, you lose only 10 percent of your fleet, and your application availability is hardly affected.

When architecting any application for high availability, consider using at least two EC2 instances in two separate Availability Zones. ­­

![AWS Cloud](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/reOZnQD2aJ-1wN1J_bwzBuePADmVCRRJI.png)


#### Resources

For more information, see the following resources:

- AWS website: [Amazon EC2](https://aws.amazon.com/ec2/)
- AWS user guide: [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- AWS user guide: [Creatie an Amazon EBS-Backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html)
- AWS user guide: [What Is EC2 Image Builder?](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html)
- AWS user guide: [Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html)
- AWS whitepaper: [Reliability Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html?ref=wellarchitected-wp)

### Amazon EC2 Instance Lifecycle

An EC2 instance transitions between different states from the moment you create it until its termination.

![Instance Lifecycle](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/RzRBaSlJf6NvgSPx_W-vfLyAzzrKyOEwn.png)

1. When you launch an instance, it enters the pending state. When an instance is pending, billing has not started. At this stage, the instance is preparing to enter the running state. Pending is where AWS performs all actions needed to set up an instance, such as copying the AMI content to the root device and allocating the necessary networking components.

2. When your instance is running, it's ready to use. This is also the stage where billing begins. As soon as an instance is running, you can take other actions on the instance, such as reboot, terminate, stop, and stop-hibernate.

3. When you reboot an instance, it’s different than performing a stop action and then a start action. Rebooting an instance is equivalent to rebooting an operating system. The instance keeps its public DNS name (IPv4) and private and public IPv4 addresses. An IPv6 address (if applicable) remains on the same host computer and maintains its public and private IP address, in addition to any data on its instance store volumes.

4. When you stop your instance, it enters the stopping and then stopped state. This is similar to when you shut down your laptop. You can stop and start an instance if it has an Amazon Elastic Block Store (Amazon EBS) volume as its root device. When you stop and start an instance, your instance can be placed on a new underlying physical server. Your instance retains its private IPv4 addresses and if your instance has an IPv6 address, it retains its IPv6 address. When you put the instance into stop-hibernate, the instance enters the stopped state, but saves the last information or content into memory, so that the start process is faster.

5. When you terminate an instance, the instance stores are erased, and you lose both the public IP address and private IP address of the machine. Termination of an instance means that you can no longer access the machine. As soon as the status of an instance changes to shutting down or terminated, you stop incurring charges for that instance.

### Difference between stop and stop-hibernate

When you stop an instance, it enters the stopping state until it reaches the stopped state. AWS does not charge usage or data transfer fees for your instance after you stop it. But storage for any Amazon EBS volumes is still charged. While your instance is in the stopped state, you can modify some attributes, like the instance type. When you stop your instance, the data from the instance memory (RAM) is lost.

When you stop-hibernate an instance, Amazon EC2 signals the operating system to perform hibernation (suspend-to-disk), which saves the contents from the instance memory (RAM) to the EBS root volume. You can hibernate an instance only if hibernation is turned on and the instance meets the hibernation prerequisites.

### Pricing

One of the ways to reduce costs with Amazon EC2 is to choose the right pricing option for the way that your applications run. AWS offers a variety of pricing options to address different workload scenarios. 

#### On-Demand Instances

With On-Demand Instances, you pay for compute capacity per hour or per second, depending on which instances that you run. There are no long-term commitments or upfront payments required. Billing begins whenever the instance is running, and billing stops when the instance is in a stopped or terminated state. You can increase or decrease your compute capacity to meet the demands of your application and only pay the specified hourly rates for the instance that you use.

On-Demand Instances are recommended for the following use cases:
- Users who prefer the low cost and flexibility of Amazon EC2 without upfront payment or long-term commitments            
- Applications with short-term, spiky, or unpredictable workloads that cannot be interrupted
- Applications being developed or tested on Amazon EC2 for the first time

### Spot Instances

For applications that have flexible start and end times, Amazon EC2 offers the Spot Instances option. With Amazon EC2 Spot Instances, you can request spare Amazon EC2 computing capacity for up to 90 percent off the On-Demand price. Spot Instances are recommended for the following use cases:

- Applications that have flexible start and end times            
- Applications that are only feasible at very low compute prices            
- Users with fault-tolerant or stateless workloads 

With Spot Instances, you set a limit on how much you want to pay for the instance hour. This is compared against the current Spot price that AWS determines. Spot Instance prices adjust gradually based on long-term trends in supply and demand for Spot Instance capacity. If the amount that you pay is more than the current Spot price and there is capacity, you will receive an instance.   

#### Savings Plans

Savings Plans are a flexible pricing model that offers low usage prices for a 1-year or 3-year term commitment to a consistent amount of usage. Savings Plans apply to Amazon EC2, AWS Lambda, and AWS Fargate usage and provide up to 72 percent savings on AWS compute usage.

For workloads that have predictable and consistent usage, Savings Plans can provide significant savings compared to On-Demand Instances. Savings Plans are recommended for the following use cases:

- Workloads with a consistent and steady-state usage 
- Customers who want to use different instance types and compute solutions across different locations
- Customers who can make monetary commitment to use Amazon EC2 over a 1-year or 3-year term

#### Reserved Instances

For applications with steady state usage that might require reserved capacity, Amazon EC2 offers the Reserved Instances option. With this option, you save up to 75 percent compared to On-Demand Instance pricing. You can choose between three payment options: All Upfront, Partial Upfront, or No Upfront. You can select either a 1-year or 3-year term for each of these options.

With Reserved Instances, you can choose the type that best fits your applications needs.  
- Standard Reserved Instances: These provide the most significant discount (up to 72 percent off On-Demand pricing) and are best suited for steady-state usage. 
- Convertible Reserved Instances: These provide a discount (up to 54 percent off On-Demand pricing) and the capability to change the attributes of the Reserved Instance if the exchange results in the creation of Reserved Instances of equal or greater value. Like Standard Reserved Instances, Convertible Reserved Instances are best suited for steady-state usage.    
- Scheduled Reserved Instances: These are available to launch within the time windows that you reserve. With this option, you can match your capacity reservation to a predictable recurring schedule that only requires a fraction of a day, a week, or a month.

#### Dedicated Hosts

A Dedicated Host is a physical Amazon EC2 server that is dedicated for your use. Dedicated Hosts can help you reduce costs because you can use your existing server-bound software licenses, such as Windows Server, SQL Server, and Oracle licenses. And they can also help you meet compliance requirements. Amazon EC2 Dedicated Host is also integrated with AWS License Manager, a service that helps you manage your software licenses, including Microsoft Windows Server and Microsoft SQL Server licenses.

- Dedicated Hosts can be purchased on demand (hourly).
- Dedicated Hosts can be purchased as a Reservation for up to 70 percent off the On-Demand price.

#### Resources

For more information, see the following resources:

- AWS user guide: [Amazon EC2: Instance Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)
- AWS user guide: [Hibernation Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html)
- AWS website: [Amazon EC2 Pricing]https://aws.amazon.com/ec2/pricing/)
- AWS website: [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
- AWS website: [Amazon EC2 Spot Instances Pricing](https://aws.amazon.com/ec2/spot/pricing/)
- AWS website: [Amazon EC2 Reserved Instances Pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/)

## Container Services

Although containers are often referred to as a new technology, the idea started in the 1970s with certain UNIX kernels (the central core of the operating system) having the ability to separate their processes through isolation. At the time, this was configured manually, making operations complex.

With the evolution of the open-source software community, containers evolved. Today, containers are used as a solution to problems of traditional compute, including the issue of getting software to run reliably when it moves from one compute environment to another.

- A container is a standardized unit that packages your code and its dependencies. This package is designed to run reliably on any platform, because the container creates its own independent environment. With containers, workloads can be carried from one place to another, such as from development to production or from on-premises environments to the cloud.

- An example of a containerization platform is Docker. Docker is a popular container runtime that simplifies the management of the entire operating system stack required for container isolation, including networking and storage. Docker helps customers create, package, deploy, and run containers.

### Difference between VMs and containers

![VMs and Containers](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/WGQMKCw2hQe2Rr1v_aLZuLt2uEP1sRZeR.png)

Containers share the same operating system and kernel as the host that they exist on. But virtual machines contain their own operating system. Each virtual machine must maintain a copy of an operating system, which results in a degree of wasted resources.

A container is more lightweight. Containers spin up quicker, almost instantly. This difference in startup time becomes instrumental when designing applications that must scale quickly during I/O bursts.

Containers can provide speed, but virtual machines offer the full strength of an operating system and more resources, like package installation, dedicated kernel, and more.

### Orchestrating containers

In AWS, containers can run on EC2 instances. For example, you might have a large instance and run a few containers on that instance. Although running one instance is uncomplicated to manage, it lacks high availability and scalability. Most companies and organizations run many containers on many EC2 instances across several Availability Zones.

If you’re trying to manage your compute at a large scale, you should consider the following:

- How to place your containers on your instances
- What happens if your container fails
- What happens if your instance fails
- How to monitor deployments of your containers

This coordination is handled by a container orchestration service. AWS offers two container orchestration services: Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).

### Managing containers with Amazon ECS

![AMazon ECS](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/MzO5qIuSFHGROPvr_wwBHSRxv2tRUlN9K.jpg)

Amazon ECS is an end-to-end container orchestration service that helps you spin up new containers. With Amazon ECS, your containers are defined in a task definition that you use to run an individual task or a task within a service. You have the option to run your tasks and services on a serverless infrastructure that's managed by another AWS service called AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of EC2 instances that you manage.

![Amazon ECS](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/Gxcc_QBrhHWZB9lz_fBTShP26hpLTwZKE.png)

If you choose to have more control by running and managing your containers on a cluster of Amazon EC2 instances, you will also need to install the Amazon ECS container agent on your EC2 instances. Note that an EC2 instance with the container agent installed is often called a container instance. This container agent is open source and responsible for communicating to the Amazon ECS service about cluster management details. You can run the agent on both Linux and Windows AMIs. 

![EC2 Container instance](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/ySRLtnrIYPZIu3eZ_YiX8p1udFI_1rzlu.jpg)

When the Amazon ECS container instances are up and running, you can perform actions that include, but are not limited to, the following:

- Launching and stopping containers
- Getting cluster state
- Scaling in and out
- Scheduling the placement of containers across your cluster
- Assigning permissions
- Meeting availability requirements

To prepare your application to run on Amazon ECS, you create a task definition. The task definition is a text file, in JSON format, that describes one or more containers. A task definition is similar to a blueprint that describes the resources that you need to run a container, such as CPU, memory, ports, images, storage, and networking information.

Here is a simple task definition that you can use for your corporate directory application. In this example, this runs on the Nginx web server.

```json
{
  "family": "webserver",
  "containerDefinitions": [
    {
      "name": "web",
      "image": "nginx",
      "memory": "100",
      "cpu": "99"
    }
  ],
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "networkMode": "awsvpc",
  "memory": "512",
  "cpu": "256"
}
```

### Using Kubernetes with Amazon EKS

![Amazon EKS](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/Tha86Y0rmyO6Etwh_VA27xMpMCpEGYGSs.jpg)

Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services. By bringing software development and operations together by design, Kubernetes created a rapidly growing ecosystem that is very popular and well established in the market.

If you already use Kubernetes, you can use Amazon EKS to orchestrate the workloads in the AWS Cloud. Amazon EKS is a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. Amazon EKS is conceptually similar to Amazon ECS, but with the following differences:

- In Amazon ECS, the machine that runs the containers is an EC2 instance that has an ECS agent installed and configured to run and manage your containers. This instance is called a container instance. In Amazon EKS, the machine that runs the containers is called a worker node or Kubernetes node. 
- An ECS container is called a task. An EKS container is called a pod.
- Amazon ECS runs on AWS native technology. Amazon EKS runs on Kubernetes. 

If you have containers running on Kubernetes and want an advanced orchestration solution that can provide simplicity, high availability, and fine-grained control over your infrastructure, Amazon EKS could be the tool for you.

Resources

For more information, see the following resources:

- AWS website: [Containers on AWS](https://aws.amazon.com/containers/services/)
- External website: [Docker: Use Containers to Build, Share and Run Your Applications](https://www.docker.com/resources/what-container)
- AWS website: [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/)
- External website: [Github: Amazon ECS Agent](https://github.com/aws/amazon-ecs-agent)
- AWS developer guide: [Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
- External website: Coursera course: [Building Containerized Applications on AWS](https://www.coursera.org/learn/containerized-apps-on-aws)
- AWS website: [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- AWS user guide: [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)


