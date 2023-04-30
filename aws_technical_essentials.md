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
- AWS whitepaper: [AWS Global Infrastructure Documentation](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html)
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
- AWS website: [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)
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

### Introduction to Serverless

#### Removing the undifferentiated heavy lifting

If you run your code on Amazon EC2, AWS is responsible for the physical hardware. You are still responsible for the logical controls, such as the guest operating system, security and patching, networking, security, and scaling.

As covered in the previous Container Services lesson, you choose to have more control by running and managing your containers on Amazon ECS and Amazon EKS. By doing so, AWS is still responsible for more of the container management, such as deploying containers across EC2 instances and managing the container cluster. However, when running Amazon ECS and Amazon EKS on Amazon EC2, you are still responsible for maintaining the underlying EC2 instances.

Is there a way to remove some of this undifferentiated heavy lifting? Yes! If you want to deploy your workloads and applications without having to manage any EC2 instances, you can do that on AWS with serverless compute.

#### Go serverless
With serverless compute, you can spend time on the things that differentiate your application, rather than spending time on ensuring availability, scaling, and managing servers. Every definition of serverless mentions the following four aspects:
- There are no servers to provision or manage.
- It scales with usage.
- You never pay for idle resources.
- Availability and fault tolerance are built in.

#### Resources

For more information, see the following resources:

- AWS website: [Serverless on AWS](https://aws.amazon.com/serverless/#:~:text=Serverless%20is%20the%20native%20architecture,services%20without%20thinking%20about%20servers.) 
- AWS website: [AWS Serverless Resources](https://aws.amazon.com/serverless/getting-started/?serverless.sort-by=item.additionalFields.createdDate&serverless.sort-order=desc)

### Serverless with AWS Fargate
#### Exploring serverless containers with AWS Fargate
Fargate abstracts the EC2 instance so that you’re not required to manage the underlying compute infrastructure. However, with Fargate, you can use all the same Amazon ECS concepts, APIs, and AWS integrations. It natively integrates with IAM and Amazon Virtual Private Cloud (Amazon VPC). With native integration with Amazon VPC, you can launch Fargate containers inside your network and control connectivity to your applications.

![AWS Fargate](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/7vdNvo_iM88pRiA2__waFpJh3C3F9hik_.jpg)

AWS Fargate is a purpose-built serverless compute engine for containers. AWS Fargate scales and manages the infrastructure, so developers can work on what they do best, application development. It achieves this by allocating the right amount of compute. This eliminates the need to choose and manage EC2 instances, cluster capacity, and scaling. Fargate supports both Amazon ECS and Amazon EKS architecture and provides workload isolation and improved security by design.

![AWS Fargate](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/XAKsYbsn84fWQzHq_sged-PS8V6WKvnHk.jpg)

Resources

For more information, see the following resources:

- AWS website: [AWS Fargate](https://aws.amazon.com/fargate/?c=ser&sec=srv)
- AWS website: [Getting Started with Serverless Computing](https://aws.amazon.com/serverless/getting-started/?serverless.sort-by=item.additionalFields.createdDate&serverless.sort-order=desc)
- Exeternal site: [Coursera course: Building Modern Python Applications on AWS](https://www.coursera.org/learn/building-modern-python-applications-on-aws)

### Serverless with AWS Lambda
#### Running code on AWS Lambda
If you want to deploy your workloads and applications without having to manage any EC2 instances or containers, you can use Lambda.

![AWS Lambda](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/mWSKFB91QCUCr3HB_VusQVGrKB5zsTQJt.jpg)

With Lambda, you can run code without provisioning or managing servers. You can run code for virtually any type of application or backend service. This includes data processing, real-time stream processing, machine learning, WebSockets, IoT backends, mobile backends, and web applications like your employee directory application!

Lambda runs your code on a high availability compute infrastructure and requires no administration from the user. You upload your source code in one of the languages that Lambda supports, and Lambda takes care of everything required to run and scale your code with high availability. There are no servers to manage. You get continuous scaling with subsecond metering and consistent performance.

#### How Lambda works

The Lambda function is the foundational principle of AWS Lambda. You have the option of configuring your Lambda functions using the Lambda console, Lambda API, AWS CloudFormation, or AWS Serverless Application Model (AWS SAM). You can invoke your function directly by using the Lambda API, or you can configure an AWS service or resource to invoke your function in response to an event.

- Function
    A function is a resource that you can invoke to run your code in Lambda. Lambda runs instances of your function to process events. When you create the Lambda function, it can be authored in several ways:
    - You can create the function from scratch.
    - You can use a blueprint that AWS provides.
    - You can select a container image to deploy for your function.
    - You can browse the AWS Serverless Application Repository. 

    ![Create Function](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/Ri48UzHPB2wpGaPV_d-1XLCQ7H3feWvVe.png)

- Trigger
Triggers describe when a Lambda function should run. A trigger integrates your Lambda function with other AWS services and event source mappings. So you can run your Lambda function in response to certain API calls or by reading items from a stream or queue. This increases your ability to respond to events in your console without having to perform manual actions. 

- Event
An event is a JSON-formatted document that contains data for a Lambda function to process. The runtime converts the event to an object and passes it to your function code. When you invoke a function, you determine the structure and contents of the event.

- Application Environment
An application environment provides a secure and isolated runtime environment for your Lambda function. An application environment manages the processes and resources that are required to run the function. 

- Deployment package
    You deploy your Lambda function code using a deployment package. Lambda supports two types of deployment packages:
    - A .zip file archive – This contains your function code and its dependencies. Lambda provides the operating system and runtime for your function.
    - A container image – This is compatible with the Open Container Initiative (OCI) specification. You add your function code and dependencies to the image. You must also include the operating system and a Lambda runtime.

- Runtime
The runtime provides a language-specific environment that runs in an application environment. When you create your Lambda function, you specify the runtime that you want your code to run in. You can use built-in runtimes, such as Python, Node.js, Ruby, Go, Java, or .NET Core. Or you can implement your Lambda functions to run on a custom runtime.

- Lambda function handler
–
The AWS Lambda function handler is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. When the handler exits or returns a response, it becomes available to handle another event. 

You can use the following general syntax when creating a function handler in Python.

```python
def handler_name (event, context):
...
return some_value
```

### Billing granularity

With Lambda, you can run code without provisioning or managing servers, and you pay only for what you use. You are charged for the number of times that your code is invoked (requests) and for the time that your code runs, rounded up to the nearest 1 millisecond (ms) of duration.

AWS rounds up duration to the nearest ms with no minimum run time. With this pricing, it can be cost effective to run functions whose execution time is very low, such as functions with durations under 100 ms or low latency APIs.

#### Resources

For more information, see the following resources:

- AWS website: [Building Applications with Serverless Architectures](https://aws.amazon.com/lambda/serverless-architectures-learn-more/)
- AWS blog: [Best Practices for Organizing Larger Serverless Applications](https://aws.amazon.com/blogs/compute/best-practices-for-organizing-larger-serverless-applications/)
- AWS developer guide: [Configuring AWS Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html)
- AWS blog: [10 Things Serverless Architects Should Know](https://aws.amazon.com/blogs/architecture/ten-things-serverless-architects-should-know/)
- AWS workshop: [AWS Alien Attack: A Serverless Adventure](https://alienattack.workshop.aws/)
- AWS blog: [Resize Images on the Fly with Amazon S3, AWS Lambda, and Amazon API Gateway](https://aws.amazon.com/blogs/compute/resize-images-on-the-fly-with-amazon-s3-aws-lambda-and-amazon-api-gateway/)
- AWS blog: [New for AWS Lambda – 1ms Billing Granularity Adds Cost Savings](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-1ms-billing-granularity-adds-cost-savings/)

## Introduction to Networking
### Networking defined

Networking is how you connect computers around the world and allow them to communicate with one another.
- One is the AWS Global Infrastructure. AWS has built a network of resources using data centers, Availability Zones, and Regions. 

### Networking basics

#### IP addresses

To properly route your messages to a location, you need an address. Just like each home has a mailing address, each computer has an IP address. However, instead of using the combination of street, city, state, zip code, and country, the IP address uses a combination of bits, 0s and 1s.

Here is an example of a 32-bit address in binary format:

![IP Address](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/44tSM5tIHfyct5jO_MqSUJDRMLwF_EJf5.png)

It’s called 32 bit because you have 32 digits. Feel free to count!

#### IPv4 notation

Typically, you don’t see an IP address in its binary format. Instead, it’s converted into decimal format and noted as an IPv4 address.

In the following diagram, the 32 bits are grouped into groups of 8 bits, also called octets. Each of these groups is converted into decimal format separated by a period.

![IPv4](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/7PlIDIOy9TP-5Hl2_3O1LCsMztT9hP6Gv.png)

An IPv4 address, for example, 192.168.1.30 is converted from four groups of eight bits.

In the end, this is what is called an IPv4 address. This is important to know when trying to communicate to a single computer. But remember, you’re working with a network. This is where **Classless Inter-Domain Routing (CIDR)** comes in.

#### CIDR notation

192.168.1.30 is a single IP address. If you want to express IP addresses between the range of 192.168.1.0 and 192.168.1.255, how can you do that?

One way is to use CIDR notation. CIDR notation is a compressed way of representing a range of IP addresses. Specifying a range determines how many IP addresses are available to you.

CIDR notation is shown here.

![CIDR](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/qG0VfltLF3yYK8Hc_spqIyeTVAORW0ECH.png)


It begins with a starting IP address and is separated by a forward slash (the / character) followed by a number. The number at the end specifies how many of the bits of the IP address are fixed. In this example, the first 24 bits of the IP address are fixed. The rest (the last 8 bits) are flexible.

![CIDR](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/IzOBlZPPXSGrNjSf_gmxwVotClkzU1FdE.png)

32 total bits subtracted by 24 fixed bits leaves 8 flexible bits. Each of these flexible bits can be either 0 or 1, because they are binary. That means that you have two choices for each of the 8 bits, providing 256 IP addresses in that IP range.

The higher the number after the /, the smaller the number of IP addresses in your network. For example, a range of 192.168.1.0/24 is smaller than 192.168.1.0/16.

When working with networks in the AWS Cloud, you choose your network size by using CIDR notation. In AWS, the smallest IP range you can have is /28, which provides 16 IP addresses. The largest IP range you can have is a /16, which provides 65,536 IP addresses.

#### Resources

For more information, see the following resources:

- External website: [Stanford: Introduction to Computer Networking](https://web.stanford.edu/class/cs101/network-1-introduction.html)
- AWS user guide: [How Amazon VPC Works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)
- External website: [Wikipedia: Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
- External website: [CIDR.xyz: An interactive IP Address and CIDR Range Visualizer](https://cidr.xyz/)

### Amazon VPC
- To maintain redundancy and fault tolerance, create at least two subnets configured in two Availability Zones.

A virtual private cloud (VPC) is an isolated network that you create in the AWS Cloud, similar to a traditional network in a data center. When you create an Amazon VPC, you must choose three main factors:

- Name of the VPC
- Region where the VPC will live – A VPC spans all the Availability Zones within the selected Region.
- IP range for the VPC in CIDR notation – This determines the size of your network. Each VPC can have up to five CIDRs: one primary and four secondaries for IPv4. Each of these ranges can be between /28 (in CIDR notation) and /16 in size.

Using this information, AWS will provision a network and IP addresses for that network.

![AWS VPC](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/vMMnDkXC9TCB3ec7_KKtsB2WCJm3nf8cP.png)

### Creating a subnet

After you create your VPC, you must create subnets inside the network. Think of subnets as smaller networks inside your base network, or virtual local area networks (VLANs) in a traditional, on-premises network. In an on-premises network, the typical use case for subnets is to isolate or optimize network traffic. In AWS, subnets are used to provide high availability and connectivity options for your resources. Use a public subnet for resources that must be connected to the internet and a private subnet for resources that won't be connected to the internet.

![AWS VPC Subnets](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/eq5IhKQ5RcYKABfK_jUajvREe6Ry6idlJ.png)

When you create a subnet, you must specify the following:

- **VPC** that you want your subnet to live in—in this case: VPC (10.0.0.0/16)
- **Availability** Zone that you want your subnet to live in—in this case: Availability Zone 1
- **IPv4 CIDR block for your subnet**, which must be a subset of the VPC CIDR block—in this case: 10.0.0.0/24

When you launch an EC2 instance, you launch it inside a subnet, which will be located inside the Availability Zone that you choose.

### High availability with a VPC

When you create your subnets, keep high availability in mind. To maintain redundancy and fault tolerance, create at least two subnets configured in two Availability Zones.

As you learned earlier, remember that “everything fails all of the time.” With the example network, if one of the Availability Zones fails, you will still have your resources available in another Availability Zone as backup.

![AWS VPC Subnets](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/R5LbUnQ4nP6VbdF9_OaaDyPzF7zr1lKW9.png)

### Reserved IPs

For AWS to configure your VPC appropriately, AWS reserves five IP addresses in each subnet. These IP addresses are used for routing, Domain Name System (DNS), and network management.

For example, consider a VPC with the IP range 10.0.0.0/22. The VPC includes 1,024 total IP addresses. This is then divided into four equal-sized subnets, each with a /24 IP range with 256 IP addresses. Out of each of those IP ranges, there are only 251 IP addresses that can be used because AWS reserves five.

![AWS Reserved IPs](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/EaINUEJOIUnjbhzM_Octk-lV6RnrruL3M.png)

The five reserved IP addresses can impact how you design your network. A common starting place for those who are new to the cloud is to create a VPC with an IP range of /16 and create subnets with an IP range of /24. This provides a large amount of IP addresses to work with at both the VPC and subnet levels.

### Gateways

![AWS Gateways](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/auqqHyg38QFb_uuK_cdDgG30XUESG1bod.png)

#### Internet gateway
To activate internet connectivity for your VPC, you must create an internet gateway. Think of the gateway as similar to a modem. Just as a modem connects your computer to the internet, the internet gateway connects your VPC to the internet. Unlike your modem at home, which sometimes goes down or offline, an internet gateway is highly available and scalable. After you create an internet gateway, you attach it to your VPC.

![AWS Gateways](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/bmQ2nDdzNUGctvTl_eB71WD-OxzwmjLTG.jpg)

#### Virtual private gateway
A virtual private gateway connects your VPC to another private network. When you create and attach a virtual private gateway to a VPC, the gateway acts as anchor on the AWS side of the connection. On the other side of the connection, you will need to connect a customer gateway to the other private network. A customer gateway device is a physical device or software application on your side of the connection. When you have both gateways, you can then establish an encrypted virtual private network (VPN) connection between the two sides.

#### AWS Direct Connect

To establish a secure physical connection between your on-premises data center and your Amazon VPC, you can use AWS Direct Connect. With AWS Direct Connect, your internal network is linked to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. This connection allows you to create virtual interfaces directly to public AWS services or to your VPC.

![AWS Direct Connect](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/Xl9KUxmhvC7-9woz_CC16Zxyi_ii4JBzG.png)

#### Resources

For more information, see the following resources:

- AWS user guide: [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- AWS user guide: [How Amazon VPC Works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)
- AWS user guide: [How AWS Site-to-Site VPN Works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)
- AWS user guide: [What Is AWS Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

### Amazon VPC Routing

- A route table contains a set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.

#### Main route table

When you create a VPC, AWS creates a route table called the main route table. A route table contains a set of rules, called routes, that are used to determine where network traffic is directed. AWS assumes that when you create a new VPC with subnets, you want traffic to flow between them. Therefore, the default configuration of the main route table is to allow traffic between all subnets in the local network. The following rules apply to the main route table:

- You cannot delete the main route table.
- You cannot set a gateway route table as the main route table.
- You can replace the main route table with a custom subnet route table.
- You can add, remove, and modify routes in the main route table.
- You can explicitly associate a subnet with the main route table, even if it's already implicitly associated.

#### Custom route tables

The main route table is used implicitly by subnets that do not have an explicit route table association. However, you might want to provide different routes on a per-subnet basis for traffic to access resources outside of the VPC. For example, your application might consist of a frontend and a database. You can create separate subnets for the resources and provide different routes for each of them.

If you associate a subnet with a custom route table, the subnet will use it instead of the main route table. Each custom route table that you create will have the local route already inside it, allowing communication to flow between all resources and subnets inside the VPC. You can protect your VPC by explicitly associating each new subnet with a custom route table and leaving the main route table in its original default state.

![AWS Route Table](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/hH9khtak8bOWKjz7_za27r6BRGtbQqnc3.png)

#### Resources

For more information, see the following resource:

- AWS user guide: [Configure Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

### AWS VPC Security
- Cloud security at AWS is the highest priority. You benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

#### Secure subnets with network access control lists

![AWS Network ACLs](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/UhwAcYcG11fm7Ver_mc0ohrPRO6iK9bfX.png)

Think of a network access control list (network ACL) as a virtual firewall at the subnet level. A network ACL lets you control what kind of traffic is allowed to enter or leave your subnet. You can configure this by setting up rules that define what you want to filter. Here is an example of a default ACL for a VPC that supports IPv4.

#### Dfault network ACL

**Inbound**
|Rule#|Type|Protocol|Port Range|Source|Allow or Deny|
|:---:|:--:|:------:|:--------:|:----:|:-----------:|
|100|All IPV4 trafic|All|All|0.0.0.0/0|Allow|
|*|All APV4 |All |All|0.0.0.0/0|DENY|


**Outbound**
|Rule#|Type|Protocol|Port Range|Source|Allow or Deny|
|:---:|:--:|:------:|:--------:|:----:|:-----------:|
|100|All IPV4 trafic|All|All|0.0.0.0/0|Allow|
|*|All APV4 |All |All|0.0.0.0/0|DENY|

The default network ACL shown in the preceding table, allows all traffic in and out of the subnet. To allow data to flow freely to the subnet, this is a good starting place.

However, you might want to restrict data at the subnet level. For example, if you have a web application, you might restrict your network to allow HTTPS traffic and Remote Desktop Protocol (RDP) traffic to your web servers.

#### Custom network ACL

**Inbound**
|Rule#|Source IP|Protocol|Port Range|Allow or Deny|Comments|
|:---:|:--:|:------:|:--------:|:-----------:|:------------|
|100|All IPV4 trafic| TCP | 443 |Allow|Allows inbound HTTPS traffic from anywhere|
|130 |192.0.2.0/24 |TCP |3389 | Allow | Allows inbound RDP traffic to the web servers from your home network’s public IP address range (over the internet gateway)|
|*|All APV4 |All |All|DENY|


**Outbound**
|Rule#|Source IP|Protocol|Port Range|Allow or Deny|Comments|
|:---:|:--:|:------:|:--------:|:-----------:|:------------|
|120|0.0.0.0/0| TCP | 1025-65535 |Allow|Allows outbound responses to clients on the internet (serving people visiting the web servers in the subnet)|
|* |0.0.0.0/0 |All |All | DENY | Denies all outbound traffic not already handled by a preceding rule (not modifiable)|

Notice that in the custom network ACL in the preceding example, you allow inbound 443 and outbound range 1025–65535. That’s because HTTPS uses port 443 to initiate a connection and will respond to an ephemeral port. Network ACLs are considered stateless, so you need to include both the inbound and outbound ports used for the protocol. If you don’t include the outbound range, your server would respond but the traffic would never leave the subnet.

Because network ACLs are configured by default to allow incoming and outgoing traffic, you don’t need to change their initial settings unless you need additional security layers.

#### Secure EC2 instances with security groups

The next layer of security is for your EC2 instances. Here, you can create a virtual firewall called a security group. The default configuration of a security group blocks all inbound traffic and allows all outbound traffic.

![EC2 security groups](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/nwn0kju3ONBqtvqz_LHSo8q3H-_Wuu73H.jpg)

You might be wondering, “Wouldn’t this block all EC2 instances from receiving the response of any customer requests?” Well, security groups are stateful. That means that they will remember if a connection is originally initiated by the EC2 instance or from the outside, and temporarily allow traffic to respond without modifying the inbound rules.

If you want your EC2 instance to accept traffic from the internet, you must open up inbound ports. If you have a web server, you might need to accept HTTP and HTTPS requests to allow that type of traffic into your security group. You can create an inbound rule that will allow port 80 (HTTP) and port 443 (HTTPS), as shown.

#### Security group inbound rules

**Inbound rules**
|Type |Protocol |Port Range |Source |
|:---:|:-------:|:---------:|:-----:|
|HTTP(80) |TCP(6) |80 |0.0.0.0/0|
|HTTP(80) |TCP(6) |80 |::/0|
|HTTPS(443) |TCP(6) |443 |0.0.0.0/0|

You learned earlier that subnets can be used to segregate traffic between computers in your network. Security groups can be used in the same way. A common design pattern is to organize resources into different groups and create security groups for each to control network communication between them.

![Security groups](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/TKmaX8OmwvTabd6y_scxJIDNUzFAqjZbL.jpg)

This example defines three tiers and isolates each tier with defined security group rules. In this case, internet traffic to the web tier is allowed over HTTPS. Web tier to application tier traffic is allowed over HTTP, and application tier to database tier traffic is allowed over MySQL. This is different from traditional on-premises environments, in which you isolate groups of resources with a VLAN configuration. In AWS, security groups allow you to achieve the same isolation without tying the security groups to your network.

#### Resources

For more information, see the following resources.

- AWS user guide: [Configure Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- AWS user guide: [Example Routing Options](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html)
- AWS user guide: [Working with Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html)
- AWS user guide: [Control Traffic to Subnets Using Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- AWS user guide: [Control Traffic to Resources Using Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)


## Storage Types on AWS
- With cloud computing, you can create, delete, and modify storage solutions within a matter of minutes.

AWS storage services are grouped into three categories: file storage, block storage, and object storage. In file storage, data is stored as files in a hierarchy. In block storage, data is stored in fixed-size blocks. And in object storage, data is stored as objects in buckets.

![AWS Storage Types](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/IMdNOqYa-xXi65Uq_oLO1YahxjimpoiS8.png)

### File storage

You might be familiar with file storage if you have interacted with file storage systems like Windows File Explorer or Finder on macOS. Files are organized in a tree-like hierarchy that consist of folders and subfolders. For example, if you have hundreds of cat photos on your laptop, you might want to create a folder called **Cat photos**, and place the images inside that folder to organize them. Because you know that these images will be used in an application, you might want to place the Cat photos folder inside another folder called **Application files**.

![File Storage](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/5d4oLziUwY01cuve_KQdGKmX7mBPvlp-E.jpg)

Each file has metadata such as file name, file size, and the date the file was created. The file also has a path, for example, computer/Application_files/Cat_photos/cats-03.png. When you need to retrieve a file, your system can use the path to find it in the file hierarchy.

File storage is ideal when you require centralized access to files that must be easily shared and managed by multiple host computers. Typically, this storage is mounted onto multiple hosts, and requires file locking and integration with existing file system communication protocols.

### Use cases for file storage

#### Web serving
Cloud file storage solutions follow common file-level protocols, file naming conventions, and permissions that developers are familiar with. Therefore, file storage can be integrated into web applications.

#### Analytics
Many analytics workloads interact with data through a file interface and rely on features such as file lock or writing to portions of a file. Cloud-based file storage supports common file-level protocols and has the ability to scale capacity and performance. Therefore, file storage can be conveniently integrated into analytics workflows.

#### Media and entertainment
Many businesses use a hybrid cloud deployment and need standardized access using file system protocols (NFS or SMB) or concurrent protocol access. Cloud file storage follows existing file system semantics. Therefore, storage of rich media content for processing and collaboration can be integrated for content production, digital supply chains, media streaming, broadcast playout, analytics, and archive.

#### Home directories
Businesses wanting to take advantage of the scalability and cost benefits of the cloud are extending access to home directories for many of their users. Cloud file storage systems adhere to common file-level protocols and standard permissions models. Therefore, customers can lift and shift applications that need this capability to the cloud.

### Block storage

File storage treats files as a singular unit, but block storage splits files into fixed-size chunks of data called blocks that have their own addresses. Each block is an individual piece of data storage. Because each block is addressable, blocks can be retrieved efficiently. Think of block storage as a more direct route to access the data.

When data is requested, the addresses are used by the storage system to organize the blocks in the correct order to form a complete file to present back to the requestor. Besides the address, no additional metadata is associated with each block.

#### Changing one character in a 1-GB file with block storage

![Block storage](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/KojgpTlFeEVGIR-p_v9a8_0p7AENmm_O_.png)

If you want to change one character in a file, you just change the block, or the piece of the file, that contains the character. This ease of access is why block storage solutions are fast and use less bandwidth.

### Use cases for block storage

Because block storage is optimized for low-latency operations, it is a preferred storage choice for high-performance enterprise workloads and transactional, mission-critical, and I/O-intensive applications.

#### Transactional workloads
Organizations that process time-sensitive and mission-critical transactions store such workloads into a low-latency, high-capacity, and fault-tolerant database. Block storage allows developers to set up a robust, scalable, and highly efficient transactional database. Because each block is a self-contained unit, the database performs optimally, even when the stored data grows.

#### Containers
Developers use block storage to store containerized applications on the cloud. Containers are software packages that contain the application and its resource files for deployment in any computing environment. Like containers, block storage is equally flexible, scalable, and efficient. With block storage, developers can migrate the containers seamlessly between servers, locations, and operating environments.

#### Virtual machines
Block storage supports popular virtual machine (VM) hypervisors. Users can install the operating system, file system, and other computing resources on a block storage volume. They do so by formatting the block storage volume and turning it into a VM file system. So they can readily increase or decrease the virtual drive size and transfer the virtualized storage from one host to another.

### Object storage

In object storage, files are stored as objects. Objects, much like files, are treated as a single, distinct unit of data when stored. However, unlike file storage, these objects are stored in a bucket using a flat structure, meaning there are no folders, directories, or complex hierarchies. Each object contains a unique identifier. This identifier, along with any additional metadata, is bundled with the data and stored.

#### Changing one character in a 1-GB file with object storage

![Object storage update](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/CGmh3y1aEWjU_-Y5_MWECIXl-KQQsHXzi.png)

Changing just one character in an object is more difficult than with block storage. When you want to change one character in an object, the entire object must be updated.

### Use cases for object storage

With object storage, you can store almost any type of data, and there is no limit to the number of objects stored, which makes it readily scalable. Object storage is generally useful when storing large or unstructured data sets.

#### Data archiving
Cloud object storage is excellent for long-term data retention. You can cost-effectively archive large amounts of rich media content and retain mandated regulatory data for extended periods of time. You can also use cloud object storage to replace on-premises tape and disk archive infrastructure. This storage solution provides enhanced data durability, immediate retrieval times, better security and compliance, and greater data accessibility. 

#### Backup and recovery
You can configure object storage systems to replicate content so that if a physical device fails, duplicate object storage devices become available. This ensures that your systems and applications continue to run without interruption. You can also replicate data across multiple data centers and geographical regions.

#### Rich media
With object storage, you can accelerate applications and reduce the cost of storing rich media files such as videos, digital images, and music. By using storage classes and replication features, you can create cost-effective, globally replicated architecture to deliver media to distributed users.

### Relating back to traditional storage systems
If you have worked with on-premises storage, you might already be familiar with block, file, and object storage. Consider the following technologies and how they relate to systems that you might have seen before:

- **Block storage** in the cloud is analogous to direct-attached storage (DAS) or a storage area network (SAN).
- **File storage** systems are often supported with a network-attached storage (NAS) server.

Adding storage in a traditional data center is a rigid process—the storage solutions must be purchased, installed, and configured. With cloud computing, the process is more flexible. You can create, delete, and modify storage solutions within a matter of minutes.

#### Resources

For more information, see the following resource:

- AWS website: [Cloud Computing Concepts Hub](https://aws.amazon.com/what-is/?faq-hub-cards.sort-by=item.additionalFields.sortDate&faq-hub-cards.sort-order=desc&awsf.tech-category=tech-category%23storage)


### File Storage with Amazon EFS and Amazon FSx
#### Amazon Elastic File System (Amazon EFS)
![Amazon EFS](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/xF9MlpFePDe7t4JL_UwxFAKO4Zsvwqe6l.jpg)

Amazon Elastic File System (Amazon EFS) is a set-and-forget file system that automatically grows and shrinks as you add and remove files. There is no need for provisioning or managing storage capacity and performance. Amazon EFS can be used with AWS compute services and on-premises resources. You can connect tens, hundreds, and even thousands of compute instances to an Amazon EFS file system at the same time, and Amazon EFS can provide consistent performance to each compute instance.

With the Amazon EFS simple web interface, you can create and configure file systems quickly without any minimum fee or setup cost. You pay only for the storage used and you can choose from a range of storage classes designed to fit your use case. 

|Standard storage classes |One zone storage classes |
|:------------------------|:------------------------|
|EFS Standard and EFS Standard-Infrequent Access (Standard-IA) offer Multi-AZ resilience and the highest levels of durability and availability.|EFS One Zone and EFS One Zone-Infrequent Access (EFS One Zone-IA) provide additional savings by saving your data in a single availability zone.|

#### Amazon FSx
![Amazon FSx](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/y9GDIyZXAzVQ2Q8X_OmLZpA6z7CA9E2R1.jpg)

Amazon FSx is a fully managed service that offers reliability, security, scalability, and a broad set of capabilities that make it convenient and cost effective to launch, run, and scale high-performance file systems in the cloud. With Amazon FSx, you can choose between four widely used file systems: Lustre, NetApp ONTAP, OpenZFS, and Windows File Server. You can choose based on your familiarity with a file system or based on your workload requirements for feature sets, performance profiles, and data management capabilities.

#### Amazon FSx for NetApp ONTAP

**Amazon FSx for NetApp ONTAP** is a fully managed service. It combines the familiar features, performance, capabilities, and API operations of on-premises NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service. FSx for ONTAP can serve as a drop-in replacement for existing ONTAP deployments, giving customers the ability to launch and run ONTAP file systems in the cloud.  

FSx for ONTAP provides rich data management features and flexible shared file storage that are broadly accessible from Linux, Windows, and macOS compute instances running in AWS or on premises.

#### Amazon FSx for OpenZFS

**Amazon FSx for OpenZFS** is a fully managed file storage service that helps you to move data residing in on-premises ZFS or other Linux-based file servers to AWS without changing your application code or how you manage data. With FSx for OpenZFS, you no longer have to worry about setting up and provisioning files servers and storage volumes. You also don't have to deal with replicating data, installing and patching file server software, detecting and addressing hardware failures, or manually performing backups.

FSx for OpenZFS delivers leading performance for latency-sensitive and small-file workloads with popular NAS data management capabilities (snapshots, and cloning), at a lower price than commercially licensed alternatives.

#### Amazon FSx for Windows File Server

**Amazon FSx for Windows File Server** provides fully managed, highly reliable and scalable Microsoft Windows file servers, backed by a fully native Windows file system. FSx for Windows File Server provides file storage that is accessible over the Service Message Block (SMB) protocol and has the ability to serve as a drop-in replacement for existing Windows file server deployments. 

As a fully managed service, FSx for Windows File Server removes the administrative tasks of setting up and provisioning file servers and storage volumes and provides ease of use for customers building and running Windows applications.

#### Amazon FSx for Lustre

The open-source Lustre file system is designed for applications that require fast storage, where you want your storage to keep up with your compute. **Amazon FSx for Lustre** makes it convenient and cost effective to launch, run, and scale the popular high-performance file system. You can link FSx for Lustre file systems to data repositories on Amazon Simple Storage Service (Amazon S3) or to on-premises data stores.

FSx for Lustre delivers the highest levels of throughput (up to 1+ TB/s) and IOPS (millions). Customers can seamlessly integrate, access, and process their Amazon S3 datasets using the Lustre high-performance file system.

#### Resources

For more information, see the following resources:

- AWS website: [Amazon EFS](https://aws.amazon.com/efs/)
- AWS website: [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/)
- AWS website: [Amazon FSx for OpenZFS](https://aws.amazon.com/fsx/openzfs/)
- AWS website: [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/?nc=sn&loc=1)
- AWS website: [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/?nc=sn&loc=1)

### Block Storage with Amazon EC2 - Instance Store and Amazon EBS
- The unique characteristics of block storage make it the preferred option for transactional, mission-critical, and I/O-intensive applications.

#### Amazon EC2 instance store

Amazon Elastic Compute Cloud (Amazon EC2) instance store provides temporary block-level storage for an instance. This storage is located on disks that are physically attached to the host computer. This ties the lifecycle of the data to the lifecycle of the EC2 instance. If you delete the instance, the instance store is also deleted. Because of this, instance store is considered ephemeral storage. Read more about it in the Amazon EC2 documentation found in the resources section at the end of this lesson.

Instance store is ideal if you host applications that replicate data to other EC2 instances, such as Hadoop clusters. For these cluster-based workloads, having the speed of locally attached volumes and the resiliency of replicated data helps you achieve data distribution at high performance. It’s also ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content.

![Amazon Instance store and Amazon EBS](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/jGPn2jaJ0poYZwj0_poD3H2NJ-YmK1HKj.png)

#### Amazon EBS

As the name implies, Amazon Elastic Block Store (Amazon EBS) is block-level storage that you can attach to an Amazon EC2 instance. You can compare this to how you much attach an external drive to your laptop. This attachable storage is called an EBS volume. EBS volumes act similarly to external drives in more than one way.

- **Detachable**: You can detach an EBS volume from one EC2 instance and attach it to another EC2 instance in the same Availability Zone to access the data on it.

- **Distinct**: The external drive is separate from the computer. That means that if an accident occurs and the computer goes down, you still have your data on your external drive. The same is true for EBS volumes.

- **Size-limited**: You’re limited to the size of the external drive, because it has a fixed limit to how scalable it can be. For example, you might have a 2 TB external drive, which means you can only have 2 TB of content on it. This also relates to Amazon EBS, because a volume also has a max limitation of how much content you can store on it.

- **1-to-1 connection**: Most EBS volumes can only be connected with one computer at a time. Most EBS volumes have a one-to-one relationship with EC2 instances, so they cannot be shared by or attached to multiple instances at one time.

#### Scaling Amazon EBS volumes
You can scale EBS volumes in two ways:-

- **Increase the volume size** only if it doesn’t increase above the maximum size limit. Depending on the volume selected, Amazon EBS currently supports a maximum volume size of 64 tebibytes (TiB). For example, if you provision a 5-TiB io2 Block Express volume, you can choose to increase the size of your volume until you get to 64 TiB.

- **Attach multiple volumes** to a single EC2 instance. Amazon EC2 has a one-to-many relationship with EBS volumes. You can add these additional volumes during or after EC2 instance creation to provide more storage capacity for your hosts.

### Amazon EBS use cases

Amazon EBS is useful when you must retrieve data quickly and have data persist long term. Volumes are commonly used in the following scenarios.

#### Operating systems
Boot and root volumes can be used to store an operating system. The root device for an instance launched from an Amazon Machine Image (AMI) is typically an EBS volume. These are commonly referred to as EBS-backed AMIs.

#### Databases
As a storage layer for databases running on Amazon EC2 that will scale with your performance needs and provide consistent and low-latency performance.

#### Enterprise applications
Amazon EBS provides high availability and high durability block storage to run business-critical applications.

#### Big data analytics engines
Amazon EBS offers data persistence, dynamic performance adjustments, and the ability to detach and reattach volumes, so you can resize clusters for big data analytics.

### EBS volume types

EBS volumes are organized into two main categories: solid-state drives (SSDs) and hard-disk drives (HDDs). SSDs are used for transactional workloads with frequent read/write operations with small I/O size. HDDs are used for large streaming workloads that need high throughput performance.  AWS offers two types of each.

- SSD volumes
- HDD volumes

### Amazon EBS benefits
- When you create an EBS volume, it is automatically replicated in its Availability zone to prevent data loss from single points of failure.
- Storage persists even when your instance doesn't.
- When activated by the user, all EBS volumes support encryption.
- EBS volumes support on-the-fly changes. Modify volume type, volume size, and input/output operations per second(IOPS) capacity without stopping your instance.
- Amazon EBS provides the ability to create backups of any EBS volume.

### Amazon EBS snapshots

Errors happen. One error is not backing up data and then inevitably losing it. To prevent this from happening to you, always back up your data, even in AWS. Because your EBS volumes consist of the data from your EC2 instance, you should make backups of these volumes, called snapshots.

EBS snapshots are incremental backups that only save the blocks on the volume that have changed after your most recent snapshot. For example, if you have 10 GB of data on a volume and only 2 GB of data have been modified since your last snapshot, only the 2 GB that have been changed are written to Amazon S3.

When you take a snapshot of any of your EBS volumes, the backups are stored redundantly in multiple Availability Zones using Amazon S3. This aspect of storing the backup in Amazon S3 is handled by AWS, so you won’t need to interact with Amazon S3 to work with your EBS snapshots. You manage them in the Amazon EBS console, which is part of the Amazon EC2 console.

EBS snapshots can be used to create multiple new volumes, whether they’re in the same Availability Zone or a different one. When you create a new volume from a snapshot, it’s an exact copy of the original volume at the time the snapshot was taken.

#### Resources

For more information, see the following resources:

- AWS user guide: [Amazon EC2 Instance Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- AWS user guide: [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
- AWS FAQs: [Amazon EBS](https://aws.amazon.com/ebs/faqs/)

### Object Storage with Amazon S3 - Amazon Simple Storage Service(S3)
- Object storage is built for the cloud and delivers virtually unlimited scalability, high durability, and cost effectiveness.

Unlike Amazon EBS, Amazon Simple Storage Service (Amazon S3) is a standalone storage solution that isn’t tied to compute. With Amazon S3, you can retrieve your data from anywhere on the web. If you have used an online storage service to back up the data from your local machine, you most likely have used a service similar to Amazon S3. The big difference between those online storage services and Amazon S3 is the storage type.

Amazon S3 is an object storage service. Object storage stores data in a flat structure. An object is a file combined with metadata. You can store as many of these objects as you want. All the characteristics of object storage are also characteristics of Amazon S3.

### Amazon S3 concepts

1[Amazon S3](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/VY8AN514gSCE-q4e_J5XS-4bErHuFtWRy.png)

In Amazon S3, you store your objects in containers called buckets. You can’t upload an object, not even a single photo, to Amazon S3 without creating a bucket first. When you store an object in a bucket, the combination of a bucket name, key, and version ID uniquely identifies the object.  

When you create a bucket, you specify, at the very minimum, two details: the bucket name and the AWS Region that you want the bucket to reside in.

![Create a bucket](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/55Srhfrd6q7hcfc-_w4B6158YVyIYUoJC.jpg)

### Amazon S3 bucket names
Amazon S3 supports global buckets. Therefore, each bucket name must be unique across all AWS accounts in all AWS Regions within a partition. A partition is a grouping of Regions, of which AWS currently has three: Standard Regions, China Regions, and AWS GovCloud (US). When naming a bucket, choose a name that is relevant to you or your business. For example, you should avoid using AWS or Amazon in your bucket name.

The following are some examples of the rules that apply for naming buckets in Amazon S3. For a full list of rules, see the link in the resources section. 

- Bucket names must be between 3 (min) and 63 (max) characters long.
- Bucket names can consist only of lowercase letters, numbers, dots (.), and hyphens (-).
- Bucket names must begin and end with a letter or number.
- Buckets must not be formatted as an IP address.
- A bucket name cannot be used by another AWS account in the same partition until the bucket is deleted.

If your application automatically creates buckets, choose a bucket naming scheme that is unlikely to cause naming conflicts and will choose a different bucket name, should one not be available.

### Object key names

The object key (key name) uniquely identifies the object in an Amazon S3 bucket. When you create an object, you specify the key name. As described earlier, the Amazon S3 model is a flat structure, meaning there is no hierarchy of subbuckets or subfolders. However, the Amazon S3 console does support the concept of folders. By using key name prefixes and delimiters, you can imply a logical hierarchy.  

For example, suppose your bucket called testbucket has two objects with the following object keys: 2022-03-01/AmazonS3.html and 2022-03-01/Cats.jpg. The console uses the key name prefix, 2022-03-01, and delimiter (/) to present a folder structure.

![prefixes-delimeters](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/LSIsk7KOv_N3TqTN_sN1Un2LLeNg_T0eo.png)

### Amazon S3 use cases

Amazon S3 is a widely used storage service, with far more use cases than could fit on one screen.

#### Backup and storage
Amazon S3 is a natural place to back up files because it is highly redundant. As mentioned in the last lesson, AWS stores your EBS snapshots in Amazon S3 to take advantage of its high availability.

#### Media hosting
Because you can store unlimited objects, and each individual object can be up to 5 TB, Amazon S3 is an ideal location to host video, photo, and music uploads.

#### Software delivery
You can use Amazon S3 to host your software applications that customers can download.

#### Data lakes
Amazon S3 is an optimal foundation for a data lake because of its virtually unlimited scalability. You can increase storage from gigabytes to petabytes of content, paying only for what you use.

#### Static websites
You can configure your S3 bucket to host a static website of HTML, CSS, and client-side scripts.

#### Static content
Because of the limitless scaling, the support for large files, and the fact that you can access any object over the web at any time, Amazon S3 is the perfect place to store static content.


### Security in Amazon S3

Everything in Amazon S3 is private by default. This means that all Amazon S3 resources, such as buckets and objects, can only be viewed by the user or AWS account that created that resource. Amazon S3 resources are all private and protected to begin with.

If you decide that you want everyone on the internet to see your photos, you can choose to make your buckets and objects public. A public resource means that everyone on the internet can see it. Most of the time, you don’t want your permissions to be all or nothing. Typically, you want to be more granular about the way that you provide access to your resources.

![S3 security](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/ePHC7_xk3qkeFBgv_qHtpoUP9GBh3EM0n.png)

To be more specific about who can do what with your Amazon S3 resources, Amazon S3 provides several security management features: IAM policies, S3 bucket policies, and encryption to develop and implement your own security policies.

### Amazon S3 and IAM policies

Previously, you learned about creating and using AWS Identity and Access Management (IAM) policies. Now you can apply that knowledge to Amazon S3. When IAM policies are attached to your resources (buckets and objects) or IAM users, groups, and roles, the policies define which actions they can perform. Access policies that you attach to your resources are referred to as resource-based policies and access policies attached to users in your account are called user policies.

![IAM Policies](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/TDWzG9LFg7gReUAy_KRLzH0N3cmxDxdbv.png)

You should use IAM policies for private buckets in the following two scenarios:
- You have many buckets with different permission requirements. Instead of defining many different S3 bucket policies, you can use IAM policies.
- You want all policies to be in a centralized location. By using IAM policies, you can manage all policy information in one location.

### Amazon S3 bucket policies

Like IAM policies, S3 bucket policies are defined in a JSON format. Unlike IAM policies, which are attached to resources and users, S3 bucket policies can only be attached to S3 buckets. The policy that is placed on the bucket applies to every object in that bucket. S3 bucket policies specify what actions are allowed or denied on the bucket.

You should use S3 bucket policies in the following scenarios:
- You need a simple way to do cross-account access to Amazon S3, without using IAM roles.
- Your IAM policies bump up against the defined size limit. S3 bucket policies have a larger size limit.

For examples of bucket policies, see the [Bucket Policy Examples](https://docs.aws.amazon.com/en_us/AmazonS3/latest/userguide/example-bucket-policies.html) link here or in the resources section.

### Amazon S3 encryption

Amazon S3 reinforces encryption in transit (as it travels to and from Amazon S3) and at rest. To protect data, Amazon S3 automatically encrypts all objects on upload and applies server-side encryption with S3-managed keys as the base level of encryption for every bucket in Amazon S3 at no additional cost.

### Amazon S3 storage classes

When you upload an object to Amazon S3 and you don’t specify the storage class, you upload it to the default storage class, often referred to as standard storage. In previous lessons, you learned about the default Amazon S3 standard storage class.

Amazon S3 storage classes let you change your storage tier when your data characteristics change. For example, if you are accessing your old photos infrequently, you might want to change the storage class for the photos to save costs.

|Storage Class |Description |
|:-------------|:-----------|
|S3 Standard|This is considered general-purpose storage for cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics.|
|S3 Intelligent-Tiering |This tier is useful if your data has unknown or changing access patters. S3 Intelligent-Tiering stores objects in three tiers: a frequent access tier, an infrequent access tier, and an archive instance access tier. Amazon S3 monitors access patterns of your data and automatically moves your data to the most cost-effective storage tier based on frequency of access.|
|S3 Standard-Infrequent Access (S3 Standard-IA) |This tier is for data that is accessed less frequently but requires rapid access when needed. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a low per-GB storage price and per-GB retrieval fee. This storage tier is ideal if you want to store long-term backups, disaster recovery files, and so on.|
|S3 One Zone-Infrequent Access (S3 One Zone-IA) |Unlike other S3 storage classes that store data in a minimum of three Availability Zones, S3 One Zone-IA stores data in a single Availability Zone, which makes it less expensive than S3 Standard-IA. S3 One Zone-IA is ideal for customers who want a lower-cost option for infrequently accessed data, but do not require the availability and resilience of S3 Standard or S3 Standard-IA. It's a good choice for storing secondary backup copies of on-premises data or easily recreatable data. |
|S3 Glacier Instant Retrieval |Use S3 Glacier Instant Retrieval for archiving data that is rarely accessed and requires millisecond retrieval. Data stored in this storage class offers a cost savings of up to 68 percent compared to the S3 Standard-IA storage class, with the same latency and throughput performance. |
|S3 Glacier Flexible Retrieval |S3 Glacier Flexible Retrieval offers low-cost storage for archived data that is accessed 1–2 times per year. With S3 Glacier Flexible Retrieval, your data can be accessed in as little as 1–5 minutes using an expedited retrieval. You can also request free bulk retrievals in up to 5–12 hours. It is an ideal solution for backup, disaster recovery, offsite data storage needs, and for when some data occasionally must be retrieved in minutes. |
|S3 Glacier Deep Archive |S3 Glacier Deep Archive is the lowest-cost Amazon S3 storage class. It supports long-term retention and digital preservation for data that might be accessed once or twice a year. Data stored in the S3 Glacier Deep Archive storage class has a default retrieval time of 12 hours. It is designed for customers that retain data sets for 7–10 years or longer, to meet regulatory compliance requirements. Examples include those in highly regulated industries, such as the financial services, healthcare, and public sectors. |
|S3 on Outposts |Amazon S3 on Outposts delivers object storage to your on-premises AWS Outposts environment using S3 API's and features. For workloads that require satisfying local data residency requirements or need to keep data close to on premises applications for performance reasons, the S3 Outposts storage class is the ideal option. |

### Amazon S3 versioning

As described earlier, Amazon S3 identifies objects in part by using the object name. For example, when you upload an employee photo to Amazon S3, you might name the object employee.jpg and store it in a bucket called employees. Without Amazon S3 versioning, every time you upload an object called employee.jpg to the employees bucket, it will overwrite the original object.
This can be an issue for several reasons, including the following:

- **Common names**: The employee.jpg object name is a common name for an employee photo object. You or someone else who has access to the bucket might not have intended to overwrite it; but once it's overwritten, the original object can't be accessed.
- **Version preservation**: You might want to preserve different versions of employee.jpg. Without versioning, if you wanted to create a new version of employee.jpg, you would need to upload the object and choose a different name for it. Having several objects all with slight differences in naming variations can cause confusion and clutter in S3 buckets.

To counteract these issues, you can use Amazon S3 versioning. Versioning keeps multiple versions of a single object in the same bucket. This preserves old versions of an object without using different names, which helps with object recovery from accidental deletions, accidental overwrites, or application failures.

![Object versioning](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/ZolDtu1ahUfKekhV_86d-BbLx9Y1g9QZN.png)

If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object. In one bucket, for example, you can have two objects with the same key but different version IDs, such as employeephoto.jpg (version 111111) and employeephoto.jpg (version 121212).

By using versioning-enabled buckets, you can recover objects from accidental deletion or overwrite. The following are examples:

- Deleting an object does not remove the object permanently. Instead, Amazon S3 puts a marker on the object that shows that you tried to delete it. If you want to restore the object, you can remove the marker and the object is reinstated.
- If you overwrite an object, it results in a new object version in the bucket. You still have access to previous versions of the object.

### Versioning states

Buckets can be in one of three states. The versioning state applies to all objects in the bucket. Storage costs are incurred for all objects in your bucket, including all versions. To reduce your Amazon S3 bill, you might want to delete previous versions of your objects when they are no longer needed.

#### Unversioned (default)
No new and existing objects in the bucket have a version.

#### Versioning-enabled
Versioning is enabled for all objects in the bucket. After you version-enable a bucket, it can never return to an unversioned state. However, you can suspend versioning on that bucket.

#### Versioning-suspended
Versioning is suspended for new objects. All new objects in the bucket will not have a version. However, all existing objects keep their object versions.

### Managing your storage lifecycle

If you keep manually changing your objects, such as your employee photos, from storage tier to storage tier, you might want to automate the process by configuring their Amazon S3 lifecycle. When you define a lifecycle configuration for an object or group of objects, you can choose to automate between two types of actions: transition and expiration.

- **Transition actions** define when objects should transition to another storage class.
- **Expiration actions** define when objects expire and should be permanently deleted.

For example, you might transition objects to S3 Standard-IA storage class 30 days after you create them. Or you might archive objects to the S3 Glacier Deep Archive storage class 1 year after creating them.

![Storage Lifecycle](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/kUMV6y6bdZ9nTmva_yJcSJtGhz1K8Fs3r.png)

The following use cases are good candidates for the use of lifecycle configuration rules:

- **Periodic logs**: If you upload periodic logs to a bucket, your application might need them for a week or a month. After that, you might want to delete them.
- **Data that changes in access frequency**: Some documents are frequently accessed for a limited period of time. After that, they are infrequently accessed. At some point, you might not need real-time access to them. But your organization or regulations might require you to archive them for a specific period. After that, you can delete them.

#### Resources

For more information, see the following resources:

- AWS website: [Amazon S3](https://aws.amazon.com/s3/)
- AWS website: [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)
- AWS user guide: [Using Versioning in S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- AWS user guide: [Bucket Naming Rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html)
- AWS user guide: [Bucket Policy Examples](https://docs.aws.amazon.com/en_us/AmazonS3/latest/userguide/example-bucket-policies.html)


## Introduction to Databases on AWS
- A high-performing database is crucial to any organization. Databases support the internal operations of companies and store interactions with customers and suppliers.

### History behind enterprise databases

Choosing a database used to be a straightforward decision. Customers had only a few options to choose from. Typically, they would consider a few vendors and then, inevitably, choose one for all their applications. Businesses often selected a database technology before they fully understood their use case. Since the 1970s, the database type most commonly selected by businesses was a relational database.

### Relational databases

A relational database organizes data into tables. Data in one table can link to data in other tables to create relationships—hence, the relational part of the name.

A table stores data in rows and columns. A row, often called a record, contains all information about a specific entry. Columns describe attributes of an entry. The following image is an example of three tables in a relational database.

![Relational Database](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/4EtG6mT8Np-kjCWm_2LDugnFFKSyS9mOy.png)

The preceding image shows a table for books, a table for sales, and a table for authors. In the books table, each row includes the International Standard Book Number (ISBN), title, author, and format. Each of these attributes is stored in its own column. The books table has something in common with the other two tables—the author attribute. That common column creates a relationship between the tables.

The tables, rows, columns, and relationships between them is called a logical schema. With relational databases, a schema is fixed. After the database is operational, it becomes difficult to change the schema. Because of this, most of the data modeling is done up front before the database is active.

### Relational database management system

With a relational database management system (RDBMS), you can create, update, and administer a relational database. Some common examples of RDBMSs include the following:

- MySQL
- PostgresQL
- Oracle
- Microsoft SQL Server
- Amazon Aurora

### Relational database use cases

Much of the world runs on relational databases. In fact, they’re at the core of many mission-critical applications, some of which you might use in your day-to-day life.

1. Applications that have a fixed schema
**These are applications that have a fixed schema** and don't change often. An example is a lift-and-shift application that lifts an app from on-premises and shifts it to the cloud, with little or no modifications.

2. Applications that need persistent storage
**These are applications that need persistent storage** and follow the ACID principle, such as:

- Enterprise resource planning (ERP) applications
- Customer relationship management (CRM) applications
- Commerce and financial applications

### Choose between unmanaged and managed databases

If you want to trade your on-premises database for a relational database on AWS, you first need to select how you want to run it—managed or unmanaged. Managed services and unmanaged services are handled similar to the shared responsibility model. The shared responsibility model distinguishes between AWS security responsibilities and the customer’s security responsibilities. Likewise, managed compared to unmanaged can be understood as a trade-off between convenience and control.

### Unmanaged databases

If you operate a relational database on premises, you are responsible for all aspects of operation. This includes data center security and electricity, host machines management, database management, query optimization, and customer data management. You are responsible for absolutely everything, which means you have control over absolutely everything.

Now, suppose you want to shift some of the work to AWS by running your relational database on Amazon Elastic Compute Cloud (Amazon EC2). If you host a database on Amazon EC2, AWS implements and maintains the physical infrastructure and hardware and installs the EC2 instance operating system (OS). However, you are still responsible for managing the EC2 instance, managing the database on that host, optimizing queries, and managing customer data.

This is called an unmanaged database option. In this option, AWS is responsible for and has control over the hardware and underlying infrastructure. You are responsible for and have control over management of the host and database.

![Shared Responsibility](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/uCmFA3cGvGhVrDs3_qnA3DCLuIj69t7zG.png)

You are responsible for everything in a database hosted on-premises. AWS takes on more of that responsibility in databases hosted in Amazon EC2.

### Managed databases

To shift more of the work to AWS, you can use a managed database service. These services provide the setup of both the EC2 instance and the database, and they provide systems for high availability, scalability, patching, and backups. However, in this model, you’re still responsible for database tuning, query optimization, and ensuring that your customer data is secure. This option provides the ultimate convenience but the least amount of control compared to the two previous options.

![Shared Responsibility](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/I4Jv2LIrmyw-EbeF_AOuKIausIFuSmauW.png)

#### Resources 

For more information, see the following resources:

- AWS website: [What Is a Relational Database?](https://aws.amazon.com/relational-database/)
- AWS website: [AWS Cloud Databases](https://aws.amazon.com/products/databases/)

## Amazon RDS
- With Amazon Relational Database Service (Amazon RDS), you can focus on tasks that differentiate your application instead of infrastructure-related tasks, like provisioning, patching, scaling, and restoring.

### Amazon RDS overview
![Amazon RDS](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/HlHSB82N6e6RWwTA_YflAxuhYwZDS5mdn.png)

Amazon RDS is a managed database service customers can use to create and manage relational databases in the cloud without the operational burden of traditional database management. For example, imagine you sell healthcare equipment, and your goal is to be the number-one seller on the West Coast of the United States. Building a database doesn’t directly help you achieve that goal. However, having a database is a necessary component to achieving that goal. 

With Amazon RDS, you can offload some of the unrelated work of creating and managing a database. You can focus on the tasks that differentiate your application, instead of focusing on infrastructure-related tasks, like provisioning, patching, scaling, and restoring.

Amazon RDS supports most of the popular RDBMSs, ranging from commercial options to open-source options and even a specific AWS option. Supported Amazon RDS engines include the following:

- **Commercial**: Oracle, SQL Server
- **Open source**: MySQL, PostgreSQL, MariaDB
- **Cloud native**: Aurora 

![Engine Types](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/9XHpI14MKiP6Tcky_ltRQnkinbsiFRUn1.png)

### Database instances

Just like the databases you build and manage yourself, Amazon RDS is built from compute and storage. The compute portion is called the database (DB) instance, which runs the DB engine. Depending on the engine selected, the instance will have different supported features and configurations. A DB instance can contain multiple databases with the same engine, and each DB can contain multiple tables.

Underneath the DB instance is an EC2 instance. However, this instance is managed through the Amazon RDS console instead of the Amazon EC2 console. When you create your DB instance, you choose the instance type and size. The DB instance class you choose affects how much processing power and memory it has.

### Storage on Amazon RDS

The storage portion of DB instances for Amazon RDS use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage. This includes MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server. 

When using Aurora, data is stored in cluster volumes, which are single, virtual volumes that use solid-state drives (SSDs). A cluster volume contains copies of your data across three Availability Zones in a single AWS Region. For nonpersistent, temporary files, Aurora uses local storage.

Amazon RDS provides three storage types: General Purpose SSD (also called gp2 and gp3), Provisioned IOPS SSD (also called io1), and Magnetic (also called standard). They differ in performance characteristics and price, which means you can tailor your storage performance and cost to the needs of your database workload.

### Amazon RDS in an Amazon Virtual Private Cloud

When you create a DB instance, you select the Amazon Virtual Private Cloud (Amazon VPC) your databases will live in. Then, you select the subnets that will be designated for your DB. This is called a DB subnet group, and it has at least two Availability Zones in its Region. The subnets in a DB subnet group should be private, so they don’t have a route to the internet gateway. This ensures that your DB instance, and the data inside it, can be reached only by the application backend.

Access to the DB instance can be restricted further by using network access control lists (network ACLs) and security groups. With these firewalls, you can control, at a granular level, the type of traffic you want to provide access into your database.

Using these controls provides layers of security for your infrastructure. It reinforces that only the backend instances have access to the database.

### Redundancy with Amazon RDS Multi-AZ

In an Amazon RDS Multi-AZ deployment, Amazon RDS creates a redundant copy of your database in another Availability Zone. You end up with two copies of your database—a primary copy in a subnet in one Availability Zone and a standby copy in a subnet in a second Availability Zone.

The primary copy of your database provides access to your data so that applications can query and display the information. The data in the primary copy is synchronously replicated to the standby copy. The standby copy is not considered an active database, and it does not get queried by applications.

![Redundancy](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/522441/v2.0/assets/HB0-VuviZSSRDWxW_427K0gUGe81kqVaq.png)

To improve availability, Amazon RDS Multi-AZ ensures that you have two copies of your database running and that one of them is in the primary role. If an availability issue arises, such as the primary database loses connectivity, Amazon RDS initiates an automatic failover.

When you create a DB instance, a Domain Name System (DNS) name is provided. AWS uses that DNS name to fail over to the standby database. In an automatic failover, the standby database is promoted to the primary role, and queries are redirected to the new primary database.

To help ensure that you don't lose Multi-AZ configuration, there are two ways you can create a new standby database. They are as follows:

- Demote the previous primary to standby if it's still up and running.
- Stand up a new standby DB instance.

The reason you can select multiple subnets for an Amazon RDS database is because of the Multi-AZ configuration. You will want to ensure that you have subnets in different Availability Zones for your primary and standby copies.

### Amazon RDS security

When it comes to security in Amazon RDS, you have control over managing access to your Amazon RDS resources, such as your databases on a DB instance. How you manage access will depend on the tasks you or other users need to perform in Amazon RDS. Network ACLs and security groups help users dictate the flow of traffic. If you want to restrict the actions and resources others can access, you can use AWS Identity and Access Management (IAM) policies. 

#### Resources

For more information, see the following resources:

- AWS website: [Amazon RDS](https://aws.amazon.com/rds/)
- AWS user guide: [Configuring an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_RDS_Configuring.html)
- AWS user guide: [Backing up and restoring an Amazon RDS DB instance](https://docs.aws.amazon.com//AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)
- AWS user guide: [Security in Amazon RDS](https://docs.aws.amazon.com//AmazonRDS/latest/UserGuide/UsingWithRDS.html)

### Purpose-built databases for all application needs

We covered Amazon RDS and relational databases in the previous lesson, and for a long time, relational databases were the default option. They were widely used in nearly all applications. A relational database is like a multi-tool. It can do many things, but it is not perfectly suited to any one particular task. It might not always be the best choice for your business needs. 

The one-size-fits-all approach of using a relational database for everything no longer works. Over the past few decades, there has been a shift in the database landscape, and this shift has led to the rise of purpose-built databases. Developers can consider the needs of their application and choose a database that will fit those needs. 

AWS offers a broad and deep portfolio of purpose-built databases that support diverse data models. Customers can use them to build data-driven, highly scalable, distributed applications. You can pick the best database to solve a specific problem and break away from restrictive commercial databases. You can focus on building applications that meet the needs of your organization.

### Amazon DynamoDB

DynamoDB is a fully managed NoSQL database that provides fast, consistent performance at any scale. It has a flexible billing model, tight integration with infrastructure as code (IaC), and a hands-off operational model. DynamoDB has become the database of choice for two categories of applications: high-scale applications and serverless applications. Although DynamoDB is the database of choice for high-scale and serverless applications, it can work for nearly all online transaction processing (OLTP) application workloads.

### Amazon ElastiCache 

ElastiCache is a fully managed, in-memory caching solution. It provides support for two open-source, in-memory cache engines: Redis and Memcached. You aren’t responsible for instance failovers, backups and restores, or software upgrades.

### Amazon MemoryDB for Redis

MemoryDB is a Redis-compatible, durable, in-memory database service that delivers ultra-fast performance. With MemoryDB, you can achieve microsecond read latency, single-digit millisecond write latency, high throughput, and Multi-AZ durability for modern applications, like those built with microservices architectures. You can use MemoryDB as a fully managed, primary database to build high-performance applications. You do not need to separately manage a cache, durable database, or the required underlying infrastructure.

### Amazon DocumentDB (with MongoDB compatibility)

Amazon DocumentDB is a fully managed document database from AWS. A document database is a type of NoSQL database you can use to store and query rich documents in your application. These types of databases work well for the following use cases: content management systems, profile management, and web and mobile applications. Amazon DocumentDB has API compatibility with MongoDB. This means you can use popular open-source libraries to interact with Amazon DocumentDB, or you can migrate existing databases to Amazon DocumentDB with minimal hassle.

### Amazon Keyspaces (for Apache Cassandra)

Amazon Keyspaces is a scalable, highly available, and managed Apache Cassandra compatible database service. Apache Cassandra is a popular option for high-scale applications that need top-tier performance. Amazon Keyspaces is a good option for high-volume applications with straightforward access patterns. With Amazon Keyspaces, you can run your Cassandra workloads on AWS using the same Cassandra Query Language (CQL) code, Apache 2.0 licensed drivers, and tools that you use today.

### Amazon Neptune

Neptune is a fully managed graph database offered by AWS. A graph database is a good choice for highly connected data with a rich variety of relationships. Companies often use graph databases for recommendation engines, fraud detection, and knowledge graphs.

### Amazon Timestream

Timestream is a fast, scalable, and serverless time series database service for Internet of Things (IoT) and operational applications. It makes it easy to store and analyze trillions of events per day up to 1,000 times faster and for as little as one-tenth of the cost of relational databases. Time series data is a sequence of data points recorded over a time interval. It is used for measuring events that change over time, such as stock prices over time or temperature measurements over time.

### Amazon Quantum Ledger Database (Amazon QLDB)

With traditional databases, you can overwrite or delete data, so developers use techniques, such as audit tables and audit trails to help track data lineage. These approaches can be difficult to scale and put the burden of ensuring that all data is recorded on the application developer. Amazon QLDB is a purpose-built ledger database that provides a complete and cryptographically verifiable history of all changes made to your application data.

#### Resources

For more information, see the following resource:

- AWS website: [AWS Cloud Databases](https://aws.amazon.com/products/databases/)

## Amazon DynamoDB
- With Amazon DynamoDB, you have a fully managed service that handles the operations work.

### DynamoDB overview

DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. With DynamoDB, you can offload the administrative burdens of operating and scaling a distributed database. You don't need to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.

With DynamoDB, you can do the following:
- Create database tables that can store and retrieve any amount of data and serve any level of request traffic. 
- Scale up or scale down your tables' throughput capacity without downtime or performance degradation. 
- Monitor resource usage and performance metrics using the AWS Management Console.

DynamoDB automatically spreads the data and traffic for your tables over a sufficient number of servers to handle your throughput and storage requirements. It does this while maintaining consistent, fast performance. All your data is stored on SSDs and is automatically replicated across multiple Availability Zones in a Region, providing built-in high availability and data durability.

### DynamoDB core components

In DynamoDB, tables, items, and attributes are the core components that you work with. A table is a collection of items, and each item is a collection of attributes. DynamoDB uses primary keys to uniquely identify each item in a table and secondary indexes to provide more querying flexibility.

![DynamoDB](images/aws/dynamodb/ZQUVJkGO9lMfwNnQ_Cvst9zY2nCARpXZi.png)

### DynamoDB use cases

DynamoDB is a fully managed service that handles the operations work. You can offload the administrative burdens of operating and scaling distributed databases to AWS.

You might want to consider using DynamoDB in the following circumstances:

- You are experiencing scalability problems with other traditional database systems.
- You are actively engaged in developing an application or service.
- You are working with an OLTP workload.
- You care deploying a mission-critical application that must be highly available at all times without manual intervention.
- You require a high level of data durability, regardless of your backup-and-restore strategy.

DynamoDB is used in a wide range of workloads because of its simplicity, from low-scale operations to ultrahigh-scale operations, such as those demanded by Amazon.com. 

#### Develop software applications
Build internet-scale applications supporting user-content metadata and caches that require high concurrency and connections for millions of users and millions of requests per second.

#### Create media metadata stores
Scale throughput and concurrency for analysis of media and entertainment workloads, such as real-time video streaming and interactive content. Deliver lower latency with multi-Region replication across Regions.

#### Scale gaming platforms
Focus on driving innovation with no operational overhead. Build out your game platform with player data, session history, and leaderboards for millions of concurrent users.

#### Deliver seamless retail experiences
Use design patterns for deploying shopping carts, workflow engines, inventory tracking, and customer profiles. DynamoDB supports high-traffic, extreme-scaled events and can handle millions of queries per second.

### DynamoDB security

DynamoDB provides a number of security features to consider as you develop and implement your own security policies. They include the following:

- DynamoDB provides a highly durable storage infrastructure designed for mission-critical and primary data storage. Data is redundantly stored on multiple devices across multiple facilities in a DynamoDB Region.  
- All user data stored in DynamoDB is fully encrypted at rest. DynamoDB encryption at rest provides enhanced security by encrypting all your data at rest using encryption keys stored in AWS Key Management Service (AWS KMS).
- IAM administrators control who can be authenticated and authorized to use DynamoDB resources. You can use IAM to manage access permissions and implement security policies.
- As a managed service, DynamoDB is protected by the AWS global network security procedures.

#### Resources

For more information, see the following resources:

- AWS website: [Amazon DynamoDB](https://aws.amazon.com/dynamodb/#)
- AWS developer guide: [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- AWS blog: [AWS Database Blog](https://aws.amazon.com/blogs/database/how-to-determine-if-amazon-dynamodb-is-appropriate-for-your-needs-and-then-plan-your-migration/)


