
ZigBee has the specification of a Network layer, which allows to implement Wireless Sensor Networks, for [[ZigBee standard]].

Its main goal is not just to support local services of ZigBee, but also to enable communication between devices in the network. Communication can be both within the local network and to outside networks (Internet). ZigBee supports both star and mesh network topologies.

The AODV (Ad-hoc On-demand Distance Vector) protocol is designed for small multi-hop networks that can support mobility. It is based on distance vector, but instead of maintain all distances with all nodes create the path only on demand.

Directed diffusion is generally used for data collection from sensors to a sink, while AODV aims to support local communication and services in addition to data collection.

AODV requires broadcasts and memory, which ZigBee chooses to use anyway despite its limitations because it is suitable for their needs, though not a fully optimized solution.

AODV is a research protocol, not fully optimized for commercial use. ZigBee makes it work for their use cases.


## Design

![[Pasted image 20230617193556.png]]

**The Network layer is built on top of [[ZigBee standard]] IEEE 802.15.4 (MAC Layer[[MAC Protocols]])

We must remember that we have three types of devices in ZigBee, and in the Network layer too.
![[Pasted image 20230617195905.png]]

* Network coordinator: it is a FFD( Full Functional Device) , creates and manages the entire network
* Routers: a FFD but with routing capabilities
* End-Devices: may be FFD or RFD(reduced) which just act as simple device in the network
![[Pasted image 20230617200452.png]]


Note that it is not really important for the Star topology, but its very important role for tree and mesh.
Note that the parent-child relationship established as a result of joins will shape the network in a tree. We have:
* root= coordinator
* **internal nodes** = *ZigBee routers*
* leaves= end-devices or routers acting as end-devices

Consider that an efficient protocols for Wireless Sensor Networks have to be simple and localized. There is a problem in assigning network addresses.
The problem is that just assigning an IP network address is impossible, you need to buy them and assign. That cannot be replicated here with thousand of devices.

If you build an autonomous network, without manual intervention, you need a way to assign to a node an address that is not already used.
It means to have a global agreement on the address to assign to a node. This may mean to create a big neighbourhood.

## Network address assignment
To assign network addresses, what is used is **the tree topology**.
The coordinator is **statically configured, as we may not have an unlimited number of end devices or routers** (the network has an already pre-configured size). Consider that the configuration is local and not totally global.
* $R_m$ : max number of routers that a router may have as children
* $D_m$:  max number of end-devices that each router may have as children
* $L_m$: maximum depth of the tree, which is the global limitation

It takes a long time to get an address. Note that the device *will join as up as possible in the tree, this minimize the number of hops*.
Addresses are assigned **according to tree structure or sequential assignment (in order of arrival) or even in a random configuration. 

## An example configuration
**Those three parameters known to the coordinator are what allows to create the three structure to assign addresses**.
Given
* $R_m$ : 2
* $D_m$:  2
* $L_m$: 3
The three structure to assign network addresses may be seen here for this network:

![[Pasted image 20230617201659.png]]
**The node IDs are assigned by going Depth first**.

Coordinator as address \[0-28\] range.
According to the parameter, we have the limitation of the size of the network, but in this way we have a set of address that every router will use.
The coordinator is then able to assign the id of the routers.
It chooses itself the devices ID, assigning itself ID 0.
Knowing the size of the subtrees routed in 1 and 14 for example.
It pre-allocates to 1 the set of addresses it needs (1->14), and it does so for router 14 too (14->26).
Then we have the two addresses for the end device (27-28).

When the first router joins:
* take address 1 itself and as set of addresses of its children in the range from 2 to 13.
	* from 2 to 11 is split in two subset, as leaves we have two endpoint (12-13). **Note how the last elements of the range are the one chosen to index end devices**.
* When a node joins, to a router, the router already knows what address to give.
* If the router does not have free addresses, it will reject any request. Two nodes will never have duplicated addresses.
	* In [[ZigBee standard]] it is needed binding, as when a node disconnects and reconnects , will may get another network address. With binding that the app is able to remain identifiable even after a disconnection.
### A question
Given:
![[Pasted image 20230618094300.png]]

We will proceed level by level:

level 3) 
- we have router 24 and endpoint 28 as child of router 23. 
level 2)
* we have router 23, which has assigned the range \[23,28] computed by doing router id: 23 + 2+3 = 28. We have router 29 which has assigned the range \[29-34]. Both are child of router 22.
* we have router 44 and endpoint 63, as child of router 43. Router 44 has range \[44-49]
* we have endpoint 19 as child of router 1.
level 1)
* we have router 22 which has assigned the range \[22,34+2] this was guessed by looking at the range of its child 29.  But we must add 2 id for the endpoint child of 22, which it does not have here
* we have router 43. which has range \[43,63], easily guessable as we have its right endpoint child with id 63.
* we have router 1, which has a leave endpoint 19. The range assigned to 1 is \[1,21], **there is an error in the slide, as each router may have 2 children and the children are given always the highest addresses in the range, here it should be either 20 or 21**.
level 0)
- it has range \[0,65\] guessable as we have its right endpoint child with id 65.


## Routing
There are then various way to do routing:
* Broadcast (to all nodes)
* Mesh routing (node to node)
* Tree routing (node to node)

### Tree
Route over a tree with addresses is trivial in a tree, visit the tree, using the ranges for said router.
![[Pasted image 20230618104744.png]]

On the tree topology there is beaconing because of the underlying [[MPCS/pages/802.15.4]].
It is necessary to do scheduling, this is because scheduling prevents the beacons of one router to collide:
* either with the beacons of their neighbors
* or with the data transmissions of its neighbors

**The beacon interval (not the beacon frame) is ideally longer than the active portions, as the idea is to make the active portions shorter**. That allows to avoid overlapping of the beacons of neighbouring routers and also the larger is the active period, the more devices can transmit beacon frames in the same neighbourhood. The beacons will *allow a coordinator, which in this case we see are the routers, to manage its connected nodes in the network* 

![[Pasted image 20230618105423.png]]
**What can be said about routing in a tree, is that it is easy as just route the message along the tree and towards the destination address**.
The beaconing means that **each relay router must synchronize with the next hop beacon frame to relay the message**

### Mesh
The ZigBee mesh network layer uses an on-demand ad hoc routing protocol (AODV). This means that routes between nodes are discovered only when needed to send data to a destination. Routes are not stored proactively.

When a ZigBee node needs to send data to another node it does not have a route for, it broadcasts a route request message (RREQ). Neighboring nodes rebroadcast this request until it reaches the destination node.

The destination node responds with a route reply message (RREP) that travels back the path of the request, establishing the route. Now the source node can send data to the destination along that path.

Each node along the path stores only the next hop toward the destination, not the entire route. So routes are partially stored on-demand as needed, but full end-to-end routing information is not maintained.

Since routes are built on-demand, ZigBee does not keep a complete distance vector routing table with routes to all possible destinations. Routes are created and stored only when data needs to be sent.

There are two cases for the sender, at each step of the routing:
* if the sender is an end device
	* it forwards the message to its parent
* if the sender is a router or **a coordinator**
	* it maintains a Routing Table, which will use to **route the message according to the routing procedure**
An example of routing table in a ZigBee router follows:
![[Pasted image 20230618110650.png]]
It contains the:
* destination address, to which route the message
* Next-hop Address: the address to which route the message to reach the Destination
* Entry status: states if it knows that the router is active, it has not responded or it will be tasked to respond

It may be seen here the structure with routing tables 
![[Pasted image 20230618111100.png]]

*Routing in a mesh involves*:
* Route Discovery whenever in the routing table there are no entries for a destination
* Forwarding directly: whenever the next hop is present for the destination in the routing table

### Mixing Mesh and Tree
The routers may maintain both the routing type information and the *routing algorithm may switch between the two*. Consider that Mesh routing does not allow beaconing, while Tree routing does allow it,
**so the algorithms must account for that in the switch**.

### Route Discovery Protocol
The protocol is initiated whenever a routing table does not contain a valid entry for a destination the router is asked to forward a message to.
All routers have a **Route Discovery Table (RDR)**. We may see an entry for the RDR, that it is made after a **route request**. The entry itself is not only created in the starter of the route request, but on all routers where the request when through.
![[Pasted image 20230618112605.png]]

* RREQ ID: a sequence number to all RREQ messages 
* Source Address: address that started the route request
* Sender Address: the router that is relaying a route request
* Forward Cost: the "cost" accumulated from source to the current device. That one will be *filled by the Route Request RREQ sent by the router*
* Residual Cost: the cost accumulated from the current device to the RREQ, it will be filled by a RREP message (Received by another router), meaning that it will be filled in the back traversal from destination to sender.
* Expiration time: the timer indicating the number of millisecond until the entry expires, as it may be old, outdated and needs to be refreshed at next request.

### Question

![[Pasted image 20230618120946.png]]

1) The router will be assigned ID -> 2,as it will have range \[2, 6\] being it the "left" child on router 1
2)  it will be assigned ID ->21, it does not have a range as it cannot have children, because its at max depth
3) it will be assigned id 8 **as we assign the lowest possible number first (a DFS)**, it will not have a range, as it will not have children, being at max depth.