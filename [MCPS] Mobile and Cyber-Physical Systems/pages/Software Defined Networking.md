Software Defined Networking (SDN) revolutionizes the architecture of networks by changing how the data-plane and control-plane can be implemented. This is necessary because the demand on the internet is increasing due to cloud computing, big data, mobile traffic, and IoT, resulting in complex traffic patterns that are difficult to manage. The problems of traffic volume and changing traffic patterns require a new approach to manage the horizontal traffic, between servers that communicate within each other.

The current networks have limitations, as there are multiple protocols, complex architectures and a lack of general principles or abstractions guiding the design of network control or management plane. In traditional routing, packets arrive at a router, and that computes the forwarding table using a routing algorithm on its own or by asking other routers. This design was key to having a resilient network without a single point of failure.

However, SDN introduces a new approach to network controlled by logically centralizing control, allowing for a more flexible and responsive network. The data plane is responsible for forwarding packets from one port to another quickly, while the control plane determines the route taken by packets from source to destination, creating the routing table. SDN makes it possible to implement different management policies and prioritize traffic based on QoS requirements.

Overall, SDN represents a significant shift in how networks are designed and managed, and it offers a more efficient and flexible approach to meeting the demands of modern internet traffic.

### Complex and dynamic Traffic Patterns
* Modern distributed applications involve **an additional  traffic between servers (called horizontal traffic)**, adding to the vertical traffic from client to server.
* There is a shift into **Unified communications services**, where multiple type of services (video, audio, call, chat, ...) are delivered into one platform.
* **Cloud**: there are unpredictable loads on enterprise routers, because of the shift into clouds.
* **Server virtualization**: allows to partition a single hardware machine into multiple ones, **this increases the traffic of the single servers**, for example because of live migrations. ***The horizontal traffic flow changes in intensity and location over time, demanding a flexible approach to manage network resources.**

![[Pasted image 20230329102828.png]]
**As of today 70% of the traffic is East-West**, the traditional data center three tier design is ill equipped to handle this.

Also with the addition of **mobile devices**, there are fast and unpredictable traffic loads on the network, the network attachment point can change rapidly.

In general depending on the application the requirements in term of QoS may change and the traffic flow must be treated in different ways.

#### Current network limitations
Those patterns requires *flexible management of network resources*. To accomplish those, the traditional networks are limited:
* There is a complex architecture that is also static, and has all independent define protocol, each of which have *addresses a portion of the networking requirements*, so they add a complexity difficult to master.
* Inconsistent policies: there is the need of doing manual procedures to change configurations in: switches, routers and firewalls. Which is an error prone procedure.
* Vendor dependence: enterprise and carries must deploy **new capabilities and service rapidly born, but they are limited by the lack of open interface for network functions, which makes the enterprise be lifted by the slow product cycles of vendor equipment (it's a bottle neck)**.

As we know, layering is a major factor in the success of the internet:
![[Pasted image 20230330154126.png]]

There are no general principles or abstraction for the *design of network control plane and data plane.*
So,***what happened was that for each new functionality, a new protocol was designed***.

Where network boxes are black boxed equipment, with their own interface coming from proprietary software, so there is a really slow protocol standardisation, but actually lots of protocols, making the control plane difficult to manage.

## Network layer functions

We have two functions at the network-layer and they are on *two different planes*:
* data plane: has the **forwarding function**, which allows to move packets from router input to router out. **It works on a fast time scale, as it receives packets and forwards them frequently**.
* control plane: it has the **routing function**, allowing determine the route taken by packers from source to destination, it is in the slow time-scale as it receives control events rarely.

There are two approaches for structuring the network control plane:

#### On Router (old traditional)
![[Pasted image 20230329104611.png]]
 
 In traditional routers, the device only implements the forwarding table and decides where to forward a packet, while the forwarding tables are computed for all devices in the control plane.

#### Software Defined Approach
![[Pasted image 20230329104652.png]]

The software-defined approach provides a clearer separation between the control plane and the data plane. However, in SDN, there is a centralized control plane that collects information about the network's status. The remote controller then writes the network's topology, calculates all the paths, and communicates with the controllers to have the forwarding table and forward packets.

While the centralization is logical, with multiple and distributed sets of controllers, this maintains a sort of resilience. The distributed architecture of the controllers in SDN is logical as centralization. CA communicates with the controllers and has the forwarding table and forward packets, and they also have statistics, which they send to the remote controller. The Remote Controller will make its routing table, create a topology, and then send the routing table to the devices.

##### Advantages and motivations
The SDN approach makes it easier to implement different policies. The central concept is to make forwarding decisions according to what is included in the forwarding table, making it easier to program the controllers and create solutions.
Also even an open implementation of the control plane fosters innovation (with OpenFlow).

The Table-based forwarding implemented by routers, can be programmed easily with **a centralized program rather than having a distributed algorithm protocol for each router**.

Destination-based routing is not enough. Shortest path routing is based solely on minimizing the cost to reach a destination, but there are cases when network operators may want to control the path that traffic takes. In these cases, they would need to manually configure all the routers, changing the link weights, or change the routing algorithm altogether. Load balancing cannot be achieved with traditional routing, until the implementation of new algorithm, but SDN provides the possibility to split traffic between the best path and another path.

![[Pasted image 20230329105054.png]]
For example if a network operator wants to re-route the traffic from u-to-z to flow on u-v-w-z, rather than u-x-y-z then **it must change the weight of the links, and wait that the router run the routing algorithm, so a new routing algorithm is needed.**
**But also the operator may want to split for load balancing the traffic, and it can't with the traditional routing algorithms**.

In summary, SDN provides the flexibility to differentiate flows and route packets in specific paths from a source to a destination, making it easier to implement different policies and create solutions.

##### The SDN solution
![[Pasted image 20230330155110.png]]
To address these limitations, a forwarding device using a generalized flow-based forwarding approach can be implemented. This approach considers more than the only destination of the packet, allowing for a real separation of the control plane and data plane.

**Generalized forwarding and SDN can be used to archive any routing desired**.


The SDN controller is a distributed application that acts as a network OS, and network-control apps can be developed to implement various features, such as access control and load balancing. These apps can use the lower-level services provided by the SDN controller's API.

Separating the important functions into layers and defining OpenAPIs and protocols is crucial for fostering innovation. There are also many open-source implementations of SDN controllers available.
In 2013, Google redesigned its data center WAN to incorporate SDN, finding it to be a more efficient and effective approach to network management.

# SDN architecture
Control plane functions are external to *data plane switches*, which can expose APIs that allow table based switch control, so that flow (which means forwarding) packets behave according to the table installed under the controller supervisor.


![[Pasted image 20230705094359.png]]
## Data-plane switches
Data-plane switches with the forwarding devices which must be as simple as possible, they are dumb devices that will decide how to forward a specific packet.
The content is decided by another entity, which is the SDN controller. So the control and data plane is separated.

The idea is that they have a :
* flow (=**forwarding**) table computed and installed under a controller supervision.
* API for table-based switch control, that define what is and is not controllable.
* Protocols to communicate with the controller, such as OpenFlow.
![[Pasted image 20230330160606.png]]

## SDN controller
The SDN controller is also referred as the network operating system, which makes decisions for the devices, such as defining some routing paths according to source and destination. For example it may execute Dijkstra algorithm to do so.

The northbound API allows to have some function separated by SDN controller, allowing 3-party to create their own logic.
In fact, we have different applications for access control and load balance, for example if the traffic is directed to the same destination, you may load balance it.
Which means that is different than applying a feature on top of a single router (e.g. CISCO). SDN wants to allows the feature to be accessed from the top to all devices in same time.

The SDN controller interacts with the network switches using the southbound API. It **is implemented as a distributed system (so for scalability, fault-tolerance, robustness and performance)**

## Network-control apps
Those app are on top of the SDN controller, and interact with it using the northbound API, they are with the SDN controller in the control plane.

Their task is:
* be the actual brain of control, implementing control functions and using lower level services and API provided by the SDN controller
As said, they can be provided by third parties which are *distinct from the routing vendor or the SDN controller*
## Overview of the architecture
![[Pasted image 20230705095011.png]]
We may see how the SDN controller may be distributed and *connect with a Westbound API and a Eastbound API*.
There can be both virtual switches and physical switches that are controlled by the SDN controller.
## SDN data plane
Is the layer that occupies of the forwarding packets between the devices. It simply follows the rules defined in the tables decided by the control-plane consisting on SDN controller (and the control apps on top). In this layer there is not an autonomous embedded devices that takes decision itself. 
**Flow tables represent the forwarding abstraction, which are on Virtual switches and Physical switches**. .
The devices in data plane have two main functions:
- data forwarding: accept incoming flows and forwarding them following in according with the rules in the table. 
- control support: talk with SDN controllers to manage the forwarding rules. A reference standard is the Open Flow switch protocol.
# Generalized forwarding: match plus action

As can be seen in the image, the packet header is checked by the switches.
![[Pasted image 20230705102254.png]]
In each router there is a flow table consulted each time when arrive a new packet. There are two type of forwarding: 
- generalized -> in according to the header fields of packets incoming. For each incoming packet in the table we find the rule and it is defined from: 
	- match: pattern values in packet header fields.
	- actions: forward, modify, send to controller.
	- priority: disambiguate the overlapping pattern.
	- counters: of bytes and of packets.
	- ![[Pasted image 20230705102422.png]]

- endpoint based -> according to the IP address of destination. 

### OpenFlow: table entries
![[Pasted image 20230420162228.png]]

#### Some examples
Destination based forwarding: the fields that are set
- `IP dst` -> the out coming address
- Action -> forward with the output port  

Firewall blocking port: the fields that are set
- `TCP dst port` -> destination port
- Action: drop all the packets

Firewall blocking an IP address: the fields that are set
- `IP src` -> address of incoming packets
- Action -> drop all the packets

Layer two destination-based forwarding: the fields that are set
- `MAC dst` -> mac address of out coming packets
- Action -> forward with output port
This can be clearly seen here:
![[Pasted image 20230705102528.png]]
So with a SDN data plane device we can implement different behaviour, without having switches, routers, NATs and firewall. This is the generalized forwarding in which we have the "match plus action" abstraction, where match bits in arriving packets headers in any layers (transport, network, data link) and take actions.  

## OpenFlow example
We may see how **network-wide behaviour can be defined with Orchestrated tables of OpenFlow**.
![[Pasted image 20230705105355.png]]
What happens here is that it is enforced that datagrams from host h5 and h6 do this path:
* they are connected to s3, which may be directly connected to s2 and may go through that link using port 4 to s2, but instead they datagrams from s3 received from h5 and h6 are forwarded via port 3 to s1.
* then from s1 the packet go to s2. 

* It is enforced enforce the route to go through s1 in conclusion.
We may see the *rules of the switches*:
![[Pasted image 20230705111031.png]]
Wee see that diagrams having as destination 10.2.\*.\* corresponding to h3 and h4 must be forwarded with the rules:
* s3: action = forward(3)
* s1 (match ingress port=1)=forward(4)
* s2(match ingress port=2 and the IP of the hosts)= forward(3/4)

##### OpenFlow Switch
![[Pasted image 20230330175113.png]]
Components:
- OpenFlow channel: channel in which the controller can *add, update, delete* the **flow entries in tables**. This can be done both *reactively* as response to other packets, and proactively.
* Tables: for packet flow processing/forwarding.
* Multiple I/O ports: for the packets that flow in and out of the devices.
* "Group table: contains rules for all flows within a given group. For instance, a group may apply to a set of output ports. One can specify that when an input matches, a certain character is obtained."

In an OpenFlow Switch we have a separation between:
- control channel: the southbound APIs to connect with the controllers.
- pipeline: set of flow tables defining the forwarding path.
- datapath: where are the tables group

A switch includes one or more flow tables, if there are many they are organized as a pipeline and they are numbered sequentially starting from zero. Then a packet enter in table 0 and continue until the end exiting from pipeline or being discarded by rules. 
![[Pasted image 20230705111854.png]]
The use of multiple tables in a pipeline, rather than a single flow table, provides the SDN controller with considerable flexibility. The packet is matched among the flow entries of flow table. If there is a matching the correspondent instruction is executed (such as updating the action set, updating the metadata value or performing actions).

Those instructions may explicitly direct the packet to another flow table (with Goto Instruction), where the same process is repeated again, to the group table, to the meter table(Meters enable OpenFlow to implement various simple QoS operations, such as rate-limiting. A meter table contains meter entries), or, finally, to an output port for forwarding.
That process may be seen here:
![[Pasted image 20230705112026.png]]

If there is more than one matches on a table, the one with the highest priority is chosen. Instead, if there is a match with a table-miss entry there are 3 possible actions:
- send packet to controller: the controller with define a new flow that will be taken by the packet and similar packets or it just can drop the packet
- direct packet to another table: there may be matches on the rest of the pipeline 
- drop the packet
Finally, if there isn't any matches and also there isn't a "special" table-miss entry (which defines an action on those type of missed packets) the packet is dropped.
# Problem
Given the network topology of the Open flow Example, implement the following behaviour and solve the problem

Suppose the desired forwarding behavior for datagrams  arriving at s2 is as follows:
a)  datagrams arriving at port 1 from hosts h5 or h6 and  having hosts h1 or h2 as destination must be forwarded  to output port 2;
b)  datagrams arriving at port 2 from hosts h1 or h2 and  having hosts h5 or h6 as destination must be forwarded  to output port 1;
c)  datagrams arriving at port 1 or 2 and having hosts h3 or  h4 as destination must be forwarded to the specified  host;
d)  hosts h3 or h4 must be able to exchange datagrams.
Specify occurrences of the s2 flow table to implement this behaviour.

## Solution
(Note: In OpenFlow, it is not possible to directly express the logical OR operator for the in_port match field in a single flow rule. Each flow rule can only match against a single value for the in_port field.)
![[solutionToSDNTables.pptx]]
![[Pasted image 20230705115402.png]]

## SDN Control Plane
There are some main principles which define the controllers architecture, but each implementation of an SDN network has its own controller. A controller is made of layers and each layer has theirs own protocols.
![[Pasted image 20230330221910.png]]

We have three layers:
* **interface layer to network control apps**: providing abstractions API to components, such as routing, access control, load balance. This layer is made up of modules that handle communication with RESTful APIs at different levels of abstraction. The SDN controller may define some computations according to a network graph. Intent specifies that the goal of the controller is to provide a high level of the application, without specifying how to implement it.
* **network-wide state management**: provides information about the state of network links, switches, and services: **such as a distributed database.** For example, there are host information such as the number of ports in switches in the network, the layout of the switches in the network, and the ports of a switch. These host information is used to connect information from the underlying data structure, create a topology and network model, build statistics on traffic volumes and load on links, and use them to manage the flow table of the switches.
* communication: this layer implements the communication between the SDN controller and the controlled switches.

The components may modify the flow table to implement new forwarding paths, and there may be topology management or modules for computing paths.

### OpenFlow Protocol

![[Pasted image 20230331152043.png]]
This protocol is the link between controllers and switches. There are three types of messages: messages from controllers to switches, asynchronous messages (switches sending messages to the controller), and symmetric messages that can be sent from either a switch or a controller.
This protocol is different from OpenFlow APIs, that are used to specify generalized forwarded actions. SDN administrators don't program switches using directly the APIs, but they use the application upper layer.

OpenFlow is a protocol used in Software-Defined Networking (SDN) that enables communication between the controller and switch. The protocol specifies a set of messages that can be exchanged between the controller and switch. These messages are categorized into two types: Controller-to-switch and Switch-to-controller messages.

***Controller-to-switch messages*** include:
-   Features: This message is used to obtain the switch's capabilities and features.
-   Configure: This message is used to query or set the switch's configuration parameters.
-   Modify state: This message is used to add, delete or modify entries in the OpenFlow table using FlowMod.
-   Packet-out: This message is sent by the controller in response to a packet-in message. It encapsulates the message and sends it out of a specific packet-out port, usually to forward the message to a destination.

***Switch-to-controller messages*** include:
-   Packet-in: This message is generated by the switch when a packet arrives that does not match any existing entry in the OpenFlow table. The switch delegates the packet to the controller for processing.
-   Flow-removed: This message is sent by the switch to inform the controller of a flow table entry removal.
-   Port-status: This message is sent by the switch to inform the controller of a port status change.

In summary, OpenFlow messages are essential for communication between the controller and switch in SDN. The controller uses various messages to query and modify the switch's behavior, while the switch generates messages to inform the controller of events or request actions.


### An example in control and data plane interaction
 
![[Pasted image 20230322173830.png]]
1) S1, switch sends an OpenFlow **port status** message to the **controller**, as it sees that the link from S1 to S2 does not work.
2) SDN controller receives it and update its link status info.
3) Whenever the Link-state info changes in the network management, then it is registered that the Dijkstra algorithm will be called.
4) the Controller will calculate again the paths, with Dijkstra algorithm, **accessing the network graph info**. Then modifies the Link-state info in the network management.
5) The link state routing APP, on top of the interface layer, will interact with the flow-table computation component in the **the SDN network management layer, to compute the new flow tables**.
6) The controller uses OpenFlow (using modify-state messages) to install the new tables in the *switches that must have their updated, in this case S1, which may now route messages to S2 via S4, and making S4 know that messages from S1 may be needed to be forwarded to S2.*

### Two types of implementation
##### OpenDayLight Controller (ODL)
![[Pasted image 20230422101810.png]]
The service abstraction layer, that is the layer containing configuration and operation data and the messaging rules, interconnects internal, external and services.
For example we may see how at the Southbound API, there are the protocols of OpenFlow and SNMP (management protocol, master slave).

#### Onos Controller
![[Pasted image 20230422102143.png]]

Control apps separate from controller with REST APIs.
The intent framework is a specification of services, defining on what operating and how.
In ONOS there is a lot of emphasis on distributed core, here are specified all the definitions of the whole network. It may be distributed, allowing for better service reliability, replication and performance scaling.


## Topology discovery and forwarding

Several devices will implement the control plane and data plane.
The controller can develop a consistent view of the topology, based on that, it can compute paths according to the requirements of the computation.
So data plane switches is relieved of the processing and storage burden
associated with routing, leading to improved performance.

While in traditional routing, the routing function is distributed, in the SDN controlled network **the routing function is centralized in the SDN controller**.
To implement routing, we need to first find out how the links are connected and how the topology is implemented.
That allows the controller to have a consistent view of the topology:
* calculating the shortest paths.
* implementing application aware routing policies.

To do so, the controller sends OpenFlow messages. The implementation of topology and routing in OpenFlow networks is not standardized across all domains. Each domain may have its own implementation and configuration of OpenFlow controllers, switches and protocols, which can lead to differences in behavior and performance. However, there are some efforts to standardize OpenFlow specifications and protocols to promote interoperability and simplify network management.

### Topology Manager
* The controller maintains the topology information for the network
* it calculates routes in the network, with the shortest path between two data plane nodes or between data plane nodes and an host.
A controller is capable of managing different requirements, for example, one flow may have the requirements of low latency, while another flow may require high bandwidth.

The problem for the controller is to discover the topology of the network, which then allows the controller to easily configure it.

Considering OpenFlow switches, they have to major initial configurations to enable the topology discovery:
- When turned on a OF switch, it has the IP address and TCP port of a controller, allowing it to connect to the controller.
- **Switches have preinstalled flow rules**, that route directly to the controller, sending (OpenFlow) **packet-In message** to the controller, **encapsulating any message of the Link Layer Discovery Protocol (LLDP)**.

### LLDP
Link Layer Discovery Protocol works at layer 2 of the OSI model and is vendor-neutral. In OpenFlow-based networks, LLDP messages allow us to find how switches are connected to each other.

Basically it is a neighbour discovery protocol, with a single jump, that allows to advertise for a switch, its identities and capabilities to near switches and *it receives those from all others*.

### LLDP Frame:
* In traditional network, every LLDP frame is sent by a switch, which activates at regular fixed intervals of time as per configuration from the network administrator
* OpenFlow-based network,**the controller asks the switches to send LLDP messages** allowing to discover the underlying topology by request of the controller.

**LLDP uses Ethernet as its data-link protocol**. With 0x88cc as the Ethernet type fo LLDP.
The contents of the packet are:
* Chassis ID: it contains the **identifier of the switch that sends** LLDP packet.
* Port ID: it contains the **identifier of the port** through which the LLDP **packet is sent**.
* Time To Live: **time in seconds** which specifies for what amount of time the information received will be valid.
* End of LLDPDU: it indicates when the payload of the LLDP packet ends.

In can be seen in the image:
![[Pasted image 20230401121155.png]]

### Switch initialization in OpenFlow
When initialised, the switch attempts to establish a connection to the controller. The switch knows that on a certain port is connected with the controller, as said by sending a LLDP in a packet-In.
Then:
* the controller sends a **FEATURE REQUEST MESSAGE** to the switch
* the switch responds with a **FEATURE REPLY MESSAGE**. The switch will inform the controller of the relevant parameters for the discovery of links, like the Switch ID, **a list of active ports and their MAC address associated**, etc.
At the end of the initial handshake, the controller knows the exact
number of active ports on the OF switches, but doesn't know about physical connections between switches. 
![[Pasted image 20230401121539.png]]


## Topology Discovery
The process of topology discovery is done periodically and it is costly. To discover the network topology, the following steps are taken:
1.  The controller generates a Packet-Out message through the Link Layer Discovery Protocol (LLDP) and sends it encapsulated to each active port of each switch.
2.  Upon receiving the LLDP message, the switch forwards it with the appropriate Port ID it is sending it from to other adjacent switches.
3.  The adjacent switches encapsulate the LLDP a Packet-In message and send it to the controller, including metadata such as Switch ID and Port ID where the LLDP packet is received.
4.  The controller, upon receiving the Packet-In from the adjacent switches, extracting data can reconstruct the physical link between switches. The information provided by packet-in message are:
	-  Switch ID and Port ID of the original switch
	-  In metadata, the Switch ID and Port ID of the adjacent switch sending the packet-In

The process of topology discovery is repeated periodically for all OF switches available in the network.
To find the **number of packet-out to send**, to find all the links, we use:
$$TOTAL_{PACKET-OUT}\sum_{i=1}^SP_i$$
Where there are S switches, interconnected by a set of L links, where for each switch there are P active ports. 
**Remembering that we sent a Packet-Out for each port, and that we will receive Packet-In by multiple neighbour switch**. So there are additional packets and delay involved.

The host table and control table are full of information for the controller. The switch will receive a packet from A, and the controller will find out what ports the packet needs to be forwarded to. The controller prepares and computes the paths and then computes the entries of the flow table involved in the path. For all switches, there are instructions populated in their flow table, where it is defined:
-   Eth Src
-   Eth Dst
-   Out port

![[Pasted image 20230401162834.png]]

#### Host reachability
Discovery is typically triggered when:
* unknown traffic enters the controller network domain:
	-> from an attached host
	-> from a neighboring router
![[Pasted image 20230401163329.png]]
For example here it is seen that an Host A, connected with Port 1 to OF Switch 1 sends a packet.
**The host table is updated with the information about A and the Switch ID and Port ID of that switch where the packet is send.**
![[Pasted image 20230401163500.png]]

**Over the time the host and Topology tables at the controller will be populated as necessary**.
We may see that the Flow table of OF Switch 1 contains one record **path for:*
* ETH address-src of host A.
* ETH address-dst of host B.
* **then the action, which will be FORWARD (port 2), meaning to forward to OF Switch 2**
Then S2 Flow Table contains:
* ETH address-src of host A.
* ETH address-dst of host B.
* * **then the action, which will be FORWARD (port 2), meaning to forward to host B**

## Path Computation
Whenever the controller receives a packet-In builds a route between **source and destination**. With a **Flow Modification message** the controller advertises the route. Then at reception of **Flow Modification** each switch in the path, *add in their Flow Table the necessary entries to match the packets from that flow*.

Whenever there is a route, for example as in the example: 
![[Pasted image 20230401165106.png]]

-   Flow Modification message are sent, in route order in the **the reverse order of it**: first to switch 2, then to switch 1. Meaning the last switch in the route first, then the preceding one, then only at the end to the first of the route switch it is send. **This is because, if the message is sent to S1, and S2 has not received the instruction before S1, then S2 will may send a packet in message to the controller, multiplying the packet messages, as it may not recognize S1, and will send its information to the controller**. This will create delays, and additional flow mode messages are needed

Meaning of Packet-In:
-   **Source**: OF Switch
-   **Destination**: OF Controller
-   **Semantic**: This message is generated by the switch when a packet arrives that does not match any existing entry in the OpenFlow table. The switch delegates the packet to the controller for processing. It can also be used by the OF Switch to encapsulate LLDP messages **to the controller after they receive an LLDP message from a neighboring switch**.

Meaning of Packet-Out:
-   **Source**: OF Controller
-   **Destination**: OF Switch
-   **Semantic**: This message is sent by the OF Controller to instruct a switch to send a packet out of a specific port. It can be used for various purposes, such as forwarding, broadcasting, and flooding (instruct to send from all port besides the receiving one). **Note**: Encapsulating LLDP messages to discover network topology is just one of the use cases of Packet-Out messages. A Packet-Out message is sent for each port of the switch.

Meaning of Packet-Mod:
-   **Source**: OF Controller
-   **Destination**: OF Switch
-   **Semantic**: This message is sent by the OF Controller to the OF Switches that are in a route from a source (Host src) to a destination (Host dst). It is sent to all switches in the route from source to destination, but it is first sent to the last switch before the host, and then to the switches before that, up to the first switch contacted by the source.


# Google - First Implementation of OpenFlow

Initially, big data centers were the ones that required SDN. Several switches interconnect computing clusters, allowing SDN to be used within a data center, allowing the caching of the ordering of switches and managing them in a rack or the entire data center.

However, making traffic engineering between sites is the problem here. So managing wide-area network links, which can be built-in a data center or built-in multiple data centers, becomes essential. The Google WAN used for infra data center traffic is one example.

Google has two backbones:
-   B2: Carries Internet-facing traffic which is growing faster than the internet.
-   B4: Inter-datacenter traffic (horizontal) which is growing more than B2 and has more traffic than B2.
![[Pasted image 20230401174551.png]]

B4 saw a 10x growth in 3.5 years. The servers are physically connected by a backbone, not internet-facing for user traffic, and this network must be cost-effective. So the link must be used as much as possible.
Google has its globally deployed WAN, which operates as data center backbone. **The number of sites are few, around a dozen**.
![[Pasted image 20230401174902.png]]


## Why having a backend backbone
* To service users, you may have different sites, as it allows to serve content with geographic locality
* For fault tolerance in case of a failure in a site. Therefore, you may need to send replicas to the different sites with different datasets. The type of traffic includes user data copies to remote data centers (for availability and reliability), remote storage access for computation over distributed sources, and large-scale data push, synchronizing state across multiple data centers.
**Having a network to connect those data center allows to have a cost effective network for high volume traffic, and it allows to handle traffic which can spike in burst suddenly.**

## Requirement for google WAN:
There are several requirements:
	- Elastic bandwidth
	- Volume
	- Priority
Which are all different for each traffic flow type of Google WAN:
1) User data copies: you may need to send replicas to the different sites with different datasets (allow to access them geographically and fault tolerance). The type of traffic includes user data copies to remote data centers (for availability and reliability).
2) Remote storage access for computation over distributed data sources.
3) Large-scale data push, synchronizing state across multiple data centers. This has the **lowest priority but it has the highest volume, while being also the least latency intensive**).

It was found that the links were underutilized in WAN routing as all links had the same treatment. As those links have a cost, there is leasing on those, as they come from different providers, making it costly. Hence, Google decided to use SDN to exploit all the links.
 
![[Pasted image 20230401180030.png]]

***B4 requirements***:
1) Elastic bandwidth demand: there are applications that may be bandwidth-intensive, but that can tolerate network failures. 
2) There are a moderate number of sites, a few dozen, so there is no need for a large routing table.
3) There are end-application control and fine-grained application control, so there is no need for over-provisioning.
4) There is a cost sensitivity as, the private intercontinental link have a cost, the link must be used at 100% capacity. 

## Main Design Decisions
Traffic Engineering: *technique to ensure throughput and sufficient QoS levels in telecommunication network, by optimizing and controlling traffic flows.*

The main design decision includes:
1. Separate HW from SW: put intelligence in software. Use low-cost switching hardware, without the need for a huge buffer. Centralize traffic engineering, not necessary using the shortest path.  So, customize the routing and monitoring protocols to requirements exploiting the powerful computing of Google Server.
2. Low cost switching hardware: having edge application that controls the traffic limits, **remove the need for large buffers**. Also by having a limited number of sites, no need for large forwarding tables.
3. Centralized Traffic engineering (TE): allowing for optimal and faster Traffic Engineering, rather than using the distributed routing. There is also the possibility to share bandwidth among competing applications. TE server consist of an application that is on top of an SDN distributed control layer.
4. Increase link utilization: By efficiently using the *expensive long haul transport*. **By also imposing to largest bandwidth consumers to adapt to available bandwidth**.

## Architecture of B4
![[Pasted image 20230401183455.png]]

* Global layer: Gateway, connected to a Central Traffic Engineering Server and abstracts details of OpenFlow and switches. The Gateway collects information and provides them to the central traffic engineering service. We have a cluster of servers, with low-cost switches and with the purpose of forwarding traffic.
* Site controller layer: for each site we have **a set of controllers**, they balance the work and distribute the redundancy. The controller translates the high-level directives of Network Control Application to each switch of its site.
* Switch hardware layer: for each site, there is a series of switches. *These intercommunicate with the iBGP protocol (Internal Border Gateway Protocol: it will connect internal routers in the WAN/Autonomous System)*. **The switch of the sites are connected to other Clusters using the eBGP protocol (eBGP: external Border Gateway Protocol) allowing the connection outside of the WAN, as they are external Autonomous Systems**.

The idea is to improve the link utilization. We have site A, site B, and site C. With OFA: part of the switch that communicates with the controller. Each site has a site controller. Not just one controller, there are more controllers for each site for reliability reasons, avoiding a single point of failure. 

The BGP protocol is used, also in the switch because it was already used, and so was possible to implement a gradual roll-out, to limit the use of BGP. Allowing each switch to give both rules from OpenFlow and BGP router.

![[Pasted image 20230424093418.png]]
Traffic engineering server elaborates an aggregation of links to compute site-site edges. These aggregations are called Flow Group and are defined as tuple of <source site, destination site, QoS>.  Then, the flow group are mapped to a specific tunnel, inside the tunnel group. A tunnel represents a site-level path in the network. Finally, the Gateway forwards these Tunnels and Flow Groups to OpenFlow controllers that in turn install them in switches using OpenFlow.
This abstraction reduces the size of the topology graph in input to the Traffic Engineering Optimization Algorithm.

The bandwidth enforcer is the component that allow to specify the bandwidth allocation to a specific application.
In conclusion OpenFlow has helped Google improving B4 backbone utilizing near 100% bandwidth for elastic loads, mirroring production events for testing on virtualized switches, reducing complexity and costs.
