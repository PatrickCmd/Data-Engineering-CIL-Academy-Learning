To refactor the Terraform script into a network module, we will split the code into different files: `variables.tf`, `main.tf`, and `outputs.tf`. This will make the code modular and reusable. Here's how you can do it:

1. Create a directory named `network` and add the following files in that directory:

`network/variables.tf`:
```hcl
variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_1_cidr_block" {
  description = "CIDR block for Public Subnet 1"
  type        = string
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr_block" {
  description = "CIDR block for Public Subnet 2"
  type        = string
  default     = "10.0.2.0/24"
}

variable "private_subnet_1_cidr_block" {
  description = "CIDR block for Private Subnet 1"
  type        = string
  default     = "10.0.3.0/24"
}

variable "private_subnet_2_cidr_block" {
  description = "CIDR block for Private Subnet 2"
  type        = string
  default     = "10.0.4.0/24"
}
```

`network/main.tf`:
```hcl
resource "aws_vpc" "my_vpc" {
  cidr_block = var.vpc_cidr_block
  tags = {
    Name = "MyVPC"
  }
}

resource "aws_subnet" "public_subnet_1" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = var.public_subnet_1_cidr_block
  availability_zone = "us-east-1a"
  tags = {
    Name = "PublicSubnet1"
  }
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = var.public_subnet_2_cidr_block
  availability_zone = "us-east-1b"
  tags = {
    Name = "PublicSubnet2"
  }
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = var.private_subnet_1_cidr_block
  availability_zone = "us-east-1a"
  tags = {
    Name = "PrivateSubnet1"
  }
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = var.private_subnet_2_cidr_block
  availability_zone = "us-east-1b"
  tags = {
    Name = "PrivateSubnet2"
  }
}

resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "MyIGW"
  }
}

resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "PublicRouteTable"
  }
}

resource "aws_route" "public_route" {
  route_table_id         = aws_route_table.public_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.my_igw.id
}

resource "aws_route_table_association" "public_subnet_1_association" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table_association" "public_subnet_2_association" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_eip" "nat_eip" {
  vpc = true
}

resource "aws_nat_gateway" "nat_gateway" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public_subnet_1.id
}

resource "aws_route_table" "private_route_table_1" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "PrivateRouteTable1"
  }
}

resource "aws_route_table_association" "private_subnet_1_association" {
  subnet_id      = aws_subnet.private_subnet_1.id
  route_table_id = aws_route_table.private_route_table_1.id
}

resource "aws_route" "private_route" {
  route_table_id         = aws_route_table.private_route_table_1.id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = aws_nat_gateway.nat_gateway.id
}

resource "aws_route_table" "private_route_table_2" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "PrivateRouteTable2"
  }
}

resource "aws_route_table_association" "private_subnet_2_association" {
  subnet_id      = aws_subnet.private_subnet_2.id
  route_table_id = aws_route_table.private_route_table_2.id
}

resource "aws_route" "private_route_2" {
  route_table_id         = aws_route_table.private_route_table_2.id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = aws_nat_gateway.nat_gateway.id
}
```

`network/outputs.tf`:
```hcl
output "vpc_id" {
  value = aws_vpc.my_vpc.id
}

output "public_subnet_1_id" {
  value = aws_subnet.public_subnet_1.id
}

output "public_subnet_2_id" {
  value = aws_subnet.public_subnet_2.id
}

output "private_subnet_1_id" {
  value = aws_subnet.private_subnet_1.id
}

output "private_subnet_2_id" {
  value = aws_subnet.private_subnet_2.id
}
```

2. Now, create a new Terraform configuration in a separate directory (e.g., `main`) to use the module:

`main/main.tf`:
```hcl
provider "aws" {
  region = "us-east-1"
}

module "network" {
  source = "../network"  # Replace with the actual path to your network module

  # Customize variables if needed, e.g.:
  vpc_cidr_block           = "10.0.0.0/16"
  public_subnet_1_cidr_block = "10.0.1.0/24"
  public_subnet_2_cidr_block = "10.0.2.0/24"
  private_subnet_1_cidr_block = "10.0.3.0/24"
  private_subnet_2_cidr_block = "10.0.4.0/24"
}
```

3. In your terminal, navigate to the `main` directory and run the following Terra

form commands:

```bash
terraform init
terraform apply
```

This will deploy the network module with the specified configurations. The output will show the IDs of the VPC, public subnets, and private subnets created by the module. You can use these IDs in other modules or resources to build your infrastructure.