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

