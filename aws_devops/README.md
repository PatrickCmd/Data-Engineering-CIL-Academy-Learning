# What Is DevOps?

DevOps is the combination of cultural philosophies, practices, and tools that increases an organization’s ability to deliver applications and services at high velocity: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes. This speed enables organizations to better serve their customers and compete more effectively in the market. 

DevOps emphasizes better collaboration and efficiencies so teams can innovate faster and deliver higher value to businesses and customers.

![devops](images/devops.png)

**DevOps** is short for Development (Dev) and Operations (Ops). Dev are the people and processes that create software. Ops are the teams and processes that deliver and monitor the software. 

Developers change things quickly, release often, and measure success by the rate of delivery. Operations are driven by maintaining stability of the application. Frequent releases are a cause for concern of the stability and reliability of the application on the supported platforms, especially during high network traffic. 

DevOps brings together formerly siloed roles (development, IT operations, quality engineering, and security) to optimize the productivity of developers and the reliability of operations.

### DevOps is a combination of:

- Cultural philosophies for removing barriers and sharing end-to-end responsibility
- Processes developed for speed and quality, that streamline the way people work
- Tools that align with processes and automate repeatable tasks, making the release process more efficient and the application more reliable

## Problems with Traditional Development Practices

Traditional ways of developing software have proven slow and inefficient, and fail to support teams' efforts to quickly deliver stable, high-quality applications. Challenges of Waterfall development, monolithic applications, manual processes, and siloed team structures cause bottlenecks and delays.

![Development Processes](images/dev_processes.png)

**Waterfall development projects** are slow, not iterative, resistant to change, and have long release cycles. Some reasons for this include:

- Requirements are rigid, set at project start, and will likely not change.
- Development phases are siloed, each starting after the previous phase has ended. Each phase is supported by highly specialized teams.

Hand offs from one phase to the other are long, often requiring teams to switch tools and spend time clarifying incomplete or ambiguous information.
- Testing and security come after implementation, making corrective actions responsive and expensive.

**Monolithic applications** are hard to update and deploy because they:

- Are developed and deployed as a unit, so when changes are made, the entire application must be redeployed
- Have tightly coupled functionality, so if the application is large enough, maintenance becomes an issue because developers have a hard time understanding the entire application
- Are implemented using a single development stack, so changing technology is difficult and costly

Manual processes throughout the application lifecycle are slow, inconsistent, and error-prone. For example, manually setting and configuring the infrastructure is time-consuming. Manually repeating this process is no guarantee that a step will not be missed. Another example is telling the developers to make sure their code is thoroughly tested before pushing it. Even with the best intentions, this manual process is slow, and does not preclude someone from forgetting a test or two.

Teams supporting the software development lifecycle have traditionally been siloed. Specialized in their skill set, teams such as business, development, quality assurance, specialists, maintenance, and operations, have been separated from each other and require scheduled and rigid hand-offs. Even though these teams have a common goal of delivering and supporting the application, they also have their own priorities, tooling, and processes. It is difficult to achieve efficiencies when project members are reporting to different units and aimed for different targets.

## Why DevOps?
### Proven success 

According to the [**Accelerate State of DevOps 2019**](https://services.google.com/fh/files/misc/state-of-devops-2019.pdf) report, organizations of any size, and in any industry, can benefit from DevOps. According to the report, teams who successfully adopt DevOps see shorter delivery cycles, decreased change failure rates, and improved performance.

### The benefits of DevOps

Organizations of all sizes, from small startups to big enterprises, can benefit from adopting DevOps. Following are some of the main benefits of DevOps.
- Agility
- Rapid delivery
- Reliability
- Scale
- Improved Collaboration
- Security

### Why do some teams initially resist adopting DevOps?

Reluctance to DevOps adoption is natural because DevOps will bring change and disrupt the way you work and interact with others. DevOps will have organizational and team-level impact. To overcome this reluctance, it is important to understand the value of DevOps, and set realistic expectations for the teams. To be successful, you need buy-in across the organization and development teams.

## DevOps Culture
A shift to DevOps requires creating and nurturing a DevOps culture, which is a culture of transparency, effective and seamless collaboration, and common goals. 

You might have the processes and tools to support DevOps but, for successful DevOps adoption, the people of the organization must have the right mindset to nurture the DevOps culture.

There are seven core principles that can help you achieve a DevOps culture.

1. **Create a highly collaborative environment**

DevOps brings together development and operations to break down silos, align goals, and deliver on common objectives. The whole team (development, testing, security, operations, and others) has end-to-end ownership for the software they release. They work together to optimize the productivity of developers and the reliability of operations. Teams learn from each other's experiences, listen to concerns and perspectives, and streamline their processes to achieve the required results.

This increased visibility enables processes to be unified and continuously improved to deliver on business goals. The collaboration also creates a high-trust culture that values the efforts of each team member, and transfers knowledge and best practices across teams and the organization.

2. **Automate when possible**

With DevOps, repeatable tasks are automated, enabling teams to focus on innovation. Automation provides the means to rapid development, testing, and deployment. Identify automation opportunities at every phase, such as code integrations, reviews, testing, security, deployments, and monitoring, using the right tools and services.

For example, infrastructure-as-code (IaC) can be used for predefined or approved environments, and versioned so that repeatable and consistent environments are built. You can also define regulatory checks and incorporate them in test that continuously run as part of your release pipeline.

3. **Focus on customer needs**

A customer first mindset is a key factor in driving development. For example, with feedback loops DevOps teams stay in-touch with their customer and develop software that meets the customer needs. With a microservices architecture, they are able to quickly switch direction and align their efforts to those needs. 

Streamlined processes and automation deliver requested updates faster and keep customer satisfaction high. Monitoring helps teams determine the success of their application and continuously align their customer focused efforts.

4. **Develop small and release often**

Applications are no longer being developed as one monolithic system with rigid development, testing, and deployment practices. Application architectures are designed with smaller, loosely coupled components. Overarching policies (such as backward compatibility, or change management) are in place and provide governance to development efforts. Teams are organized to match the required system architecture. They have a sense of ownership for their efforts. 

Adopting modern development practices, such as small and frequent code releases, gives teams the agility they need to be responsive to customer needs and business objectives.

5.  **Include security at every phase**

To support continuous delivery, security must be iterative, incremental, automated, and in every phase of the application lifecycle, instead of something that is done before a release. Educate the development and operations teams to embed security into each step of the application lifecycle. This way, you can identify and resolve potential vulnerabilities before they become major issues and are more expensive to fix. 

For example, you can include security testing to scan for hard-coded access keys, or usage of restricted ports.

6. **Continuously experiment and learn**

Inquiry, innovation, learning, and mentoring are encouraged and incorporated into DevOps processes. Teams are innovative and their progress is monitored. With innovation, failure will happen. Leadership accepts failure and teams are encouraged to see failure as a learning opportunity. 

For example, teams use DevOps tools to spin-up environments on demand, enabling them to experiment and innovate, perhaps on the use of new technology to support a customer requirement.

7. **Continuously improve**

Thoughtful metrics help teams monitor their progress, evaluate their processes and tools, and work toward common goals and continuous improvement. For example, teams strive to improve development performance measures such as throughput.

They also strive to increase stability and reduce the mean time to restore service. Using the right monitoring tools, you can set application benchmarks for usual behaviors, and continuously monitor for variations.

## DevOps Practices
DevOps culture leads to DevOps practices that are geared toward streamlining and improving the development lifecycle, to reliably deliver frequent updates, while maintaining stability. 

1. **Communication and collaboration**

DevOps teams set strong cultural norms around transparency of information and communication. These cross-functional teams have ownership and thus, instead of evaluating just their work, they consider the project needs collectively. They build empathy for each other’s efforts, partnerships, and trust, while collaborating towards common goals. They physically bring together traditional development and operations workflows and systematically improve productivity. 

DevOps tools and automation of the delivery process, support these consolidated processes and workflows, coordinate efforts, automate repetitive tasks, and facilitate feedback loops required in good communication and collaboration.

2. **Monitoring and Observability**

Monitoring and observability are used to assess how effective changes to the application and infrastructure are, and how they impact performance and overall user experience. Part of DevOps feedback loops, monitoring and observability help teams react, learn, plan, and improve.

An observable system is a system that generates enough data from all resources, applications, and services in the form of logs, metrics, and traces to gain system-wide operational visibility. Logs report on discrete events, such as warnings. Metrics capture health and performance information, such as request rate or response time. Traces report on transactions and the flow of data across a distributed system, such as one comprised of microservices. 

By observing a system, you can draw concise inferences about why something is happening.

Monitoring tells you what is happening with your system. By consolidating and visualizing data gathered by an observable system over time, teams gain insight on performance, identify trends, can set alarms, and make predictions on expected outcomes.

3. **Continuous Integration**

Continuous integration is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This way, teams can resolve merging issues and code defects early, when they are easier and more cost effective to resolve.

Continuous integration most often refers to the build or integration stage of the software release process. It requires both an automation component (for example, a CI or build service) and a cultural component (for example, learning to integrate frequently). The key goals of continuous integration are to find and address bugs quicker, improve software quality, and reduce the time it takes to validate and release new software updates.

4. **Continuous delivery/Continuous deployment**

Continuous delivery is a software development practice where every code change is automatically built, tested, and then deployed to a non-production testing or staging environment. Manual approval is required before pushing to production. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process.

Continuous deployment is similar to continuous delivery, but with automatic deployment to production. Tested code does not need an explicit approval before being pushed to production.

5. **Microservices architecture**

A microservices architecture, is a design approach that builds an application as a set of loosely coupled services. Each service is designed for a set of capabilities and focuses on solving a specific business problem. Services do not need to share any of their code or implementation with other services. Any communication between individual components happens via well-defined APIs. These services can be assigned to fully accountable teams, and be developed, tested, an deployed independently of other services.

According to research from DevOps Research and Assessment (DORA), the type of architecture the team settles on, is a direct predictor of how successful they will be with achieving continuous delivery. The nature of microservices supports faster development, updates and corrections, and quicker deployments.

6. **Infrastructure as Code**

Development, testing, and production run on complex environments comprised of hardware and software. Manually spinning up and setting environments does not scale and is error prone. 

Infrastructure as code (IaC) is a practice in which infrastructure is provisioned and managed using code and software development techniques, such as version control and continuous integration.

The cloud’s API-driven model enables developers and system administrators to interact with infrastructure programmatically, and at scale, instead of needing to manually set up and configure resources. Because environments are defined by code, they can quickly be deployed with dynamically enforced compliance, updated with the latest patches, rolled back to a previous version, or duplicated in repeatable ways. Also, by reacting to environment changes through modification to this code, you can track changes, optimize resources, and improve system uptime. 


A DevOps pipeline is a set of stages that move code from source, all the way to deployment. The graphic that follows depicts typical stages in a DevOps pipeline and depicts the phases involved in a CI/CD pipeline.

![DevOps Pipeline](images/devops_pipeline.png)

A CI/CD pipeline is a good example of how DevOps teams use tools to streamline workflows and standardize practices. A CI/CD pipeline assures code quality, security, and fast, consistent deployments by repeatably progressing through the pipeline. DevOps teams iteratively remove process overlaps, human errors, and bottlenecks through automation.

Every DevOps team requires an efficient and reliable CI/CD pipeline. A CI/CD pipeline requires a well-integrated tool chain. 


## DevOps Tools
