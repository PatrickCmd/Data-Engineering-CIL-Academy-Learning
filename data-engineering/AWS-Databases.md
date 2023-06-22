# Building with AWS Databases

## AWS Well-Architected Framework

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on Amazon Web Services (AWS). Using the AWS Well-Architected Framework helps you learn architectural best practices for designing and operating secure, reliable, efficient, cost-effective, and sustainable workloads in the AWS Cloud. It provides a way for you to consistently measure your architectures against best practices and identify areas for improvement. The process for reviewing an architecture is a constructive conversation about architectural decisions and is not an audit mechanism.

The AWS Well-Architected Framework describes key concepts, design principles, and architectural best practices for designing and running workloads in the cloud. By answering a few foundational questions, you will learn how well your architecture aligns with cloud best practices, gaining guidance for making improvements. The framework provides a consistent approach to evaluating systems against the qualities you expect from modern cloud-based systems and the changes that would be required to achieve those qualities. 

> For more information, view the AWS [**Well-Architected Framework whitepaper**](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

### General design principles

In a traditional IT environment, the team has to guess infrastructure needs and sometimes over-provision or under-provision for those needs. A small change could have cascading effects on the main system that prevents companies from experimenting and testing at scale. Investment made in the infrastructure gets frozen in time, even though the customers and market technology changes. Using the cloud eliminates most of these traditional concerns. The AWS Well-Architected Framework identifies a set of general design principles to facilitate good design in the cloud. 

1. **Stop guessing your capacity needs**

If you make a poor capacity decision when deploying a workload, you might end up sitting on expensive idle resources or dealing with the performance implications of limited capacity. With cloud computing, these problems can go away. You can use as much or as little capacity as you need and scale up and down (or in and out) automatically. You can monitor your workloads and capacities and make those changes within minutes after receiving alarms or notifications when certain processes reach thresholds.

2. **Test systems at production scale**

In the cloud, it is much more cost effective to simulate your production environment than doing this on premises. Always run full tests at production scale and then decommission those resources after the test. Remember, in most cases, you are only paying for the time in which things are running.

3. **Automate to make architectural experimentation easier**

Computers are faster, dispassionate, and more consistent than humans. For this reason, you should automate whenever possible. With automation, you can create and replicate your workloads at low cost and avoid the expense of manual effort. You can track changes to your automation, audit the impact, and revert to previous parameters when necessary. The cloud makes decisions less stressful, because they are rarely decisions that can't be undone.

4. **Allow for evolutionary architecture**

Architectural decisions were often implemented as static, one-time events, with a few major versions of a system during its lifetime. As a business and its context continue to evolve, these initial decisions might hinder the system's ability to deliver changing business requirements. In the cloud, the capability to automate and test on demand lowers the risk of impact from design changes. This lets systems evolve over time so that businesses can take advantage of innovations as a standard practice.

5. **Drive architecture using data**

In the cloud, you can collect data on how your architectural choices affect the behavior of your workload. This facilitates making fact-based decisions on how to improve your workload. Your cloud infrastructure is code, so you can use that data to inform your architecture choices and improvements over time. Depending on what your data is telling you, you can make adjustments within your code. Unlike with traditional on-premises workloads, you don't have to make these assumptions without data to support it.

6. **Improve through game days**

Test how your architecture and processes perform by regularly scheduling game days to simulate events in production. This will help you understand where improvements can be made and can help develop organizational experience in dealing with events.


### The six pillars

The AWS Well-Architected Framework and its six pillars provide a lens to design and evaluate workloads in the cloud. Each of these pillars and their associated design principles are significant in building in the cloud. 

- Operational Excellence
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability
- Security

The AWS Well-Architected Framework provides guidance on building and operating reliable, secure, efficient, and cost-effective systems in the Amazon Web Services (AWS) cloud. The framework consists of six pillars, which are key areas of focus when designing and evaluating architectures. Let's explore each pillar:

1. Operational Excellence:
This pillar focuses on optimizing operational processes and procedures to deliver business value efficiently. It involves continuous improvement, defining operational standards, managing workload and resources, monitoring, and automating processes.

Here are the five operational excellence design principles:

- Perform operations as code:
Performing operations as code involves treating infrastructure, configurations, and operational procedures as version-controlled artifacts. It emphasizes the use of automation and infrastructure-as-code tools to provision and manage resources. By representing operational procedures as code, organizations can apply software engineering practices to operations, enabling reproducibility, scalability, and consistency.

- Annotate documentation:
Documentation is crucial for effective operations. The principle of annotating documentation encourages maintaining up-to-date, accurate, and detailed documentation that includes system architectures, operational procedures, dependencies, and key information about the environment. By documenting critical aspects of the system, organizations can improve operational efficiency, enable knowledge sharing, and facilitate troubleshooting and incident response.

- Make frequent, small, reversible changes:
Making frequent, small, and reversible changes refers to adopting an agile and iterative approach to system changes. This principle suggests that organizations should avoid large, infrequent changes that carry higher risks and instead focus on making smaller, incremental changes. By implementing changes in smaller increments, organizations can reduce the impact of failures, gain faster feedback, and improve the overall stability and reliability of the system.

- Refine operations procedures frequently:
Refining operations procedures frequently encourages organizations to continuously review and improve their operational processes. It involves analyzing operational data, monitoring system performance, and collecting feedback from operators and users. By regularly reviewing and refining operational procedures, organizations can identify areas for improvement, eliminate bottlenecks, optimize processes, and enhance the overall efficiency and effectiveness of operations.

- Anticipate failure:
Anticipating failure involves proactively identifying potential points of failure and designing systems to be resilient and fault-tolerant. This principle emphasizes the use of architectural patterns and practices that can handle failures gracefully. It includes techniques such as redundancy, fault isolation, and automatic recovery. By anticipating failure and implementing resilient architectures, organizations can minimize the impact of failures, improve system availability, and enhance the overall reliability of their systems.

By following these operational excellence design principles, organizations can optimize their operational processes, improve system reliability, and enhance the efficiency of their cloud-based systems on AWS.

2. Security:
Security is a top priority for any system. This pillar emphasizes the implementation of appropriate security measures to protect data, systems, and assets. It covers identity and access management, data protection, detective controls, infrastructure protection, and incident response.

Security design principles are a set of guidelines provided by the AWS Well-Architected Framework to help organizations build and maintain secure systems in the cloud. These principles focus on protecting data, assets, and infrastructure, and promoting a robust security posture. Here are the five security design principles:

- Implement a strong identity foundation:
Implementing a strong identity foundation involves establishing secure authentication and authorization mechanisms. Organizations should adopt AWS Identity and Access Management (IAM) to manage user identities, define granular access controls, and enforce the principle of least privilege. By implementing strong identity and access management practices, organizations can ensure that only authorized individuals and services can access resources and minimize the risk of unauthorized access.

- Enable traceability:
Enabling traceability involves implementing comprehensive logging, monitoring, and auditing capabilities. Organizations should leverage AWS CloudTrail, Amazon CloudWatch, and other logging services to track user activities, system events, and API calls. By enabling traceability, organizations can detect and investigate security incidents, identify suspicious behavior, and ensure accountability and compliance.

- Apply security at all layers:
Applying security at all layers refers to implementing multiple layers of security controls to protect systems and data. Organizations should employ a defense-in-depth approach, using a combination of network security, encryption, web application firewalls, and intrusion detection and prevention systems. By implementing security controls at various layers, organizations can mitigate risks, detect and prevent attacks, and maintain the confidentiality and integrity of their systems.

- Automate security best practices:
Automating security best practices involves using automation and scripting to enforce security policies, configuration standards, and security controls. Organizations should utilize tools like AWS CloudFormation and AWS Config to automatically provision resources with predefined security configurations. By automating security practices, organizations can reduce human error, enforce consistent security controls, and ensure that security measures are consistently applied across their environments.

- Protect data in transit and at rest:
Protecting data in transit and at rest emphasizes the need for strong encryption mechanisms. Organizations should use Transport Layer Security (TLS) for secure communication over the network and encryption services like AWS Key Management Service (KMS) to encrypt sensitive data at rest. By encrypting data in transit and at rest, organizations can protect against unauthorized access and ensure the confidentiality and integrity of their data.

By following these security design principles, organizations can establish a robust security foundation for their cloud-based systems. By implementing strong identity management, enabling traceability, applying security at all layers, automating security practices, and protecting data through encryption, organizations can reduce security risks, safeguard their assets and data, and maintain a secure environment on AWS.

3. Reliability:
Reliability ensures that a system operates as expected, without interruption, and can recover from failures. This pillar emphasizes the need for planning, preparing, and managing events such as outages and disasters. It includes aspects like system resiliency, fault tolerance, backup and restore mechanisms, and service continuity.

Reliability design principles are a set of guidelines provided by the AWS Well-Architected Framework to help organizations build and operate reliable systems in the cloud. These principles focus on ensuring system availability, fault tolerance, and the ability to recover from failures. Here are the five reliability design principles:

- Test recovery procedures:
Testing recovery procedures involves simulating failure scenarios and validating the ability of the system to recover. Organizations should regularly test backup and restore processes, disaster recovery plans, and system resilience mechanisms. By testing recovery procedures, organizations can identify and address potential issues, validate the effectiveness of their recovery strategies, and increase confidence in the system's ability to withstand failures.

- Automatically recover from failure:
Automatically recovering from failure emphasizes the use of automated mechanisms to detect and recover from failures without manual intervention. Organizations should implement self-healing capabilities, automated monitoring, and automated scaling to ensure that the system can automatically detect failures and take appropriate actions to restore normal operation. By automating recovery processes, organizations can minimize downtime, reduce the impact of failures, and improve the overall system availability.

- Scale horizontally to increase aggregate system availability:
Scaling horizontally involves distributing the workload across multiple instances or resources to increase the system's availability. Instead of relying on a single instance or resource, organizations should design systems that can dynamically scale out by adding more instances or resources as demand increases. By distributing the workload, organizations can handle increased traffic, improve fault tolerance, and enhance the overall system availability.

- Stop guessing capacity needs:
Stop guessing capacity needs suggests that organizations should avoid overprovisioning or underprovisioning resources based on guesswork. Instead, they should adopt a data-driven approach to capacity planning. By using monitoring and analytics tools, organizations can collect data on resource utilization, performance metrics, and user behavior to make informed decisions about resource allocation and scaling. By accurately predicting capacity needs, organizations can optimize resource usage, avoid unnecessary costs, and ensure that the system can handle workload fluctuations.

- Manage change in automation:
Managing change in automation emphasizes the importance of automating change management processes. Organizations should use automation tools and processes to manage changes to the system, including updates, patches, configuration changes, and deployments. By automating change management, organizations can reduce the risk of human error, ensure consistency across environments, and improve the reliability of the system.

By following these reliability design principles, organizations can build resilient and fault-tolerant systems in the cloud, ensuring high availability, quick recovery from failures, and the ability to handle changes and fluctuations in workload.

4. Performance Efficiency:
This pillar focuses on using computing resources efficiently to meet system requirements and scale as needed. It involves selecting the right resource types, optimizing workload performance, monitoring resource utilization, and implementing elastic scaling to handle varying demand.

Performance efficiency design principles are a set of guidelines provided by the AWS Well-Architected Framework to help organizations optimize the performance of their systems in terms of resource utilization, scalability, and responsiveness. These principles focus on selecting the right resources, designing efficient architectures, and effectively managing workloads. Here are the five performance efficiency design principles:

- Democratize advanced technologies:
Democratizing advanced technologies involves leveraging the capabilities of managed services, automation, and advanced tools provided by AWS. Organizations should adopt cloud-native services and features to offload undifferentiated heavy lifting, reduce complexity, and benefit from AWS's continuous innovation. By using managed services and advanced technologies, organizations can focus on value-added activities and accelerate the development and deployment of their applications.

- Go global in minutes:
Going global in minutes refers to designing systems that can scale and operate globally with minimal effort. Organizations should design architectures that leverage AWS's global infrastructure to distribute workloads across multiple regions and availability zones. By utilizing AWS's global network, organizations can provide low-latency access to users in different geographical regions, improve fault tolerance, and enhance the responsiveness and scalability of their systems.

- Use serverless architectures:
Using serverless architectures involves leveraging AWS Lambda and other serverless computing services to build scalable, event-driven applications. Organizations should design systems that can execute code on-demand, eliminating the need for provisioning and managing servers. By adopting serverless architectures, organizations can reduce operational overhead, improve resource utilization, and achieve automatic scaling based on workload demands.

- Experiment more often:
Experimenting more often encourages organizations to adopt a culture of continuous experimentation and innovation. Organizations should create environments that allow for quick and low-cost experimentation, such as using AWS's sandbox accounts or isolated development environments. By promoting a culture of experimentation, organizations can encourage innovation, test new ideas, validate assumptions, and improve the overall performance and efficiency of their systems.

- Mechanical sympathy:
Mechanical sympathy refers to designing systems that are aligned with the characteristics and capabilities of the underlying infrastructure. Organizations should understand the performance characteristics of AWS services and underlying components to design architectures that leverage their strengths. By considering the behavior and limitations of the underlying infrastructure, organizations can optimize resource utilization, reduce latency, and improve the overall performance and efficiency of their systems.

By following these performance efficiency design principles, organizations can optimize the performance of their systems on AWS, achieve efficient resource utilization, and ensure scalability and responsiveness to meet their business needs.

5. Cost Optimization:
Cost optimization aims to achieve the desired outcomes at the lowest possible cost. This pillar involves understanding and managing costs, making informed decisions about resource selection, monitoring usage, and implementing cost-effective solutions. It also includes strategies like rightsizing resources, leveraging discounts, and analyzing spending patterns.

Cost optimization design principles are a set of guidelines provided by the AWS Well-Architected Framework to help organizations optimize costs and maximize the value they derive from their cloud-based systems. These principles focus on understanding and managing costs, making informed decisions about resource selection, and continuously optimizing spending. Here are the five cost optimization design principles:

- Adopt a consumption model:
Adopting a consumption model involves paying only for the resources and services actually consumed. Organizations should align resource allocation with demand, leveraging services like AWS Lambda and Amazon S3 to pay for actual usage. By adopting a consumption model, organizations can optimize costs by eliminating overprovisioning and paying only for what they use.

- Measure overall efficiency:
Measuring overall efficiency encourages organizations to continuously monitor and optimize resource utilization. By using AWS monitoring and analytics tools, organizations can gain insights into resource usage, identify inefficiencies, and optimize resource allocation. This principle emphasizes the importance of analyzing cost and performance metrics to identify areas for improvement and achieve cost-effective resource utilization.

- Stop spending money on undifferentiated heavy lifting:
Organizations should avoid spending money on undifferentiated heavy lifting, which refers to activities that do not directly contribute to their core business value. By utilizing managed services and automation provided by AWS, organizations can offload operational tasks and focus on higher-value activities. This principle encourages organizations to leverage AWS's managed services to reduce operational costs and enhance productivity.

- Analyze and attribute expenditure:
Analyzing and attributing expenditure involves tracking costs and attributing them to specific resources, projects, or teams. Organizations should implement cost allocation tags and use AWS Cost Explorer and other cost management tools to analyze and allocate costs accurately. By understanding cost drivers and allocating expenses effectively, organizations can identify cost-saving opportunities, optimize resource allocation, and make informed decisions about resource usage.

- Use managed services to reduce cost of ownership:
Using managed services helps organizations reduce the cost of ownership by leveraging AWS's expertise and economies of scale. Organizations should evaluate and adopt managed services for database management, analytics, machine learning, and other capabilities instead of building and maintaining their own infrastructure. By using managed services, organizations can reduce infrastructure management costs, increase operational efficiency, and benefit from cost-effective solutions.

By following these cost optimization design principles, organizations can optimize their costs on AWS, achieve better resource utilization, and ensure that their spending aligns with business goals. By continuously monitoring and optimizing costs, organizations can maximize the value they derive from their cloud-based systems while minimizing unnecessary expenses.

6. Sustainability:
Sustainability design principles refer to guidelines provided by the AWS Well-Architected Framework that aim to promote environmentally responsible practices and reduce the carbon footprint of cloud-based systems. These principles focus on optimizing resource usage, minimizing waste, and adopting sustainable practices. Here are the four sustainability design principles:

- Efficiently use computing resources:
Efficiently using computing resources involves optimizing resource utilization to minimize energy consumption and waste. Organizations should implement strategies like rightsizing instances, leveraging auto-scaling to match demand, and using serverless architectures to eliminate idle resource usage. By efficiently using computing resources, organizations can reduce energy consumption, lower costs, and minimize the environmental impact of their systems.

- Enable efficient data storage and processing:
Enabling efficient data storage and processing emphasizes the importance of optimizing data management practices. Organizations should implement data compression techniques, utilize efficient data storage services like Amazon S3 Intelligent-Tiering, and leverage serverless computing for data processing. By reducing data storage requirements and optimizing data processing workflows, organizations can minimize energy consumption and contribute to a more sustainable environment.

- Design for resiliency and durability:
Designing for resiliency and durability involves implementing architectures that can withstand failures and reduce the need for resource-intensive recovery operations. Organizations should leverage AWS's highly durable services, like Amazon S3 for object storage, and design for fault tolerance and redundancy. By building resilient and durable architectures, organizations can minimize data loss, decrease recovery time, and reduce the energy consumed during failure scenarios.

- Use renewable energy sources:
Using renewable energy sources encourages organizations to power their cloud-based systems with renewable energy. AWS provides regions that are powered by renewable energy sources, such as wind and solar power. Organizations can choose to deploy their systems in these regions to reduce the carbon footprint associated with their operations. By leveraging renewable energy sources, organizations can support sustainability efforts and contribute to a greener and more sustainable cloud infrastructure.

By following these sustainability design principles, organizations can design and operate cloud-based systems that are more environmentally friendly and contribute to sustainable practices. By optimizing resource usage, implementing efficient data management strategies, designing for resiliency, and using renewable energy sources, organizations can reduce their environmental impact and support a more sustainable future.

7. Well-Architected Framework Review:
This pillar represents the continuous improvement process. It encourages conducting regular reviews of architectures against the well-architected best practices, identifying areas for improvement, and implementing changes accordingly. It also emphasizes the importance of learning from operational events and using feedback to refine architectures over time.

These pillars provide a structured approach to design, implement, and operate systems on AWS. By addressing each pillar, organizations can build reliable, secure, and efficient architectures that align with best practices and help them achieve their business goals.

### AWS Well-Architected Tool?

The AWS Well-Architected Tool is a service offered which can be accessed within the console. It provides a consistent process for measuring your architecture using AWS best practices.

#### Benefits
- Get architectural guidance.
- Review your workloads consistently.
- Identify and implement improvements.
- Customize your review.


### Further reading
- [**AWS Well-Architected Framework webpage**](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc)
- [**AWS Well-Architected Framework whitepaper**](https://docs.aws.amazon.com/wellarchitected/latest/framework/wellarchitected-framework.pdf)
- [**AWS Well-Architected course**](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/2045/aws-well-architected)
- [**Amazon CloudWatch**](https://aws.amazon.com/cloudwatch/)
- [**Performance Insights**](https://aws.amazon.com/rds/performance-insights/)
- [**Amazon DynamoDB global tables**](https://aws.amazon.com/dynamodb/global-tables/)
- [**Amazon RDS Read Replicas**](https://aws.amazon.com/rds/features/read-replicas/)
- [**Disaster Recovery of Workloads on AWS: Recovery in the Cloud**](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [**Maintenance Window**](https://aws.amazon.com/premiumsupport/knowledge-center/rds-maintenance-window/)
- [**Performance Efficiency whitepaper**](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
- [**AWS Cloud Databases**](https://aws.amazon.com/products/databases/)
- [**Managing Throughput Capacity Automatically with DynamoDB Auto Scaling**](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)
- [**Amazon RDS Read Replicas**](https://aws.amazon.com/rds/features/read-replicas/)
- [**Cost Optimization Pillar - AWS Well-Architected Framework whitepaper**](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [**Sustainability Pillar - AWS Well-Architected Framework whitepaper**](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [**Security best practices in IAM**](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [**What is AWS Secrets Manager?**](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [**Security Pillar - AWS Well-Architected Framework whitepaper**](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [**Shared Responsibility**](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/shared-responsibility.html)
- [**Using SSL/TLS to encrypt a connection to a DB instance**](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)
- [**What is AWS Well-Architected Tool?**](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html)
- [**Navigating Best Practices with the AWS Well-Architected Tool**](https://www.youtube.com/watch?v=n4BTqappip0)


## Data Types

### Data source types

#### Structured
**Structured** data is often organized to support transactional and analytical applications. Structured data is most commonly stored in relational databases but can also be stored in nonrelational databases. This data source type is valuable because you can gain insight into overarching trends by efficiently running powerful data queries and analysis.

The example data below is structured transactional data.

|order_id |last_name |first_name  |order_total  |
|:--------|:---------|:-----------|:------------|
|123216 |Wolf |Nikki |62.26|
|599764 |Salazar |Carlos |45.79|

#### Semi-Structured
**Semi-structured** data can be just as predictable and organized as structured data. The difference is that semi-structured data is flexible and can be updated without the requirement to change the schema for every single record in a table. Semi-structured data allows a user to capture any data in any structure as data evolves and changes over time. Semi-structured data is often stored in nonrelational stores.

Examples of semi-structured data include XML, email, and JSON, which is shown below.

![Semi-structured data](images/semi-structured-data.png)

#### Unstructured

**Unstructured** data is not organized in any distinguishable or predefined manner. Common stores for unstructured data are nonrelational key-value databases. Unstructured data is full of irrelevant information, which means data needs to first be processed to perform any kind of meaningful analysis.

Examples of data considered to be unstructured are text messages, word processing documents, videos, photos, and other images. These files are not organized other than being placed into a file system, object store, or another repository such as a data lake.

![Unstructured data](images/unstructured-data.png)

## Database Services Offered by AWS

![AWS Database Offerings](images/aws-database-offerings.png)

### Amazon Relational Database Service (Amazon RDS)

Amazon Relational Database Service (Amazon RDS) is a web service that streamlines setting up, operating, and scaling relational databases in the cloud. With Amazon RDS, you can manage common database administration tasks such as operating system patching, database updates, and backups. Supported database engines include PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server.

### Amazon Aurora

Amazon Aurora is part of the managed database service Amazon RDS. Aurora is compatible with MySQL and PostgreSQL. With Aurora, you can combine the performance and availability of traditional enterprise databases with the simplicity and cost effectiveness of open-source databases.

### Amazon DynamoDB

Amazon DynamoDB is a fully managed key-value, nonrelational database service that provides fast and predictable performance with seamless scalability. With DynamoDB, you can create database tables that store and retrieve data and serve any level of request traffic. You can scale up or scale down your tables' throughput capacity without downtime or performance degradation.

### Amazon Keyspaces

Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra–compatible database service. With Amazon Keyspaces, you can run your Cassandra workloads on AWS using the same Cassandra application code and developer tools that you use today.

### Amazon DocumentDB

Amazon DocumentDB (with MongoDB compatibility) is designed from the ground up to give you the performance, scalability, and availability you need when operating mission-critical MongoDB workloads at scale. In Amazon DocumentDB, the storage and compute are decoupled, so each can scale independently.

### Amazon Neptune

Amazon Neptune is a fast, reliable, fully managed graph database service for applications that work with highly connected datasets. Neptune offers read replicas for high availability. You can create point-in-time copies and configure continuous backup to Amazon Simple Storage Service (Amazon S3) with replication across Availability Zones.

### Amazon Timestream

Amazon Timestream is a fast, scalable, fully managed time series database service for Internet of Things (IoT) and operational applications that facilitates storage and analysis of trillions of events per day at one-tenth the cost of relational databases.

### Amazon Quantum Ledger Database (Amazon QLDB)

Amazon Quantum Ledger Database (Amazon QLDB) is a fully managed ledger database. It provides a complete verifiable history of all application data changes and is built with tried and tested technology used inside AWS for years to solve building reliable system-of-record applications at scale.

### Amazon ElastiCache

Amazon ElastiCache offers fully managed Redis and Memcached in-memory data stores. You can build data-intensive apps or improve the performance of your existing apps by retrieving data from high throughput and low latency in-memory data stores.

### Amazon MemoryDB

Amazon MemoryDB for Redis is a Redis-compatible, durable, in-memory database service that delivers ultra-fast performance. It offers fully managed Redis with durability. MemoryDB is purpose built to serve modern microservices applications such as data-intensive real-time apps, mobile and web apps, media and entertainment, gaming, e-commerce and retail, and banking and finance.

### Amazon Redshift

Amazon Redshift is an enterprise-level, petabyte-scale, fully managed data warehousing service. With Amazon Redshift, you can achieve efficient storage and optimum query performance through a combination of massively parallel processing, columnar data storage, and very efficient, targeted data compression encoding schemes.

### Amazon Athena

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard structured query language (SQL). Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.