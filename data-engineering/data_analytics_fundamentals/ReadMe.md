# Introduction to data analysis solutions

We introduce the concept of data analytics and data analysis solutions and discuss the challenges of working with large data sets that must rapidly produce meaningful insights. We also introduce you to the five challenges (the 5 Vs) of data analysis. Lastly, we define what you need to know plan your data analysis solution.

## Data analytics and data analysis solutions

### Definitions

**Analysis** is a detailed examination of something in order to understand its nature or determine its essential features.

**Data analysis** is the process of compiling, processing, and analyzing data so that you can use it to make decisions.

**Analytics** is the systematic analysis of data. **Data analytics** is the specific analytical process being applied.

Data analytics is vital to businesses large and small. Data analytic processes are combined to create data analysis solutions, which help businesses decide where and when to launch new products, when to offer discounts, and when to market in new areas. Without the data provided by data analytics, many decision makers would base their decisions on intuition and pure luck.

As businesses begin to implement data analysis solutions, challenges arise. These challenges are based on the characteristics of the data and analytics required for their use case. In the past, these challenges have been defined as "big data" challenges.  However, in today's cloud-based environment, these challenges can apply to small or slow data sets nearly as often as very large, fast data sets.

**Big data** is an industry term that has changed in recent years. Big data solutions are often part of data analysis solutions. 

> Organizations spend **millions** of dollars on data storage. The problem isn’t **finding** the data—the problem is **failing** to do anything with it. 

### Benefits of data analytics on a big scale
- **Customer Personalization**: What products should be shown to the customer based on their  buying habits?
- **Fraud Detection**: Is this pending transaction fraudulent?
- **Security Threat Detection**: What usage patterns indicate potential security risks from bad actors?
- **User Behavior**: Based on social media feeds, how much influence does this person have? What kinds of products or services would they be interested in promoting?
- **Financial Modeling and Forecasting**: What trends can be detected in these terrabytes of financial data? How can that be used to predict future market shifts?
- **Real-Time Alerting**: What is the problem and who needs to be notified?

**Effective** data analysis solutions require both storage and the ability to analyze data in near real time, with low latency, while yielding high-value returns.

### Characteristics of big data

Data is generated in many ways. The big question is where to put it all and how to use it to create value or generate competitive advantages. The challenges identified in many data analysis solutions can be summarized by five key challenges: **volume**, **velocity**, **variety**, **veracity**, and **value**.

Not all organizations experience challenges in every area. Some organizations struggle with ingesting large volumes of data rapidly. Others struggle with processing massive volumes of data to produce new predictive insights. Still others have users that need to perform detailed data analysis on the fly over enormous data sets. 

### Components of a data analysis solution

A data analysis solution has many components. The analytics performed in each of these components may require different services and different approaches. 

A data analysis solution includes the following components.

![Components](images/data_analytics_components.png)

- **Ingest/Collect**: Collecting the raw data from transactions, logs, and IoT devices is a challenge. A good data analysis solution allows developers to ingest a wide **variety** of data-structured, semi-structured, and unstructured at any speed, from batch to streaming.

- **Store**: Agood data analysis solution should provide secure, scalable, and durable storage. This storage should include data stores that can house structured, semi-structured, and unstructured data.

For example, data warehouses efficiently store structured analytical data, databases can store both structured and semi-structured data, and data lakes can store all three forms of data.

- **Process/analyze**: First, data must be processed, transforming it to make the data more consumable. As part of the processing, the data will also be analyzed. This usually means sorting, aggreagating, joining, and applying business logic to produce meaningful analytical data sets. The final step is to load this analytical data set into a new storage location, like a data lake, database, or data warehouse.

- **Consume/visualize**: You have two ways to consume data: by querying or by using business intelligence (BI) tools. Querying produces results that are great for quick analysis by data analysts. BI tools produce visualizations that are grouped into reports and dashboards to help users explore data and determine the best actions to take.

## Introduction to the challenges of data analytics

Due to increasing volume, velocity, variety, veracity, and value of data, some data management challenges cannot be solved with traditional database and processing solutions.  That's where data analysis solutions come in.

A brief definition of the five challenges will help you understand each one before you move on.

![Teminology](images/data_analysis_terms.png)

1. **Volume**: Volume means the amount of data that will be ingested by the solution- the total size of the data coming in. Solutions must work efficiently across distributed systems and be easily expandable inorder to accommodate spikes in traffic.

2. **Velocity**: Velocity means the speed of data entering a solution. Many organizations now require near real-time ingestion and processing of data.
The high velocity of data results in a shorter time to analyze than traditional data processing can provide.
Solutions must be able to manage this velocity efficiently. Processing systems must be able to return results within an acceptable time frame.

3.  **Variety**: Data can come from manay different sources. Variety means the number of different sources - and the types of sources - that the solution will use.

Solutions need to be sophisticated enough to manage all the different types of data while providing accurate analysis of the data.

4. **Veracity**: Veracity is the degree to which data is accurate, precise, and trusted. It is contigent on the integrity and trustworthiness of the data.

Solutions should be able to identify the common flaws in the data and fix them before the data is stored. This is known as **data cleansing**: This process must be able to be completed within the time requirements of the solution, up toand including real-time processing speed.

5. **Value**: Value is the ability for a solution to extract meaning ful information from the data that has been stored and analyzed. Solutions must be able to produce the right form of analytical results to inform business decision makers and stakeholders of insights using the trusted reports and dashboards.

### Planning a data analysis solution

Data analysis solutions incorporate many forms of analytics to store, process, and visualize data. Planning a data analysis solution begins with knowing what you need out of that solution.

#### Know where your data comes from
The majority of data ingested by data analysis solutions comes from **existing on-premises databases and file stores**. This data is often in a state where the required processing within the solution will be minimal.

**Streaming data** is a source of business data that is gaining popularity. This data source is less structured. It may require special software to collect the data and specific processing applications to correctly aggregate and analyze it in near real-time.

**Public data sets** are another source of data for businesses.  These include census data, health data, population data, and many other datasets that help businesses understand the data they are collecting on their customers.  This data may need to be transformed so that it will contain only what the business needs.

#### Know the options for processing your data
There are many different solutions available for processing your data. There is no one-size-fits-all approach. You must carefully evaluate your business needs and match them to the services that will combine to provide you with the required results. 

#### Know what you need to learn from your data
You must be prepared to learn from your data, work with internal teams to optimize efforts, and be willing to experiment. 

It is vital to spot trends, make correlations, and run more efficient and profitable businesses. It's time to put your data to work.


## Volume – data storage

When businesses have **more data** than they are able to **process and analyze**, they have a **volume problem**.

### Exponential growth of business data

Businesses have been storing data for decades—that is nothing new. What has changed in recent years is the ability to analyze certain types of data.

There are three broad classifications of data source types:
- **Structured data** is organized and stored in the form of values that are grouped into rows and columns of a table.

- **Semistructured data** is often stored in a series of key-value pairs that are grouped into elements within a file.

- **Unstructured data** is not structured in a consistent way. Some data may have structure similar to semi-structured data but others may only contain metadata.

Many internet articles tout the huge amount of information sitting within unstructured data. New applications are being released that can now catalog and provide incredible insights into this untapped resource.

But what is unstructured data? It is in every file that we store, every picture we take, and email we send.

![Data Types](images/data_types.png)

> Data sets are getting bigger and more diverse every single day.

Modern data management platforms must capture data from diverse sources at speed and scale. Data needs to be pulled together in manageable, central repositories—breaking down traditional silos. The benefits of collection and analysis of all business data must outweigh the costs.

### Introduction to Amazon S3
Data analysis solutions can ingest data from just about anywhere. However, the closer your data is to your processing system, the better that processing system will perform. In AWS, the Amazon Simple Storage Service (Amazon S3) is the best place to store all of your semistructured and unstructured data.

### Amazon S3 concepts

To get the most out of Amazon S3, you need to understand a few simple concepts. First, Amazon S3 stores data as **objects** within **buckets**.

An **object** is composed of a file and any metadata that describes that file. To store an object in Amazon S3, you upload the file you want to store into a bucket. When you upload a file, you can set permissions on the object and add any metadata.

**Buckets** are logical containers for objects. You can have one or more buckets in your account and can control access for each bucket individually. You control who can create, delete, and list objects in the bucket. You can also view access logs for the bucket and its objects and choose the geographical region where Amazon S3 will store the bucket and its contents.

![S3](images/amazon_s3.png)

#### Accessing your content

Once objects have been stored in an Amazon S3 bucket, they are given an **object key**. Use this, along with the bucket name, to access the object.

Below is an example of a URL for a single object in a bucket named **doc**, with an object key composed of the prefix **2006-03-01** and the file named **AmazonS3.html**.

![Object Url](images/object_url.png)

An **object key** is the unique identifier for an object in a bucket. Because the combination of a bucket, key, and version ID uniquely identifies each object, you can think of Amazon S3 as a basic data map between "bucket + key + version" and the object itself. Every object in Amazon S3 can be uniquely addressed through the combination of the web service endpoint, bucket name, key, and (optionally) version.

- [**Object metadata**](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-metadata): For each object stored in a bucket, Amazon S3 maintains a set of system metadata.

### Data analysis solutions on Amazon S3

There are numerous advantages of using Amazon S3 as the storage platform for your data analysis solution.

- **Decoupling of storage from compute and data processing**: With Amazon S3, you can cost-effectively store all data types in their native formats. You can then launch as many or as few virtual servers needed using Amazon Elastic Compute Cloud (Amazon EC2) and use AWS analytics tools to process your data. You can optimize your EC2 instances to provide the correct ratios of CPU, memory, and bandwidth for best performance.

Decoupling your processing and storage provides a significant number of benefits, including the ability to process and analyze the same data with a variety of tools.

- **Centralized data architecture**: Amazon S3 makes it easy to build a multi-tenant environment, where many users can bring their own data analytics tools to a common set of data. This improves both cost and data governance over traditional solutions, which require multiple copies of data to be distributed across multiple processing platforms.

Although this may require an additional step to load your data into the right tool, using Amazon S3 as your central data store provides even more benefits over traditional storage options.

- **Integration with clusterless and serverless AWS services**: Combine Amazon S3 with other AWS services to query and process data. Amazon S3 also integrates with AWS Lambda serverless computing to run code without provisioning or managing servers. Amazon Athena can query Amazon S3 directly using the Structured Query Language (SQL), without the need for data to be ingested into a relational database.

With all of these capabilities, you only pay for the actual amounts of data you process or the compute time you consume.

- **Standardized Application Programming Interfaces(APIs)**: Representational State Transfer (REST) APIs are programming interfaces commonly used to interact with files in Amazon S3. Amazon S3's RESTful APIs are simple, easy to use, and supported by most major third-party independent software vendors (ISVs), including Apache Hadoop and other leading analytics tool vendors. This allows customers to bring the tools they are most comfortable with and knowledgeable about to help them perform analytics on data in Amazon S3.

### Introduction to data lakes

Storing business content has always been a point of contention, and often frustration, within businesses of all types. Should content be stored in folders? Should prefixes and suffixes be used to identify file versions? Should content be divided by department or specialty? The list goes on and on.

The issue stems from the fact that many companies start to implement document or file management systems with the best of intentions but don't have the foresight or infrastructure in place to maintain the initial data organization.

Out of the dire need for organizing the ever increasing volume of data, data lakes were born.

- **A data lake** is a centralized repository that allows you to store structured, semistructured, and unstructured data at any scale.

![Data lake](images/data_lake.png)

Data lakes promise the ability to store all data for a business in a single repository. You can leverage data lakes to store large volumes of data instead of persisting that data in data warehouses. Data lakes, such as those built in Amazon S3, are generally less expensive than specialized big data storage solutions. That way, you only pay for the specialized solutions when using them for processing and analytics and not for long-term storage. Your extract, transform, and load (ETL) and analytic process can still access this data for analytics. 

Below are some of the benefits of data lakes. 
- Single source of truth.
- Store any type of data, regardless of structure.
- Can be analyzed using AI and machine learning.

### Benefits of a data lake on AWS
- Are a **cost-effective data storage** solution. You can durably store a nearly unlimited amount of data using Amazon S3.
- Implement industry-leading **security and compliance**. AWS uses stringent data security, compliance, privacy, and protection mechanisms.
- Allow you to take advantage of **many different data collection and ingestion tools** to ingest data into your data lake. These services include Amazon Kinesis for streaming data and AWS Snowball appliances for large volumes of on-premises data.
- Help you to **categorize and manage your data** simply and efficiently. Use AWS Glue to understand the data within your data lake, prepare it, and load it reliably into data stores. Once AWS Glue catalogs your data, it is immediately searchable, can be queried, and is available for ETL processing.
- Help you turn data into **meaningful insights**. Harness the power of purpose-built analytic services for a wide range of use cases, such as interactive analysis, data processing using Apache Spark and Apache Hadoop, data warehousing, real-time analytics, operational analytics, dashboards, and visualizations.

### Amazon EMR and data lakes

Businesses have begun realizing the power of data lakes. Businesses can place data within a data lake and use their choice of open source distributed processing frameworks, such as those supported by Amazon EMR. Apache Hadoop and Spark are both supported by Amazon EMR, which has the ability to help businesses easily, quickly, and cost-effectively implement data processing solutions based on Amazon S3 data lakes.

### Data lake preparation

> Data scientists spend **60%** of their time **cleaning and organizing data** and **19% collecting data sets**.

Data preparation is a huge undertaking. There are no easy answers when it comes to cleaning, transforming, and collecting data for your data lake. However, there are services that can automate many of these time-consuming processes.

Setting up and managing data lakes today can involve a lot of manual, complicated, and time-consuming tasks. This work includes loading the data, monitoring the data flows, setting up partitions for the data, and tuning encryption. You may also need to reorganize data, deduplicate it, match linked records, and audit data over time.

### AWS content organization and curation

#### Data lake on AWS

> **Business Challenge**: Imagine a business that has millions of files stored in numerous on-premises server-based and network-attached storage solutions. The business is struggling to navigate all of the locations and provide users with quick, reliable access to this content both locally and from the cloud.

Traditional data storage and analytic tools can no longer provide the agility and flexibility required to deliver relevant business insights. That’s why many organizations are shifting to a data lake architecture.

A data lake on AWS can help you do the following:

- Collect and store any type of data, at any scale, and at low cost
- Secure the data and prevent unauthorized access
- Catalog, search, and find the relevant data in the central repository
- Quickly and easily perform new types of data analysis
- Use a broad set of analytic engines for one-time analytics, real-time streaming, predictive analytics, AI, and machine learning

- [**Data lakes on AWS**](https://aws.amazon.com/big-data/datalakes-and-analytics/): Quickly build, test, and deploy your data lake with AWS and partner solutions.

#### AWS Lake Formation (currently in preview)

> **Business Challenge**: Imagine a business that has thousands of files stored in Amazon S3. The business needs a solution for automating common data preparation tasks and organizing the data in a secure repository.

AWS Lake Formation makes it easy to set up a secure data lake in days. A data lake is a centralized, curated, and secured repository that stores all your data, both in its original form and when prepared for analysis. A data lake enables you to break down data silos and combine different types of analytics to gain insights and guide better business decisions. AWS Lake Formation is in preview only.

- [**AWS Lake Formation**](https://aws.amazon.com/lake-formation/?nc2=h_m1): Build a secure data lake in days.

AWS Lake Formation makes it easy to ingest, clean, catalog, transform, and secure your data and make it available for analysis and machine learning. Lake Formation gives you a central console where you can discover data sources, set up transformation jobs to move data to an Amazon S3 data lake, remove duplicates and match records, catalog data for access by analytic tools, configure data access and security policies, and audit and control access from AWS analytic and machine learning services.

Lake Formation automatically configures underlying AWS services to ensure compliance with your defined policies. If you have set up transformation jobs spanning AWS services, Lake Formation configures the flows, centralizes their orchestration, and lets you monitor the processing of your jobs.

### Introduction to data storage methods

As the volume of data has increased, so have the options for storing data. Traditional storage methods such as data warehouses are still very popular and relevant. However, data lakes have become more popular recently. These new options can confuse businesses that are trying to be financially wise and technically relevant.

So which is better: data warehouses or data lakes? Neither and both. They are different solutions that can be used together to maintain existing data warehouses while taking full advantage of the benefits of data lakes.

#### Data warehouses

A data warehouse is a **central repository** of structured data from many data sources. This data is **transformed**, **aggregated**, and **prepared** for business reporting and analysis.

![Data warehouse](images/data_warehouse.png)

A data warehouse is a central repository of information coming from one or more data sources. Data flows into a data warehouse from transactional systems, relational databases, and other sources. These data sources can include structured, semistructured, and unstructured data. These data sources are transformed into structured data before they are stored in the data warehouse.

Data is stored within the data warehouse using a schema. A schema defines how data is stored within tables, columns, and rows. The schema enforces constraints on the data to ensure integrity of the data. The transformation process often involves the steps required to make the source data conform to the schema. Following the first successful ingestion of data into the data warehouse, the process of ingesting and transforming the data can continue at a regular cadence.

Business analysts, data scientists, and decision makers access the data through business intelligence (BI) tools, SQL clients, and other analytics applications. Businesses use reports, dashboards, and analytics tools to extract insights from their data, monitor business performance, and support decision making. These reports, dashboards, and analytics tools are powered by data warehouses, which store data efficiently to minimize I/O and deliver query results at blazing speeds to hundreds and thousands of users concurrently.

#### Data marts (A subset of data warehouse)

Data warehouses can be massive. Analyzing these huge stores of data can be confusing. Many organizations need a way to limit the tables to those that are most relevant to the analytics users will be performing.

A subset of data from a data warehouse is called a **data mart**. Data marts only **focus on one subject or functional area**. A warehouse might contain all relevant sources for an enterprise, but a data mart might store **only a single department’s sources**. Because data marts are generally a copy of data already contained in a data warehouse, they are often **fast and simple to implement**.

![Data mart](images/data_mart.png)

#### Traditional data warehousing: pros and cons

|Pros |Cons |
|:----|:----|
|Fast data retrieval |Costly to implement |
|Curated data sets |Maintenance can be challenging |
|Centralized storage |Security concerns |
|Better business intelligence |Hard to scale to meet demand |

### Amazon Redshift benefits

This is where Amazon Redshift comes in. Amazon Redshift overcomes all of these negatives by providing a cloud-based, scalable, secure environment for your data warehouse. Amazon Redshift is easy to set up, deploy, and manage and provides up to 10 times faster performance than other data warehousing solutions.

|Benefits of Amazon Redshift |
|:---------------------------|
|Faster performance |
|10x faster than other data warehouses |
|Easy to set up, deploy, and manage |
|Secure |
|Scales quickly to meet your needs |

### Comparing data warehouses and data lakes

#### Analyzing a data warehouse

For analysis to be most effective, it should be performed on data that has been processed and cleansed. This often means implementing an ETL operation to collect, cleanse, and transform the data. This data is then placed in a data warehouse. It is very common for data from many different parts of the organization to be combined into a single data warehouse.

Amazon Redshift is a data warehousing solution specially designed for workloads of all sizes. Amazon Redshift Spectrum even provides the ability to query data that is housed in an Amazon S3 data lake.

![Analyzing a data warehouse](images/analyze_data_warehouse.png)

#### Analyzing a data lake

**Data lakes extend data warehouses**

Data lakes provide customers a means for including unstructured and semistructured data in their analytics. Analytic queries can be run over cataloged data within a data lake. This extends the reach of analytics beyond the confines of a single data warehouse.

Businesses can securely store data coming from applications and devices in its native format, with high availability, durability, at low cost, and at any scale. Businesses can easily access and analyze data in a variety of ways using the tools and frameworks of their choice in a
high-performance, cost-effective way without having to move large amounts of data between storage and analytics systems.

![Analyzing a data lake](images/analyze_data_lake.png)

#### AWS: Data lakes and Analytics

AWS provides a comprehensive portfolio of services that enable customers to build their data lakes in the cloud and analyze all their data with the broadest set of analytical approaches, including machine learning.

As a result, there are more organizations running their data lakes and analytics on AWS than anywhere else.

![Data lake](images/data_lake.png)

![](images/data_x-tics.png)

### Data storage on a BIG scale

We have discussed several recommendations for storing data: 

- When storing individual objects or files, we recommend Amazon S3.
- When storing massive volumes of data, both semistructured and unstructured, we recommend building a data lake on Amazon S3.
- When storing massive amounts of structured data for complex analysis, we recommend storing your data in Amazon Redshift.

> When many people think of working with a massive volume of fast-moving data, the first thing that comes to mind is Hadoop. Within AWS, Hadoop frameworks are implemented using Amazon EMR and AWS Glue. These services implement the Hadoop framework to ingest, transform, analyze, and move results to analytical data stores.

### Apache Hadoop

Hadoop uses a **distributed processing architecture**, in which a task is mapped to a cluster of commodity servers for processing. Each piece of work distributed to the cluster servers can be run or re-run on any of the servers. The cluster servers frequently use the **Hadoop Distributed File System (HDFS)** to store data locally for processing. The results of the computation performed by those servers are then reduced to a single output set. One node, designated as the master node, controls the distribution of tasks and can automatically handle server failures.

![Hadoop](images/apche_hadoop.png)

#### Benefits of using Apache Hadoop
- **Handle uncertainty better**: Hadoop facilitates data navigation, discovery, and one-time data analysis. With Hadoop, you can compensate for unexpected occurrences by analyzing large amounts of data quickly to form a response.

- **Manage data variety**: Unlike traditional database systems, Hadoop can process structured, semistructured, or unstructured data. This includes virtually any data format currently available.

In addition to natively handling many types of data (such as XML, CSV, text, log files, objects, SQL, JSON, and binary), you can use Haddop to transform data into formats that allow better integration into your existing data sets. Also, you can store data with or without a schema and perform large-scale ETL operations to transform your data.

![Data variety](images/data_variety.png)

- **wide selection of solutions**: Because Hadoop is open source, several ecosystem projects are available to help you analyze the multiple types of data Hadoop can process and analyze.

These projects give you tremendous flexibility when you are developing data analytics solutions. Hadoop’s programming frameworks (such as Hive and Pig) can support almost any data analytics use case for your applications.

- **Build for volume and velocity**: Because of Hadoop’s distributed architecture, Hadoop clusters can handle tremendous amounts of data affordably. Adding additional data processing capability is as simple as adding additional servers to your cluster (horizontal scaling).

### Implementing Hadoop with Amazon EMR

Amazon EMR is the AWS service that implements Hadoop frameworks. The service will ingest data from nearly any data source type at nearly any speed! Amazon EMR has the ability to implement two different file systems: HDFS or the Elastic MapReduce File System (EMRFS). A file system is a set of organizational rules that govern how files are stored. 

#### HDFS

To handle massive volumes of data rapidly, the processing system required a way to distribute the load of reading and writing files across tens or even hundreds of high-powered servers. HDFS is distributed storage allowing files to be read and written to clusters of servers in parallel. This dramatically reduces the overall length of each and every operation.

It is helpful to understand the inner workings of an HDFS cluster. An HDFS cluster primarily consists of a NameNode, which manages the file system metadata, and DataNodes, which store the actual data.


Amazon EMR is the AWS service that implements Hadoop frameworks. An Amazon EMR process begins by ingesting data from one or more data sources and storing that data within a file system. If using HDFS, the file system is stored as an elastic block store volume. This storage volume is ephemeral meaning that the storage is of a temporary nature. Once the data has been copied into the HDFS volume, the transformation and analysis of the data is performed. The results are then sent to an analytical data store, such as an Amazon S3 data lake or Amazon Redshift data warehouse.

#### Amazon EMRFS

Amazon EMR provides an alternative to HDFS: the EMR File System (EMRFS). EMRFS can help ensure that there is a persistent "source of truth" for HDFS data stored in Amazon S3. When implementing EMRFS, there is no need to copy data into the cluster before transforming and analyzing the data as with HDFS. EMRFS can catalog data within a data lake on Amazon S3. The time that is saved by eliminating the copy step can dramatically improve performance of the cluster.

## Velocity – data processing

When businesses **need rapid insights** from the data they are collecting, but the **systems** in place simply **cannot meet the need**, there's a **velocity** problem.

### The problem of velocity

The speed at which data is being generated is ever accelerating. Emails, photos, Twitter and Facebook posts, log files, and IoT devices are all examples of data that is being generated rapidly and must be collected, processed, analyzed, and stored at high speeds. 

The collection and processing of data are combined into a single concept known as data processing.

### Definition

**Data processing** means the collection and manipulation of data to produce meaningful information. Data collection is divided into two parts, data collection and data processing.

![Data processing](images/data_processing.png)

### Introduction to data processing methods

Data processing is vital to any data system. Data processing defines the methods that are used to collect data and present it to storage or analytic mechanisms.

Data processing may only need to be performed once a day, making results available the following morning, or it may need to be performed and made available immediately. This variance in the speed at which data processing must occur can be broken down into four categories.

![Methods](images/data_processing_methods.png)

### Characteristics of data processing velocity

A system's ability to process data will depend heavily on the requirements placed on it. Choosing the right system is critical for successful implementation. Below are the characteristics of the four velocities on both collecting and processing data.

#### Collecting Data

**Batch**: Velocity is very predictable with batch processing. It amounts to large bursts of data transfer at scheduled intervals.

**Periodic**: Velocity is less predictable with periodic processing. The loss of scheduled events can put a strain on systems and must be considered.

**Near real-time**: Velocity is a huge concern with near real-time processing. These systems require data to be processed within minutes of the initial collection of the data. This can put tremendous strain on the processing and analytics systems involved.

**Real-time**: Velocity is the paramount concern for real-time processing systems. Information cannot take minutes to process. It must be processed in seconds to be valid and maintain its usefulness.

#### Processing Data

**Batch and periodic**: Once the data has been collected, processing can be done in a controlled environment. There is time to plan for the appropriate resources.

**Near real-time and real-time**: Collection of the data leads to an immediate need for processing. Depending on the complexity of the processing (cleansing, scrubbing, curation), this can slow down the velocity of the solution significantly. Plan accordingly.

### Data acceleration

Another key characteristic of velocity on data is data acceleration, which means the rate at which large collections of data can be ingested, processed, and analyzed. Data acceleration is not constant. It comes in bursts. Take Twitter as an example. Hashtags can become hugely popular and appear hundreds of times in just seconds, or slow down to one tag an hour. That's data acceleration in action. Your system must be able to efficiently handle the peak of hundreds of tags a second and the lows of one tag an hour. 

### Attributes of batch and stream processing

The table below highlights the difference between batch and stream processing: 

![Batch and Stream](images/batch_stream_processing.png)


### Introduction to batch data processing

Batch processing is often thought of as a slow process. This is not the case. Batch processing must quickly and efficiently consume a huge amount of data all at once. This poses challenges that do not exist with stream processing.

Batch data processing provides companies with the ability to dive deep into the data they have collected to produce complex analytics that simply cannot be achieved using streaming analytics.

**Batch processing** is the processing of a series of programs, or jobs, on one or more computers without manual intervention. Data is collected into batches asynchronously. The batch is sent to a processing system when specific conditions are met, such as a specified time of day. The results of the processing job are then sent to a storage location that can be queried later as needed.

![Batch Processing](images/batch_processing.png)

#### Batch data processing with Amazon EMR and Apache Hadoop

Organizations that need big data solutions are working with data at such a high volume and velocity that traditional environments cannot meet their needs.

Amazon EMR is a managed service for implementing Apache Hadoop workloads. In addition to running the Apache Hadoop framework, you can also run other popular distributed frameworks such as Apache Spark, HBase, Presto, and Flink in EMR. You have the added advantage of being able to interact with data in other AWS data stores such as Amazon S3 and Amazon DynamoDB. 

Amazon EMR notebooks provide a serverless development and collaboration environment for one-time querying and exploratory analysis. You can manipulate the data and generate data plots using rich graphical tools. Amazon EMR notebooks monitor your jobs and even help you debug code from the notebooks.

#### Exploring Apache Hadoop

Apache Hadoop is a scalable storage and batch data processing system. It uses commodity server hardware and provides fault tolerance through software. Hadoop complements existing data systems by simultaneously ingesting and processing large volumes of data, structured or not, from any number of sources, which enables deeper analysis than any one system can provide. These results can be delivered to any existing enterprise system for further use independent of Hadoop.

Hadoop is a platform that provides distinct modules.

- **Hadoop Common**: Hadoop Common is the set of Java utilities and libraries that support the other Hadoop modules. These libraries help abstract the file system from the processing components. These Java files and scripts are required to start Hadoop.

- **Hadoop Distributed File System (HDFS)**: Hadoop Distributed File System (HDFS) is the distributed file system that stores the data in a high-throughput environment of community nodes. This architecture ensures very high aggregate bandwidth access to application data..

- **Hadoop YARN**: Hadoop YARN is the resource management framework responsible for scheduling and processing jobs.

- **Hadoop MapReduce**: Hadoop MapReduce is a YARN-based system that allows for parallel processing of large data sets on the cluster.

### Batch processing architecture

Batch processing can be performed in different ways using AWS services. 

The architecture diagram below depicts the components and the data flow of a basic batch analytics system using a traditional approach. This approach uses **Amazon S3** for storing data, **AWS Lambda** for intermediate file-level ETL, **Amazon EMR** for aggregated ETL (heavy lifting, consolidated transformation, and loading engine), and **Amazon Redshift** as the data warehouse hosting data needed for reporting. 

![Batch Architecture](images/batch_architecture_1.png)

The architecture diagram below depicts the same data flow as above but uses AWS Glue for aggregated ETL (heavy lifting, consolidated transformation, and loading engine). AWS Glue is a fully managed service, as opposed to Amazon EMR, which requires management and configuration of all of the components within the service.

![Batch Architecture](images/batch_architecture_2.png)

####  Batch processing use cases

**Log analytics**

Amazon EMR can be used to process logs generated by web and mobile applications. The service helps customers turn petabytes of unstructured or semistructured data into useful insights about their applications or users. In such use cases, logs are usually collected in batches and aggregated and analyzed at the end of the day for meaningful insights.

**Unified view of data across multiple data stores**

You can use the AWS Glue Data Catalog to quickly discover and search across multiple AWS data sets without moving the data. Once the data is cataloged, it is immediately available for search and query using Amazon Athena, Amazon EMR, and Amazon Redshift Spectrum. 

**Predictive analytics**

Apache Spark on EMR includes MLlib for scalable machine learning algorithms, or you can use your own libraries. By storing datasets in-memory, Spark can provide great performance for common machine learning workloads. 

**Queries against an Amazon S3 data lake**

Data lakes are an increasingly popular way to store and analyze both structured and unstructured data. If you want to build your own custom Amazon S3 data lake, AWS Glue can make all your data immediately available for analytics without moving the data.

### Introduction to stream data processing

Stream data processing is one of the fastest growing areas of processing. The number of devices that are collecting information in real time is growing rapidly. This drives the need for processing solutions that can match the velocity of data generation.

Stream data processing gives companies the ability to get insights from their data within seconds of the data being collected.

Companies can no longer afford to neglect or avoid the vast amounts of data that is steaming in from web applications, ecommerce purchases, in-game player activity, and information from social networks.

![Stream processing](images/stream_data_processing.png)

#### Processing big data streams

There are many reasons to use streaming data solutions. In a batch processing system, processing is always asynchronous, and the collection system and processing system are often grouped together. With streaming solutions, the collection system (producer) and the processing system (consumer) are always separate. Streaming data uses what are called data producers. Each of these producers can write their data to the same endpoint, allowing multiple streams of data to be combined into a single stream for processing. Another huge advantage is the ability to preserve client ordering of data and the ability to perform parallel consumption of data. This allows multiple users to work simultaneously on the same data.

#### Benefits of stream processing

![Streaming](images/stream_data_processing_2.png)

#### Stream data processing with Amazon Kinesis

In stream processing, you use multiple services: one service to ingest the constant stream of data, one to process and analyze the stream, and one to load the data into an analytical data store if required. Amazon Kinesis meets each of these needs, and you can use each Kinesis service independent of the others to create an optimal streaming solution.

1. **Amazon Kinesis Data Firehose**: Amazon Kinesis Data Firehose is the easiest way to capture, transform, and load data streams into AWS data stores for near real-time analytics with existing business intelligence tools. 

2. **Amazon Kinesis Data Streams**: Amazon Kinesis Data Streams enables you to build custom, real-time applications that process data streams using popular stream processing frameworks. 

3. **Amazon Kinesis Video Streams**: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), and other processing. 

4. **Amazon Kinesis Data Analytics**: Amazon Kinesis Data Analytics is the easiest way to process data streams in real time with SQL or Java without having to learn new programming languages or processing frameworks.

#### Stream processing architecture

Several services are involved in the following architecture
- Amazon Kinesis Data Firehose
- Amazon Kinesis Data Analytics
- Amazon S3
- Amazon Athena
- Amazon Quicksight

In this architecture, sensor data is being collected in the form of a stream. The streaming data is being collected from the sensor devices by **Amazon Kinesis Data Firehose**. This service is configured to send the data to be processed using **Amazon Kinesis Data Analytics**. This service filters the data for relevant records and send the data into another Kinesis Data Firehose process, which places the results into an **Amazon S3** bucket at the serving layer.

Using **Amazon Athena**, the data in the Amazon S3 bucket can now be queried to produce insightful dashboards and reports using **Amazon QuickSight**.

![Architecture](images/stream_architecture.png)

#### Combined processing architecture

It is important to remember that streaming analytics is very limited. Due to the size of each data packet and the speed the data is moving, you are limited to simple analytics such as aggregating and filtering the data. Due to this limitation, it is common for businesses to incorporate batch analytics to produce deeper insights into the data before producing dashboards and reports on the data.

In the following architecture, streaming data is collected by the same **Amazon Kinesis Data Firehose** service seen in the above architecture. This time however, the data is placed directly into an **Amazon S3** bucket. A separate process loads user device settings into a second Amazon S3 bucket. **AWS Glue** is then used to combine the two Amazon S3 data stores and transform them into a single result set, which is loaded into a third Amazon S3 bucket at the Serving Layer.

Using Amazon Athena, the data in the third Amazon S3 bucket can now be queried. Amazon QuickSight can be used to produce dashboards that include content from both Amazon Athena and the first Amazon S3 bucket where the raw streaming data was loaded. This allows the business to perform comparative analysis on the data.

![Architecture](images/stream_architecture_2.png)

Now that you have seen the two architectures independently, it is time to see how they work together to form a complete end-to-end solution.

![Architecture](images/stream_architecture_3.png)

### Stream processing use cases

#### Build video analytics applications
You can use Amazon Kinesis to securely stream video from camera-equipped devices in homes, offices, factories, and public places to AWS. You can then use these video streams for video playback, security monitoring, face detection, machine learning, and other analytics. Integrating this data into your applications allows for a wide variety of customer enhancements and data mining capabilities.

#### Evolve from batch to real-time analytics
With Amazon Kinesis, you can perform real-time analytics on data that has been traditionally analyzed using batch processing in data warehouses or using Hadoop frameworks. The most common use cases include data lakes, data science and machine learning. You can use Kinesis Data Firehose to continuously load streaming data into your Amazon S3 data lakes. You can also update machine learning models more frequently as new data becomes available, ensuring accuracy and reliability of the outputs.

[**Try a tutorial**](https://aws.amazon.com/getting-started/projects/build-log-analytics-solution/).

#### Analyze IoT device data
You can use Amazon Kinesis to process streaming data from IoT devices such as consumer appliances, embedded sensors, and TV set-top boxes. You can then use the data to send real-time alerts or take other actions programmatically when a sensor exceeds certain operating thresholds. Use our sample IoT analytics code to build your application. No need to start from scratch.
