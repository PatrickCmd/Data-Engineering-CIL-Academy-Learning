# Amazon ElastiCache - Service Introduction

Amazon ElastiCache offers fully managed Redis and Memcached distributed memory caches. Seamlessly deploy, run, and scale popular open source-compatible in-memory data stores. Build data-intensive apps or improve the performance of your existing apps by retrieving data from high throughput and low latency in-memory data stores.

- [**ElastiCache website**](https://aws.amazon.com/elasticache/)

Amazon ElastiCache works as an in-memory data store to support the most demanding applications requiring sub-millisecond response times. As a fully managed service, you no longer need to perform management tasks such as hardware provisioning, software patching, setup, configuration, monitoring, failure recovery, and backups.

- [**ElastiCache user guides**](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html)

## Service Demonstration

### Preparing the environment

#### Create a VPC

The first step in configuring the environment is to create an Amazon Virtual Private Cloud (VPC) to hold the resources for both an Amazon Elastic Compute Cloud (Amazon EC2) instance and the ElastiCache cluster.

In this project, the following settings were used:

- Name: Amazon ElastiCache Project
- IPv4 CIDR block: 10.70.0.0/16
- Internet gateway: ElastiCache IGW
- Route table: ElastiCache Project Public 

The internet gateway and associated route table are for accessing the EC2 instance.

To launch a simple Amazon ElastiCache service project with a VPC, an Internet Gateway (IGW), and a public route table, you can use the AWS CLI. Below are the commands to achieve this:

#### Step 1: Create a VPC

```bash
# Create the VPC
aws ec2 create-vpc --cidr-block 10.70.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Amazon ElastiCache Project}]'
```

#### Step 2: Create an Internet Gateway (IGW)

```bash
# Create the Internet Gateway
aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=ElastiCache IGW}]'
```

#### Step 3: Attach the Internet Gateway to the VPC

```bash
# Get the Internet Gateway ID and VPC ID from the previous commands' output
# Replace 'IGW_ID' and 'VPC_ID' with the actual IDs
aws ec2 attach-internet-gateway --internet-gateway-id IGW_ID --vpc-id VPC_ID
```

#### Step 4: Create a public route table

```bash
# Create the public route table
aws ec2 create-route-table --vpc-id VPC_ID --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=ElastiCache Project Public}]'
```

#### Step 5: Create a public route

```bash
# Get the public route table ID from the previous command's output
# Replace 'ROUTE_TABLE_ID' with the actual ID
aws ec2 create-route --route-table-id ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --gateway-id IGW_ID
```

Now, you have set up a VPC with an Internet Gateway and a public route table, which allows access to the internet. The next step would be to launch the Amazon ElastiCache cluster, but since the specific settings for the cluster were not provided, I'll do that in next steps.

#### Create subnets

ElastiCache is a managed service that connects to subnets in your VPC.

In this project, the following settings were used:

- **Private subnet 1**
    - Name: ElastiCache Private 01
    - CIDR: 10.70.101.0/24
- **Private subnet 2**
    - Name: ElastiCache Private 02
    - CIDR: 10.70.102.0/24
- **Public subnet 1**
    - Name: ElastiCache Public 01
    - CIDR: 10.70.201.0/24

To create subnets and associate the public subnet with the public route table, you can use the following AWS CLI commands:

#### Step 1: Create the subnets

```bash
# Create the private subnet 1
aws ec2 create-subnet --vpc-id VPC_ID --cidr-block 10.70.101.0/24 --availability-zone us-east-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=ElastiCache Private 01}]'

# Create the private subnet 2
aws ec2 create-subnet --vpc-id VPC_ID --cidr-block 10.70.102.0/24 --availability-zone us-east-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=ElastiCache Private 02}]'

# Create the public subnet 1
aws ec2 create-subnet --vpc-id VPC_ID --cidr-block 10.70.201.0/24 --availability-zone us-east-1c --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=ElastiCache Public 01}]'
```

#### Step 2: Associate the public subnet with the public route table

```bash
# Describe the route tables to get the ID of the public route table
# Replace 'ElastiCache Project Public' with the name of your public route table if different
aws ec2 describe-route-tables --filters "Name=tag:Name,Values=ElastiCache Project Public"

# Get the public route table ID from the previous command's output
# Replace 'ROUTE_TABLE_ID' with the actual ID
# Replace 'SUBNET_ID' with the ID of the public subnet created in Step 1 for ElastiCache Public 01
aws ec2 associate-route-table --subnet-id SUBNET_ID --route-table-id ROUTE_TABLE_ID
```

Now, the public subnet named "ElastiCache Public 01" is associated with the public route table, which means it can access the internet via the Internet Gateway we created earlier. The two private subnets are ready to be used by Amazon ElastiCache.

#### Create security groups

Security groups control access to EC2 instances and ElastiCache clusters. In this project, two security groups were created: one for the EC2 instance and the other for the ElastiCache cluster.

In this project, the following settings were used:

- **Group 1**
    - Name: ElastiCache EC2
    - Description: SSH access to EC2 instance
    - Rule: Allow SSH (port 22) from 0.0.0.0/0 (the internet)
- **Group 2**
    - Name: ElastiCache Access from EC2
    - Description: ElastiCache Access from EC2
    - Rule: Allow TCP port 6379 from the group "ElastiCache EC2"

You could use a single group for both EC2 and ElastiCache access.

To create the security groups as described, you can use the AWS CLI with the following commands:

#### Step 1: Create the "ElastiCache EC2" Security Group

```bash
# Create the "ElastiCache EC2" security group
aws ec2 create-security-group --group-name "ElastiCache EC2" --description "SSH access to EC2 instance" --vpc-id VPC_ID
```

Note: Replace `VPC_ID` with the actual ID of your VPC.

#### Step 2: Add an inbound rule to allow SSH access from the internet (port 22)

```bash
# Get the "ElastiCache EC2" security group ID from the previous command's output
# Replace 'SECURITY_GROUP_ID' with the actual ID
aws ec2 authorize-security-group-ingress --group-id SECURITY_GROUP_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
```

#### Step 3: Create the "ElastiCache Access from EC2" Security Group

```bash
# Create the "ElastiCache Access from EC2" security group
aws ec2 create-security-group --group-name "ElastiCache Access from EC2" --description "ElastiCache Access from EC2" --vpc-id VPC_ID
```

Note: Replace `VPC_ID` with the actual ID of your VPC.

#### Step 4: Add an inbound rule to allow TCP port 6379 from the "ElastiCache EC2" security group

```bash
# Get the "ElastiCache Access from EC2" and "ElastiCache EC2" security group IDs from the previous commands' outputs
# Replace 'SECURITY_GROUP_ID_1' with the actual ID of "ElastiCache Access from EC2" group
# Replace 'SECURITY_GROUP_ID_2' with the actual ID of "ElastiCache EC2" group
aws ec2 authorize-security-group-ingress --group-id SECURITY_GROUP_ID_1 --protocol tcp --port 6379 --source-group SECURITY_GROUP_ID_2
```

Now, you have created two security groups. The "ElastiCache EC2" group allows SSH access to EC2 instances from the internet, while the "ElastiCache Access from EC2" group allows TCP port 6379 access from instances associated with the "ElastiCache EC2" security group. These security groups can be used for controlling access to both EC2 instances and ElastiCache clusters in your VPC.

#### Create an Amazon EC2 instance

You can use any Amazon Machine Image (AMI) for this. EC2 instances created from AWS AMIs have the AWS Command Line Interface (AWS CLI) tools preinstalled.

In this project, the following settings were used:

- VPC: Amazon ElastiCache Project
- Subnet: ElastiCache Public 01
- Software: Redis CLI

#### Install the Redis CLI

On Amazon Linux, the Redis CLI is available as an "Amazon Linux Extra" topic.

To install:

```sh
sudo amazon-linux-extras install redis4.0
```

For information about Amazon Linux extras, see https://aws.amazon.com/amazon-linux-2/faqs/#Amazon_Linux_Extras.

To launch an EC2 instance and install the Redis CLI on an Amazon Linux instance, follow the steps below:

Step 1: Launch the EC2 Instance

You can use the AWS CLI to launch an Amazon Linux EC2 instance with the following command:

```sh
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxxxx --instance-type t2.micro --key-name YourKeyPair --security-group-ids sg-xxxxxxxx --subnet-id subnet-xxxxxxxx
```

Replace the following placeholders:

- `ami-xxxxxxxxxxxxxxxxx`: The AMI ID of the Amazon Linux image.
- `YourKeyPair`: The name of the key pair you want to use for SSH access.
- `sg-xxxxxxxx`: The security group ID that allows inbound SSH traffic (port 22).
- `subnet-xxxxxxxx`: The subnet ID where you want to launch the instance.

Step 2: SSH into the EC2 Instance

Use SSH to connect to your EC2 instance:

```sh
chmod 400 /path/to/YourKeyPair.pem
ssh -i /path/to/YourKeyPair.pem ec2-user@public_ip_address
```

Replace `/path/to/YourKeyPair.pem` with the path to your private key file and `public_ip_address` with the public IP address of your EC2 instance.

Step 3: Install the Redis CLI

On the Amazon Linux instance, install the Redis CLI using the "Amazon Linux Extras":

```sh
sudo amazon-linux-extras install redis4.0
```

After running this command, the Redis CLI will be installed on your Amazon Linux instance.

Step 4: Test Redis CLI

You can test if the Redis CLI is working by running the following command:

```sh
redis-cli
```


This will start the Redis CLI and connect to the Redis server. You can then use Redis commands to interact with the server.

That's it! You have now launched an Amazon Linux EC2 instance and installed the Redis CLI on it. You can use this instance to work with Redis and perform various operations using the Redis CLI. Remember to stop or terminate the instance when you are done to avoid unnecessary charges.

#### Create a subnet group

It is recommended that you place your ElastiCache database in a private subnet.

In this project, the following settings were used:

- Name: Elasticache-subnet-group
- Description: Private subnet access for Elasticache
- VPC: Amazon Elasticache Project
- Add all private subnets.

To launch an Amazon ElastiCache database in the specified subnet group, follow the steps below:

Step 1: Create a Subnet Group

```bash
# Replace 'Elasticache-subnet-group' and 'Private subnet access for Elasticache' with your desired names
aws elasticache create-cache-subnet-group --cache-subnet-group-name Elasticache-subnet-group --cache-subnet-group-description "Private subnet access for Elasticache" --subnet-ids SUBNET_ID_1 SUBNET_ID_2
```

Replace `Elasticache-subnet-group` with your desired subnet group name and `Private subnet access for Elasticache` with your desired description. Also, replace `SUBNET_ID_1` and `SUBNET_ID_2` with the IDs of the private subnets you want to add to the subnet group. For example:

```bash
aws elasticache create-cache-subnet-group --cache-subnet-group-name Elasticache-subnet-group --cache-subnet-group-description "Private subnet access for Elasticache" --subnet-ids subnet-xxxxxxxx subnet-yyyyyyyy
```

Step 2: Launch an ElastiCache Database

Next, you can use the AWS Management Console or AWS CLI to launch an ElastiCache database (e.g., Redis or Memcached) and associate it with the created subnet group. You will need to choose the subnet group you created in Step 1 during the ElastiCache database setup process.

Note: Since you didn't specify the specific settings for the ElastiCache database in your project description, I cannot provide the exact CLI command for launching the ElastiCache database. However, I can guide you on how to do it through the AWS Management Console:

1. Go to the AWS Management Console and navigate to the ElastiCache service.
2. Click on "Create" to launch a new ElastiCache cluster.
3. Choose the engine you want to use (e.g., Redis or Memcached).
4. In the "Cluster details" section, specify the desired settings for your database, such as node type, number of replicas, etc.
5. In the "Advanced Redis settings" (for Redis) or "Advanced Memcached settings" (for Memcached), select the desired subnet group that you created in Step 1.
6. Complete the setup process by specifying other necessary settings (e.g., security group, parameter group, encryption, etc.).
7. Click on "Create" to launch the ElastiCache database with the specified settings.

Make sure to choose the appropriate security group and parameter group settings based on your requirements. Also, ensure that the security group allows access from your EC2 instances (if needed).

By following these steps, you'll have launched an Amazon ElastiCache database in the specified subnet group with private subnet access.

### Using Terraform

Below is the Terraform configuration to create the resources described earlier, including VPC, subnets, internet gateway, route table, security groups, and Amazon ElastiCache cluster:

First, let's create a directory structure for Terraform modules:

```
project/
├── main.tf
├── variables.tf
├── outputs.tf
├── vpc/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── elasticache/
    ├── main.tf
    ├── variables.tf
    └── outputs.tf
```

Now, let's define the Terraform configuration for each module:

### main.tf (in the root directory)

```hcl
provider "aws" {
  region = "us-east-1"  # Change to your desired region
}

module "vpc" {
  source  = "./vpc"
  vpc_cidr_block = "10.70.0.0/16"
}

module "elasticache" {
  source = "./elasticache"
  vpc_id = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
}
```

### variables.tf (in the root directory)

```hcl
variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  default     = "10.70.0.0/16"
}

variable "private_subnet_cidrs" {
  description = "List of CIDRs for private subnets"
  default     = ["10.70.101.0/24", "10.70.102.0/24"]
}
```

### outputs.tf (in the root directory)

```hcl
output "elasticache_endpoint" {
  value = module.elasticache.elasticache_endpoint
}
```

### vpc/main.tf

```hcl
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = "Amazon ElastiCache Project"
  }
}

resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidrs)
  vpc_id = aws_vpc.main.id
  cidr_block = var.private_subnet_cidrs[count.index]

  tags = {
    Name = "ElastiCache Private ${count.index + 1}"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "ElastiCache IGW"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "ElastiCache Project Public"
  }
}

resource "aws_route" "public_internet" {
  route_table_id = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.main.id
}

resource "aws_route_table_association" "public_subnet_association" {
  count = length(var.private_subnet_cidrs)
  subnet_id = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.public.id
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}
```

### elasticache/main.tf

```hcl
resource "aws_elasticache_subnet_group" "this" {
  name        = "Elasticache-subnet-group"
  description = "Private subnet access for Elasticache"
  subnet_ids  = var.private_subnet_ids
}

resource "aws_security_group" "elasti_cache_ec2" {
  name_prefix = "ElastiCache-EC2"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "elasti_cache_access_from_ec2" {
  name_prefix = "ElastiCache-Access-from-EC2"

  ingress {
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    security_groups = [aws_security_group.elasti_cache_ec2.id]
  }
}

resource "aws_elasticache_cluster" "this" {
  engine           = "redis"
  node_type        = "cache.t2.micro"
  num_cache_nodes  = 1
  port             = 6379
  subnet_group_name = aws_elasticache_subnet_group.this.name

  security_group_ids = [
    aws_security_group.elasti_cache_access_from_ec2.id,
  ]
}

output "elasticache_endpoint" {
  value = aws_elasticache_cluster.this.cache_nodes.0.address
}
```

With this Terraform configuration, you can create the entire infrastructure by running `terraform init`, `terraform plan`, and `terraform apply` commands. The final output will provide you with the ElastiCache endpoint that you can use to connect to the Redis cluster.
