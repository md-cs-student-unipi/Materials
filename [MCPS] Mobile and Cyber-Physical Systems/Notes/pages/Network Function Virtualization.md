Allows to make networks programmable, with different requirements.

![[Pasted image 20230405162419.png]]
At the time, the traffic to monitor were increasing and still now increasing.
Previous, the companies used *specialized hardware* to manage flows. 
It has been decided to deploy your specific hardware device, once it has been figured out to have some amount of traffic flow.
**But you are not flexible**:
* days: deployment and configuration take several time.
* cost: after the initial configuration of a network, that shall last years. The load on the network have to remain the same for a lot. 

In an enterprise network as above, you may have load balances, proxies and firewall. The Mail, Web, VPN, IDS are network functions which could be virtualized.


A typical enterprise network can be seen here:
![[Pasted image 20230705122006.png]]
For example in a system of **80K users across tens of sites, we got that there may be a lot of functions in a network.** As we see for appliances, we see each:
![[Pasted image 20230405163205.png]]

Network evolves to support evolving requirements. We do not have the pure end to end models, for instance we have the load balancer and the gateway. We also have authentication functions which allow to process packets.
In the image they were hardware device, so the integration was fixed, not adaptive to dynamic traffic volumes. Changing equipment, to change the new flows, will mean that you will need to spend on training besides CAPEX of devices.

### TelCo vs Service Providers
Services Provider, which are over the top operator, they innovate very fast.
They develop and deploy a new feature or a new idea in 2-6 months.
In the other side the TelCo operators will have a longer of development.
![[Pasted image 20230405163753.png]]

The TelCo providers wanted to learn from the Software provider. Ideally, internet players use specified software upon generally purpose hardware.
![[Pasted image 20230405163833.png]]

### NFV idea
Decouple Hardware from Software and *implement the network functions when needed.*

A network service, may be composed by more than one network function.
For example a pipeline of firewall and load balancer.
The idea is to use virtualization technology to define the network function, and without the need of installing new hardware.
You may not need to acquire new hardware and need to relocate your functions to adapt with your demand

The definition is: virtualization, implemented as virtual machine, which run on general purpose hardware.
Before the idea was to have in the past hardware to function, with one physical node per role.
![[Pasted image 20230405164356.png]]

Now, we HAVE FUNCTIONS (implemented via virtualized software) which are hosted and execute on general purpose servers:
![[Pasted image 20230405164419.png]]

### Use cases:
* BNG: broad-net network gateway: access point of subscriber of network.
* CG-NAT: withing the network of internet service providers. 
* Routers: implemented as virtual routers.
* There may be functions to optimize the delivery of services, such as CDN with Cache Servers. 
* Many others

#### One example of using NFV for mobile network (vEPC)

The Evolved Packet Core (EPC) is a framework for providing converged voice 
and data on a 4G Long-Term Evolution (LTE) network.

The evolved packet networks and 5G Radio Access can be virtualized, to use resources in a more flexible way, but also improve network usage, higher availability, higher resiliency, elasticity and topology reconfiguration to optimize performance.

The evolved packet core will be deployed as application running on devices on data center, which are in all the point of presence of TelCo.
![[Pasted image 20230405165036.png]]

While Antenna is Hardware and can't be changed and also Baseband Unit functions that process the signal, cannot be modified because implemented in Hardware, there are the virtualization of each base station to make a virtualized environment to manage all these.
![[Pasted image 20230405165213.png]]

With NFV:
* implement the network elements on applications and software.
* relocate them on the current needs of the network.
* in that way the capacity of the infrastructure resource of the operator is better used.
* that means faster innovation, so if you implement a new version of your software, you will deploy as software and with virtualization that you do very fast, allowing to scale up and down service as required.

**Overhead is a trade-off, as dedicate hardware is more performer than an implementation with NFV. In the first implementation of NFV you also consider non specialized hardware, so you lose performance, but you recover in flexibility**. Hypervisor will be needed and this introduces a little overhead, but you may use the resources flexibly.

If a new service of software comes out, you may change the usage of your resources and have more optimized functions. The technology now has evolved and there are a lot of technology to implement function as process, but *there are a lot of/many points where one can create more performer points, to mitigate the overhead of this technology.*

## NFV service
An operator needs to put a chain of those network functions. What could be done is to implement a differentiated treatment of the traffic flows.
According to traffic flow, route and packet; the network can be easily programmed so, that **flow may be processed in different way in different time of the day**. For example in night time the parental control may be added.

The blue traffic: analyzed by a firewall and for example pass through a video optimizer.
![[Pasted image 20230405170041.png]]

A VNF can be viewed as a graph, where the nodes are represented by virtual device and the edges by logical and physical links.
The VNF nodes could be anything, a firewall, monitoring function or DNS/load balancer. These are needed to create a communication between different infrastructure.

We want that VNF 1 and VNF 2 and VNF 3 communicate.
We have an end to end service. In an enterprise network we have for example a termination that could be a data center of a service provider.
The network function will be *executed on a Data Center*. **The logical links will be mapped to physical links**, and these can be wired or wireless. You have the termination, at the end of the service chain, that is interconnected to the final endpoint.

![[Pasted image 20230405171256.png]]
A VNF would be the function of a 4G and 5G network.

### An example
This gives us a more realistic view of what can be provided.
Run the software on infrastructures. For example VNF-1 on NFVI-PoP (point of presence), can be placed to endpoint 1 or another, depending for example on closeness.
We need a virtualization to migrate and instantiate functions. You need some entity to manage the networks functions.
![[Pasted image 20230405171702.png]]
The operator will have a centralized component, that decides what VMs to allocate and put on physical machine. Also setup the links so that the functions can communicate.

## NFV architectural framework

In NFV framework there are 3 main components:
- NVFI - network function virtualization infrastructure: Comprises the hardware and software resources that create the environment in which VNFs are deployed, it is required to set up the network service.
- VNF - The collection of VNFs implemented in software to run on virtual computing, storage, and networking resources. It is required due to the decoupling network functions into software and hardware.
- NFV MANO - network function virtualization management and orchestration: Framework for the management and orchestration of all resources in the NFV environment. It is required for NFV-specific management and orchestration.
![[Pasted image 20230405172007.png]]

### NFV infrastucture
The infrastructure is composed by hardware and software components, in which the environment is executed, deployed and managed. The three resources virtualized are computing, storage and network, these provide their service by the hypervisor that create a virtualization layer.
Computing machine are supposed to be general purpose and the storage resource can be standalone as NAS, or attached directly to server.

![[Pasted image 20230425103718.png]]
- Compute domain: provides commercial off-the-shelf (COTS) high-volume servers and storage.
- Hypervisor domain: mediates the resources of the compute domain to the VMs of the software appliances, providing an abstraction of the hardware.
- Infrastructure network domain: comprises all the generic high volume switches interconnected into a network that can be configured to supply network services.

We can have two type of infrastructure: 
***NFVI-POP network***: interconnects computing and storage, including also a specific components to connect external world. For example an inside data-center network.
***Transport network***: networks that interconnect different type of above network. Provide to forward and routing packets between networks owned by different operator.

#### Example: OpenStack networking deployment
Allows to define, on compute nodes, different instances of VMs.
![[Pasted image 20230405172413.png]]
In a compute node, you may have more than one VM on a node. You may have also some layer 2 Switch. 
We may define different networks in NFV:
* network of the provider
* different overlay networks
* overlay networks, we may have networks which define to who to assign the traffic.

##### vSwitch
The concept of switches, implemented as software and executed within a node is also to be considered. What happens is that we have on a VM, a virtual interface.
We have one or more entry points in the physical switch: the network interface card (NIC), upon this we have the software switch (vSwitch), one for each NIC, connected by the interface at each virtual machine.

A layer 2 or layer 3 interconnection, could be implemented as a switch.
The VM receives from Hardware card and transmit packets to destination in the network. One example is Open vSwitch.
# NFV Reference Architectural Framework
We may see in the image the Reference Architectural Framework:
![[Pasted image 20230705122524.png]]
We will see in detail below.

### NFV Management and Orchestration (NFV MANO)

![[Pasted image 20230425111312.png]]
- include orchestration and lifetime management of both hw/sw resources.
- include database where are stored information about deployments and lifecycle properties of services, resources and functions.
- define interface used for communication between components of the MANO.
- provide the provisioning of VNFs and related operations.

A network service may be composed of different VNF and the role of the function to implement a VNF manager may be demanded to a single software.

#### VIM
Virtualized infrastructure manager: is an instance of a VM. Usually there is only one VIM for each data-center and in fact, we will have different data centers with different managers. With an overall networking environment have to need a single MANO managing multiple VIMs.
The most used VIM in real world is OpenStack: a open source software to manage 

#### VNFM 
Virtual Network Function Manager: the component that is in charge for instantiate, scale, measure and terminate the network services. This oversees the entire life cycle of a function instance, assisting in resolving problem, performance measuring, scaling in-out and so on.

#### NFVO
Network Function Virtualization Orchestrator: is responsible to install and configure network services, VNF packages and global resource management, including the entire life cycle.
We can individuate two different type of orchestration:
- network service orchestration: management and coordination of an end-to-end service that involves VNFs. That means, it can create end-to-end service that between different VNFs and it can instantiate VNFMs, where feasible.
- resource orchestration: management and coordination of the resources under the management of different VIMs.

Here two type of open source orchestrator: 
1) OSM MANO: most adopted
2) ONAP: unix foundation community


### Repositories
Repositories may have descriptions. We can have four different types of repos:
- Network service catalog: list of usable network services represented by a deployment template. 
- VNF catalog: database of VFN descriptors, they explain the deployment and the operation behaviours.
- NFVI resource: list utilized for the purpose of establishing a new service instance.
- NFV instances: list containing details about network service instances and VNF instances.

The life cycle must be showed too. With NFV one may a rule to migrate NFV to a node with more capacity or scale to a different node.
## NSD example
![[Pasted image 20230405173926.png]]

vndf contains:
![[Pasted image 20230705122217.png]]
Then we have:
![[Pasted image 20230705122342.png]]
We have two functions:
* iperf: program to measure the maximum throughput to one client to another service
* target: iperf-service
* vnfd: a list of VNF, which has a description
* vnf dependency: says that there is a dependency. There must be measurements with clients and to measure

The vendor can be different than the one of a network service.
Operators may use 3rd party software, implementing a specific function. The part more interesting is that one may point to the image needed to automate VM.

You may point to the script to automate the deployment. The deployment flavour: allows to decide for example the size of the VMs, it provides a way to describe the requirements in terms of CPU and memory. It is the same as specifying in deployments of Kubernetes.

This is a little example in which one single VNF is deployed: ![[Pasted image 20230425123041.png]]




