# Amazon Neptune

Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine optimized for storing billions of relationships and querying the graph with milliseconds latency.

- [**Neptune website**](https://aws.amazon.com/neptune/)

Amazon Neptune is a dynamic tool that should be implemented in situations where the data is not only highly connected but also requires queries that exploit this connected structure. There are many design, development, and performance benefits to using a graph database optimized for graph workloads.

- [**Neptune developer resources**](https://docs.aws.amazon.com/neptune/latest/userguide/get-started.html)

## Service Demonstration

This demonstration walks through how to get started with your first Amazon Neptune cluster, including loading and verifying that the data is in the database.

### Preparing the environment

#### Create a VPC

The first step in configuring your environment is to create a virtual private cloud (VPC) to hold the resources for both your Amazon Elastic Compute Cloud (Amazon EC2) instance and the Neptune database.

In this project, the following settings were used:

- Name tag: Amazon Neptune Project
- IPv4 CIDR block: 10.40.0.0/16

#### Create the subnets

Neptune requires two subnets in two different Availability Zones for high availability. This project also uses a public subnet for the EC2 instance itself.

In this project, the following settings were used:

- **Private subnet 1**
    - Name: Neptune Project Private Subnet 01
    - CIDR: 10.40.101.0/24
- **Private subnet 2**
    - Name: Neptune Project Private Subnet 02
    - CIDR: 10.40.102.0/24
- **Public subnet**
    - Name: Neptune Project Public Subnet
    - CIDR: 10.40.201.0/24

#### Create an Amazon EC2 instance
You can use any Amazon Machine Image (AMI) for this.

In this project, the following settings were used:

- The instance was placed in the Neptune Project VPC.
- The instance was placed in the Neptune Project Public Subnet.

#### Create security groups

Security groups are what control who has access to the EC2 instance and Neptune database.

In this project, the following settings were used:

- **Group 1**
    - Security group name: EC2 for Neptune
    - Description: SSH access to EC2 for Neptune Project
    - Add a rule using SSH port 22 and select My IP.
- **Group 2**
    - Security group name: Neptune DB Access
    - Description: Access from EC2
    - Add a rule using the custom TCP port 8182 and select the EC2 for Neptune security group.

#### Create an IAM role 

Neptune requires an AWS Identity and Access Management (IAM) role. This role must allow Neptune to access Amazon Simple Storage Service (Amazon S3) for loading data.

For all of the required steps, see https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM.html.

In this project, the following settings were used:

- Role name: NeptuneLoadfromS3

#### AWS CLI

To launch the simple Neptune project described above using the AWS CLI, you will need to perform several steps. Below is the AWS CLI commands to create the necessary resources:

1. Create a VPC:

```bash
aws ec2 create-vpc --cidr-block 10.40.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Amazon Neptune Project}]'
```

2. Create subnets:

```bash
# Private subnet 1
aws ec2 create-subnet --vpc-id <VPC_ID> --cidr-block 10.40.101.0/24 --availability-zone <AVAILABILITY_ZONE_1> --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Neptune Project Private Subnet 01}]'

# Private subnet 2
aws ec2 create-subnet --vpc-id <VPC_ID> --cidr-block 10.40.102.0/24 --availability-zone <AVAILABILITY_ZONE_2> --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Neptune Project Private Subnet 02}]'

# Public subnet
aws ec2 create-subnet --vpc-id <VPC_ID> --cidr-block 10.40.201.0/24 --availability-zone <AVAILABILITY_ZONE_1> --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Neptune Project Public Subnet}]'
```

Replace `<VPC_ID>` with the ID of the created VPC and `<AVAILABILITY_ZONE_1>` and `<AVAILABILITY_ZONE_2>` with the desired Availability Zones for the private subnets.

3. Create an Amazon EC2 instance:

```bash
aws ec2 run-instances --image-id <AMI_ID> --instance-type <INSTANCE_TYPE> --subnet-id <PUBLIC_SUBNET_ID> --security-group-ids <SECURITY_GROUP_1_ID> --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Neptune Project EC2}]'
```

Replace `<AMI_ID>` with the ID of the desired Amazon Machine Image, `<INSTANCE_TYPE>` with the desired EC2 instance type, `<PUBLIC_SUBNET_ID>` with the ID of the public subnet created in step 2, and `<SECURITY_GROUP_1_ID>` with the ID of "Group 1" security group.

4. Create security groups:

```bash
# Group 1 - EC2 for Neptune
aws ec2 create-security-group --group-name "EC2 for Neptune" --description "SSH access to EC2 for Neptune Project" --vpc-id <VPC_ID>

aws ec2 authorize-security-group-ingress --group-id <SECURITY_GROUP_1_ID> --protocol tcp --port 22 --cidr $(curl -s https://checkip.amazonaws.com)/32

# Group 2 - Neptune DB Access
aws ec2 create-security-group --group-name "Neptune DB Access" --description "Access from EC2" --vpc-id <VPC_ID>

aws ec2 authorize-security-group-ingress --group-id <SECURITY_GROUP_2_ID> --protocol tcp --port 8182 --source-group <SECURITY_GROUP_1_ID>
```

Replace `<VPC_ID>` with the ID of the created VPC, `<SECURITY_GROUP_1_ID>` with the ID of the "Group 1" security group, and `<SECURITY_GROUP_2_ID>` with the ID of the "Group 2" security group.

5. Create an IAM role:

Since IAM roles require additional configuration using IAM policies, the steps are beyond the scope of a single CLI command. Please follow the official documentation link provided in the project description to create the IAM role "NeptuneLoadfromS3" with the necessary permissions.

Remember to replace the placeholder values (e.g., `<VPC_ID>`, `<AMI_ID>`, `<INSTANCE_TYPE>`, etc.) with actual values specific to your AWS account and desired configurations.

#### Terraform

To create the AWS infrastructure using Terraform, we'll break down the resources into modules to organize the code better. Before proceeding, make sure you have Terraform installed and configured with appropriate AWS credentials.

Create the following directory structure:

```
neptune_project/
  ├── main.tf
  ├── variables.tf
  ├── outputs.tf
  ├── ec2_instance/
  │   ├── main.tf
  │   ├── variables.tf
  │   └── outputs.tf
  ├── security_groups/
  │   ├── main.tf
  │   ├── variables.tf
  │   └── outputs.tf
  └── iam_role/
      ├── main.tf
      ├── variables.tf
      └── outputs.tf
```

Below are the contents of each file:

1. `neptune_project/main.tf`

```hcl
provider "aws" {
  region = "us-west-2"  # Change to your desired region
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "3.6.0"
  
  name = "Amazon Neptune Project"
  cidr = "10.40.0.0/16"
}

module "subnets" {
  source = "terraform-aws-modules/subnet/aws"
  version = "3.0.0"
  
  vpc_id = module.vpc.vpc_id

  private_subnets = [
    {
      cidr = "10.40.101.0/24"
      availability_zone = "us-west-2a"  # Change to your desired AZ
      tags = {
        Name = "Neptune Project Private Subnet 01"
      }
    },
    {
      cidr = "10.40.102.0/24"
      availability_zone = "us-west-2b"  # Change to your desired AZ
      tags = {
        Name = "Neptune Project Private Subnet 02"
      }
    },
  ]

  public_subnets = [
    {
      cidr = "10.40.201.0/24"
      availability_zone = "us-west-2a"  # Change to your desired AZ
      tags = {
        Name = "Neptune Project Public Subnet"
      }
    },
  ]
}

module "ec2_instance" {
  source = "./ec2_instance"
  subnet_id = module.subnets.public_subnets[0].id
  security_group_ids = [module.security_groups.ec2_for_neptune_security_group_id]
  ami = "ami-0c55b159cbfafe1f0"  # Replace with your desired AMI ID
}

module "security_groups" {
  source = "./security_groups"
  vpc_id = module.vpc.vpc_id
  ssh_cidr_block = var.ssh_cidr_block
}

module "iam_role" {
  source = "./iam_role"
}
```

2. `neptune_project/variables.tf`

```hcl
variable "ssh_cidr_block" {
  description = "The SSH CIDR block to allow access to EC2 instance."
  default = "0.0.0.0/0"  # Allow SSH access from anywhere. Update to restrict access if needed.
}
```

3. `neptune_project/outputs.tf`

```hcl
output "neptune_project_vpc_id" {
  value = module.vpc.vpc_id
}

output "neptune_project_public_subnets" {
  value = module.subnets.public_subnets[*].id
}

output "neptune_project_ec2_instance_id" {
  value = module.ec2_instance.ec2_instance_id
}
```

4. `neptune_project/ec2_instance/main.tf`

```hcl
resource "aws_instance" "ec2" {
  ami           = var.ami
  instance_type = "t2.micro"
  subnet_id     = var.subnet_id
  vpc_security_group_ids = var.security_group_ids
  tags = {
    Name = "Neptune Project EC2"
  }
}
```

5. `neptune_project/ec2_instance/variables.tf`

```hcl
variable "subnet_id" {
  description = "The ID of the public subnet where the EC2 instance will be placed."
}

variable "security_group_ids" {
  description = "The list of security group IDs for the EC2 instance."
}

variable "ami" {
  description = "The AMI ID for the EC2 instance."
}
```

6. `neptune_project/security_groups/main.tf`

```hcl
resource "aws_security_group" "ec2_for_neptune" {
  name_prefix = "EC2 for Neptune"
  description = "SSH access to EC2 for Neptune Project"
  vpc_id      = var.vpc_id

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_cidr_block]
  }
}

resource "aws_security_group" "neptune_db_access" {
  name_prefix = "Neptune DB Access"
  description = "Access from EC2"
  vpc_id      = var.vpc_id

  ingress {
    description = "Access from EC2"
    from_port   = 8182
    to_port     = 8182
    protocol    = "tcp"
    security_groups = [aws_security_group.ec2_for_neptune.id]
  }
}
```

7. `neptune_project/security_groups/variables.tf`

```hcl
variable "vpc_id" {
  description = "The ID of the VPC where the security groups will be created."
}

variable "ssh_cidr_block" {
  description = "The SSH CIDR block to allow access to EC2 instance."
  default = "0.0.0.0/0"  # Allow SSH access from anywhere. Update to restrict access if needed.
}
```

8. `neptune_project/iam_role/main.tf`

```hcl
resource "aws_iam_role" "neptune_load_from_s3" {
  name = "NeptuneLoadfromS3"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "neptune.amazonaws.com"
        }
      }
    ]
  })
}
```

9. `neptune_project/iam_role/variables.tf`

```hcl
# No variables required for this module, but you can add them if needed in the future.
```

Now you have the Terraform configuration using modules to create the Neptune project infrastructure. After running `terraform init`, `terraform apply`, the resources will be provisioned on AWS. Remember to replace any placeholder values like `ami` in `neptune_project/main.tf` with your desired AMI ID.

Make sure to check the Terraform documentation for the module sources `terraform-aws-modules/vpc/aws`, `terraform-aws-modules/subnet/aws`, or use different versions depending on your Terraform version and requirements.


### More resources
- [**Getting started with Neptune**](https://docs.aws.amazon.com/neptune/latest/userguide/get-started.html)
- [**Loading data into Neptune**](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html)
- [**Creating the required IAM role**](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM.html): This page takes you through the steps to create and configure the required IAM role for allowing Neptune to access Amazon S3 for loading data.
