In conventional approaches when monitoring with sensors, the sensors are just transducers, connected by wire to a centralized control device.
Nowadays this in not true.
*Sensors have become intelligent, they can process the sensed data and are microsystems with processors, memory and multiple transducers*.
Furthermore they communicate wireless and are autonomous, being battery-powered.

Since are autonomous, sensors will build a network, without not just direct communication and *its not just a communication with a direct control node.*
At the same time this network does not need a fixed structure, such as one made with cables, making the solution easily deployable.

## Sensor deployment
Sensors are deployed in a Sensing Field and can form a network where
* Some sensor may act as sinks, 
* other as sources. 
The sinks will interface the wireless sensor network with the world. The data are transmitted to a sink and then they will go to the internet. It is necessary that sink is a router, as it forwards it to the internet for the user.
![[Pasted image 20230615095657.png]]
IoT devices do not need to perform any routing functionalities, they just need them for access point. In this sensor network we have routing problems within a network. Where we deal here with devices that have reduced resources.

### Wireless Sensor Network
In Wireless sensor network, **the network is organized according to the data distribution**. In this type of network, the application and network are indistinguishable. It makes sense to organize the routing around the data. 

The sensors will generally sample environmental parameters.
Producing streams of data: **the data streams can be pre-processed locally and then further forwarded to a sink.**

There may be moments in which the sink may be temporally unavailable, hence the network operates autonomously **pre-processing and storing sensed data**.
The only requirement in this case is to have enough memory, as the sensors act as loggers.

*To allow the network to function well and store data when sinks are unavailable, energy efficiency is a key factor*.

Consider that the networks of such kind must be easy to deploy, there must no be cables and they must be self-configurable, with no centralized control.
Also the sensors are very cheap and there should be some redundancy to get better fault tolerance, allowing also to scale up easily. Sensors may also be mobile and move in a field.

The sensors can be programmed on the fly, allowing to adapt them to changing conditions and implement new sensing task. They can receive updates over the air and they have to be able to reboot their selves.

The number of sensor nodes can be several orders of magnitude higher than common networks. Consider that the nodes are dense and prone to failure, since they are highly constrained in power, computational capabilities and memory.
*There may happen topology changed depending on node failures and mobility*.
Those nodes instead of being general purpose, are with built with one purpose, sensing and sending the data. So there is a tight integration of the network with the sensing task.



# Data Centric vs Node Centric

In traditional routing protocols, there are computational and memory requirements that are:
* large routing table
* large size of packet headers
* many layers to handle

Also in traditional routing the network and the Node ID description is organized around network addresses.
A network address in the traditional network, does not give any information on the devices. In general the addressing is **identity based**.

Instead here we want to represent the device:
* the physical place where the device is taking data, so attribute a Node ID based on an attribute-based addressing, giving location awareness to the network. The goal is to create **data-driven routing**.

## Data centric routing
One of the best approaches to organize the network is:
* description of the data
* attributes of the data
Consider network based on different parameters, then the routing depends on the query on data.

E.g.: to do the query = Temperature < 5. It creates a routing tree reaching all the nodes interested in the query, and then they sent back the information related to the temperature.
As it may be seen here:
![[Pasted image 20230615115847.png]]
So the nodes, identified by the attribute of the temperature, will be queried.
From the network point of view, some nodes will all be transmitting data, but as the organization of the network as data collection tree, some of the data may travel along the same path, so some sensor will communicate with the same path and are related to the same query.

From the network point of view, that is a waste. 
To optimize the network and reduce these inefficiencies meta-aggregation is computed; it involves data aggregation at the crossing of two paths for two independent pieces of information related to the same query. In this way you may forward just one message rather than two, in such way aggregating two paths.

*Locally produced data may be aggregated to other data actually, given that there are multiple sensor along paths to the sink*.

#### Location Awareness
Location Aware load, may be based on the fact that the network is organized in term of addresses, so that a location is associate with data for example.
One may for example query the temperature of sensors for a certain area.
![[Pasted image 20230615120836.png]]

To reduce resource consumption and improve efficiency, it may be beneficial to collapse the application layer and network layer, which is a characteristic of the data centric paradigm used in wireless sensor networks.
This paradigm involves other type of problems, such as the implosion problem:
* **implosion problem**: data are forwarded to the sink according to its attributes. Every time you do something like forwarding packet to the sink, it is like two different independent data is arriving, the sink should be able to recognize that *those are not two event happening*, but just one that is recognized as being sent by multiple nodes. ![[Pasted image 20230615122020.png]] 
	In that case what happens is **flooding by dissemination**, a node A starts by flooding its data to all its neighbors as it may send a request/data, then two copies of the request/data will arrive at node D, the system wastes resources **as two copies of the request are send and also two copies of the response will be sent back. This is because there are the path from A to D.**

* overlap problem: since we deploy sensors with their range, we may catch the noise of a room and noise from outside, the range of a microphone may partially cover the outside, every sensor is placed at precise positions, but has a coverage bigger than its place. The device may detect things coming around them. In their range, the sensor may overlap. It is not easy in the sink to tell if two independent even happened or if just one being sent by two nodes that sensed the same event. ![[Pasted image 20230615122218.png]] 
	It may be seen that the sensors may flood their data by sending them raw and without aggregation. There is the need of suitable aggregation algorithms to solve this problem.

# Directed Diffusion
**Directed Diffusion is a coordination protocol to perform distributed sensing of the environment**. Sensors are deployed without external infrastructure, and when turned on they start exchanging information.

The sensing task can be parameterised and the network itself may be queried by sending a specific request for a specific sensing task. 

Directed diffusion is data centric:
* all communications are for named data
* the data generate by sensors are named by $<attribute,value>$ pairs
* a node itself requests data by sending interests for named data

A question to the network may be:
"*How many pedestrians do you observe in the geographical region X?*" which is a question to the sensor network.

Each node request data and the sensor will respond to specifying query, so a node ask the network by sending the query and the network respond.

Data is *named* with an attribute-value pair, the sink will **disseminate a sensing task in the network, asking the sensors to do that task, by sending a so called "interest"** for the named data.
The dissemination of interests will setup: **gradients**. They are  data, which are interested in spatial variation in the attribute or parameters, they draw from sensors "events" that match the interests, for example a temperature going above a certain threshold in a particular area.

The sensor network work on a interest, and through the gradient the data is sent to the sink, there are some cases, multiple sensors may detect the same event, resulting in duplicate data. The data flow along the gradients, which are distributed in the sensors, following multiple paths. The sink will recognize to just process one message, by **"reinforcing"** it.

### Format of an interest to activate a task
The fields of a task are :
* Type: type of sensitive task to activate, **the task is data centric, as it activates as specific sensor**
* Interval: sampling rate, so at which rate an event should be notified to the sink (in ms). This expresses two things, the sampling rate and the rate at which information should be transmitted. It allows nodes in the path to know that the message will flow 1 for every 20 ms (for example) to tune the duty cycle and make energy saving. What is enabled is called cross-layer optimization
* duration: time perform the operation, the task is activated only for a period.
* region: we express ranges, of a rectangle, with 4 points.  **The coordinates may refer to a GPS-based coordinate system**. This expresses the location awareness

### Responses to interests with events
The system responds with a tuple, composed of:
* type: type of the event, e.g.: *four-legged animal* for an animal sensors
* instance: the instance of the type, e.g.: *elephant*
* location: coordinate, e.g.: *<125, 220>*
* intensity: amplitude of the signal, e.g.: 0.6
* confidence in matching, e.g.: 0.85
* timestamp of event, e.g.: 21:04:43

### Interests lifecycle
Interests are produced by sinks *periodically*. Multiple sinks if present may produce their own interest.
The interests are:
* exploratory in which the sink announces the query
- refreshes which are necessary because *the dissemination of interests is not reliable*
A node receiving the interest may forward it selectively to a subset of neighbors. All nodes must have a unique IDs.
 
### Interest propagation
**All interests that differs only in sampling rate are aggregated**.
Interests are put into a cache and they will expire from the cache when the duration time expires.
Each interest in a cache has a gradient, which expresses
- **direction**: representing the node from which the interest was received, *this allows to route the data from event back to the sink*
- **a data rate**
*The same interest may be received from different nodes, so there will be several gradients from which the data may be sent, doing multiple paths*.

#### Motivations
There is also a dynamic management of the network, where the part of the network that is producing the most relatable information is reinforced. The network of this type is intrinsically unreliable. Considering low power and cheap hardware deployed in a field; using wireless communication that are intrinsically weak, so there is the possibility that you may lose some sensors, then, redundancy is needed and make periodical polls. If requests are lost in the network, a redundant will bring the result, also by injecting a new interest after a node died by battery depletion, the network is forced to reformat. That explains why the cache expire and why there are refreshes of the interests.

#### Propagation
The interest propagates in the network, the gradient consider relevant information to the interest and associates it with the rate of transmission. 

If two different interests A and B are injected by the sink, then the gradients will overlap *over the physical links*, but they will keep different properties: type of event, area if interest, ... In general all properties derived by the interest from the sink

The gradients will **associate the rate to which the interest rate may fall**. There may be independent queries for topics, the interests may have independent rates of transmission and sampling, they will just overlap and be independent from each other. For each interest there will be intersecting *data rate*. So there may be for the same interest different forwarding from a node.
The idea is, as long as a interest is not satisfied, the request is sent and sent again. 
An example of network with a single sink is:
![[Pasted image 20230615152506.png]]

## Questions
1. What is a gradient?
2. Why does an interest is repeated periodically? Isn’t the first one sufficient? 
3. How does the mechanism of directed diffusion may be used to optimize the underlying MAC layer?? (cross-layer optimization)
1) A gradient is a data that is set up in the network when an interest propagates. It contains the following information:
	- Direction: The direction towards the node from which the interest was received. This is used to route data back to the sink.
	- Data rate: The rate at which data should be sent towards the sink for that interest. This is specified in the interest and allows nodes to optimize their duty cycle.
	- Timestamp: The time when the interest was received. This is used to determine when the gradient expires.
	- Other interest attributes: Other attributes from the interest like the sampling rate, duration, etc.
	The gradients essentially create a data flow pipe in the direction of the sink. Data that matches the interest and is generated at any node will flow along this pipe towards the sink at the specified data rate. The gradients implement a form of data-centric routing where the routing path is determined by the content of the data.
	
	The key purpose of the gradients is to route relevant data back to the sink as efficiently as possible while accounting for the energy constraints of the nodes. By specifying data rates in the interests and gradients, Directed Diffusion achieves a degree of cross-layer optimization.

2) Interests are repeated periodically because the dissemination of interests in the network is unreliable. Nodes can fail or interests can get lost. By periodically re-sending the interests, the network is ensured to receive the interest and set up the gradients. The periodic re-sending also allows new nodes that join the network to receive the interest and participate in the sensing task.

3) Directed diffusion enables cross-layer optimization by providing information about the data sampling rate in the interest. This information can be used by the nodes to tune their duty cycle and save energy. For example, if a node knows that it will receive data once every 20 ms for a particular interest, it can keep its radio on only during those 20ms periods. This allows the nodes to optimize their energy consumption based on application layer information.
[[MAC Protocols]]

# State Machine of Directed Diffusion
The sink is the medium used by the user to sample. The user connects to the sink.
Whenever the sink **sees that X,Y,Z node are the one with relevant information, the sink will not send the interest to another node K. What happens than for K is that since the interest have a duration, K after that duration will not receive requests anymore for that particular interest.**

The interests are disseminated by the sink over the network using the broadcast protocol. What a sensor device does when receiving an interest is to setup a gradient, then a sensing task. Once the sensor detects an event, **matching an interest in the cache**, it:
* starts sampling the event at the higher sampling rate of the **corresponding gradients**
* sends a message back to the sink, to do so it uses gradients associated with the interests in cache.
	* The gradients correspond to the neighbors interested in the event.
	* If a message is lost, there is a chance that the same device will be reached from another path.
The Neighbors will forward the data only if the corresponding and its gradient are in its cache. **Also since the messages for the same interest may arrive from different neighbours, it will filter messages, keeping only one to forward, so aggregating them.** The filtering may be seen in the following image, as the same event is detected by 5 and 6, but 2 will forward just one message! ![[Pasted image 20230615163004.png]]

### Simplified state machine
![[Pasted image 20230615155311.png]]
As it may be seen here the states are:
* Sampling:
	* which remains to sampling when an event matching interest is in cache or receives an event matching interest in cache. **Then it will perform the action to forward the event to the sink through a gradient**.
	* when the interest expires, the action performed is to delete the interest from cache and remains to sampling. An interest expires from caches, and from this point on the device will stop sampling for that interest.
	* when an interest is received, **then it adds the interest in cache, it sets up the interest gradient and forwards the interest**.
	* if the cache becomes empty, it does nothing, we switch to the idle mode.
* Idle: **in this state the device waits for interests**
	* when a new interest is received, it *adds the interest in the cache, sets the gradient and forward the interest* and finally switches the state to sampling.

A device matches the events with the interest in cache or it gets from another device an event that match an interest in cache, in both, the device forwards it.
Generally: if device has information or receives information, then it forwards it to the sink.

All of those are parallel tasks, not in threads but there is a schedule task mechanism in the context of embedded devices, as you share with different tasks the execution, the main loop will cycle through task and will give each some time to execute. 

Gradients are structures present in the node, where the nodes are the edges of the graph by the way.

The events may be notified multiple times in the sink, once for each paths. 
*This at least enforces redundancy, allowing the data to arrive with more probability*. You cannot control the level of redundancy sadly, as a consequence there is the problem of implosion. You may associate to the response the fact that a node detects the message.
The routing itself is based on the dissemination of the gradient.
*When the sink detects an implosion, it may decide that its too much work to process, so interest to a node is stopped and allows to stop the forwarding through a path, allowing only one path, as a consequence of the* **reinforcement**.

#### Same event
If two Nodes detect the same event, then it is up to the sink to decide if they are independent or not. How it does is beyond the scope of this course lucky for us.

The focus is not on the reliability of the initial message, but on the whole network as a whole.  

### Reinforcement
What reinforcement consists in, is basically that once the sink starts receiving data matching an exploratory interest, from a *specific sensor n*. Then what happens is:
* the sink **reinforces n, to improve the quality of the received data**. This means improve the sampling rate of that sensor in that interest. The exploratory interests have a low sampling rate.
	 
The reinforcement will propagate along the whole path from which the events are received, up to the sensor n being the source of the event.
This phenomenon can be seen here:
![[Pasted image 20230615162638.png]]

### Redundancy
While a message may be lost, as there is no reliability:
* interests are periodically send, as they are refresh 
* messages flow constantly, the next one will come soon
* **there is an implicit assumption that the data sampling is redundant, as more sensor will get the data for the same interest, so if one fails there will always be another one**

### The advantage of Directed Diffusion
* simple: multiple app are built on top, here the information to make the network work is less than the traditional one, just a few bytes are sent in the message. It works on a simple finite state machine.  This implementation is really suitable for low density device, allowing to make an affordable network. 
* scalable: large network is possible due to the fact there is no need of complex data structures. 
* effective: you do not need high network processing, and if you need its just localised. There is no requirement for complex data aggregation and pre-processing.
* robust: you may need different sensors for some events such as a bomb explosion, this means that the device must communicate point to point to do that, you use broadcast to all nodes and you have directed acyclic graphs for data delivery, if one node fails, there will be another path to the sink.

### Processing locally vs centrally, a problem
For example in the camera for face detection is costly.
Transmitting 1 bit, costs as processing 1000 bits. There are trade off between transmitting and processing, this is the same concept of edge computing. Doing the process locally is difficult in directed diffusion, as it required adjacent device to communicate locally, while its made to communicate with the sink.
So the problem of needing to send data rather than local processing makes costlier directed diffusion in cases where large quantities of data may be pre-processed.

# A simple WSN organization
The Directed Diffusion Paradigm itself suggests a way to organize a WSN.
* One sink will act as :
	* coordinator and
	* gateway to the internet
* a routing tree is rooted in the sink
* **there will be periodic refreshes of the data collection tree**.

The assumptions are:
* one sink, with id 0, which is denoted as $n_0$. The sink will have a double radio interface
	* one to the internet
	* one to the WSN
* each node will gave an unique node id $n_i$
* the sink will initialize and maintain the routing tree

**The kind of messages that a sensor sends are unicast messages, directed from itself to the sink**.
Meanwhile the sink is capable of broadcasting to the entire network messages and it does.

## Tree routing
We may see as follow the pseudo code of the  sink and the pseudo code of a node i.
```C
TIME RTInitTime = …; // timer to wait for the init of routing tree
TIME RTRefreshTime = …; int c;//time until next refresh of the routing tree
int c;
void init() { 
	set_timer(RTInitTime); 
	read c; // from permanent memory 
}
event timer_fires(){ 
	routing_tree_init(); 
}

void routing_tree_init() {
	c ++;
	store c;
	msg= <RTInit,0,all,0,c>; //prepare a RTInit message
	broadcast(msg); //broadcast msg to neighbors
	set_time(RTefreshTime); // set timer to next refresh
}
event receive(msg){
	if (msg.type == DATA) {
		<forwards msg on the serial>; 
	} 
	else if (msg.type == RTInit) 
		<disregards msg>;
	}
}
```
We may see how it will periodically initialize again the tree.
It will discard the `RTInit` message it may receive from the network since they are propagated and the nodes may also them to it.
The function `routing_tree_init` will set the timer to expire after `RTefreshTime`.
The messages will have type `RTInit`.

The messages may be seen better there:
![[Pasted image 20230615173926.png]]
The `brcIndex` refers to how many broadcast messages were received from the sink. The sinks stores it in $c$, which for it represent the number of routing_tree_init broadcasts it did.


For the node i instead the pseudo code is:
```C
TIME SampleTime = …; //time to wait for next data sampling
BOOL RTFormed; //TRUE If the routing tree is ready
int rely, br; 
//Rely=id of the relay node to the sink, which is the parent in the routing tree, which is also known as gradient in directed diffusion 
//BR= counter of broadcast messages received from the sink
//
void init() {
	br=0;
	rely = 0;
	RTFormed = FALSE; // no RTInit received yet 
}
event timer_fires(){ 
	d = readData();
	msg = <Data, i, rely,i,d>; 
	send(msg); // unicasts msg to rely node
	set_timer(SampleTime)
}

event time_fires() {
	c ++;
	store c;
	msg= <RTInit,0,all,0,c>; //prepare a RTInit message
	broadcast(msg); //broadcast msg to neighbors
	set_time(RTefreshTime); // set timer to next refresh
}
event receive(msg){
	if (msg.type == DATA) 
		send(<Data, i, rely, msg.origin, msg.data> );
	else // msg is a RTInit
		if (msg.brcIndex>br){
			br=msg.brcIndex; //the c from sink
			RTFormed = true;
			set_timer(SampleTime);
			rely = msg.source;
			broadcast(<RTInit, i, all, msg.origin, msg.brcIndex>); //forwards RTInit
		else<msg is stale: disregard>
		}
}
```

What the code does is to send msg to a rely nodes, every time the timer fires, after SampleTime.
The timer is set after a message is received, but said message must be greater than the current broadcast index, otherwise its discarded.
The node will also rely the message to all other nodes.

The image shows the pseudo code of the message send to initialize all node, in action.
We may see how the message is sent in broadcast
![[Pasted image 20230615185437.png]]
* type = RTInit
* source (Relay Node) = 0 (the sink has node id 0)
* forward (Next hop) = all (broadcast)
* origin = 0 (sink)
* c = "value reached of the turn of the broadcast/refresh"

Then when $n_1$ has processed the receive, it will send a message to its neighbours, which also include SINK and $n_2$, it is just $n_3$ that is now reachable.

![[Pasted image 20230616100452.png]]

Furthermore it can be seen that:
* sink discards all `RTInit` messages
* $n_2$ will discard the message because its `brcIndex` is not greater than the one received from sink, as its the same c.
* $n_3$ will accept the message
	* type = RTInit
	* source (Relay Node) = 1 (it is node $n_1$ relaying the message)
	* forward (Next hop) = all (broadcast, as all RTInit are)
	* origin = 0 (sink, it was the one starting the chain)
	* c = "value reached of the turn of the broadcast/refresh"

Furthermore when $n_2$ sends it broadcast RTInit, all others will refuse it:
![[Pasted image 20230616101753.png]]

We may see how an event message may reach the sink from $n_3$:
![[Pasted image 20230616101907.png]]
in the event timer_fires, once SampleTime passes, the node $n_3$ sends a message. It may be seen how it will **saved as relay the node $n_1$ which was the one that sent to it the message**. So the message sent is to $n_1$ is:
* type: DATA
* source = 3
* forward = 1
* origin = 3
* d = **the data read from the sensor**
What $n_1$ will do is then to forward the message to its relay, which is the sink, as it directly sent the `RTInit` message, The message is:
* type: DATA
* source = 1
* forward = 0 (sink)
* origin = 3
* d = **the data read from the sensor by $n_3$**


As we can easy and low cost to organize. Each node will have a relay node to use to reach the sink.
If for whatever case $n_1$ goes down, in the next "repetition" there is still $n_2$ that will send RTInit to $n_3$ and so $n_2$ will become its relay.

### Scalability but limited
1. Directed diffusion is scalable in the sense that each node maintains minimal state and does little computation. Even as the network grows, the amount of work each node does remains small.
2. However, nodes near the sink have a higher burden since they have to forward messages for many other nodes. Their radios require more power to handle the increased communication. This can limit scalability near the sink. That may be seen in the previous example as only $n_2$ and $n_1$ were connected to the sink, so in a larger network they would need a lot of radio communication power to handle that burden of relaying message to the sink.
3. If there are only a few nodes connecting parts of the network, they can become overwhelmed by having to forward messages for many other nodes. This also limits scalability.

![[Pasted image 20230616103709.png]]
In this image there are two sinks at the top right and bottom left corner. What is seen is the power consumption with the black colour. We see how the nodes near the sink are really the ones with more power consumption. There are possible solutions,  organizing the network differently, placing the sinks in differently way. 
In the following image it can be observed four different configuration: 
* CEN(Centralized Energy-efficient Network): spreads sinks in the network, evenly associating nodes to different sinks, CEN is a centralized Heuristic: it puts the sinks at the center
* DIS (Distributed Intelligent System): it is a decentralized heuristic: it puts the sinks at the corners
* RND: Random Mobility, spread randomly the sinks:
* STATIC: optimal static sink placement
![[Pasted image 20230616104720.png]]
The darker nodes are the one that will suffer more, as they are closer to the sink, they have larger power consumption.
At the same time, DIS is capable of delivering much more packets, even more than static. DIS is a more energy aware solution over RND and STATIC.
There are options such as have multiple sinks or mobile sinks.
In fact, DIS and CEN heuristic have interchangeable performance, they can be exchanged independently depending on the cases.


### Other issues
Direct diffusion assume that the sink is permanently connected to the network, **but** at the same time the sink may not always be present as there could be issues. **The network does not operate autonomously as the sink must be permanently connected to the network**.
As such we must think of mechanism to store information on the network.
Basically, **directed diffusion and tree-based WSN are not suitable for complex data processing, as they do not exploit processing (edge computing) and storage capabilities of the sensors**. Consider that to detect composite events, it requires communication among sensors.
*More complex network require more complex routing*.


### Why edge computing
![[Pasted image 20230616110232.png]]
We may see that, a big input, such as an image, sent with input bandwidth of 880 Kbps with 1 GOPS (Giga operation per second) can be compressed to require for transmission amount just is 0.16 Kbps  in bandwidth,which is very low, achieving a compression factor of 500x.
**The compression that you may get with processing rather than sending data is a lot.**
If you do not do on-board processing, you need to transmit and you need to use the radio at high duty cycle.
There is a trade off of spending more energy in process rather than just send.

### Composite events
The composite events are events that may be detected only if sampling from multiple sensors which are heterogeneous and spread over a large area, if you exploit communication patterns that let sensor talk. 
This detection requires the sensor to exchange data and perform distributed data aggregation.

# GPSR (Greedy Perimeter Stateless Routing)

In response to that, if one wants to implement in network processing and implement a communication pattern that is arbitrary, we have routing protocols that let two arbitrary device communicate with each other. One possibility is to take the Internet Routing protocol and to put into wireless layers.
Traditional routing protocols like IP routing would allow any two devices in a network to communicate, providing arbitrary connectivity. However, these protocols require storing routing tables which scale poorly for large networks of low-power devices.

The problem with it, would be, for a network of 10,000 devices:
* For a network of 10,000 nodes, representing the network topology as an adjacency matrix would require a 10,000 by 10,000 matrix, meaning 100 billion elements.
* Storing the distance vectors for just 10,000 nodes would already require substantial memory. Each distance vector would have 10,000 entries, one for the next hop to each of the other nodes. With each entry requiring a node address, storing 10,000 distance vectors would require around 20 kilobytes of memory just for the routing tables.
Consider that low-power devices have limited RAM memory available, which is needed not just for routing but also for buffering data and executing instructions. 

You cannot afford the memory on low power device. On direct diffusion, you can scale up on the memory as many device as you wish, and you do not have have large memory overhead, but you have the previously stated problems.

### Geographical Position
Rather than using IP address or simple Coordinates such as in directed diffusion for the queries, an idea is to use Geographical Position. 
This fits also with the deployment of the network, the sensor network will be deployed on a field, and its abstracted on a square with coordinates. Over a plane we represent the network and its topology, knowing to which device each other are connected. It will never happen that distant device will communicate, only physically close device will communicate due to the transmission range.
The goal is to use the coordinate to find the destination.

The first proposal to do this is GPSR, allowing to provide arbitrary node-to-node routing, assuming limited resources and communication overhead.

The protocol assumption:
* field deployment, so on a two dimensional space
* each nodes knows the position of neighbours, with a localization algorithm and GPS
* the source knows the coordinates of the destination, which is a bit of a problem, as one may not know it, to solve this a DNS service and Distributed Hash Table was thought about, with the DHT the burden to store the domain name service is split among the nodes in the network.
The protocol is scalable, as only the geographical position are needed.
**There is no need to have route discovery and to have large route caches or routing table**.
What is used by the protocol to route the messages are:
* packet headers which contain the destination coordinate, meaning that *the route itself must not be stored in the headers*

**Typical protocols uses broadcast to get positions, with distance vectors protocols and at a certain moment they will reach all part of the network after the start of the broadcast**. In GPSR there is no requirement for that.
It is really scalable as the packet headers there are just:
* coordinate of the destination
* little more information
The idea is that every device will forward the packet to destination **using only local information.**

### Summary of why not to use other protocols
Classic routing mechanism are not enough scalable and efficient enough for Wireless Sensor Network. That includes also Directed Diffusion.
The particularity of wireless sensor networks is that their topology may continuously change.
All classical protocol approaches require resources from the individual devices in order to be managed.
Routing protocols need a growing with the size of the network data, the amount of memory is by far too small.
Algorithms such as distance vector or link state require that every device should have a knowledge of the whole network.


### GPSR working
Adopting routing protocols that are geographical, using geo coordinates to address the individual nodes.
Routing is organized on the relative position of the device.
The routing protocol can manage only local information, it is strongly localized and every protocol knows only about its local neighbors, reducing the amount of memory needed.

It is scalable, given this property of managing local information it does not need any information propagation, it just needs local exchange of information. 
It works in two modes that are used in conjunction:
* **Greedy** forwarding(default mode): if you need to reach a device at a given coordinate, forward the packet to one of your neighbours, and it will pick up another one that is closest to the destination, **note that the node selected must be closer than the neighbour contacted itself, to make sure that its making progress**. There is a limitation on this mechanism, when using a greedy algorithm, you may be trapped on a local optimum, which is not the global one. All the neighbour are farther from the destination than the node itself, which is by far the optimal. Greedy forwarding can become trapped and fail to find a suitable next hop node when no neighbor nodes are located closer to the destination than the current node. This limits the reliability of greedy forwarding mode.
* Perimeter forwarding: see next.

### Greedy Forwarding
* S forwards a packet to destination D
	* S looks on its neighbours: {b,a,c}
	* S will select as next hop, a neighbor defined as y such that
		* y is closer to D than S
		* among the neighbors, y is the closest to the destination
**Greedy forwarding fails when the packet encounters a void**
* It happens that a is the closest to D, so it forwards to it.
* Then a, working in greedy mode, it selects on its neighbours what it identifies as the closest, which is e and forwards the message to e.

Then greedy finds a point where there is no way to make further progress. D is beyond a void and x does not have any neighbour closer to D than itself.
That may be seen here:
![[Pasted image 20230616125645.png]]

### Perimeter mode
**There you can switch to perimeter mode. If there is a void region, you identify its perimeter, and you forward the packet on the void area clockwise or anticlockwise until you can turn back to greedy mode**.
What happens here is that in perimeter mode, going clockwise, you go to w, *which is not the greedy choice as its further away geographically from D than x*. But we reach u, at u we go back to greedy mode because **the condition to return to greedy mode is that there are neighbours closer to the destination than the node starting perimeter mode**.

Since you are doing a clockwise, if the network is connected, so there are not subset of nodes, then you will find the destination. But if there are separated partitions, the protocol will sure fail.
What makes the difference with another protocol, different than GPSR, is that the decision the node take when switching from the modes. 
When they switch from perimeter mode to greedy mode is exactly when a neighbour of the current node is found to be closer than the node starting perimeter mode to the destination.

When in perimeter mode, in order to turn correctly around perimeter, you need a state, in the header of the packet, so that every node knows how to forward the packet.
**We need to stop perimeter mode, or we will make a loop and go over D**.
By including the state in the packet header, each node can make informed decisions about the direction in which to forward the packet along the perimeter, ensuring that it eventually reaches the intended destination without getting stuck or trapped in a loop.

### Example
![[Pasted image 20230616144656.png]]
A packet arrives in node x by greedy forwarding, the node notices that there is not any node nearer to the destination, then switch to perimeter mode.
So, we forward to y then from y to u when at u is not safe to switch in greedy mode, even if is out the void zone.
What would happen if one would change to greedy mode in u is that, technically possible to "progress" in greedy mode, as there is neighbours one closer than u to the destination, but that  neighbour is y, which is not connected to D or to any node closer than itself. 
**In the example it is safe to keep moving in perimeter mode until we get to w**, just going to z is **not enough to go to greedy mode**. In principle we could but may risk to go back to u, actually its from w that we switch, because w is connected to t that is closer than the node x which is the node from where perimeter mode started.

## Node view and movements
A node has only the coordinates of its neighbours, it does not know what is beyond the void region. The goal is to identify the nodes that are on the perimeter.

The perimeter mode direction, then if its below, it spans anticlockwise, until it finds the first outgoing edge.
Z spans counterclockwise until it finds an outgoing edge.
When reaching a node, it spans into the edges to find the correct one.

The routing is basically around the void and it is based on the Right Hand Rule or Left Hand Rule, which is equivalent.

![[Pasted image 20230523113823.png]]

* When arriving from y to x, it selects **the *first* counterclockwise edge from (x,y)**. Remember that it is the first encountered counterclockwise.
* so that the movement is the traversal of the interior of a closed polygonal region in clockwise order. You select counterclockwise to *move clockwise*. Expanding on that: when moving from node y to node x, the protocol selects the first counterclockwise edge from the perspective of the edge (x,y) and node y. This ensures that the movement follows the traversal of the interior of a closed polygonal region in a counterclockwise or clockwise order, respectively.


There is the problem that we may have a cycle. That is because **edges may gross, if they do, what may happen is that the RHR may take a degenerate tour, that does not trace the boundary of a closed polygon**. As we can see here, what is happen is that we return to u and then back to x as we take the opposite direction from the last choice (from counterclockwise to clockwise, going to the edge from u to x).
![[Pasted image 20230523114031.png]]

**What happens is that going counter clockwise from the edge (u,w), the first counterclockwise edge met is the edge (u,x) so we go forward to x, which is actually the starting node of perimeter mode, creating a cycle.**


# Graph Planarization

What GPSR does it to apply **the perimeter mode to a planar graph P, obtained from graph G** (the entire WSN). A planar graph is a graph that has not edge crossing each other.
The planar can be:
* Relative Neighborhood Graph of G (RNG)
* Gabriel Graph of G (GG)
If I take an arbitrary graph and I take Gabriel Graph of G, **I cannot create arbitrarily links, it just can ignore some links**. In addition, in the final graph all links are bidirectional. 
But in certain cases, you may want to enforce a unidirectional link between nodes to establish a specific communication pattern or to optimize energy consumption in a wireless sensor network. In such scenarios, you can introduce additional constraints or rules during the graph construction phase to create unidirectional links.

Both RNG and GG are reduction G, an in particular RNG is a reduction of GG.
Both can be constructed by a distributed and localized algorithm, distributed because all the nodes are executed at the same time. The execution depends on the neighbours.
We have only information on the local nodes on the planarized graph.

Once the graph is planarized, any node will know what link it can use on perimeter mode.
When using greedy mode instead, all the nodes of the original graph G are used.
All nodes execute the algorithms to construct RNG and GG, as the algorithm is distributed and localized. **Nodes will exploit only local information about its neighbors**.

##### Properties
* If G is connected, then the planar graph P is connected
* P is obtained from G by removing edges
* Since P is computed with a distributed algorithm, it requires little memory and has a low computational overhead

### Relative Neighbourhood Graph
Formally the Relative Neighborhood Graph P of G is defined as:
* Edge $(u,v) \in P$ <=> (if and only if)
	$$(u,v)\in G \hspace{0.2cm} \land \hspace{0.2cm} d(u,v)\leq max_{\forall{w\in N(u)\cup N(v)}}(d(u,w),d(w,v))$$
* Meaning that for all neighbours of u and v, we check that said node has distance for both that are closer than using their link
* considering node u and a link with v
	* for each neighbor $v\in N(u)$, the edge (u,v) is kept only if there is a node which for both has a distance shorter than d(u,v)
Considering a link between u & v; if the region, enclosed in the two circles centered in u and the other in v, is empty. Otherwise the link from u to v must be disregarded.

In figure it may be seen how the red area must be empty to keep the link from u to v. There is node w that has distance greater from v than (u,v).  While it is true that w may be closer to u than v, its not to v, so the calculated maximum creates this inequality d(u,v)$\leq$ d(w,v) **which is true**.

![[Pasted image 20230616170129.png]]

### Gabriel Graph
Consider that the previous formula may also be rewritten as:
* Edge $(u,v) \in P$ <=> (if and only if)
	$$(u,v)\in G \hspace{0.2cm} \land \hspace{0.2cm} d(u,v)^2 \leq d(u,w)^2+d(w,v)^2 \forall{w\in N(u)\cup N(v)})$$

* GG is built with a distributed graph and keeps more links than RNG
* RNG is *actually a sub-graph of GG*
* RNG or GG are still both suitable for GPSR
We can see how the required empty area is tinier in GG.
![[Pasted image 20230616172452.png]]

### Save of connectivity
We can remove the an edge from the red area, what we can see is that: **if we remove one edge on the red area, it does not destroy connectivity. Doing that in region hasn't this property could destroy the connectivity of the network**.

![[Pasted image 20230616173050.png]]
Both GG and RNG preserve connectivity!
This is because, the node will be closer both to u and v, and will be connected to both. Keeping the assumption that its perfectly circular in connectivity.
The idea is to delete the crossing links. Consider that we may have a crossing edge if two nodes one up and down are on the red area. Cutting the long red edge, we do not have this problem.

Gabriel Graph: takes the circle centered among u,v. If the region is empty, the link should be kept, otherwise the link must be cut out if there is one node.
The planar graph can be obtained by just getting localized information for the algorithm.

**We may see about how much we reduce in edges thanks to planarization**:
![[Pasted image 20230616173527.png]]

GPSR performance:
* very aggressive to go back to greedy
* greedy makes long jumps
* perimeter short jump
	* the shortest are the perimeter, the better it is
	* this is why Relative Neighbor Graph works better, it would make the perimeter shorter
	
## Planar graph and planarization
In the planar graph edges represent the shortest line connecting two points that are connection.
This is a bi-dimensional embedding of a graph and it refers to placing the nodes of the graph in a 2 dimensional plane (like an x-y coordinate plane) such that the edges correspond to the connections between the nodes. This results in having two types of faces.
* Interior faces:
	- closed polygonal regions which are bounded by the graph edges
* One (and just one) exterior face:
	- this is an unbounded face outside the outer boundary of the graph
As it may be seen in the image:
![[Pasted image 20230617111917.png]]

F1, F2, F3 are the tree isolates internal faces (INTERNAL), plus there is the exterior phase, which is the that is the external plane, which is the external boundary of the network.
The exterior face is not necessarily "out of the network". It is still considered part of the planar graph embedding.

While the exterior face represents the unbounded area surrounding all the finite faces, it still contains nodes and edges that are part of the network.

### Complex example
![[Pasted image 20230617112921.png]]
From x we go into perimeter mode, there we have a directive x-D.
A routing algorithm uses a directive, "x-D", to identify lines in a network. Packets in the network will eventually reach certain points that we call "greedy points" - nodes that have a connection allowing a change in mode.

The algorithm "GPSR" takes an aggressive approach to guiding packets to the greedy points. Most routing algorithms simply find any node with a connection allowing a change in direction. But GPSR is greedy - it actively seeks out the greedy points.

Once at the greedy point, GPSR then navigates packets around the perimeter of the network, moving from a clockwise to a counter-clockwise direction or vice versa, to navigate around areas where connections do not exist. This avoids sending packets where they may "cycle" or loop endlessly. By using the "x-D" directive it identifies the lines and avoids non-connected areas, and the GPSR actively finds the points at which directions can change, packets can efficiently navigate even in networks with irregular shapes.

GPSR recognize at a certain node, that it has a hop better than the start of perimeter mode. With perimeter then it reaches easily the destination.
**Consider that greedy mode is much faster than perimeter mode in reaching the destination, so it is fundamental for the algorithm to reach a state where it switches to greedy mode as soon as possible**.

When a packet is transmitted in GPSR, it is forwarded along the shortest path to the destination. At each hop, the next node is selected based on the neighbor that results in the greatest decrease in perimeter length to the destination.

* On each face, GPSR uses the right hand rule, the goal is to reach an edge that **crosses the directive x-D** combined with edge closer to D, than x.
* When arriving at that edge **GPSR will move to the adjacent face crossed by x-D**
	* GPSR recognize that it reaches a new face, as the packet records
		* $L_f$: the point on the intersection between x-D and the current edge
		* $e_o$: the first edge crossed in the new face
* when reaching the new face, if and only if the current node is closer to D than x, then GPSR switches to greedy mode. Perimeter mode is basically just intended to recover from a **local maximum which puts the algorithm in loop**.
 ![[Pasted image 20230617150707.png]]
When GPSR switches to a new face during packet forwarding, it continues to use the perimeter forwarding mode to forward the packet along the boundary of the new face until it reaches a node that is closer to the destination than the current node.

### Failure
It may happen that there is no connection to D as it may be is in the void area or is just unreachable.
Note that:
* If D is reachable from x, so if the original graph G is connected **then GPSR always finds a route, but not for arbitrary planar graph, just for networks planarized with RNG or GG**
* As we may see in the graph below, D may be unreachable
	* in some case, such as below, D lies inside an interior face of $F_i$
	* in other cases, D lies in the exterior face $F_e$:
		* the packet will reach the face itself, being it $F_i$ if interior or being $F_e$ if exterior
		* **the algorithm tours around the face, once it reaches again the edge $e_0$ which was grossed when reaching the face it understand that it cannot reach the destination**, from there the packet is dropped

That may be seen here, we cycle from $L_f$ in perimeter mode, until we reach again the edge connecting to it!

![[Pasted image 20230617125704.png]]
Once reached the phase F3, there is not greed process.
You go on perimeter mode and you cannot switch to another face, as it is the one adjacent to the void region of the destination. The packet will reach the same path of where it started the perimeter mode. At a certain point the destination is unreachable as we cycle in perimeter mode.


![[Pasted image 20230523120147.png]]

What if the destination is in the exterior phase?
We reach the node closer to the destination, the node will switch in perimeter mode. It does not know that it is in the exterior.
It finds in two neighbors the perimeter.
All the other nodes will do the same, following the exterior phase. The packet will be forward around all the perimeter of the external phase, until it returns to the same node starting perimeter mode, from there the packet will be disregarded as the node cannot be reached.

If the network is very dense, with lots of neighbours, it will mean that it will forward in greedy node. If the nodes in transmission range are few, the performance degrades.

### Approaches
What happens for GPSR is that it relies on updated information about the neighbors position. Note that the neighbors may change their position if they are mobile.
What happens is that for every little change, there is the need to create a fresh planarized graph, as the **performance degrades if a stale one is used**.

**Doing planarization for each topology change is not good at all, as node may:** move within a transmission range continuously. What happens is that continuously new RNG or GG are produced. This causes link instability.

#### Solution
The solution to this is a proactive approach:
* nodes periodically communicate their position to neighbors, doing what is defined as beaconing.
* the beacons will then be used to keep a neighbors list for each node then, where there is an excessive amount of changes, it is done a planarization.



# GPSR simulations and GPSR drawbacks

![[Pasted image 20230617163815.png]]

If the beaconing interval decreases, **sending beacons more frequently**, it will improve delivery rate , *so more packets can be sent to destination*. At the same time, *this overhead can affect bandwidth an energy consumption*.
At the same time note that, the routing overhead *by sending beacon packets* is independent from mobility, because beacons are proactive so they work even if the nodes are static.

Comparing it to DSR: or Dynamic Source Routing. It is a reactive (on-demand) routing protocol where:
- Routes are discovered only when needed
- Route discovery involves flooding Route Request packets in the network
- The discovered route is stored in the packet header

Other simulations noted that:
* path length is nearly optimal if the network is dense*.
* 95% of packets are delivered through the shortest path, while DSR does that in only 85% of the packets
* DSR uses a different caching policy rather than beaconing, which has the problem of holding some paths that are no longer optimal
* Greedy routing approximates well the shortest paths
![[Pasted image 20230617172818.png]]

## Properties

If there is an obstacle a node cannot reach another one and in that case the condition of planarization does not hold.
That may be seen here:
![[Pasted image 20230617173606.png]]
You may see that there is line, where $u$ can still reach $w$, but w and $v$ cannot communicate. 
In fact it can be seen in figure below: the range formed by $w$ (big blue one) create the yellow area in which there are not any nodes, and if the obstacle would not be present the connection between $w$ $v$ would be set.
![[Pasted image 20230630151833.png]]

Another property could be that a node have not a circular range, and it can seen here $v$ does not see $w$. But $v$ can reach it through $u$.
![[Pasted image 20230617173932.png]]
This could be seen as an obstacle between $w$ $v$, as the example before.

## Drawbacks

Whenever the links are not all bi-directional, **an obstacle or non-circular transmission will produce loops in the GPSR packet forwarding**.
The solution to this problem was found but cumbersome, so they gave up.

It may be seen here:
![[Pasted image 20230617174205.png]]
There is a loop because x and u have a unidirectional link and there is an obstacle in the middle.
The problem of the obstacle is that without it the link x,u would be dropped as x,v is the one kept with the minimum distance with $d(x,v)^2\leq d(x,u)^2 + d(v,u)^2$

That is because x will forward the packet to u, thinking that its closer than itself to the destination, **u** will not be able to forward the packet to x; there, perimeter mode stops with failure. If the link was bidirectional we could have sent the packet in perimeter mode to x.

#### Solution
Create a set of coordinates unrelated to the geographical position, that circumvent this problem to reach the destination, logical coordinates.

The slides solution is mutual witness, which enforces to keep the link unidirectional between (x,u) if it finds that there does not exist a link (v.x).

[[The ZigBee Network Layer]]
