# Amazon DocumentDB

This demonstration walks through getting started with your first Amazon DocumentDB cluster and shows you how to both load and query your data.

## Preparing the environment

### Create a VPC

The first step in configuring the environment is to create an Amazon Virtual Private Cloud (VPC) to hold the resources for both an Amazon Elastic Compute Cloud (Amazon EC2) instance and the Amazon DocumentDB database.

In this project, the following settings were used:

- Name: Amazon DocumentDB Project
- IPv4 CIDR block: 10.50.0.0/16
- Internet gateway: DocumentDB IGW
- Public route table: DocumentDB Project Public
- Private route table: DocumentDB Project Private

The internet gateway and associated route table are for accessing the EC2 instance.

### Create Subnets

Amazon DocumentDB is a managed service that connects to subnets in your VPC.

In this project, the following settings were used:

- **Private subnet 1**
    - Name: DocumentDB Private 01
    - CIDR: 10.50.101.0/24
    - Route table: DocumentDB Project Private
- **Private subnet 2**
    - Name: DocumentDB Private 02
    - CIDR: 10.50.102.0/24
    - Route table: DocumentDB Project Private
- **Public subnet 1**
    - Name: DocumentDB Public 01
    - CIDR: 10.50.201.0/24
    - Public route table: DocumentDB Project Public

### Create security groups

Security groups control access to EC2 instances and the Amazon DocumentDB database. Two security groups were created: one for an EC2 instance and the other for the Amazon DocumentDB cluster.

In this project, the following settings were used:

- **Group 1**
    - Name: DocumentDB EC2
    - Description: EC2 instance used to access DocumentDB
    - Rule: Allow SSH (port 22) from 0.0.0.0/0 (the Internet)
- **Group 2**
    - Name: DocumentDB access from EC2
    - Description: Restrict access to DocumentDB2
    - Rule: Allow TCP port 27017 from the group "DocumentDB EC2"
You could use a single group for both EC2 and DocumentDB access.

### Create an EC2 instance

You can use any Amazon Machine Image (AMI) for this. Amazon EC2 instances created from AWS AMIs have the AWS Command Line Interface (AWS CLI) tools preinstalled.

In this project, the following settings were used:

- VPC: Amazon DocumentDB Project
- Subnet: DocumentDB Public 01
- Software package: Mongo shell
- TLS security: rds-combined-ca-bundle.pem

Instructions on how to install the Mongo shell can be found here: https://docs.aws.amazon.com/documentdb/latest/developerguide/getting-started.connect.html

### Transport Layer Security (TLS)

Transport Layer Security (TLS) is enabled by default for new Amazon DocumentDB clusters.

The public key is here: https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
For this demo, the downloaded file, rds-combined-ca-bundle.pem, was saved in the home directory.

### Create a subnet group

It is recommended that you place your Amazon DocumentDB database in a private subnet.

In this project, the following settings were used:

- Name: DocumentDB-subnet-group
- Description: Private subnet access for DocumentDB
- VPC: Amazon DocumentDB Project
- Add all private subnets.


### AWS CLI

To launch the simple Amazon DocumentDB project, you'll need to perform several steps using AWS CLI commands. Below are the commands for each step:

Step 1: Create a VPC
```bash
aws ec2 create-vpc --cidr-block 10.50.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Amazon DocumentDB Project}]'
```

Step 2: Create Subnets
```bash
# Private Subnet 1
aws ec2 create-subnet --vpc-id YOUR_VPC_ID --cidr-block 10.50.101.0/24 --availability-zone YOUR_AVAILABILITY_ZONE --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=DocumentDB Private 01}]'

# Private Subnet 2
aws ec2 create-subnet --vpc-id YOUR_VPC_ID --cidr-block 10.50.102.0/24 --availability-zone YOUR_AVAILABILITY_ZONE --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=DocumentDB Private 02}]'

# Public Subnet 1
aws ec2 create-subnet --vpc-id YOUR_VPC_ID --cidr-block 10.50.201.0/24 --availability-zone YOUR_AVAILABILITY_ZONE --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=DocumentDB Public 01}]'
```

Step 3: Create Security Groups
```bash
# Group 1: DocumentDB EC2 Security Group
aws ec2 create-security-group --group-name "DocumentDB EC2" --description "EC2 instance used to access DocumentDB" --vpc-id YOUR_VPC_ID
aws ec2 authorize-security-group-ingress --group-id YOUR_GROUP1_ID --protocol tcp --port 22 --cidr 0.0.0.0/0

# Group 2: DocumentDB Access from EC2 Security Group
aws ec2 create-security-group --group-name "DocumentDB access from EC2" --description "Restrict access to DocumentDB" --vpc-id YOUR_VPC_ID
aws ec2 authorize-security-group-ingress --group-id YOUR_GROUP2_ID --protocol tcp --port 27017 --source-group YOUR_GROUP1_ID
```

Step 4: Create an EC2 Instance
```bash
aws ec2 run-instances --image-id YOUR_AMI_ID --count 1 --instance-type YOUR_INSTANCE_TYPE --key-name YOUR_KEY_PAIR_NAME --subnet-id YOUR_PUBLIC_SUBNET1_ID --security-group-ids YOUR_GROUP1_ID --user-data file://install_mongo_shell.sh
```

Replace `YOUR_AMI_ID`, `YOUR_INSTANCE_TYPE`, `YOUR_KEY_PAIR_NAME`, `YOUR_PUBLIC_SUBNET1_ID`, and `YOUR_GROUP1_ID` with appropriate values.

Step 5: Download the TLS certificate and save it in the home directory.
```bash
curl -o ~/rds-combined-ca-bundle.pem https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
```

Step 6: Create a Subnet Group
```bash
aws docdb create-db-subnet-group --db-subnet-group-name DocumentDB-subnet-group --db-subnet-group-description "Private subnet access for DocumentDB" --subnet-ids YOUR_PRIVATE_SUBNET1_ID YOUR_PRIVATE_SUBNET2_ID
```

Replace `YOUR_PRIVATE_SUBNET1_ID` and `YOUR_PRIVATE_SUBNET2_ID` with the appropriate subnet IDs.

Now, you have set up the required components for your Amazon DocumentDB project. Remember to replace the placeholder values in the commands with your actual resource IDs and settings. Also, make sure you have AWS CLI installed and configured with the appropriate IAM credentials to execute these commands.


### Terraform

Terraform configuration that uses modules to create the Amazon DocumentDB project with VPC, subnets, security groups, and EC2 instance. Before you use Terraform, make sure you have installed it on your system.

Here's the Terraform configuration:

1. Create a new directory for your Terraform project and create the following files:

- `main.tf`: Main configuration file.
- `variables.tf`: Define input variables.
- `outputs.tf`: Define outputs for easy access to resource information.
- `providers.tf`: Specify the AWS provider.
- `vpc_module`: A directory for the VPC module (contains `main.tf`, `variables.tf`, and `outputs.tf`).
- `ec2_module`: A directory for the EC2 instance module (contains `main.tf`, `variables.tf`, and `outputs.tf`).

2. Here are the contents of each file:

`main.tf`:
```hcl
provider "aws" {
  region = "us-west-2"  # Replace with your desired AWS region
}

module "vpc" {
  source = "./vpc_module"

  vpc_name           = "Amazon DocumentDB Project"
  vpc_cidr           = "10.50.0.0/16"
  public_subnet_cidr = ["10.50.201.0/24"]
  private_subnet_cidr = ["10.50.101.0/24", "10.50.102.0/24"]

  enable_public_subnet_route = true
}

module "ec2_instance" {
  source = "./ec2_module"

  vpc_id              = module.vpc.vpc_id
  public_subnet_id    = module.vpc.public_subnet_ids[0]
  key_name            = "YOUR_KEY_PAIR_NAME"  # Replace with your EC2 key pair name
  ami                 = "YOUR_AMI_ID"  # Replace with your desired EC2 AMI ID
  instance_type       = "YOUR_INSTANCE_TYPE"  # Replace with your desired EC2 instance type
  security_group_ids  = [module.vpc.security_group_id, module.vpc.documentdb_security_group_id]
}
```

`variables.tf`:
```hcl
variable "vpc_name" {
  description = "The name of the VPC."
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC."
}

variable "public_subnet_cidr" {
  description = "The CIDR blocks for public subnets."
  type        = list(string)
}

variable "private_subnet_cidr" {
  description = "The CIDR blocks for private subnets."
  type        = list(string)
}

variable "enable_public_subnet_route" {
  description = "Enable public subnet route for Internet Gateway."
  default     = true
}

variable "key_name" {
  description = "The name of the EC2 key pair."
}

variable "ami" {
  description = "The ID of the AMI to use for the EC2 instance."
}

variable "instance_type" {
  description = "The type of instance to start."
}

variable "security_group_ids" {
  description = "The security group IDs for EC2 instances."
  type        = list(string)
}
```

`outputs.tf`:
```hcl
output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnet_ids" {
  value = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  value = module.vpc.private_subnet_ids
}

output "ec2_instance_id" {
  value = module.ec2_instance.instance_id
}
```

`providers.tf`:
```hcl
provider "aws" {
  region = "us-west-2"  # Replace with your desired AWS region
}
```

`vpc_module/main.tf`:
```hcl
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr

  tags = {
    Name = var.vpc_name
  }
}

resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidr)

  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidr[count.index]
  map_public_ip_on_launch = var.enable_public_subnet_route

  tags = {
    Name = "DocumentDB Public 0${count.index + 1}"
  }
}

resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidr)

  vpc_id     = aws_vpc.main.id
  cidr_block = var.private_subnet_cidr[count.index]

  tags = {
    Name = "DocumentDB Private 0${count.index + 1}"
  }
}

resource "aws_security_group" "ec2" {
  name_prefix = "DocumentDB EC2"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "documentdb" {
  name_prefix = "DocumentDB access from EC2"

  ingress {
    from_port       = 27017
    to_port         = 27017
    protocol        = "tcp"
    security_groups = [aws_security_group.ec2.id]
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "security_group_id" {
  value = aws_security_group.ec2.id
}

output "documentdb_security_group_id" {
  value = aws_security_group.documentdb.id
}
```

`vpc_module/variables.tf`:
```hcl
variable "vpc_name" {
  description = "The name of the VPC."
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC."
}

variable "public_subnet_cidr" {
  description = "The CIDR blocks for public subnets."
  type        = list(string)
}

variable "private_subnet_cidr" {
  description = "The CIDR blocks for private subnets."
  type        = list(string)
}

variable "enable_public_subnet_route" {
  description = "Enable public subnet route for Internet Gateway."
  default     = true
}
```

`vpc_module/outputs.tf`:
```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "security_group_id" {
  value = aws_security_group.ec2.id
}

output "documentdb_security_group_id" {
  value = aws_security_group.documentdb.id
}
```

`ec2_module/main.tf`:
```hcl
resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = var.public_subnet_id
  key_name      = var.key_name

  security_groups = var.security_group_ids

  user_data = <<-

EOF
              #!/bin/bash
              curl -o ~/rds-combined-ca-bundle.pem https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
              EOF

  tags = {
    Name = "DocumentDB EC2 Instance"
  }
}

output "instance_id" {
  value = aws_instance.example.id
}
```

`ec2_module/variables.tf`:
```hcl
variable "vpc_id" {
  description = "The ID of the VPC."
}

variable "public_subnet_id" {
  description = "The ID of the public subnet."
}

variable "key_name" {
  description = "The name of the EC2 key pair."
}

variable "ami" {
  description = "The ID of the AMI to use for the EC2 instance."
}

variable "instance_type" {
  description = "The type of instance to start."
}

variable "security_group_ids" {
  description = "The security group IDs for EC2 instances."
  type        = list(string)
}
```

`ec2_module/outputs.tf`:
```hcl
output "instance_id" {
  value = aws_instance.example.id
}
```

3. Replace the placeholders in the `main.tf` file with your desired values for the EC2 instance.

4. Run `terraform init` to initialize the working directory.

5. Run `terraform apply` to create the Amazon DocumentDB project.

Note: This is a basic configuration, and you might need to further customize it based on your specific requirements. Additionally, for the TLS certificate, you can download it during the instance user data execution or use AWS Secrets Manager to manage the certificate securely.


### CloudFormation

To launch the Amazon DocumentDB project using AWS CloudFormation, you can create a CloudFormation template in YAML or JSON format. Here, I'll provide a YAML template as an example:

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Amazon DocumentDB Project"

Parameters:
  VpcCidrBlock:
    Type: String
    Description: "CIDR block for the VPC"
    Default: "10.50.0.0/16"

  PublicSubnetCidrBlock1:
    Type: String
    Description: "CIDR block for Public Subnet 1"
    Default: "10.50.201.0/24"

  PrivateSubnetCidrBlock1:
    Type: String
    Description: "CIDR block for Private Subnet 1"
    Default: "10.50.101.0/24"

  PrivateSubnetCidrBlock2:
    Type: String
    Description: "CIDR block for Private Subnet 2"
    Default: "10.50.102.0/24"

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCidrBlock
      Tags:
        - Key: Name
          Value: "Amazon DocumentDB Project"

  InternetGateway:
    Type: AWS::EC2::InternetGateway

  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: "DocumentDB Project Public"

  PublicRoute:
    Type: AWS::EC2::Route
    DependsOn: VPCGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: "0.0.0.0/0"
      GatewayId: !Ref InternetGateway

  PublicSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PublicSubnetCidrBlock1
      AvailabilityZone: !Select [0, !GetAZs ""]
      Tags:
        - Key: Name
          Value: "DocumentDB Public 01"

  PrivateSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PrivateSubnetCidrBlock1
      AvailabilityZone: !Select [0, !GetAZs ""]
      Tags:
        - Key: Name
          Value: "DocumentDB Private 01"

  PrivateSubnet2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Ref PrivateSubnetCidrBlock2
      AvailabilityZone: !Select [1, !GetAZs ""]
      Tags:
        - Key: Name
          Value: "DocumentDB Private 02"

  DocumentDBEC2SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: "DocumentDB EC2"
      GroupDescription: "EC2 instance used to access DocumentDB"
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: "0.0.0.0/0"

  DocumentDBSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: "DocumentDB access from EC2"
      GroupDescription: "Restrict access to DocumentDB"
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 27017
          ToPort: 27017
          SourceSecurityGroupId: !Ref DocumentDBEC2SecurityGroup

  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: "YOUR_AMI_ID"  # Replace with your desired EC2 AMI ID
      InstanceType: "YOUR_INSTANCE_TYPE"  # Replace with your desired EC2 instance type
      KeyName: "YOUR_KEY_PAIR_NAME"  # Replace with your EC2 key pair name
      SubnetId: !Ref PublicSubnet1
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          curl -o /home/ec2-user/rds-combined-ca-bundle.pem https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem

Outputs:
  VpcId:
    Value: !Ref VPC

  PublicSubnetIds:
    Value:
      - !Ref PublicSubnet1

  PrivateSubnetIds:
    Value:
      - !Ref PrivateSubnet1
      - !Ref PrivateSubnet2

  EC2InstanceId:
    Value: !Ref EC2Instance
```

Make sure to replace `YOUR_AMI_ID`, `YOUR_INSTANCE_TYPE`, and `YOUR_KEY_PAIR_NAME` with your desired values for the EC2 instance.

To launch this CloudFormation stack:

1. Save the above YAML template to a file (e.g., `documentdb-project.yaml`).

2. Go to the AWS Management Console, navigate to the CloudFormation service.

3. Click "Create stack" and choose "With new resources (standard)".

4. Upload the `documentdb-project.yaml` file.

5. Follow the wizard to provide parameter values and create the stack.

AWS CloudFormation will then create the resources for your Amazon DocumentDB project based on the specified template.
