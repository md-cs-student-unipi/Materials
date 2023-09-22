
ComNetsEmu allows to emulate applications of  [[Software Defined Networking]] and [[Network Function Virtualization]].

It is designed as an extension of Mininet.

## Mininet
MIninet is a network emulation, which runs on the linux virtual kernel:
+ switches
+ routers
+ end-hosts
+ links on a single Linux kernel

Mininet hosts are processes running in the same OS kernel, sharing process ids, user names and file system.
*For each host there is their independent network stack and network resource*.
What is done for all **virtual hosts** is that Mininet creates a process, attached to the **network namespace**. For each network namespace, it has a *virtual network interface*, with associated data, ARP caches and routing table.

So we have:
virtual host -> process -> unique network namespace -> virtual network, network data, [[ARP]] cache and routing table.
Each host may have a Ethernet virtual interface, defined as GNU/Linux virtual Ethernet device (vEth).

#### vEth
vEth devices are created in *interconnected pairs*. Packets are transmitted and received instantly from one pair to another. *It represents a virtual Ethernet device, so a virtual Ethernet cable connecting two devices*.
It can be seen how the vEth of  two hosts named eth0 (virtual host) are connected to a software switch veth1 and veth2.
![[Pasted image 20230415093235.png]]


A switch can be connected to a virtual switch. *The parameters of the links, can be totally configurable*, so delay and bandwidth for example.

### Mininet Data Plane
The mininet data plane has two component:
* the vEth pairs: a full-duplex link between two network interfaces is *the same or another separated namespace*. The packet transmitted from one interface are forwarded directly to the other pair interface. Each interface behaves as a Ethernet interface.
* Linux traffic control: used to configure the parameters of the **virtual links**, with bandwidth, delay and loss rate. Also used for shaping, scheduling, classification and dropping.

## Creating a topology:
With *sudo mn* it is possible to initialize a default topology.
It is possible to use python scripts to create flexible topologies, by overriding the build() function of `mininet.topo` class.
![[Pasted image 20230415095548.png]]


### Mininet main classes
* Topo: the base class of topologies, allowing to add Switches, Hosts and Links (a bidirectional link, unless noted otherwise).
* Mininet: main class to create and manage a network, with `start` to start a network, or `pingAll` to test that all nodes **can ping each other**.

There is also a CLI, which provides useful commands and can be invoked on a network. Among the commands, there is the ability to have an xterm window which allows to monitor the nodes, but also to run commands on the individual nodes.
To implement the CLI, one just pass a *network object to the `CLI()` constructor*.

# ComNetsEmu

ComNetsEmu allows to replace the hosts of Mininet, which are processes, with **Docker containers**. It uses Docker-in-Docker, so there is a nested virtualization. **A DockerHost replaces the default host type of Mininet, and it deploys internally the other containers**. The DockerHost is used to emulate a physical host running container applications.

The architecture can be seen in this picture:
![[Pasted image 20230415101018.png]]

We may have different DockerHost, with multiple containers inside: the containers inside a Server A(docker host) will  have a **Shared network namespace**. The containers are connected with a **vEthernet to the Data Plane Server vSwitch**. A DockerHost, which represent a client, will be connected with a vEthernet to a client vSwitch.

The client vSwitch is connected to the Server vSwitch inside the Data Plane. In the dataplane there are, and they are connected:
* the SDN controller
* Application configuration manager