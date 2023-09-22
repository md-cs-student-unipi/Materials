SDN used to make network slicing, with SDN and a dataflow switch.
The concept of network slicing is relevant on mobile networks.
The evolution of mobile network, up to 5G, made us see that the mobile architecture evolve to support more challenging environment with 3 main use cases. There are combinations of use cases with many requirements.

MMTC: massive machine type communication, with internet of things, having a large number of sensors and actuators divided, configuring the devices remotely and use them remotely.
The idea is to have an high number of devices in a very narrow place, where a sensor may provide few data.

Another scenario is to have need of devices with low response time along large coverage area, so it is important to have reliable and low sensible communication instead of massive machine type communication. This is the case of enhanced Mobile Broadband (eMBB).

The third case is the instant and ultra reliable communication (URLLC). This is needed for all type of application with zero latency and ultra reliable, such as autonomous driving or remote medical surgery.

To deal all these scenarios, the solution is to have implemented different partitions in the network, with different requirements and different logical behaviour; but all lean on the same physical infrastructure. **It is introduced network slicing to create different slices and satisfy the required features to those.**

Idea: put on physical links and network with datacenter different subnetworks for different kind of logical networks. Creating a logical network on top of the physical, so you can shape the network to address well the requirements of a specific use case.

A network slice is a virtual end to end network built on top of a physical end to end network, it may see as a big VPN. It allows to cope with different requirements, quality of service, functionalities, specific users, etc...
![[Pasted image 20230630141753.png]]


### Enablers
[[Network Function Virtualization]] is important, as there are network management entity and other, which are functionalities that can be implemented as virtual network functions, so software running on  a virtualization function and that can be moved or replaced where one needs.
A network slice can be made with the management and orchestration entity of VNF. It can be thought as a real complex network service, with a specific network service for a specific VNF.

[[Software Defined Networking]]: allows to treat for different traffic flows, different behaviours. Some flow can have high bandwidth, while for sensor communication may need lower bandwidth and also need to process those data close to the location where those sensor data are made.

The virtual infrastructure manager, allows to manage the datacenter.
SDN and NFV are used in conjunction and that can be done in several ways.


## Slices of 5G

![[Pasted image 20230630121657.png]]

**Ultra High Definition slice**: one Edge Cloud and Core Cloud. The first is located close to the physical antenna. In the UHD slice, there is the DU (distribution unit), allowing to move core function close to end devices, always in the edge cloud.

**The Core Cloud** is the main computation core, there is the Content Delivery network for the UHD slice. 
On the edge cloud we may place some support operations, but it has less resources than the core cloud. 

In the mission critical IoT slices, several network functions may be located on the edge, with some application functions allowing communication and services to vehicles for example. In the edge there are core functions, distributed unit and a V2X server that can be both on the Edge and Cloud. Here, it is done the main computation for pre-processing data.
Also by moving some function on the edge, you save bandwidth from the edge to the cloud.
Again, in phone slice we have more on the core IMS (IP Multimedia Subsystem) is for multimedia. 
Or finally, we have Massive IoT Slice, in which there are functions even of IoT in the cloud.

We may store some rules, so that the packets can flow through VNF. And to isolate the slices both datacenter switches and rules are used. 

Between antennas and the edge cloud there is a router with SDN SW, which allows to classify the traffic. It is classified as traffic of a specific slice, and the traffic may be divided in multiple forwarding rules, according to slice to which flow it belongs.

With the VPN represented with the cloud, through it the packets are forwarded to the Core Cloud, which are handled in the Core Cloud by the router of the SDN SW.
The SDN controller programs the routers control plane to make them work in such way and modifies them when the requirements change.

![[Pasted image 20230630121630.png]]

# Hands On
RYU Controller API and OpenVSwitchCLI. We will  install flow rules, using RYU controller, with a python application that is ready to test the API.
The command line of OVS will allow us to see the flows and implement behaviours to add flows.

Topology: hosts and switches which are interconnected emulating complex topologies
	In normal topologies, all hosts can communicate with all other hosts.

H2 and H4 can communicate with each other can communicate, but we enforce here separation from high part and low part and enforce paths from parts.

With mininet we can also enforce that the links of the upper slices have an upper bandwidth in high part of 10 MB/s, in the lower part 1 MB/s.

On top we gave a controller c1, which executes a network application on top to enforce said behaviour.

`network.py` we set up the topology **physically**

`topologyslicing.py`: instruct the controller to the type of slices we want to realise.


In `network.py`: use mininet.


To realise slices with RYU: we use the RYU controller, which is an mediator, talking with the OF switch, providing to it **the specification of the slices with a python application `topologyslicing.py`**

`mininet> sh ovs-ofctl dump-flows s1`
s1 is the name of our switch, to get flows on the switch


All down the least rule, which means go to the controller if you did not find the same flow
 cookie=0x0, duration=196.119 s, table=0, n_packets=4, n_bytes=368, priority=0 actions=CONTROLLER:65535

You may see that h1 is connected on the switch on a interface.

 cookie=0x0, duration=196.119s, table=0, n_packets=4, n_bytes=368, priority=0 actions=CONTROLLER:65535

To direct the flows, with the first two rules:
 cookie=0x0, duration=259.096s, table=0, n_packets=35, n_bytes=2794, priority=1,in_port="s1-eth1" actions=output:"s1-eth3"
 cookie=0x0, duration=259.090s, table=0, n_packets=34, n_bytes=2724, priority=1,in_port="s1-eth2" actions=output:"s1-eth4"

rules of the low slice 

 cookie=0x0, duration=259.082 s, table=0, n_packets=13, n_bytes=1102, priority=1,in_port="s1-eth3" actions=output:"s1-eth1"
 cookie=0x0, duration=258.297s, table=0, n_packets=13, n_bytes=1078, priority=1,in_port="s1-eth4" actions=output:"s1-eth2"


![[Pasted image 20230419172118.png]]


To see the traffic, we may listen t all interfaces of the controller and write on a pcap file to then open on wire shark.

https://manpages.ubuntu.com/manpages/trusty/man8/ovs-ofctl.8.html

Put the flow from s2 to 
`mininet> sh ovs-ofctl del-flow s2 "in_port=s2-eth1 priority=1  actions=output:s2-eth4"`


With the command net, we can get the topology of a network.

`mininet> sh ovs-ofctl add-flow s2 "in_port=s2-eth1, priority=1,actions=output:s2-eth3"`

Where we take the flows from the s2 to s5, specifying the output port of s2, which by the net command we saw that was the port going on the input of s5.

Use the command `net` to get all the physical rules.

To have flows from s5 to s2:
`mininet> sh ovs-ofctl add-flow s5 "in_port=s5-eth1, priority=1, actions=output:s5-eth2"`


Final rule: all flows from s5, passing through s2, must go to s3.
Doing that effectively killed the link from h1 to h2, as s2 shuld not forward to s4.


`mininet> sh ovs-ofctl del-flows s2 in_port=s2-eth2`



4 packets transmitted, 4 received, 0% packet loss, time 3064 ms
rtt min/avg/max/mdev = 0.052/0.095/0.208/0.065 ms
```
mininet> sh ovs-ofctl add-flow s2 "in_port=s2-eth1, priority=1,actions=output:s2-eth3" 
mininet> sh ovs-ofctl add-flow s2 "in_port=s2-eth1, priority=1,actions=output:s5-eth1" 
ovs-ofctl: s5-eth1: output to unknown port
mininet> sh ovs-ofctl add-flow s5 "in_port=s5-eth1, priority=1,actions=output:s5-eth2" 
mininet> sh ovs-ofctl add-flow s2 "in_port=s5-eth4, priority=1,actions=output:s2-eth2" 
ovs-ofctl: s5-eth4: invalid or unknown port for in_port
mininet> sh ovs-ofctl add-flow s2 "in_port=s2-eth4, priority=1,actions=output:s2-eth2" 
mininet> h1 ping h3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
64 bytes from 10.0.0.3: icmp_seq=1 ttl=64 time=0.251 ms
64 bytes from 10.0.0.3: icmp_seq=2 ttl=64 time=0.070 ms
64 bytes from 10.0.0.3: icmp_seq=3 ttl=64 time=0.068 ms
64 bytes from 10.0.0.3: icmp_seq=4 ttl=64 time=0.067 ms
64 bytes from 10.0.0.3: icmp_seq=5 ttl=64 time=0.069 ms
64 bytes from 10.0.0.3: icmp_seq=6 ttl=64 time=0.061 ms
64 bytes from 10.0.0.3: icmp_seq=7 ttl=64 time=0.076 ms
64 bytes from 10.0.0.3: icmp_seq=8 ttl=64 time=0.069 ms
64 bytes from 10.0.0.3: icmp_seq=9 ttl=64 time=0.067 ms
```

