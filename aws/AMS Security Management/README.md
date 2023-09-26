# AWS Managed Services (AMS): Security Management

- [Introduction to AMS Security](#introduction-to-ams-security)
  * [What is the AMS security process?](#what-is-the-ams-security-process-)
  * [The AMS shared responsibility model](#the-ams-shared-responsibility-model)
    + [Responsibilities](#responsibilities)
- [AMS Security Principles](#ams-security-principles)
  * [What are the AMS security principles?](#what-are-the-ams-security-principles-)
  * [Protections provided through security principles](#protections-provided-through-security-principles)
- [AMS Security Controls](#ams-security-controls)
  * [What are the controls applied by AMS?](#what-are-the-controls-applied-by-ams-)
    + [Examples from each of the control groups](#examples-from-each-of-the-control-groups)
- [Governance and Compliance](#governance-and-compliance)
  * [What is governance and compliance?](#what-is-governance-and-compliance-)
  * [How does AMS help with compliance?](#how-does-ams-help-with-compliance-)
- [Conclusion](#conclusion)
  * [Why is the security management process important?](#why-is-the-security-management-process-important-)

## Introduction to AMS Security
### What is the AMS security process?
Security management is the process by which AMS identifies an organization's assets, and then implements policies and procedures to protect them. AMS works to deliver a secure environment and set of processes that allow you to innovate and deliver your products and services with confidence.

### The AMS shared responsibility model
#### Responsibilities
- **AMS Responsibilities**: **AMS** is responsible and accountable for infrastructure-related incidents that are detected by you or our systems.
    - Operating systems
    - Network configuration
    - Firewall rules
    - Identity and access management
    - Data encryption
- **Customer Responsibilities**: Application-specific incidents remain **your** responsibility.

## AMS Security Principles
### What are the AMS security principles?

AMS applies four distinct principles to its practices and processes to improve the security of your managed environments. These principles are:
1. Secure by default
2. Least privilege
3. Just-in-time access
4. Assume breach

AMS builds processes around security activities that present high risk to your environment and often prove difficult to implement correctly. These include repeatable activities, as well as undifferentiated tasks, that are best addressed through automation.

### Protections provided through security principles
**Secure by default:**
- Secure configuration of environment (AWS account, Microsoft Active Directory federation)
- Secure configuration of resources (Amazon Machine Image (AMI)/operating systems)
- Secure access model (applies to your engineers as well as AMS engineers)
- Baselining (international standards, hardened AMIs)
- Defense in depth (many layers of protection, network, identity and access management)

**Least privilege**
- Applies to IAM, as well as Active Directory via federation
- Only the rights needed to perform action are granted
- Limited number of users
- Privileges to be granted are regularly reviewed

**Just-in-time access**
- Non-persistent access
- Time-limited access
- Applies to both your engineers and AMS engineers

**Assume breach**
- Holistic view of your accounts including AMS deployed infrastructure
- Every supported resource in your account is monitored

## AMS Security Controls
### What are the controls applied by AMS?
AMS automates a family of security controls that is applied to your managed account. A control is an individual protection put in place to limit the risk of breach to your environment. 

Controls are organized into logical groups: 

- Protective
- Detective
- Adaptive
- Responsive

#### Examples from each of the control groups
**Protective:**
- Managed Trend Micro (antivirus, anti-malware, intrusion detection/prevention)
- Patch management
- Just-in-time access
- Security groups
- Change management
- Legislative checks (GDPR, financial conduct authorities)
- Separation of duties
- Validation of compliance (HIPPA, PCI)
- Logging and audit

**Detective:**:
- All activity in AWS accounts monitored
- Log aggregation
- Netflow, Amazon Simple Storage Service (Amazon S3), API calls
- Evolution of AWS Cloud (e.g., adding new Regions)
- Unauthorized changes, whether malicious, accidental, or well-intentioned
- Introduction of previously unused services to your account
- Changes to all resources
- Preservation of audit data
- Related events/alerts combined into master incidents
- "Big picture" view of managed accounts

**Adaptive:**
- Network activity and traffic volume
- Endpoints and ports
- Reconnaissance and exploratory  activities
- Data exfiltration and destruction
- Time of day/type of activity patterns
- Data centers and geographical location
- IP address

**Responsive:**
- Profile network activity and identity behavior
- Identify problematic behavior
- Identify unused paths/rules
- Automated lockdown of network perimeter
- Automated lockdown of resources via antivirus/anti-malware
- Identify change freeze windows, etc.
- Provide automated lenience under stress conditions

## Governance and Compliance
### What is governance and compliance?
Governance and compliance have a symbiotic relationship. Governance establishes the guardrails and strategy for meeting business objectives. Compliance is the process of ensuring application of the business objectives defined by governance. The result is that your environment is meeting your business objectives. 

### How does AMS help with compliance?
**Proactive monitoring**: AMS will monitor your environment and either take proactive action or alert you of any findings. How AMS acts on findings is agreed to during the onboarding process.

**AWS Management Console**: You can log into the AWS Management Console to interact directly with the compliance tools such as Amazon GuardDuty, Amazon CloudWatch, and AWS Config.

**Internal tooling**: If your organization’s internal tools support it, you can ingest this data to perform your own compliance monitoring. Then, take action using requests for change and change types with AMS.

## Conclusion
### Why is the security management process important?

Proper application of information security controls remains a challenge for many organizations. AMS addresses these challenges by automating the processes that are necessary to secure your accounts.

By establishing security principles that create a template for your environment and applying a wide set of security controls through repeatable processes, AMS builds your account using a secure framework. In addition, AMS establishes the monitoring necessary to detect and respond to deviation from your baseline.
