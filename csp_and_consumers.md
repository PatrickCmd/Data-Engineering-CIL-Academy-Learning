# Cloud Service Providers and Consumers

Cloud service providers and consumers are two essential players in the cloud computing ecosystem.

- **A cloud service provider (CSP)** is a company that provides cloud-based services and resources, such as computing power, storage, and applications, to businesses and individuals. CSPs can include large technology companies like Amazon Web Services, Microsoft Azure, and Google Cloud, as well as smaller, specialized providers.

- **Cloud consumers**, on the other hand, are the customers who use the services and resources provided by the CSPs. They may be businesses or individuals who use the cloud for a wide range of purposes, such as hosting websites, running applications, storing and processing data, or collaborating on projects.

## Resources
1. [Cloud Service Providers (CSPs) Explained](https://www.bmc.com/blogs/csp-cloud-service-providers/)
2. [AWS Vs Azure Vs GCP | Amazon Web Services Vs Microsoft Azure Vs Google Cloud Platform](https://www.youtube.com/watch?v=nrqmYvjHHJg)
3. [AWS vs Azure vs GCP | Amazon Web Services vs Microsoft Azure vs Google Cloud Platform | Intellipaat](https://www.youtube.com/watch?v=n24OBVGHufQ)
4. [Cloud consumer](https://itlaw.fandom.com/wiki/Cloud_consumer)


## Azure Fundamentals
- [Introduction to Azure Fundamentals](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-fundamentals/)
- [Microsoft Azure Fundamentals: Describe cloud concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/)
-[Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)
- [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)
- [Azure Fundamentals: Describe Azure management and governance](https://learn.microsoft.com/en-gb/training/paths/describe-azure-management-governance/)
- [What Is Azure? | Microsoft Azure Tutorial For Beginners | Microsoft Azure Training | Simplilearn](https://www.youtube.com/watch?v=3Arj5zlUPG4)
- [Why Choose Azure Over AWS](https://www.youtube.com/watch?v=XyO2PPf47eY)


## GCP Digital Foundations
- [Digital Transformation with Google Cloud](https://www.cloudskillsboost.google/course_templates/266)
- [Innovating with Data and Google Cloud](https://www.cloudskillsboost.google/course_templates/267)
- [Infrastructure and Application Modernization with Google Cloud](https://www.cloudskillsboost.google/course_templates/265)
- [Understanding Google Cloud Security and Operations](https://www.cloudskillsboost.google/course_templates/271)


## AWS Fundamentals

### AWS categories of services
The following is a list of the AWS categories of services.

- Analytics
- Cost Management
- Internet of Things
- Storage
- Application Integration
- Customer Engagement
- Machine Learning
- Robotics
- AR and VR
- Database
- Management and Governance
- Satellite
- Blockchain
- Developer Tools
- Media Services
- Networking and Content Delivery
- Business Applications
- End User Computing
- Migration and Transfer
- Security, Identity, and Compliance
- Compute
- Game Tech
- Mobile

### AWS core service

Core service areas:

- Compute
- Storage
- Databases
- Networking
- Security

### AWS Global Infrastructure
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

### Compute
### [Compute Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)

- [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) 
    - Provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. In the compute area, there are various options for the types of resources you might want to launch, such as the following:

        - Virtual machines
        - Containers
        - Batch processing compute resources
        - Serverless compute
    - [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
- [Serverless - AWS Lambda](https://docs.aws.amazon.com/lambda/latest/operatorguide/lambda-event-driven-paradigm.html): is a fully managed serverless compute service.
- [Containers](https://aws.amazon.com/containers/)
    - Containers orchestration
        - [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) and [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) are the container orchestrating services that help you schedule, maintain, and scale the fleet of nodes running your containers. They also give you a centralized way of monitoring and controlling how you want your containers launched.
        - Amazon ECS is an AWS container orchestration tool giving you seamless control over your containerized application.
        - Amazon EKS is a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications. 

### Storage
- [Amazon Simple Storage Service - Amazon S3](https://aws.amazon.com/s3/?nc=sn&loc=0): Amazon Simple Storage Service (Amazon S3) is a fully managed, serverless, low-cost, object-level storage service. With Amazon S3, you store unlimited amounts of data (with different formats) on AWS. Amazon S3 offers multiple storage options.
    - [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)
    - [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/index.html?nc2=h_ql_doc_s3)
- [Amazon Elastic Block Store (Amazon EBS)]()

    Amazon EBS has the following benefits:
        - Persistent network-attached block storage for instances that can persist even after the EC2 instance to which this storage is attached is terminated
        - Different drive types
        - Scalable 
        - Pay only for what you provision
        - Snapshot functionality 
        - Encryption available to enhance security
    - [Amazon EBS Volume types](https://aws.amazon.com/ebs/volume-types/)

- [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/?c=s&sec=srv)
    - [Amazon Elastic File Systems Overview](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
        - When you need a serverless shared file system, you can use Amazon Elastic File System (Amazon EFS).
        - Amazon EFS provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance.
        - With Amazon EFS, you can build high performing and cost-optimized file systems on AWS benefitting from the built-in-elasticity, durability, and availability.

- [Amazon FSx](https://aws.amazon.com/fsx/)
    - Amazon FSx makes it easy and cost effective to launch, run, and scale feature-rich, high-performance file systems in the cloud. 
    - It supports a wide range of workloads with its reliability, security, scalability, and broad set of capabilities. 
    - Amazon FSx is built on the latest AWS compute, networking, and disk technologies to provide high performance and lower total cost of ownership (TCO). And as a fully managed service, it handles hardware provisioning, patching, and backups—freeing you up to focus on your applications, your end users, and your business.
    - You can choose between four widely used file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre.

### Databases
- [AWS Cloud Databases](https://aws.amazon.com/products/databases/)

#### Explore AWS services grouped by database type in more detail. 
- Relational database
    - [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
        - It is compatible with MySQL, so you can run those engines with increased performance on AWS.
        - The database supports High availability and durability, and you can run it serverless. This takes care of automatically scaling the resources for you.
        - With Aurora, you also can run the database with multi-Regional replicas.
        - Performance and availability of commercial-grade databases at 1/10th the cost.
    - [Amazon RDS](https://aws.amazon.com/rds/)
        - You can choose Amazon Relational Database Service (Amazon RDS) to launch the database in the Multi-AZ configuration if you want to deploy it for high availability (HA).
        - The service will launch the primary and standby databases in different Availability Zones and set up synchronous replication of data and failover strategy. 
        - If the primary database goes down, the standby picks up the traffic.
    - [Managed relational database—Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
        - Amazon RDS is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.
        - Managed means you still have the power to decide how the database will be launched, but Amazon RDS will launch it for you. You can set up, operate, and scale a relational database in the cloud with just a few clicks. Amazon RDS is compatible with multiple engines, and you can use it to launch the Amazon Aurora database. 
        - Choose from seven popular engines: Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server.
    - [Amazon Redshift](https://aws.amazon.com/redshift/)
        - Amazon Redshift is a data warehouse service that provides benefits from columnar storage. 
        - With this approach, you can perform complex queries on your data, helping you run online analytical processing (OLAP) workloads.

- Key-value database 
    - [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
        - With DynamoDB, you can achieve single-digit millisecond performance at any scale.
        - It is a fully managed, serverless, nonrelational database.
        - DynamoDB is a great choice when you're looking for seamless database scalability. DynamoDB will automatically scale to meet demand.
        - DynamoDB is also an excellent choice for workloads that involve working with databases, flexible schemas, and high throughput (with many read/write requests). 
        - For example, using Amazon DynamoDB for running Leaderboard would be a good use case.

- In-memory database 
    - Amazon ElastiCache
        - Unlock microsecond latency 
        - Scalable caching service
    - Amazon MemoryDB for Redis
        - Compatible 
        - Durable

- Document database 
    - Amazon DocumentDB (with MongoDB compatibility)
        - Scale JSON workloads with ease
        - Use an enterprise-ready document database service compatible with MongoDB

- Wide column database 
    - Amazon Keyspaces
        - Scalable
        - Highly available 
        - Run your Apache Cassandra workloads

- Amazon Neptune AWS service (Graph database)
    - [Amazon Neptune](https://aws.amazon.com/neptune/)
        - Amazon Neptune is used for simplifying the setup and running of your graph databases. 
        - This helps you run databases aware of relationships between data. 
        - Amazon Neptune can be useful for fraud detection, social media, and similar applications.
        - Build applications that work with highly connected datasets. 

- Time Series database
    - Amazon Timestream
        - Fast
        - Scalable
        - Store and analyze trillions of events per day

- Ledger database
    - Amazon Quantum Ledger Database (Amazon QLDB)

        Provides logs that are as follows:

        - Transparent
        - Immutable
        - Cryptographically verifiable

### Networking
- [Amazon VPC](https://aws.amazon.com/vpc/)
    - Amazon VPC is your private network space you create to launch your resources in the AWS Cloud.
    - More than one VPC can be launched into your AWS accounts.
    - A private network that provides logical isolation for your workloads
        - This private network is logically isolated from other VPC or remote networks; for example, isolating development from testing.
        - You can control the traffic that can flow in and out of Amazon VPC and the resources launched within.
        - You can also control how to connect your VPC with other networks.
    - Custom access controls and security settings for your resource
        - You can use different VPCs to launch different workloads or stages or workloads if you want to benefit from such logical isolation.
        - You configure how the packets travel through the layers of your network.

- [Amazon Route 53](https://aws.amazon.com/route53/) is a highly available and scalable cloud DNS service.
    - [Route 53 Routing Policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
    - Route 53 has various benefits:
        - Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. 
        - You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.
        - DNS translates domain names into IP addresses.
        - With Route 53, you can purchase and manage domain names and configure DNS settings.      
        - Route 53 has multiple routing options.

- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
    - [Route 53 routing traffic to an ELB load balancer](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html)
    - Amazon Route 53 is a DNS service. Elastic Load Balancing (ELB) is the load balancing service. 
    - Elastic Load Balancing is a web service that improves an application's availability by distributing incoming traffic between two or more EC2 instances. 
    - ELB automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs).
    - It also serves as a single point of contact with your application. 
    - As a result, your end users do not need to be aware of how many machines your application is running on or all the details, such as the IP addresses of those machines.
        

## Cloud/DevOPs practice exercises
- [All Round Devops exercises](https://github.com/bregman-arie/devops-exercises)
- [AWS exercises](https://github.com/bregman-arie/devops-exercises/blob/master/topics/aws/README.md)

## The Cloud Resume Challenge
- [Cloud Resume Challenge](https://cloudresumechallenge.dev/)
