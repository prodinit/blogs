# Docker Networking - Bridge vs Host vs Overlay 

## What is Networking?
It allows one docker container to interact/communicate with other docker containers and the host system.

<figure><img src="https://i.ibb.co/GvJ3xQQ/network.png"><figcaption></figcaption></figure>

## Networking Scenarios
1. Container 1 can talk to Container 2
2. Container 1 is isolated from Container 2
3. Host can talk to both Container 1 and Container 2

## Types of Networking
1. Bridge Networking
2. Host Networking
3. Overlay Networking

## Bridge Networking
You launch a host (EC2/VM/droplet/etc), that host is comes up with a default `eth0` network, suppose 172.10.1.1. 

When you run a docker container inside the host, the container will have its own default `eth0` network, suppose 172.11.1.1

Now, when host with x.x.1.1 IP tries to ping docker container with x.x.1.2 IP, it gets a networking error. 

To solve this, docker by default creates a `veth` virtual eth and connect it with both docker container and the host. `veth` acts like a bridge and allows communication between docker container and host. This `veth` is called bridge network.

You can create custom bridge networks to achieve isolated networks for any container. 

<figure><img src="https://i.ibb.co/Y7rNq50/bridge.png"><figcaption>Bridge Networking</figcaption></figure>

## Host Networking
It is a networking mode in which a Docker container shares its network namespace with the host machine. For example, If you run a container that binds to port 80 and uses host networking, the container’s application is available on port 80 on the host’s IP address.

One limitation with the host driver is that it doesn’t work on Docker desktop: you need a Linux host to use it.

## None Networking
The none network driver does not attach containers to any network. Containers do not access the external network or communicate with other containers. You can use it when you want to disable the networking on a container.

## Overlay Networking
Overlays use networking tunnels to deliver communication across hosts. This allows containers to behave as if they are on the same machine by tunneling network subnets from one host to the next. 

Overlays focus on the cross-host communication challenge.

## Conclusion
We have covered docker networking, networking scenarios and types of networks.
- Reach us out if you need help in containerising your applications.



#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags
<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.