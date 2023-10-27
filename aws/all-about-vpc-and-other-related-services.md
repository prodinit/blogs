# A-Z of AWS VPC and other services - with Terraform

This blog is going to be an end-to-end guide for AWS VPC networking. I understand there are a lot of AWS services you need to take care of at the time of setting up networking. It can be overwhelming but this will help you understand exactly what is needed for the kickstart.

The services/concepts we are going to understand are:

- AWS VPC
- CIDRs
- Subnets (Public and Private)
- Internet Gateway
- Elastic IP
- NAT Gateway
- Route table and association with subnets

Some other additional concepts:

- Network ACL
- Security Groups
- VPC peering
- VPC Flow logs
- VPC endpoints


## VPC

- AWS has regions (us-east-1, ap-south-1 etc)
- Each region can have upto 5 VPCs
- VPC is like owning a part of data center (or similar to renting out a virtual server)

> A VPC is your own private network where you can manage all your web servers, applications, databases, etc. Every service created on AWS has to be part of a VPC. Even the services that you create without adding them to an existing VPC are automatically added to the default VPC created by AWS.

Each region have AZs (availability zones), for example, AZs in us-east-1 are us-east-1a, us-east-1b, us-east-1c.  **VPCs are spread across AZs**

## CIDRs

This helps us define an IP address range in your VPC. It consists of two components:

Base IP: 192.10.0.0, 172.0.0.0, etc.

Subnet Mask: /16, /24, etc

**High value subnet mask with fewer IP addresses. The lower the value of the subnet mask, the more IP addresses there are.**

### Terraform to create AWS VPC
```
resource "aws_vpc" "vpc" {
  cidr_block           = "15.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = true
  enable_dns_hostnames = "true"

  tags = {
    "resource" : "vpc-network",
  }
}
```

## Subnets (Public and Private)

Subnets are part of your VPC’s CIDRs IP address range. Each subnet is associated with a particular availability zone (AZ) within an AWS region. When you create subnets in your VPC, you can choose to make them either public or private.

- Public subnet: The subnet that is connected to the Internet Gateway (IGW) is nothing but the public subnet.
- Private subnet: The subnet that is not connected to the Internet Gateway (IGW) is nothing but the private subnet.

<figure><img src="https://i.ibb.co/Z6Dj1Vb/file.png"><figcaption></figcaption></figure>

### Terraform to create AWS VPC
```
variable "PUBLIC_SUBNET_CIDRS" {
  type        = list(any)
  description = "List of public subnet cidr"
  default     = ["15.0.0.0/20", "15.0.16.0/20"]
}

variable "PRIVATE_SUBNET_CIDRS" {
  type        = list(any)
  description = "List of private subnet cidr"
  default     = ["15.0.128.0/20", "15.0.144.0/20"]
}

resource "aws_subnet" "private_subnets" {
  count             = length(var.PRIVATE_SUBNET_CIDRS)
  vpc_id            = aws_vpc.vpc.id
  cidr_block        = element(var.PRIVATE_SUBNET_CIDRS, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    "resource" : "private-subnet ${count.index + 1}",
  }
}

resource "aws_subnet" "public_subnets" {
  count                   = length(var.PUBLIC_SUBNET_CIDRS)
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = element(var.PUBLIC_SUBNET_CIDRS, count.index)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = "true"

  tags = {
    "resource" = "public-subnet ${count.index + 1}",
  }
}
```

## Internet Gateway
- It allows resources in a VPC to connect to the internet.
- It doesn’t come with VPC, it needs to be created separately.
- 1 IGW can be attached to the 1 VPC.
- Internet gateways on their own don't allow Internet access.
- Route tables must be edited with IGW.

```
resource "aws_internet_gateway" "i_gateway" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    "resource" = "internet-gateway",
  }
}
```

<figure><img src="https://i.ibb.co/gwdX8s8/file.png"></figure>

## Elastic IP

- An Elastic IP address is a static, public IPv4 address designed for dynamic cloud computing.
- You can associate an Elastic IP address with any instance or network interface in any VPC in your account.

```
resource "aws_eip" "elastic_ip" {
  vpc        = true
  depends_on = [aws_internet_gateway.i_gateway]

  tags = {
    "resource" = "elastic-ip",
  }
}
```

## NAT Gateway

- NAT Gateway is used to enable instances present in a private subnet to help connect to the internet or AWS services.
- It is present in public subnets.
- Need to setup NAT gateway if subnets are present in multiple AZs
- The elastic IP address is associated with a NAT gateway

```
resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.elastic_ip.id
  subnet_id     = aws_subnet.public_subnets[0].id

  depends_on = [aws_internet_gateway.i_gateway]
  tags = {
    "resource" = "nat-gateway",
  }
}
```

<figure><img src="https://i.ibb.co/nzDCNkk/file.png"></figure>

## Route table

- Each subnet in your VPC is associated with a route table that tells it how to handle traffic.
- A route table is like a set of directions that tells data packets where to go based on their destination IP address.

### Create Route table using terraform
```
resource "aws_route_table" "rtb_private" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }
  tags = {
    "resource" = "Private Route Table"
  }
}

resource "aws_route_table" "rtb_public" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.i_gateway.id
  }

  tags = {
    "resource" = "Public Route Table"
  }
}
```

### Associate Route table with subnets
```
resource "aws_route_table_association" "public_subnet_asso" {
  count          = length(var.PUBLIC_SUBNET_CIDRS)
  subnet_id      = element(aws_subnet.public_subnets[*].id, count.index)
  route_table_id = aws_route_table.rtb_public.id
}

resource "aws_route_table_association" "private_subnet_asso" {
  count          = length(var.PRIVATE_SUBNET_CIDRS)
  subnet_id      = element(aws_subnet.private_subnets[*].id, count.index)
  route_table_id = aws_route_table.rtb_private.id
}
```

### How to differentiate between public and private subnet

The subnet you attached to the internet gateway (IGW) is a public subnet and the one that doesn't have an IGW is a private subnet.
 

Some additional concepts like VPC peering, VPC endpoint etc will be discussed in some other blog.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="AWS" src="https://img.shields.io/badge/AWS-8A2BE2" />
<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.