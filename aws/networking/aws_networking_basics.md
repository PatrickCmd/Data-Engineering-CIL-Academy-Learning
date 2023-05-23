# AWS Networking Basics

**Resources**
- [Amazon VPC User guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [AWS Networking Basics for Programmers | Hands On - Travis Media](https://www.youtube.com/watch?v=2doSoMN2xvI)

## What is a VPC and CIDR range?

**A VPC (Virtual Private Cloud**) is a virtual network environment within a cloud computing service such as Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure. It enables you to create a logically isolated section of the cloud where you can launch and manage your virtual servers, storage, and other resources.

**A CIDR (Classless Inter-Domain Routing) range**, often referred to as a `CIDR block`, is a notation used to specify the range of IP addresses that can be assigned to the resources within a VPC. CIDR notation combines the IP address with a prefix length, represented as a slash followed by a number (e.g., /24), which indicates the number of bits used for the network portion of the IP address.

For example, a CIDR range of `10.0.0.0/16` represents a VPC with a network address of `10.0.0.0` and a prefix length of `16 bits`. In this case, the VPC can accommodate up to `65,536` IP addresses (2^16) ranging from `10.0.0.0` to `10.0.255.255`. The prefix length determines the number of available IP addresses within the VPC and can be adjusted to meet specific requirements.

CIDR ranges allow efficient allocation and management of IP addresses within a VPC, as they provide flexibility in defining the size of the network and the number of available IP addresses.

### CIDR range 10.0.0.0/24

The CIDR range `10.0.0.0/24` represents a VPC with a network address of `10.0.0.0` and a prefix length of `24 bits`. In CIDR notation, the prefix length specifies the number of bits in the network portion of the IP address. In this case, the first `24` bits (3 bytes) are dedicated to the network portion, leaving the remaining `8` bits (1 byte) for host addresses.

To understand the range of IP addresses covered by this CIDR block, let's break down the components:

1. Network address: 10.0.0.0
   This is the base address of the network. It represents the starting point of the CIDR block.

2. Prefix length: 24
   The prefix length of 24 indicates that the first 24 bits of the IP address are reserved for the network portion.

Now, let's calculate the range of IP addresses within this CIDR block:

1. The network portion of the IP address remains fixed: 10.0.0.
   The last byte (8 bits) is reserved for host addresses.

2. Host addresses: 0 to 255
   The 8 bits (1 byte) available for host addresses can range from 0 to 255. However, some addresses may be reserved for special purposes, such as network or broadcast addresses.

Combining the network address and the possible host addresses, the range of IP addresses within the CIDR block 10.0.0.0/24 is:
- Starting IP address: 10.0.0.0
- Ending IP address: 10.0.0.255

In this case, there are `256` available IP addresses (`2^8`) for assigning to resources within the VPC, ranging from `10.0.0.0` to `10.0.0.255`.

## What is AWS VPC subnets?

In AWS (Amazon Web Services), a `VPC (Virtual Private Cloud)` subnet is a segmented portion of a VPC's IP address range. Subnets are used to divide a VPC into smaller, more manageable networks within the cloud environment. Each subnet resides in a specific Availability Zone (AZ) and can be associated with different resources, such as EC2 instances or RDS databases.

Here are some key points to understand about AWS VPC subnets:

1. IP Address Range:
   When creating a subnet, you define an IP address range, known as the CIDR block, which specifies the range of IP addresses available within that subnet. For example, a subnet might have the CIDR block `10.0.0.0/24`, which represents a range of `256` IP addresses.

2. Availability Zones (AZs):
   AWS divides its regions into multiple isolated locations called `Availability Zones (AZs)`. Each subnet is associated with a single AZ and exists within that specific AZ. Subnets can span multiple AZs within the same region, allowing you to distribute resources across different physical infrastructure for increased availability and fault tolerance.

3. Public and Private Subnets:
   Subnets in AWS can be categorized as either public or private. `Public subnets` are directly accessible from the internet and usually contain resources like load balancers or instances serving public-facing applications. `Private subnets`, on the other hand, do not have direct internet connectivity. They are typically used for resources that require internal communication within the VPC, such as databases or application servers.

4. Internet and NAT Gateways:
   Public subnets are associated with an Internet Gateway, which enables outbound internet access and allows resources within the subnet to communicate with the internet. Private subnets, which lack direct internet access, can use a Network Address Translation (NAT) Gateway or a NAT instance to facilitate outbound internet connectivity for essential services like software updates.

5. Route Tables:
   Each subnet has an associated route table that controls the traffic flow within the VPC. The route table contains rules that determine where network traffic is directed. For example, a public subnet's route table might include a rule to send internet-bound traffic to the Internet Gateway.

6. Communication between Subnets:
   Subnets within the same VPC can communicate with each other by default. This allows resources in one subnet to interact with resources in another. However, you can control and restrict communication between subnets using network access control lists (ACLs) or security groups.

7. VPC Peering:
   AWS VPC peering allows you to establish a private network connection between two VPCs in the same or different regions. This enables communication between resources in different VPCs as if they were within the same network, without the need for internet access.

VPC subnets provide a flexible way to organize and manage resources within your AWS infrastructure. By carefully planning your subnet architecture and considering factors such as security, availability, and scalability, you can design a robust and efficient network environment for your applications and services.

## what is a security group?

In AWS (Amazon Web Services), a **security group** is a fundamental component of network security that acts as a virtual firewall for your Amazon EC2 instances. It controls inbound and outbound traffic by allowing you to define rules that permit or deny specific types of network communication.

Here are key points to understand about security groups:

1. Network-Level Security:
   A security group operates at the network interface level and acts as a virtual firewall for EC2 instances within a VPC (Virtual Private Cloud). It provides control over both inbound (incoming) and outbound (outgoing) traffic at the instance level.

2. Stateful Traffic Filtering:
   Security groups use stateful traffic filtering, which means that if you allow incoming traffic for a specific request, the response traffic for that request is automatically allowed to return. You do not need to create separate rules for inbound and outbound traffic. This simplifies the configuration and improves ease of use.

3. Allow/Deny Rules:
   You can define rules within a security group to specify which types of traffic are allowed or denied based on protocols, ports, and IP address ranges. For example, you can create rules to allow SSH (Secure Shell) access on port 22 from a specific IP range or allow HTTP traffic on port 80 from any source.

4. Granularity and Scope:
   Security group rules can be granular, allowing you to control traffic at the individual port and protocol level. You can also apply security groups to multiple instances, either individually or by associating them with subnets or network interfaces.

5. Dynamic Updates:
   Security group rules can be modified at any time to accommodate changes in your network requirements. You can add, remove, or modify rules without interrupting the running instances associated with the security group. These changes are applied almost instantly.

6. Default Security Group:
   When you create a new VPC, AWS automatically creates a default security group for that VPC. By default, this security group allows all outbound traffic and denies all inbound traffic. You can modify the rules of the default security group or create custom security groups to suit your specific needs.

7. Multiple Security Groups:
   An EC2 instance can be associated with multiple security groups. The rules from all associated security groups are combined to determine the allowed inbound and outbound traffic for that instance. This allows you to apply different sets of rules to different instances based on their requirements.

Security groups play a vital role in securing your AWS resources by controlling inbound and outbound traffic to your EC2 instances. They provide an effective means to enforce network-level access controls and reduce the risk of unauthorized access or malicious activity within your cloud environment.

## What is a gateway?

In general networking terms, a **gateway** is a network node or device that serves as an entry or exit point for data traffic between different networks. It acts as a bridge or intermediary that connects two or more networks with different protocols, addressing schemes, or topologies, allowing them to communicate and exchange data.

Here are a few types of gateways commonly encountered in networking:

1. Default Gateway:
   In TCP/IP networking, the default gateway is the IP address of the router or device that acts as the entry point for outbound traffic from a local network to reach destinations on other networks. It is usually configured on individual devices (e.g., computers, servers) and serves as the default route for sending packets to remote networks.

2. Internet Gateway:
   An internet gateway, as mentioned in the context of AWS VPC, is a specific type of gateway that connects a private network (e.g., VPC) to the public internet. It provides a bridge between the private network and the internet, enabling communication and access to internet resources.

3. Protocol Gateway:
   A protocol gateway is a device or software component that translates and facilitates communication between networks that use different protocols. It understands the protocols used on both sides and acts as a translator, allowing data to be exchanged seamlessly between the two networks. For example, a protocol gateway might translate between TCP/IP and Serial protocols.

4. Voice Gateway:
   In the context of telephony, a voice gateway is a device that connects traditional analog or digital phone systems (e.g., landlines) to Voice over IP (VoIP) networks. It converts voice signals from traditional phone lines into IP packets for transmission over the IP network and vice versa, enabling the integration of legacy telephony systems with modern IP-based communication.

5. Media Gateway:
   A media gateway is a device that connects different types of communication networks, such as PSTN (Public Switched Telephone Network) and IP networks, to facilitate the conversion of voice, video, or data signals. It converts media streams from one format to another, allowing interoperability between different network types.

Gateways play a crucial role in enabling communication and data exchange between networks that may have different protocols, addressing schemes, or technologies. They provide the necessary translation and routing functions to ensure seamless connectivity and interoperability.

## What is an internet gateway?

In AWS (Amazon Web Services), an **internet gateway** is a horizontally scalable, highly available AWS-managed service that allows communication between resources within a VPC (Virtual Private Cloud) and the internet. It acts as a gateway or entry point for internet traffic to enter or leave the VPC.

Here are key points to understand about internet gateways and their relationship with AWS VPC:

1. Internet Connectivity:
   An internet gateway provides the means for resources within a VPC to connect to the internet and receive inbound traffic from the internet or send outbound traffic to the internet. It serves as a bridge between the VPC and the public internet.

2. Public Access:
   When an internet gateway is attached to a VPC, all instances within the VPC with a public IP address or an Elastic IP address can communicate with the internet. This allows resources such as web servers or public-facing applications to be accessible from the internet.

3. Traffic Routing:
   To enable communication between the VPC and the internet, a routing rule in the VPC's route table directs internet-bound traffic to the internet gateway. This rule specifies that any traffic with a destination outside the VPC's IP address range should be routed through the internet gateway.

4. Inbound Traffic:
   Inbound traffic from the internet is typically initiated by external users or services and is directed to the public IP or Elastic IP of an instance within the VPC. The internet gateway routes this traffic to the appropriate instance based on the rules defined in the VPC's security groups.

5. Outbound Traffic:
   Outbound traffic from instances within the VPC can be sent to the internet through the internet gateway. This includes traffic initiated by instances accessing external services or retrieving data from the internet. The internet gateway routes the outbound traffic to its intended destination on the internet.

6. One-to-One Relationship:
   Each VPC can have only one internet gateway associated with it. This means that all instances within the VPC share the same internet gateway for internet connectivity.

7. Private Subnets and NAT Gateway:
   By default, instances in private subnets of a VPC do not have direct internet connectivity. If resources in private subnets need outbound internet access, a Network Address Translation (NAT) Gateway or a NAT instance can be used in conjunction with a routing rule in the route table. The NAT Gateway or instance serves as a proxy to allow outbound traffic from private subnets to access the internet through the internet gateway.

The internet gateway plays a crucial role in connecting resources within a VPC to the internet, enabling public accessibility and facilitating outbound internet traffic. By managing inbound and outbound communication through the internet gateway and configuring appropriate security measures, you can control and secure the flow of traffic between your VPC and the public internet.


## What is a Route table?

In AWS (Amazon Web Services), a **route table** is a virtual networking component that controls the routing of network traffic within a Virtual Private Cloud (VPC). It acts as a set of rules that determine where network traffic is directed, allowing you to define the paths for inbound and outbound traffic within your VPC.

Here are key points to understand about route tables in AWS:

1. Default Route Table:
   When you create a VPC, AWS automatically creates a default route table for that VPC. The default route table contains a predefined local route that ensures communication within the VPC. Initially, all subnets within the VPC are associated with the default route table.

2. Custom Route Tables:
   Besides the default route table, you can create additional custom route tables to suit your specific networking requirements. Each custom route table can have its own set of routes and be associated with specific subnets within the VPC.

3. Routes:
   A route table consists of routes, which define the paths for network traffic. Each route specifies a destination IP address range and a target. The target can be another network interface, an internet gateway, a virtual private gateway (for connecting to a VPN), a NAT gateway, or a VPC peering connection. The routes determine where traffic should be sent based on its destination.

4. Routing Priority:
   When multiple routes match a given destination, the most specific route (with the longest matching prefix) is used to determine the path. AWS evaluates the routes in order of their priority, allowing you to control traffic routing based on the specificity of the destination IP address ranges.

5. Route Propagation:
   You can enable or disable route propagation for specific route tables. When enabled, the route table receives routes from other AWS services such as Virtual Private Gateways or Transit Gateways, allowing you to connect your VPC to external networks.

6. Associating Route Tables with Subnets:
   Subnets within a VPC can be associated with specific route tables. When a subnet is associated with a route table, the routes in that table determine how inbound and outbound traffic is directed for resources within that subnet.

7. Internet Gateway and NAT Gateway:
   The association of a route table with a subnet determines whether the subnet has direct internet connectivity. To enable internet access for a subnet, you typically associate it with a route table that has a route pointing to an internet gateway. For private subnets that require outbound internet access, you can associate them with a route table that has a route pointing to a NAT gateway or NAT instance.

Route tables in AWS provide a crucial mechanism for controlling and directing network traffic within a VPC. By defining routes and associating them with subnets, you can determine how traffic flows within your VPC, enable internet access, and establish connectivity to external networks. This flexibility allows you to design and manage your network infrastructure according to your specific requirements.

## What is NAT gateway?

In AWS (Amazon Web Services), a **NAT (Network Address Translation) gateway** is a managed service that allows resources within private subnets to communicate with the internet while remaining protected from direct inbound traffic. It provides outbound internet connectivity for instances in private subnets within a Virtual Private Cloud (VPC).

Here are key points to understand about NAT gateways in the context of AWS:

1. Outbound Internet Access:
   A NAT gateway allows resources within private subnets to access the internet for tasks like software updates, accessing external services, or downloading patches. It acts as a middleman or proxy, allowing outbound traffic from private subnets to reach the internet while hiding the private subnet's IP addresses.

2. IP Address Translation:
   When a resource in a private subnet sends outbound traffic to the internet through a NAT gateway, the NAT gateway replaces the source IP address of the request with its own public IP address. This provides a level of security by hiding the private subnet's IP addresses from the internet.

3. High Availability and Scalability:
   AWS NAT gateways are highly available and scalable. They are automatically deployed in multiple Availability Zones (AZs) within a region to provide redundancy and fault tolerance. If one NAT gateway fails, traffic is automatically routed to the healthy NAT gateways in other AZs.

4. Elastic IP:
   Each NAT gateway is associated with an Elastic IP (EIP). The EIP provides a static public IP address that remains associated with the NAT gateway even if it is stopped or restarted. The Elastic IP allows resources on the internet to send responses back to the NAT gateway.

5. Managed Service:
   NAT gateways are managed by AWS, meaning that you don't have to worry about the underlying infrastructure, patching, or scaling. AWS takes care of the operational aspects, ensuring the service is highly available and running smoothly.

6. Billing:
   AWS charges for the use of NAT gateways based on factors such as the amount of data processed and the duration of usage. You can refer to the AWS Pricing page for specific details on the pricing model.

7. Alternative: NAT Instance:
   In addition to NAT gateways, AWS also provides the option to use a NAT instance. A NAT instance is an EC2 instance that you configure and manage yourself to perform NAT functionality. While it offers more flexibility, it requires manual configuration and management compared to the fully managed NAT gateway service.

NAT gateways play a critical role in enabling outbound internet connectivity for resources in private subnets within an AWS VPC. By leveraging NAT gateways, you can ensure that your private subnet instances have secure and controlled access to the internet while keeping their IP addresses hidden.
