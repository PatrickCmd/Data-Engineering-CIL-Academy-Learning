# AWS CLI

- [AWS CLI UserGuide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
- [Installation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS Command Line Interface Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [aws-cli V2](https://github.com/aws/aws-cli/tree/v2)

**AWS CLI CheatSheets

- [AWS CLI V1 - CheatSheet - bluematador](https://www.bluematador.com/learn/aws-cli-cheatsheet#What-is-the-AWS-CLI?)


**Confirm installed inversion**

```sh
aws --version
```

**Configuring the AWS CLI**

Follow link [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for more details.

**Command structure in the AWS CLI**

```
aws <command> <subcommand> [options and parameters]
```

The following example lists all of your Amazon S3 buckets.

```sh
aws s3 ls
```

## Amazon EC2 CLI

To list the AWS CLI commands for Amazon EC2, use the following command.

```sh
aws ec2 help
```

For long-form examples of AWS CLI commands, see [AWS CLI code examples repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli) on GitHub

### Creating, displaying, and deleting Amazon EC2 key pairs

**[Create Keypair](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html)**

To create a key pair, use the [aws ec2 create-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-key-pair.html) command with the `--query` option, and the `--output` text option to pipe your private key directly into a file.

```sh
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem
```

**E.g**

```sh
aws ec2 create-key-pair --key-name dataEC2Key --query 'KeyMaterial' --output text > dataEC2Key.pem
```

For PowerShell, the `> file` redirection defaults to `UTF-8` encoding, which cannot be used with some SSH clients. So, you must convert the output by piping it to the out-file command and explicitly set the encoding to ascii.

```sh
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text | out-file -encoding ascii -filepath MyKeyPair.pem
```

Your private key isn't stored in AWS and can be retrieved only when it's created. You can't recover it later. Instead, if you lose the private key, you must create a new key pair.

If you're connecting to your instance from a Linux computer, we recommend that you use the following command to set the permissions of your private key file so that only you can read it.

```sh
chmod 400 MyKeyPair.pem
```

**Display your key pair**

The following example displays the fingerprint for MyKeyPair

```sh
aws ec2 describe-key-pairs --key-name MyKeyPair
```

```sh
aws ec2 describe-key-pairs --key-name dataEC2Key
```

**Delete your key pair**

To delete a key pair, run the [aws ec2 delete-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-key-pair.html) command, substituting `MyKeyPair` with the name of the pair to delete.

```sh
aws ec2 delete-key-pair --key-name MyKeyPair
```

```sh
aws ec2 delete-key-pair --key-name dataEC2Key
```

### [Creating, configuring, and deleting security groups for Amazon EC2](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html)

You can create a security group for your Amazon Elastic Compute Cloud (Amazon EC2) instances that essentially operates as a firewall, with rules that determine what network traffic can enter and leave.

**Create a security group**

You can create security groups associated with virtual private clouds (VPCs) .

The following [aws ec2 create-security-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-security-group.html) example shows how to create a security group for a specified VPC.

```sh
aws ec2 create-security-group --group-name my-sg --description "My security group" --vpc-id vpc-1a2b3c4d
```

**e.g**

```sh
aws ec2 create-security-group --group-name data-ec2-sg --description "data ec2 instance security group" --vpc-id vpc-054f0e96084ac7d49
```

To create an EC2-VPC security group and store the output in a variable, you can use the following bash command:

```bash
security_group_id=$(aws ec2 create-security-group --group-name <group_name> --description <description> --vpc-id <vpc_id> --output text --query 'GroupId')
```

Replace `<group_name>` with the desired name for your security group, `<description>` with a brief description, and `<vpc_id>` with the ID of your VPC.

The command uses the AWS CLI to create a security group and assigns the resulting security group ID to the `security_group_id` variable. The `--output text --query 'GroupId'` option ensures that only the GroupId value is returned and stored in the variable.

After running this command, you can access the security group ID using the `$security_group_id` variable in subsequent steps or commands.

```sh
security_group_id=$(aws ec2 create-security-group \
    --group-name data-ec2-sg \
    --description "data ec2 instance security group" \
    --vpc-id vpc-054f0e96084ac7d49 \
    --output text --query 'GroupId')
```

```sh
echo $security_group_id
```

To view the initial information for a security group, run the [aws ec2 describe-security-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html) command. You can reference an EC2-VPC security group only by its vpc-id, not its name.

```sh
aws ec2 describe-security-groups --group-ids sg-903004f8
```

```sh
aws ec2 describe-security-groups --group-ids $security_group_id
```

**Add rules to your security group**

When you run an Amazon EC2 instance, you must enable rules in the security group to allow incoming network traffic for your means of connecting to the image.

For example, if you're launching a Windows instance, you typically add a rule to allow inbound traffic on TCP port 3389 to support Remote Desktop Protocol (RDP). If you're launching a Linux instance, you typically add a rule to allow inbound traffic on TCP port 22 to support SSH connections.

Use the [aws ec2 authorize-security-group-ingress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-security-group-ingress.html) command to add a rule to your security group. A required parameter of this command is the public IP address of your computer, or the network (in the form of an address range) that your computer is attached to, in [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation.

> **Note**
We provide the following service, https://checkip.amazonaws.com/, to enable you to determine your public IP address. To find other services that can help you identify your IP address, use your browser to search for "what is my IP address". If you connect through an ISP or from behind your firewall using a dynamic IP address (through a NAT gateway from a private network), your address can change periodically. In that case, you must find out the range of IP addresses used by client computers.

The following example shows how to add a rule for RDP (TCP port 3389) to an EC2-VPC security group with the ID sg-903004f8 using your IP address.

To start, find your IP address.

```sh
curl https://checkip.amazonaws.com
```

```sh
my_ip=$(curl https://checkip.amazonaws.com)
echo $my_ip
```

You can then add the IP address to your security group by running the `aws ec2 authorize-security-group-ingress` command.

```sh
aws ec2 authorize-security-group-ingress --group-id sg-903004f8 --protocol tcp --port 3389 --cidr x.x.x.x/x
```

```sh
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 3389 --cidr ${my_ip}/24
```

The following command adds another rule to enable SSH to instances in the same security group.

```sh
aws ec2 authorize-security-group-ingress --group-id sg-903004f8 --protocol tcp --port 22 --cidr x.x.x.x/x
```

```sh
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port 22 --cidr ${my_ip}/24
```

To view the changes to the security group, run the [aws ec2 describe-security-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html) command.

```sh
aws ec2 describe-security-groups --group-ids sg-903004f8
```

```sh
aws ec2 describe-security-groups --group-ids $security_group_id
```

**Delete your security group**

To delete a security group, run the [aws ec2 delete-security-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-security-group.html) command.

> **Note**
You can't delete a security group if it's currently attached to an environment.

The following command example deletes an EC2-VPC security group.

```sh
aws ec2 delete-security-group --group-id sg-903004f8
```

```sh
aws ec2 delete-security-group --group-id $security_group_id
```

### Launching, listing, and terminating Amazon EC2 instances

You can use the AWS Command Line Interface (AWS CLI) to launch, list, and terminate Amazon Elastic Compute Cloud (Amazon EC2) instances. 
If you launch an instance that isn't within the AWS Free Tier, you are billed after you launch the instance and charged for the time that 
the instance is running, even if it remains idle.

> **Note**
For additional command examples, see the [AWS CLI reference guide](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).

**Launch your instance**

To launch an Amazon EC2 instance using the AMI you selected, use the [aws ec2 run-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html) command. You can launch the instance into a virtual private cloud (VPC).

Initially, your instance appears in the pending state, but changes to the running state after a few minutes.

The following example shows how to launch a `t2.micro` instance in the specified subnet of a `VPC`. Replace the `italicized` parameter values with your own.

```sh
aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e
```

```sh
instance_name=data-engineer-ec2-instance
key_pair_name=dataEC2Key
instance_id=$(aws ec2 run-instances \
    --image-id ami-053b0d53c279acc90 \
    --count 1 \
    --instance-type t2.micro \
    --key-name $key_pair_name \
    --security-group-ids $security_group_id \
    --subnet-id subnet-035a487bcac05edda \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$instance_name}]" \
    --output text --query 'Instances[0].InstanceId'
)
echo $instance_id
```

**Add a block device to your instance**

Each instance that you launch has an associated root device volume. You can use block device mapping to specify additional `Amazon Elastic Block Store (Amazon EBS)` volumes or instance store volumes to attach to an instance when it's launched.

To add a block device to your instance, specify the `--block-device-mappings` option when you use `run-instances`.

The following example parameter provisions a standard Amazon EBS volume that is 20 GB in size, and maps it to your instance using the identifier `/dev/sdf`.

```sh
--block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"Ebs\":{\"VolumeSize\":20,\"DeleteOnTermination\":false}}]"
```

The following example adds an Amazon EBS volume, mapped to `/dev/sdf`, based on an existing snapshot. A snapshot represents an image that is loaded onto the volume for you. When you specify a snapshot, you don't have to specify a volume size; it will be large enough to hold your image. However, if you do specify a size, it must be greater than or equal to the size of the snapshot.

```sh
--block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"Ebs\":{\"SnapshotId\":\"snap-a1b2c3d4\"}}]"
```

The following example adds two volumes to your instance. The number of volumes available to your instance depends on its instance type.

```sh
--block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"VirtualName\":\"ephemeral0\"},{\"DeviceName\":\"/dev/sdg\",\"VirtualName\":\"ephemeral1\"}]"
```

The following example creates the mapping (/dev/sdj), but doesn't provision a volume for the instance.

```sh
--block-device-mappings "[{\"DeviceName\":\"/dev/sdj\",\"NoDevice\":\"\"}]"
```


**Add a tag to your instance**

A tag is a label that you assign to an AWS resource. It enables you to add metadata to your resources that you can use for a variety of purposes. For more information, see [Tagging Your Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the Amazon EC2 User Guide for Linux Instances.

The following example shows how to add a tag with the key name `"Name"` and the value `"MyInstance"` to the specified instance, by using the [aws ec2 create-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-tags.html) command.

```sh
aws ec2 create-tags --resources i-5203422c --tags Key=Name,Value=MyInstance
```

```sh
aws ec2 create-tags --resources $instance_id --tags Key=Name,Value=$instance_name
```

**Connect to your instance**

When your instance is running, you can connect to it and use it just as you'd use a computer sitting in front of you. For more information, see Connect to Your [Amazon EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the Amazon EC2 User Guide for Linux Instances.


**List your instances**

You can use the AWS CLI to list your instances and view information about them. You can list all your instances, or filter the results based on the instances that you're interested in.

The following examples show how to use the [aws ec2 describe-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html) command.

The following command lists all your instances.

```sh
aws ec2 describe-instances
```

The following command filters the list to only your `t2.micro` instances and outputs only the `InstanceId` values for each match.

```sh
aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"
```

The following command lists any of your instances that have the tag `Name=MyInstance`.

```sh
aws ec2 describe-instances --filters "Name=tag:Name,Values=MyInstance"
```

```sh
aws ec2 describe-instances --filters "Name=tag:Name,Values=$instance_name"
```

```sh
aws ec2 describe-instances --filters "Name=tag:Name,Values=$instance_name" --query "Reservations[].Instances[].InstanceId"
```

The following command lists your instances that were launched using any of the following AMIs: `ami-x0123456`, `ami-y0123456`, and `ami-z0123456`.

```sh
aws ec2 describe-instances --filters "Name=image-id,Values=ami-x0123456,ami-y0123456,ami-z0123456"
```

```sh
image_id=ami-053b0d53c279acc90
aws ec2 describe-instances --filters "Name=image-id,Values=$image_id" --query "Reservations[].Instances[].InstanceId" --output text
```

**Terminate/Stop your instance**

Terminating an instance deletes it. You can't reconnect to an instance after you've terminated it.

Stopping an instance doesn't delete it. You can reconnect to an instance aafter you have stopped it.

As soon as the state of the instance changes to `shutting-down` or `terminated`, you stop incurring charges for that instance. 
If you want to reconnect to an instance later, use [stop-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/stop-instances.html) instead of `terminate-instances`. For more information, see [Terminate Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html) in the Amazon EC2 User Guide for Linux Instances.

To delete an instance, you use the command [aws ec2 terminate-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-instances.html) to delete it.

```sh
aws ec2 terminate-instances --instance-ids i-5203422c
```

```sh
aws ec2 terminate-instances --instance-ids $instance_id
```

To stop an instance, you use the command [aws ec2 stop-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/stop-instances.html) to stop it.

```sh
aws ec2 stop-instances --instance-ids i-5203422c
```

```sh
aws ec2 stop-instances --instance-ids $instance_id
```

To start a stopped instance, you use the command [aws ec2 start-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/start-instances.html) to start it.

```sh
aws ec2 start-instances --instance-ids i-5203422c
```

```sh
aws ec2 start-instances --instance-ids $instance_id
```
