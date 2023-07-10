# Questions:

**Q1: How many IP Addresses can I get for [1.1] a /16 netmask and [1.2] a /28 netmask**

- For [1.1] / 16 netmask: The first 16 bits are network bits and remaining 16 are host bits (because 32 bits in total minus 2164 network bits = 16 host bits). This means that the total possible IP addresses in this range are 2^16 (65536 total IP addresses minus 2 addresses reserved for **network** and **broadcasting**)
    - 2 ^ 16 - 2 = 65,534 Available usable IP addresses.


- For [1.1] / 28 netmask: The first 28 bits are network bits and remaining 4 are host bits (because 32 bits in total minus 28 network bits = 4 host bits). This means that the total possible IP addresses in this range are 2^4 (16 total IP addresses minus 2 addresses reserved for **network** and **broadcasting**)
    - 2 ^ 4 - 2 = 14 Available usable IP addresses.


**Q2: I have a CIDR block of 192.168.0.0/20 which I need to assign to subnets within my VPC. I wish to create exactly eight sub-networks out of this block. Can you give me the subnet addresses for each of the eight sub-networks in ascending order in the format a.b.c.d/n (e.g. 192.168.0.0/22)?**

- For the CIDR block 192.168.0.0/20, the subnet mask (/20) indicates that the first 20 bits of the IP address are the network address, while the remaining 12 bits are available for host addresses.

- In this case, with a /20 subnet mask, you have a total of 2^12 = 4,096 IP addresses in the block. However, the first and last IP addresses within the block are reserved for the network address and the broadcast address, respectively. Therefore, the number of usable IP addresses will be 4,096 - 2 = 4,094.

- To create exactly eight sub-networks out of the CIDR block 192.168.0.0/20, you need to divide the block into eight smaller subnets with `/23` prefix length. Each /23 subnet will allow for 512 IP addresses, with 510 usable addresses.

> **Note**: No of subnets= 2^n, `n` being the bits borrowed from the host side of the network. 8=2^3. New subnest mask wil be `20+3=/23` which is equal to `255.255.254.0`. `256-254=2`, add the `2` to the network address given to get the next addresses.

Here are the eight subnets derived from the CIDR block 192.168.0.0/20 using a /23 prefix length:

1. Subnet 1: 192.168.0.0/23 (Range: 192.168.0.0 - 192.168.1.255)
2. Subnet 2: 192.168.2.0/23 (Range: 192.168.2.0 - 192.168.3.255)
3. Subnet 3: 192.168.4.0/23 (Range: 192.168.4.0 - 192.168.5.255)
4. Subnet 4: 192.168.6.0/23 (Range: 192.168.6.0 - 192.168.7.255)
5. Subnet 5: 192.168.8.0/23 (Range: 192.168.8.0 - 192.168.9.255)
6. Subnet 6: 192.168.10.0/23 (Range: 192.168.10.0 - 192.168.11.255)
7. Subnet 7: 192.168.12.0/23 (Range: 192.168.12.0 - 192.168.13.255)
8. Subnet 8: 192.168.14.0/23 (Range: 192.168.14.0 - 192.168.15.255)

Each subnet has its own range of IP addresses, and you can assign these subnets to different parts of your VPC as needed. Remember that the first and last IP address within each subnet range are reserved for the network and broadcast addresses, respectively, so the usable IP addresses for each subnet will be `192.168.x.1` to `192.168.x.254`.


**Q3: How many hosts will each of my subnetworks in Q2 above be able to address?**

- Each /23 subnet will allow for `512` IP addresses, with `510` usable addresses(hosts).

**Q4: Bonus question: What will be the broadcast address of the last (8th) sub-network in the block?**

- For the `8th` subnet `Subnet 8: 192.168.14.0/23 (Range: 192.168.14.0 - 192.168.15.255)`. The broadcast address would be `192.168.15.255`
