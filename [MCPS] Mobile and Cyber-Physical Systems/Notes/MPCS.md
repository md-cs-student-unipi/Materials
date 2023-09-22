
***Academic year: 2022-2023***

Classes note by **Calogero Turco** c.turco1@studenti.unipi.it
With the collaboration and revision of:
- Davide Pirolo

*Teachers: S. Chessa, F. Paganelli*

<div style="page-break-after: always"></div>

 <div style='page-break-after: always'></div> 


# Chapter 1: Internet Of Things
Sensors read data from the external world. Actuators interact with the physical world.

For example a radio interface is a sensor, but also an actuator. The internet of things is the embodiment of cyber physical system.

Cyber-physical system allow to interact with the environment.
In a smart environment objects can be moved, but to be able to do so, they need to have physical properties (e.g.: be small).
Their form factor is also important, for example not a box Arduino.

Consider also that the device are in the wild, so they must be secure, we need redundancy and low cost to be substituted.

Note that they are connected wireless.

A definition of Smart environment is: they can be defined with a variety of characteristics, on the application they serve, the interaction models with humans, including the system aspect an the multi-faceted, conceptual and algorithmic consideration that enable them to operate seamlessly and unobtrusively.

They interact with humans, they have their own **business logic**, but different than a PC, the interact is more implicit and made integrated in the environment.

They are seamless, as they may be hidden in other objects, they blend in the environment. But they are **interconnected with the digital world, retaining their ability while being placed everywhere.**

They basically recognize content, figure the user needs at the time and provide service to the end user.

## Structure of IoT
The internet of things can be seen as a stack:
* Perception layer: physical objects and sensors
* Communication layer: network and wireless technology
* Resource and service management
* Data and Knowledge management: data analysis
* Domain specific service which makes smart an environment.
- An orthogonal layer is the Security layer, encompassing them all.

We have basically sensors, connected to wireless, then the cloud.
Where in the cloud there are the business to provide the services.

##### Sensors the perception layer
In some cases, there may not be systems to measure something. While we may have to measure directly some other times.

An example: sensors for logistic system. In logistic there are several problems:
* tracking (Workers, objects, products) -> indoor tracking, time message exchanges, NFC to detect proximity or use orientation with gyroscope
* warehouse logistics -> NFC, Bluetooth, ...
* outdoor monitoring (Containers, fleet livestock) -> GPS, pressure, inclinometer
* good guarantees (food) -> temperature, humidity, accelerometer

## Platform for IoT
While sensors and actuators are on the edge, the internet is behind, the data are stored, processed and presented in the cloud.
For example [[ThingSpeak]] provides a web-based DB, allowing to attach on the cloud the component.

IoT devices must also be updated, but this cannot be done by an operator, as they are everywhere, we don't want to send a person there, we must provide a way that this can be done remotely. 

Other service concern abstraction and virtualization, also consider that the information of the sensors are at very low level, so we must **add semantic** to data, adding layers to process them. One must relate the data with the sensors producing the data.

#### Identification
Identification is the mechanism to allow discover the devices in a platform. There is difference in a localization system between the same device being places somewhere. It is a problem for the placer, but how does the application know where the device is placed?
You may not know that the devices are connected in the proper way, you need a mechanism of **identifying and pairing solve this**.

#### Abstraction and Virtualization
There are services to manage abstraction and virtualization, which is a **digital twin concept for example, where we act on the digital twin of a physical device, to interact directly on it, then we must know how to link the devices**. Service composition is a way to combine services to implement more abstract applications.

#### NoSQL
Tables in SQL impose a very rigid structure, while managing efficiently queries, we simplify the way in which you manage the data, avoiding a rigid structure while making the operations for example of joins slower.
But if you need simple queries, and write data from a sensors, then its better to use NoSQL, also they scale very well horizontally.
An example is MongoDB. Store data in terms of document JSON instead of data.

MongoDB has **collections (corresponding to the table in a relational db, one document per collection), which contains object, and the objects may be different**, IoT objects are exposed to the wild, so if we replace them or add another sensor, the data structure may be different than the other data structure.
E.g.: go from 8 bit temperature in a sensors to a 16 bit sensor. You may have to change the structure of the db on SQL, but not on MongoDB.

This choice arise because is easier to change an interface than a db, we may have data of different type in the DB and easy handling them in the web server DB for example.

In MongoDB a query targets also target different collections so different documents.
The query allows to index data and also to modify data.

## Security in IoT
In IoT, there are a heterogeneous number of devices that are connected to the internet, and some of them may be constrained or unconstrained, and may be connected behind a gateway or not. Some devices also have security features, while others do not. These devices send and receive data over the internet.

To improve the security of IoT devices, it would be better to standardize them and equip them with all the necessary features. However, sometimes IoT devices are full of bugs due to manufacturers prioritizing functionality over security during production.

##### Patching Vulnerability
One of the biggest challenges with IoT devices is patching vulnerabilities. Some IoT devices do not have an operating system with a security layer or the capability to check updates and install them locally, making them vulnerable to attacks. Even if there are capabilities for patching, end-users may be unaware of the vulnerability or unable to apply the patch. In such cases, re-designing the devices may be the only solution.

##### Sensors and actuators vulnerabilities
IoT devices also face problems with sensors and actuators. With sensors, the main concern is confidentiality, while with actuators, fake commands may create a significant negative impact. Additionally, IoT devices can be used to create a botnet and attack infrastructure, or be subject to ransomware attacks that can lock the doors of an entire hotel.

##### IUT-T advises
To address these security concerns, the International Telecommunication Union (ITU-T) has recommended several security measures for IoT devices, such as communication security, data management security, integration of security policy and techniques, and mutual authentication and authorization.

##### IoT gateway security
The gateway is the most powerful device in an IoT deployment and almost always present. As such, the gateway can implement most of the security measures necessary to protect the data it manages and devices connected to it. This includes physical and firmware authentication functions, self-diagnosis, and self-repair. In the deployment phase, it is crucial to identify devices and connect them to the gateway securely, ensuring that the gateway supports the necessary configurations correctly.

Overall, security remains a major challenge for IoT devices. With the growing number of IoT devices being connected to the internet, it is important to ensure that these devices are secure, reliable, and functional to prevent cyber attacks that can have disastrous consequences.

## IoT issues
As we have smart environment, that are very different between them and have to operate in seamlessly and unobtrusively mode. They are able to recognize context, figuring out the needs of the user at the right time and provide service. 
We find different issues in IoT devices:
* latency
* reliability
* in sending the data to the cloud.

One solution is to push the ability to analyse the data in the edge of the system. Exploit the microcontroller, connected to the sensors, which has low power capabilities to implement some business logic. But pay attention on how much you can push intelligence in the end device.

Consider that the information collected by the sensors are even noisy. If you have multiple sensors, it is possible that they give you information that are contrasting, this information is flowing very fast towards a central server.

At the same time, you expect to implement, based on those information, a context aware system to figure out which is adaptable to changing situations.
You will rely on low powered device, with memory processing and networking constrained capability. Those aspect converge into other problems, Edge and Fog computing. The artificial intelligence instead works on the context awareness and continuous adaptation.

### Edge and Fog network
**Edge network**: end devices, connected in an enterprise network, they can be actuators, sensors or device connected to fog layer (gateway).
**Fog network**: access points and local servers which are able to provide part of the services offered by the cloud, unloading the computation both on end-device and cloud, for instance deleting the noised data.
**Core network**: made by routers, where internet doesn't operate in terms of time guarantee, but by QoS, in this case the standards are typical of the internet. Here the connection is wire.
**Cloud network/data center**: response time is transactional (Databases), connect different fog network distributed geographically and high performance system, such as cluster computing resource.

[[Cloud-Edge Continum and Fog]], in IoT even the network around the servers receive a big burden by the devices. We add this FOG tier, which has access points near the devices, so that their functionalities can be enabled locally. You need to keep a connection to the cloud, the transfer of information is better if you operate on bunch of data.
When you implement processing, you filter out the information, this in terms of the processing.

We can organize the network where, a device by itself may not have the ability to connect directly to the network, as it cannot connect direct to the gateway, as it is not far away. It allows to connect to each other as only **one is connected to gateway and it provides it to the other**.

## Artificial Intelligence in IoT
Try to take intelligence from where it is. By doing:
1) Curated knowledge: express human intelligence, with knowledge and inference. Represent a set of rules written in natural language statements, then make an inference and take decision. 
	PROBLEM: You will face a series of heterogeneous time-series of sensed data, which are noisy, redundant and fast flowing.
1) Neural Network

Machine learning: automatic system that learn from data. Train the machine, then test it. 
Paradigms of ML: 
- unsupervised learning, based on a large dataset, where the machine must find the relationships of the data.
- Supervised data: you feed the relationships, so machine is good to predict what is happening now and in the future. 
- Reinforcement learning: provide feedback based on the output. Supervised learning and reinforcement learning are useful when you have all the data to understand the past

Embedding AI capabilities was not thought about in the past, nowadays some devices embed them actually.

## Blockchain in IoT
Distributed Ledger where you can story information from third party and you can guarantee that:
* information is consistent 
* once it is stored it cannot be changed by anybody.
You may associate an action of computing with Smart Contracts.

In a supply chain, record any information, for example you may monitor with sensors the goods, while being shipped and kept.
Anytime good pass form one hand to another, in the blockchain you may check its quality. You may certify that the exchange happened with the goods and the goods have good quality.
Of course you need IoT to get the data, as humans could do that but they aren't made automatically.

# IoT Structure
## Sensors and Actuators

Sensors and actuators are the fundamental components of an IoT system. Sensors detect and read data from the external world, and actuators interact with the physical world. Together, they provide the basis for interacting with and monitoring the environment. Examples of sensors include temperature sensors, motion sensors, light sensors, and humidity sensors. Examples of actuators include motors, servos, and solenoids.

Some devices, such as a radio interface, can act as both a sensor and an actuator. This is because they can both read data from the external environment and interact with the physical world.

## Cyber-Physical Systems

The Internet of Things (IoT) is the embodiment of a cyber-physical system. Cyber-physical systems allow for interaction with the environment, making objects in the environment able to move and be manipulated. However, for objects to be able to move, they need to have certain physical properties. For example, they may need to be small, have a certain form factor, or be located in a certain position.

In a smart environment, objects are seamless and can blend in with the environment, but they are interconnected with the digital world, allowing them to be placed anywhere while still retaining their ability to recognize context and provide service to the end-user.

## Smart Environments

A smart environment is a system that can be defined by a variety of characteristics based on the application they serve, the interaction models with humans, including the system aspects, and their multi-faceted, conceptual, and algorithmic considerations that enable them to operate seamlessly and unobtrusively.

Smart environments interact with humans and have their own business logic. However, the interaction is more implicit and integrated into the environment compared to a PC. They blend in with the environment and can be hidden in other objects.

Smart environments recognize context, figure out the user's needs at the time, and provide services to the end-user. Examples of smart environments include smart homes, smart cities, and smart factories.

To make an environment smart, all the mechanisms need to be in place to ensure that it is reliable and has minimal failures. These mechanisms include discovering objects, binding them so that they are connected properly, and minimizing the amount of manual work that needs to be done.

There may also be ways to recognize when a sensor breaks and then consider how to add a new one. For example, in logistics, sensors can be used to track workers, objects, and products, monitor warehouse logistics, monitor outdoor activities such as containers, fleet, and livestock, and ensure good guarantees, such as food.

## IoT Interoperability

Interoperability is important in the IoT because systems are installed by actors who may not be highly skilled, and different standards may offer different solutions to the same problem. Some examples of standards include MQTT, ZigBee, and ThingSpeak.

The change from IPv6 to IPv4 was done gradually, with the possibility to wrap IPv6 under IPv4 before the switch. With IPv6, there may be up to 655.571 billion devices per square meter on Earth.

## Understanding the Structure of the Internet of Things

The Internet of Things (IoT) is made up of various layers that work together to create a smart environment. Each layer has its own components and functions, and they include:
![[Pasted image 20230302180118.png]]
### Perception Layer
The perception layer includes physical objects and sensors that detect and measure various things in the environment. Examples of sensors include GPS trackers, temperature sensors, and motion sensors.

### Communication Layer
The communication layer is responsible for transmitting the data from the sensors to the cloud. The communication is wireless and can be through WiFi, Bluetooth, cellular networks, or other types of wireless communication.

### Resource and Service Management Layer
This layer manages the resources and services that IoT devices need, including power, bandwidth, storage, and processing power.

### Data and Knowledge Management Layer
The data and knowledge management layer handles the collection, storage, processing, and analysis of data collected by IoT devices. It also manages the knowledge derived from the data, such as predictions and recommendations.

### Domain-Specific Service Layer
The domain-specific service layer provides specific services that make the environment smart, such as home automation, smart city, or industrial automation.

### Security Layer
Security is critical for the IoT because of the sensitive nature of the data collected and transmitted by the devices. The Security layer encompasses all other layers to ensure the safety and integrity of the data.

## Applications of IoT Sensors
Sensors are a crucial part of the Perception layer, and they can be used in various applications, such as logistics. In logistics, sensors can help track workers, objects, and products, monitor warehouse logistics, and monitor containers, fleet, and livestock.

## The IoT Platform and Databases
IoT consists of the sensors and actuators on the edge and have the cloud behind them, thee are various cloud platforms for IoT.. The cloud provides a web-based database, such as ThingSpeak, to attach the components on the cloud.
Thing speak allows to be configured to store data from sensors, it uses input channels to receive and store sensors data. Some of those input channel may be public (for example weather forecast). 

IoT devices must be remotely updated, and there are services available to manage abstraction and virtualization, such as the digital twin concept.

IoT platforms provide: the **software layer between IoT devices and applications**, functionalities that are distributed between the devices themselves, gateways and servers in the cloud or edge. **Platforms are not just for data collection, but provide a series of complex functionalities.**
![[Pasted image 20230302180754.png]]

Some functionalities are:
* identification: identify uniquely the things in the platform.(Ip address, URI, Object identifiers OID, UUID etc.)
* discovery:  find devices, resources and or services within an IoT deployment
* Device management: deployment, maintenance and decommission
* Abstraction/virtualization
* Service composition
* Semantics:
* Initialization/configuration
* Device monitoring (temperature internal, battery level)
* remote control
* diagnostic and fault detection
* System Logging and management


### Abstraction/ Virtualization
IoT devices **as services**, which can be provided to whom requests them.
We have the digital twin concept, where a digital twin is mapped to a real machine, the twin represents the machine state and acting on the digital twin will influence the device.

### Service composition
It allows to build composite services: by integrating services of different IoT devices and Software components.
![[Pasted image 20230302192359.png]]
An example:
![[Pasted image 20230302192417.png]]

![[Pasted image 20230302192800.png]]
The platform encompasses all the layers above the perception layers and offers functionalities to various domain specific services.

### NoSQL databases.
NoSQL databases, such as MongoDB, are better suited for IoT applications than traditional SQL databases. They have a flexible structure and can handle data of different types, making them more suitable for IoT devices that may have different data structures. MongoDB has collections that contain objects, and the objects may be different, allowing the database to scale horizontally.
Those type of database can be used in big data and real-time applications such as in our case.

#### MongoDB
In Mongo DB records are document, in JSON notation.
The structure of the document is:
* name/value pairs (string,int,arrays of different types)
## Conclusion
The IoT has a specific structure or stack that includes several layers, each with its own components and functions. Understanding the layers of the IoT and how they work together is essential in creating smart environments. Security is also critical, as it encompasses all layers to ensure the safety and integrity of the data collected and transmitted by the devices.

 <div style='page-break-after: always'></div> 


# Chapter 2: Interoperability and Standards
### Vertical silos
When we build a solution to be working on own devices only. The layers (Communication, application, ...) must be implemented by us, forgetting about interoperability. It is a silos as it is encloses and it does not communicate with the outside.
If other vendors offer solutions with their components, their solution will not work with our.

**Why?** It encompasses a solution where the customers must be forced to work with the company, as business model.
This is acceptable if the cost of implement the whole system from scratch is covered by the gain of having the customer locked in.

### Beyond the interoperability

Communication standards are indexed based on data rate and range. You may identify four different rules:
* range
* data rate
Eg: LORA may give you a low data rate and long distance. There are also 3G, 4G and 5G (with functionalities for IoT in it), where they have big data rate and long range.

#### 5G vs 4G
5G improves 4G on several dimensions. In particular 4G works with 300km/h moving items, while with 5G up to 500km/h, supporting users moving really fast. 5G allows real time communication, in a few milliseconds, it also reduces the range from antenna to device, this advantage is that it consumes less power. Finally it introduces the machine to machine communication functionalities.

We can see the 5G use scenarios as three type:
* Massive Machine  Type communication
* Enhanced mobile broadband
* Ultra reliable and low latency communication.

# Standard

When a technology, becomes mature, the cost of the technology for the end user go down, the technology becomes more accessible, which happens for all customers coming to the market.
After charging the initial users, you can afford the cost of reduction. Once you developed fully a technology, you don't want to put other investment to improve it again. Usually you find more revenue in the business layer. There is a problem:
* you want to invest in the app layer
* but you must invest to keep updated the underlying technology, which is now just a big cost for you. At this point it becomes better to make it become a standard.
At this point "coopetition" became fundamental, different companies put together the effort to develop the technologies, dividing the cost, and all benefit of these. A new standard is create to have also a certain grade of interoperability. But this companies are all in competition between theirs on the business side. This is also called consortium: you have **competing consortium with competing standards**. For example for LOLA there are competitors.

Also the development continues and there are problems also at the upper layer, so it is a never ending process. The more technology improves, the more there will be problem layers over layers.

Some standards may be opposing, as some alliance may uphold one standard, and other will uphold another standard. This became a problem, because with too many standards the interoperability decrease and so it is difficult to cooperate. 

To deal with incompatible standards, we need **gateways, that translate even high level protocol into a different one**.

#### Configurations:
1) **Type A**: All the devices are produced by the same vendor and same protocol of that vendor is used to communicate. The protocol may not be a standard, but the communication method may have a specification. The service gateway is used to communicate with the internet. ![[Pasted image 20230825111347.png]]
2) **Type B**: The devices, with different color means that they are of different manufacturers, but they are communicating with the same standard, as they have the blue lines. In this case we need a gateway too, as we need to connect the devices to internet, and the service gateway applies the mapping of the communication protocol to the outside network protocols. One example: ZigBee as communication protocol. ![[Pasted image 20230825111404.png]]
3) **Type C**: we may have three different local network, with in those network having the devices communicate with a specific proprietary protocol to communicate or a standard. The same manufacturer may produce devices to respond different standard as we can see red connected with blue line. The **Service Gateway isn't unable to connect to each other, as they must need a mapping between their standards to the standards of other networks**. The *integration Gateway is able to map the protocols on into each other*, (Think about a temperature sensors and an application layer that reads the data and sends it. There are different ways of this transmission from sensors to user may be implemented, with push mechanism the sensors sends data as soon as it is available, or we may have a pop mechanism, where user ask for data and the device sends it, if you have a standard where only behaviour 1 implemented and another with behaviour 2 implemented, they are totally incompatible, so the integration gateway performs the translation to make them compatible). ![[Pasted image 20230825111429.png]]
4) **Type C/ll**: (Google Home and Alexa): speech recognition devices and interaction with humans, it happened a dominance of the market as it cost to make those successful devices. So from the point of view of the manufacturer instead of create its own code, use the **imposed code of those manufacturer, where the Integration Gateway becomes Google Home and Alexa, but the networks must speak with it using those mandated communication protocols**. So the device strength on the market is used to force their standard. (It is improper to call it integration gateway practically, but we call it that way as it is forcing integration as the service gateways are obligated to use that language). ![[Pasted image 20230825111443.png]]
5) Type D: the integration gateway may be seen as a series of gateways that map outside protocols to their own internal protocol (so from service gateway mapped only to integration gateway). The integration gateway are all different in practise, they enforce reliability, as if one gateway goes down there are the others. ![[Pasted image 20230825111457.png]]


 <div style='page-break-after: always'></div> 


# Chapter 3: MQTT
An example of application level for IoT is MQTT (Message Queuing Telemetry Transport), which covers the session and presentation layers (layers 5 and 6) of the TCP/IP stack. MQTT is a middleware that provides features to the Application Layer.
 
#### Why not TCP/IP for IoT
The Internet Protocol (IP) provides addressing and routing with best-effort. The Transport layer consists of TCP (providing reliability with flow control and congestion control over IP) and UDP (providing an interface to IP). HTTP is used for request/response.
The Internet protocol suite was not designed for IoT, which has unique resource constraints, in fact devices are expected to work for many years and are constrained in power, memory, and connection. Therefore, IoT has different requirements, including:

**Network requirements**:
1.  Scalability: there are millions of devices, so scalability is essential. Multi-hop networks or mesh networking allow devices to communicate with each other and support communication between each other, even if there is not enough coverage from the access points.
2.  Security
3.  Addressing: scalable address space and low-overhead network protocols. For example, the IPv6 solution of long addresses means having a very long header. The 6loPan effort is to bring IPv6 to a low-power network. 120 bits are too much for an address, so it is shrunk to make the device communicate on 802.15.4.

**Device requirements**:
1.  Low power/battery power: low duty cycle.
2.  Limited capacity: creating code with a small footprint and creating algorithms with low complexity.
3.  Low cost: device reliability is lower.


![[Pasted image 20230302170949.png]]


MQTT is a lightweight publish/subscribe and reliable communication protocol that builds on top of TCP. Although TCP is heavier than UDP. MQTT is designed to be a session layer on top of the transport. There are some versions on top of UDP, but MQTT is generally thought of as being on top of TCP, specifically in port 1883, if it used without security, or in 8883 if it used SSL protocol.

The MQTT protocol uses a client/server architecture. To the user, it offers a publish/subscribe paradigm. On the client side, it is lightweight and uses publish/subscribe. On the server side, called broker it is heavier. MQTT is data agnostic (meaning that it can transport data in multiple format).

There are three actors in MQTT:
-   Publisher: client
-   Subscriber: client
-   Event service (broker): server contacting both publisher and subscriber.

The publisher produces events, and it doesn't know if anybody is reading the information that produces. It doesn't know if someone will read the information and when. The subscriber provides a description of the data to the broker. The subscriber specifies to the broker the description of the data which interested in, and the broker provides the data of that description to the subscribers.
Publishers and subscribers do not share time, space, synchronization or name/address of each other.

The Broker keeps a TCP channel with each publisher and subscriber, implementing matching along with subscriptions and provides messages to the subscribers requesting said information.

#### Operations
* Publish
* Subscribe
* Notify
* Unsubscribe
 
![[Pasted image 20230302171443.png]]



## MQTT Specifications
MQTT is a publish-subscribe protocol where publishers and subscribers agree on topics for data exchange.

### Filtering
Broker keeps track of all topics in the network, all messages are part of at least one topic and client have to subscribe to that topic to receive the communication. So events can be filtered in according to content, structure or even both.

### Connection
All clients should be connected with a TCP connection to the broker. Communication may not be in real time due to latency before the completion of a deployment. Subscribers may be connected to the broker without a publisher, or there may be a failure. Every clients must know the hostname, IP and port of broker.

### Decoupling
Publish-subscribe decouples synchronization. Subscribers can be programmed with callbacks to receive published data. The server (broker) has most of the complexity and keeps track of each message published and who has received, so this is very suitable for low power device.

### QoS
MQTT has three QoS levels (0,1,2) to assure the reliable delivery of messages. Level 0 is usually used. The protocol stack MQTT is at level 5 and 6.

### Session
MQTT has a concept of session to keep conceptual connections beyond the TCP connection concept of session. A CONNECT message contains a client ID (allowing to resume a session later), clean session, username/password, and will flags.
A session starts with a **CONNECT message**

## Connect message

![[Pasted image 20230303184624.png]]

#### Client ID(can be empty)
Is an uniquely client identifier, if is not provided, the broker will assign one. If a client ID is specified, the broker knows who the client is.

#### Clean Session (optional)
This means that the broker will store all subscriptions and missed messages. Using a persistent session adds overhead and may be difficult to maintain. It is mandatory to use a QoS of level 1 and 2 in this case.

#### Username and Password
A username and password can be sent optionally, but unless there is security at the transport layer, they are sent in clear.

#### Will flags (optional)
If a client disconnects ungracefully, the broker will notify all other clients. The message will be associated with a topic, so clients must subscribe to that topic of the will flag.

#### Keep alive (optional)
The broker expects to receive periodical messages from the client saying "I am ALIVE". These messages are expressed in 16-bit intervals. If the keep alive message does not arrive, the last will message will be sent if it is set, to all interested subscribers. Keep alive is a 16-bit word that indicates the delay to send the keep alive message. If set to 0, it means not to send.

#### Acknowledge and session present
MQTT has an application/session-level acknowledgement. The acknowledgment informs the client whether the broker accepted the connection or not, for example, if it is overloaded. It may also send a Session present message indicating whether the broker has information about the client from past sessions.

## Publish message

![[Pasted image 20230303184440.png]]
A publish message contains a topic and a payload. In MQTT, the payload can be of any type, text, binary, JSON, etc. The broker sees the payload as a bunch of bytes, and it is up to the subscriber to know what to do with it.

Once the broker acknowledges a message, the publisher forgets it.

###### Specifications
-   PacketId: A sequence number that allows for returning an acknowledgment. It may be 0 if using QoS equal to zero; otherwise, one must specify it.
-   TopicName: It is recommended to build a topic following best practices so that others know what is being done, generally topics are structured in hierarchical mode, like a path in file system.
-   QoS: Represented in 2 bits, indicating 0, 1, or 2.
-   Payload: actual message
-   RetainFlag: Retained messages ask the broker to retain a message. If a subscriber subscribes after the message is published, the broker sends the message kept to the subscriber.
-   DupFlag: This indicates that the message is a duplicate. This is meaningful only if QoS is > 0.

When the broker receives a publish message, it acknowledges the message (if requested, with QoS>0) and forwards the message to all subscribers after identifying them. The publisher can forget the message entirely if it receives the ack.

## Subscribe message
-   packetId: A sequence number.
-   topic_X: a string contained the name of topic
-   QoS: Subscribers can manage the QoS of clients independently of the publisher, who may define the topic. 
(Last two may be repeated with different topics in place of X and different QoS).

## Suback message
-   packetId: A sequence number.
-   returnCode: States what the possible QoS is. The level can be the one requested or lower for each topic or 128 to indicate that subscribing failed.

## Unsubscribe message
It can be sent with:
-   packetId: A sequence number
-   topic_X (can insert multiple topics in the same message)

As an answer, there is an UNSUBACK message, which contains the same PacketId of the UNSUBSCRIBE message.


## Topics
Topics can be organized hierarchically using the slash (/) as a separator. It is suggested to use a logical criteria to organize topics, for example, by the placement of publishers in a home: home/firstfloor/bedroom/presence.

MQTT allows for easy creation of interoperable devices. To connect to the broker and subscribe to topics, devices simply need to establish a connection. 

Wildcards such as + and # can also be used to select specific topics. For example, home/firstfloor/+/presence selects all presence sensors in all rooms of the first floor, and home/firstfloor/# selects all sensors in the first floor.

There are also topics specific to MQTT internal statitics that use the $ symbol, such as $SYS/broker/clients/connected, which displays the number of clients connected, and $SYS/broker/clients/disconnected, which notifies when a client disconnects. 
However, subscribing to $SYS/broker/# may result in an overload of messages for the client.
The $ topics aren't standardized and for topics in general there are some conventions ensuring performance:

-   Do not start a topic with a dash.
-   Do not use spaces or special characters.
-   Keep topics short to avoid overburdening devices with low memory.
-   Use only ASCII characters of type UTF-8, which can be recognized correctly by all brokers.
-   Use hierarchies that are easily extendable to avoid having to redesign/reprogram everything.
-   Do not subscribe with # unless you have a high-power machine or need to keep an audit.

## QoS
MQTT supports three levels of Quality of Service (QoS):

-   QoS 0: At most once. This level is suitable for frequently updated data, such as temperature sensors. Losing an update is not a problem, as a more accurate update will be available shortly.![[Pasted image 20230303185634.png]]

-   QoS 1: At least once. This level is suitable for environments where disconnections may be frequently faulty. One client (publisher) must buffer its message, as the broker sends an acknowledgement (or to the broker to a subscriber). It may be possible that a message is received multiple times, as the ACK may be missed in the subscriber. ![[Pasted image 20230303185648.png]]

-   QoS 2: Exactly once. This level is suitable if TCP goes down frequently. QoS 2 uses a double handshake with an overhead of 3 messages to send only one message. But it allows to be sure that a message is received, and only once by the recipient (being the broker or the subscriber). So this is the most resilient but also the slowest. 
	N.B.: The double handshake is needed because the first it used to send the message topic, then the second is needed to agree to discard the state. Only the PUBREC isn't sufficient because if it is lost then the client send it another time, but now server has two copies and the only way to know if it possible to discard is PUBREL.
	  ![[Pasted image 20230303185703.png]]


### Flow from broker to client
Packet identifiers are different for each client, even if it is the same message for the same topic, publisher and subscriber can have different QoS. If the broker goes down, persistent sessions ensure that messages with QoS 1 and QoS 2 can be stored and sent, and this happens always and for all the messages.

When a client disconnects and reconnects, it does not have to subscribe to topics again. It will receive stored messages with QoS 1 and QoS 2. However, it is recommended to avoid persistent sessions with QoS 0, and only use it if missing data or old messages are not important.

![[Pasted image 20230303190007.png]]

## Persistent Sessions
It is requested at CONNECT time, with:
* flag cleanSession. 
* CONNACK: the broker sends a message confirming weather the session is persistent.

In this case all clients have to store state in a persistent session, so:
* store all messages in a QoS 1 and 2 not acked by the broker
* All received QoS 2 messages not confirmed by the broker.
The messages of **persistent session will be stored as long as the system allows it**.
Since the persistent sessions introduce high overhead use them only where messages are important or when you can't lose any type of messages.

## Retained Message
Sometimes it may take too much time before getting information about a sensor. This cannot be solved with a persisted session unless the connection was opened before the publishing of the message and it was published with QoS 1 or 2.

You can use a retained message, so to say to the Broker: _keep the last message published with that topic_. The broker will keep the message and send it immediately to new subscribers.

The publisher must set retainFlag=True precisely in the message. It has nothing inherited with the persistent session. As persistent would get all the messages from the disconnection. Also, a client can have topics with retained messages or not, with persistent you would get for all topics.

Generally, it makes sense to set if for devices with infrequent updates. The last will may be combined with the retain message if a machine may say if it is on or off, and if it fails, it may send with its last will that it is off.

It may be possible to delete a retained message, by pushing a retained empty message. A new retained message will overwrite the one before.

## Last Will & testament
Specified at connect time, with a topic and a message to send. This will be sent when the client **abruptly (ungraceful) disconnects** (network interruption or improvise power off ). The broker throws away the last will only if the client abruptly disconnects; if it normally disconnected, then it will not send and discard it.
-   lastWillTopic: the topic
-   lastWillQoS: a QoS level (0,1,2)
-   lastWillMessage: a string
-  lastWillRetain: boolean to decide if retained or not

Very often the last will is used in combination with the retained message.
One example is a light switch that crash while having set a retained ON. As last will it can have a message with payload OFF which is retained and will override the message of before.

## Keep Alive
This message is used when between client and broker we want to maintain an active connection. The interval of keep alive message is specified in CONNECT message. When sending a KeepAlive, the broker starts counting time. When one sends **any message**, such as a PUBREQ (publish request), then it is reset. The client could also send a PINGREQ, responded with PINGRESP.
![[Pasted image 20230311153810.png]]

If the PINGREQ is not send in time, then the broker will *turn off the connection and send the last will with the testament message if present*.


# Exercise

![[Pasted image 20230311160456.png]]
1.  subscriber already listening
2.  publishing before subscribing, but there is the retained flag so the subscriber receives the message
3.  publishing before but no keep alive


## General Packet format
The packet format is as follows
![[Pasted image 20230311153353.png]]

There is a fixed header of 2 bytes:
![[Pasted image 20230303174843.png]]

The length is encoded with 1 byte, using 7 bit for the standard length of up to 127 of length, there is the Extra length field (of 1 bit, the most significant) allowing to specify that there is a larger field for a length bigger than 127 bytes.
Only the headers bits of publish are meaningful for us. When it is a response, the fourth bit will be a 1.

![[Pasted image 20230303190221.png]]

It encodes all the possible connect packet types.
NOTE: the $ topic referring to the broker statistics, are implementation dependant.

The packets have **variable header**, and contain a packet identifier, **encoded** with two bytes. The CONNECT and CONNACK packets do not have that instead. The PUBLISH packet contains this information only if QoS > 0.

There are other information depending on the control packet type. For example CONNECT packets include the protocol name, version and a number of flags.
Also there may be a payload, mandatory or not with additional information.
![[Pasted image 20230311152435.png]]
# Arduino MQTT client library

It is restricted to:

-   only QoS 0 and 1
-   no security with SSL/TLS
-   Payload limited to 128 bytes.


# Constructors 
* PubSubClient()
* PubSubClient(server,port,{callback},client,{stream})
* We can construct with an empty client and specify after the parameters.
Server: IPaddress of the broker
Port: port used by the broker
callback: a pointer to the callback function called when a message arrives for a subscription created by this client
client: an instance of Client that can connect to a specified internet, IP address and portClient
Stream: an instance of Stream, which is used to store received messages.
# Functions

1) boolean connect (clientID, username, password, willTopic, willQoS, willRetain, willMessage):
	1) Connects the client specifying the *will message*, username and password. The API includes other connect messages with lesser parameters
	2) the type of username, password, willTopic, willMessage are const char \[\].
	3) willQoS, willretain are int
2) void disconnect ()
3) int publish(topic,payload, length, retained): return 1(true) if publish succeed else false (0)
4) boolean subscribe (topic, \[qos\]): topos is a const char \[\], basically a string. The qos is an int, so we have an array of ints.
5) boolean unsubscribe (topic)

The I am Alive messages do not need to be implemented here, but the client is able to send them with the:
* boolean loop () function.

Then there is:
* int connected() that checks whether the client is connected to the server
* int state(): returns the current state of the client, if a connection attempt fails, then this is used to get more information about the failure


The following functions configure the parameters of the server if not initialized at the construction:
* PubSubClient setServer (server, port) 
* PubSubClient setCallback (callback) 
* PubSubClient setClient (client) 
* PubSubClient setStream (stream)



# MQTT competitors

There are other protocols operating at the same level and can be used as an alternative.
	1) HTTP: you may use HTTP to use the post/read feature, to set up the state of a device on a remote database.  For example on ThingSpeak we can send data with HTTP. The scaling is less efficient with HTTP, while MQTT is publish subscribe so the broker may be scalable, making it parallel to making it easier to scale. With HTTP clients will query the IoT devices, one can have the HTTP server to have a connection that manages the connections to the IoT devices, as they are limited on connections.
	2) HTTP resources, there are more resources needed for HTTP, as HTTP have larger messages and is not for just IoT
HTTP is used as much as MQTT, as not all IoT devices are small powered.


You may not always have the possibility of having parallel brokers, so it may be a problem, and it can be a single of point of failure.

Also since MQTT relies on TCP, which is not cheap for low-end devices, so there is the overhead of wake-up tome to establish the TCP connection, having then a delay. A TCP connection must be established between devices. UDP would be more lightweight.


# CoAP

1) It is a more recent standard, while MQTT is more well-known and widely used.
2) CoAP is specialized as a web transfer protocol, specialized for Machine to Machine communication. It is built on top of UDP.


It attempts to bring IPv6 to low-powered devices by compressing their long addresses and big headers.
It is designed with 8-bit microcontrollers, using small amounts of ROM and RAM.

Under it there is IPv6 over Low-Power Wireless Personal Area Netowork, it consist in 6LoWPAN and is a constrained network over IPv6. In this case it allows to shrink the size of the IPv6 header to be supported by low end devices.


The strengths of CoAP are:
-   Native UDP support
-   Support for multicast
-   Security features
-   Possibility of using low MQTT

Weaknesses:
-   The standard is less mature than MQTT
-   Reliability is not improved and is the same as MQTT.


CoAP uses the client/server paradigm, with:
* sensors/actuators as servers
* applications as client 
A CoAP node use protocols that can interface directly with HTTP and so on devices communicating with it. While MQTT requires a bridge.
On CoAP we have the same model of HTTP, without the need to have a broker, here we can directly connect to the device, as a client server.
**This model allows to also connect directly with each other the devices** as client server, building on top of UDP and IP, with small headers with compact encoding of information and a resource *directory that provides discovery features*.

The commands are the same of REST so:
* GET
* PUT
* POST
* DELETE
There is also a security level with 3072-bits RSA. In general CoAP is designed to be used with low energy devices.


![[Pasted image 20230311124919.png]]
We see the two protocols working along side, with their difference. We see that both can work with HTTP requests to end devices, byt with MQTT there is the need of a Broker.
The CoAP node we can see in the right can have connections 1 to Many. While the MQTT nodes only 1:1 with the broker.
The CoAP nodes can then be connected with a node that works as gateway, while for MQTT it is the broker that acts as a gateway.
It is possible to also have a CoAP node that has not a gateway.
# Exercise:
![[Pasted image 20230311120010.png]]
1.  Subscribing after the publishing means that even with a persistent session, you do not get the event if it is not retained.
    
2.  The message is retained, so it arrives.
    
3.  Both messages arrive after subscribe, so the subscriber will see both.
    
4.  There is no message retention, so the subscriber does not receive it even if the session is persistent.
    
5.  The message is retained, so it arrives.
    
6.  Since QoS is 0, the subscriber does not receive the message if it is off and the message is not kept.
    
7.  Since QoS is 1, the subscriber receives the message even if it is off because the message is kept.
[[ZigBee standard]]

 <div style='page-break-after: always'></div> 


# Chapter 4: Many Faces of IoT
Here are some points taken from the paper. [[manyfaceshigligted.pdf]]
With systems based on the publish/subscribe interaction scheme,
subscribers register their interest in an event, or a pattern of events, and are
subsequently asynchronously notified of events generated by publishers.
This paper factors out the common
denominator underlying these variants: full decoupling of the communicating entities
in time, space, and synchronization. 


## Burden
To reduce the burden of application designers, the glue between the different entities in such large-scale settings should rather be provided by a dedicated middleware infrastructure, based on an adequate communication scheme. The publish/subscribe interaction scheme is receiving increasing attention and is claimed to provide the loosely coupled form of interaction required in such large-scale settings.

Subscribers have the ability to express their interest in an event, or a pattern of events, and are subsequently notified of any event generated by a publisher, which matches their registered interest. An event is asynchronously propagated to all subscribers that registered interest in that given event.

## Basic Interaction Scheme
In other terms, in the publish/subscribe interaction, producers publish information on a software bus, which serves as an event manager. On the other hand, consumers subscribe to the specific information they want to receive from that bus. This information is commonly referred to as an event, and the process of delivering it is known as a notification.

The basic system model for publish/subscribe interaction (Figure 1) is built upon an event notification service. This service is responsible for storing and managing subscriptions, as well as efficiently delivering events. It provides the necessary infrastructure for handling the dynamic nature of subscriptions and ensuring timely and reliable event delivery.

![[Pasted image 20230620181912.png]]


Subscribers register their interest in events by typically calling a `subscribe()` operation on the event service, without knowing the effective sources of these events.
The symmetric operation `unsubscribe()` terminates a subscription.

To generate an event, a publisher typically calls a `publish()` operation. The event service propagates the event to all relevant subscribers. As a result, the event service can be viewed as a proxy for the subscribers, ensuring that the events are distributed to the appropriate recipients.

Publishers also often have the ability to advertise the nature of their future events through an `advertise()` operation.


## Space Decoupling
Space decoupling: The interacting parties do not need to know each other.
The publishers publish events through an event service, and the subscribers receive these events indirectly through the event service. The publishers do not usually hold references to the subscribers.
Subscribers do not usually hold references to the publishers, neither do they know how many of these publishers are participating in the interaction.

## Time Decoupling
Time decoupling: The interacting parties do not need to be actively participating in the interaction at the same time.
The subscriber might get notified about the occurrence of some event while the original publisher of the event is disconnected.

## Synchronization decoupling
Synchronization decoupling: Publishers are not blocked while producing events, and subscribers can get asynchronously notified (through a callback).
Publishers and subscribers do not interact in a synchronous manner and therefore their interactions are not synchronous.
**Decoupling the production and consumption of information increases scalability by removing all explicit dependencies between the interacting participants.**
Well adapted to distributed environments that are asynchronous by nature, such as mobile environments.

# The siblings: Pub/Sub variations
Subscribers are usually interested in particular events or event patterns, rather than all events. The different ways of specifying the events of interest have led to several subscription schemes. In this section, we compare the two most widely used schemes, namely topic-based and content-based publish/subscribe, as well as the recently proposed type-based subscription scheme.

## Topic based
The earliest publish/subscribe scheme was based on the notion of topics or subjects.
Participants can publish events and subscribe to individual topics, which are identified by keyword.
Consequently, subscribing to a topic T can be viewed as becoming a member of a group T, and publishing an event on topic T translates accordingly into broadcasting that event among the members of T.
In practice, topic-based publish/subscribe systems introduce a programming abstraction that maps individual topics to distinct communication channels.
Every topic is viewed as an event service of its own, identified by a unique name, with an interface offering `publish()` and `subscribe()` operations.

The topic abstraction is easy to understand and enforces platform interoperability by relying only on strings as keys to divide the event space. Various systems have proposed additions to the topic-based scheme. One useful improvement is the use of hierarchies to orchestrate topics. While group-based systems offer flat addressing, where groups represent disconnected event spaces, nearly all modern topic-based engines offer a form of hierarchical addressing. This allows programmers to organize topics according to containment relationships.

Most systems allow topic names to contain wildcards, Wildcards offer the possibility to subscribe and publish to several topics whose names match a given set of keywords. This includes subscribing to an entire subtree or a specific level in the hierarchy.


## Content-Based
**The topic-based publish/subscribe variant represents a static scheme which offers only limited expressiveness.**
**The publish/subscribe variant improves on topics by introducing a subscription scheme based on the actual content of the considered events.** In other terms, events are not classified according to some predefined external criterion (e.g., topic name), but according to the properties of the events themselves.

Consumers subscribe to selective events by specifying filters using a subscription language. The filters define constraints, usually in the form of name-value pairs of properties and basic comparison operators (=, <, ≤, >, ≥), which identify valid events. Constraints can be logically combined (and, or, etc.) to form complex subscription patterns. Some systems, like the Cambridge Event Architecture (CEA) [Bacon et al. 2000], also provide for event correlation: participants can subscribe to logical combinations of elementary events and are only notified upon occurrence of the composite events.

Subscription patterns are used to identify the events of interest for a given subscriber and propagate events accordingly. For subscribing, a variant of the `subscribe()` operation is provided by the event service, with an additional argument representing a subscription pattern.
There are several means to represent such patterns:
* strings
* template objects: When subscribing, a participant provides an object `t`, which indicates that the participant is interested in every event that conforms to the type of `t` and whose attributes all match the corresponding attributes of `t`, except for the ones carrying a wildcard (null).
* executable code: Subscribers provide a predicate object capable of filtering events at runtime.  Executable code is not widely used in practice because the resulting filters are extremely hard to optimize.
**The content-based scheme enforces a finer granularity than a static scheme based on topics.** To achieve the same functionality with topics, the subscriber would either have to filter out irrelevant events, or topics would need to be split into several subtopics—one for each company (and recursively several subtopics for different price "categories"). The first approach leads to an inefficient use of bandwidth, while the second approach results in a high number of topics and an increased risk of redundant events.

## Type-based
Topics usually regroup events that present commonalities not only in content but also in structure. This observation has led to the idea of replacing the name-based topic classification model by a scheme that filters events according to their type.

The notion of event kind is directly matched with that of event type. This enables a closer integration of the language and the middleware. Moreover, type safety can be ensured at compile-time by parameterizing the resulting abstraction interface by the type of the corresponding events (without any type cast in the resulting code).

![[Pasted image 20230620183708.png]]

**Subtyping can be used to subscribe to both stock quotes and requests.**
It is important to notice that type-based publish/subscribe can lead to a natural description of content-based filtering through public members of the considered event type, while ensuring the encapsulation of these events. This is achieved in our example of Figure 15 by declaring only **private data members and enforcing their access through public methods.**


 <div style='page-break-after: always'></div> 


# Chapter 5: ZigBee standard
It is a standard for wireless sensor networks, allows to build large network covering large domain, it does not use TCP/IP, but it provides support to connect devices to the rest of the internet, allowing a ZigBee network to be connected to the internet. ZigBee can be considered an IoT standard.

The practical scope of this standard is, in a certain sense, limited in scope. It tried to enter the healthcare market, but it was dominated by Bluetooth. Even though ZigBee is not the most widely used program, it is still widely used, including in end-user programs. ZigBee is more complex than other standards.

#### Requirements of the standard:
1.  Build an independent network of devices that can self-construct with minimal or no manual intervention and without the need for maintenance, limited or no human intervention.
2.  Long battery life (e.g., 10 years).
3.  Low data rate (needs to guarantee very long battery life, so there is a trade-off with good performance).
4.  Interoperability: all devices developed with the ZigBee standard must be compatible with each other.

#### Features of the standard:
1. Can be used globally: since it is a wireless standard, the law decides the frequencies reserved for a certain use. On the private use frequencies, there are constraints on the power. For example, on ZigBee and Bluetooth, you cannot transmit with high power, or it would disrupt other signals.
2. Reliable and self-healing: reliable as the internal method of communication is reliable. Self-healing comes as a byproduct of redundancy that can be set up in that network.
3. Support a large number of devices, using the concept of multi-hop networks.
4. Easy to deploy and comes with built-in security features.

![[Pasted image 20230310150309.png]]
[[MPCS/pages/802.15.4]] is the standard that builds the stack at the MAC layer and Physical Layer, made in 2003. The ZigBee alliance defines the Network layer and the Application Layer. In the first layer, there is a Transportation layer, made in 2004.

# 802.15.4
802.15.4 is an infrastructure-less protocol. There are no access points, and devices communicate end to end. It is short-range and can operate in the same frequencies of WiFi 802.11 and Bluetooth 802.15.1, because they perceive each other as noise, in fact, the frequencies are used in orthogonal ways.
The data rate advertised **worldwide** is 250 kbps, but it is difficult or impossible to achieve.
To reach this data rate one must use the brands of 2400-2484.5 MHz worldwide.

In general the specifics of it are:
* low-rate Wireless Personal Area Network (PAN) specification for physical and MAC layers
* Infrastructure-less
* Short range
* Star and peer-to-peer topologies supported
* Licence-free frequency band. In Europe the frequencies are of 868–868.6 MHz (above there are the worldwide ones).

# ZigBee layers
![[Pasted image 20230310151026.png]]

**Components of the application layer:**
* Application Framework: contains up to 240 APO (APplication Object), where each APO is a user-defined ZigBee application.
* ZigBee Device Objects: provides services to let the APO organize into a distributed application.
* APplication Support sublayer (APS): provides data and management services to the APO and ZDO

ZigBee is built on top of the MAC layer 802.15.4. The application layer has a transport layer that is much lighter than TCP. Then we have the ZigBee Device Object, which provides the main services to organize the application into a distributed application. The behavior of the standard is implemented in the ZDO.

For example, the connection to an existing network must not be implemented by the user. Instead, it is the ZDO that handles it. The implementation is done by the manufacturer of the ZigBee devices. Manufacturers provide the device, embed it in a shell, and deliver it.

If one uses an Arduino to create a solution, this stack must be programmed on its own to implement all the device's behaviors.

### Primitives
Each service is specified by a set of primitives of four generic types:
- request: invoked by the upper layer to request for a specific service
- indication: generated by the lower layer and directed to the upper layer to notify the occurrence of an event related to a specific service.
- response: invoked by the upper layer to complete a procedure previously initiated by an indication primitive.
- confirm: generated by the lower layer and directed to the upper layer to convey the results of one or more previous service requests.

Services may not use all the for primitives actually.
![[Pasted image 20230310154700.png]]

The communication goes from a request on device 1, going down to layer n-1. Then in device 2, the request becomes an indication, going as an indication to layer n+1. Sometimes not all the primitives are used.
![[Pasted image 20230311115551.png]]

The Application object at the physical layer needs physical transmission. So the data units are present at each level. The PPDU stands for physical **protocol** data unit and is the one exchanged from physical to physical.
![[Pasted image 20230311115541.png]]

## Network Layer
FFD: Full functional devices, consisting in routers and network coordinators. 
RFD: are end devices, basically a reduced functional device.

At the network layer, devices are not the same. We identify three types of devices at the network layer:
1. Network Coordinator: Since ZigBee does not have an infrastructure with Access Points deployed statically, here it is a device that takes the role of creating the network, making decisions, and interfacing with the rest of the network. In general, the coordinator is the one creating the network.
2. Router: if the network is large, the router forwards the message in that. From the PoV of capabilities, routers and coordinators have the same.
3. End devices: They cannot communicate with the rest of the network. They must be attached to routers or coordinators to be part of it. The reason to have separate types of devices is to support low power devices. Implementing as end devices allows not implementing all the standards, while routers must implement all.

### Topologies
![[Pasted image 20230311115421.png]]

1.  In ZigBee, the Star topology is commonly used, where the coordinator acts as the central hub and all communications pass through it. End devices are connected directly to the coordinator, and routers are used to extend the range of the network.    
2.  In the Tree topology, there is no direct communication with the coordinator. Instead, routers are used to relay the packets from the source end device to the destination end device via the coordinator. Routers in the Tree topology have either two leafs - other routers or end devices - or one leaf.
3.  The Mesh topology is a more flexible option that allows for multiple endpoints to connect via routers. Unlike the Tree topology, there is no tree-like structure in a Mesh network. Instead, data packets can take multiple paths to reach their destination, and each node can act as a router to forward packets to other nodes in the network. Mesh networks are highly resilient and can self-heal in the event of a node failure.

The network layer provides the following services:
-   data transmission using unicast or multicast.
-   network initialization.
-   device addressing.
-   managing routes and supporting routing.
-   managing connections and disconnections to devices.

A ZigBee network is formed incrementally. The join mechanism allows devices to connect to the coordinator one after the other, and then a network with an arbitrary topology is formed.

The network layer uses Request, Indication, and Confirm primitives without Response, and sometimes the Indication primitive is missing.
Network discovery allows discovery of other ZigBee networks to connect to.

GET/SET allows for reading and setting an internal parameter of the network layer, acting locally on the network layer.

Connecting to a ZigBee network can be done in two ways:
1.  Being a coordinator, accepting requests, and then coordinating.
2.  Being a router or an end-device and connecting to the coordinator device.

The role of a device is decided at compile time, meaning that we decide what to implement on each device (coordinator, gateway), then put the device in a shell, and deliver it.

The first thing a device can do in ZigBee is either to join an existing network or create a new one. Non-coordinator devices will try to join a network, while coordinators will attempt to create one.

### Set up
In ZigBee, each device can only be part of one independent network. 
The application layer runs code and tries to find network information by invoking a network information request to the network layer. The network layer implements a single network on multiple frequencies, but only on one channel. To set up a channel, a set of frequencies is chosen that is not too noisy and free to establish a network.

In ZigBee, there are 16 frequencies in the 2.4 MHz band. The MAC layer looks for a channel with low noise levels to establish a network, performing an energy scan. It measures the amount of energy in each channel and returns a report on the state of the channels, allowing the network layer to choose the optimal channel for establishing the network.

#### Create a network
The process of forming a network involves creating a Personal Area Network (PAN) over a particular channel.

The **coordinator takes address 0(0x0000)**, while other devices take dynamic addresses. Zigbee devices use both 64-bit IEEE addresses and 16-bit network addresses for addressing. The IEEE address is unique to each device, while the network address is assigned dynamically by the coordinator. The network layer is responsible for maintaining a table of addresses for each device in the network, and it can allocate or de-allocate network addresses as necessary.


#### Process of Network formation:
![[Pasted image 20230311113603.png]]
The coordinator assigns itself the 16-bit network address 0x0000.
0) From Application layer send a NETWORK-FORMATION.request to the Network layer. 
1) Phase 1: The Zigbee device must first perform an energy scan to determine the channels that are free to use. The network layer performs the initial scan by asking the MAC layer to do with a SCAN-request. **This is needed to look for a channel that does not conflict with other existing networks**, so with the one a lowest noise. The MAC layer sends a SCAN.confirm to the Network layer as response with a list of the **channels with the strongest signal**.
2) Phase 2: The Network layer sends another SCAN.request, specifying the **channel with the strongest signal**, for which then the MAC layer performs an **active scan**, finding if there are any networks in the neighbourhood. It is done to ensure that any coordinators in the channel are discovered. The active scan helps to find a device communicating over that channel, and if no packets (**beacon frame**) are transmitted, it indicates that the channel is free.
3) Then the MAC layer sends a SCAN.confirm then **returns the list of all the available channel for network formation**.
4) The Network layer selects a channel and **select a PAN identifier which is not already in use by other PANs**.

Once a coordinator creates a network over a channel, it sends beacons to indicate that a network exists. A beacon contains an ID, PAN ID, and other parameters, and the layer takes note of the noises paired with the ID to find a channel where it can create a network.

#### Join
Joining a Zigbee network can be done in two ways:
1.  Join by association: The device initiates the join to the existing network  by sending an association request to a router or coordinator.    
2.  Direct join: Requested by a router or coordinator to ask a device to join its PAN, so there must be an operator choosing what device to connect.

##### By association
On the client side, to join a network:
1.  The client should find if there are existing networks around, and on what channel, then ask them to connect. The application layer, which is provided by the provider, must only be configured. To do so, the client asks to the network layer to do a NETWORK.DISCOVERY.request. The Network layer will forward a SCAN.request to the MAC layer that will perform the **ACTIVE SCAN**.
2.  After the active SCAN, the MAC layer sends a SCAN.confirm to the Network layer, the Network layer in turn sends a NETWORK-DISCOVERY.confirm, so the application layer arrives *the list of all neighbor networks is presented*.
3.  It is not up to the network layer to decide which network to join. Choosing the appropriate network will require a decision of a technician. These are the networks available, and the application layer selects a PAN (usually an operator). So the technician selects a PAN.    
4.  With the JOIN.request, you ask for a network address, but you do not have one. Usually you need one to communicate with a network, but there is an exception to do the join. So the JOIN.request, goes from Application layer to Network layer. The JOIN.request is called with parameters:
	-  PAN identifier of the selected network
	-  Flag indicating weather it is joined as router or end device
5. The JOIN.request primitive in the network layer select a **parent node** P in the PAN from the neighbourhood:
	- In star topology: P is the coordinator and the device will join as end device
	-  In tree topology: P is **a coordinator or a router, the device will join as router or as end-device**
6. The Network layer sends an ASSOCIATE.request to the MAC layer, which starts the Association protocol, allowing to **obtain the 16-bits short address**. The MAC layer will do the JOIN, and when doing so, you will receive a beacon from the coordinator of a network you are connecting to (if in the same area or get the beacon from a router forwarding here). Then the MAC layer sends the ASSOCIATE.confirm to the Network layer, which contains the address. Finally the Network layer sends the JOIN.confirm to the Application layer.
7. From  there on the Network layer will use the 16-bits network address to communicate over the network.
    
![[Pasted image 20230311113139.png]]


All the layers must be informed of the join, and all the layers must allocate resources and take notes of the networks, not just the MAC.

-   MAC layer should do the low-level communication.
-   Network layer handles routing and higher level of communication.

In fact, the JOIN protocol is at the Network layer, while the ASSOCIATE is on the MAC layer.

This protocol is executed by the router and end device exactly the same way. There will be on the side of the coordinator another JOIN protocol.

Even in a Tree topology, the routers will forward the beacon to allow to connect to a network. You can decide what routers, in the multi-hop network, to use. In general, use the router closer to the coordinator, which can be the parent.

When you JOIN, you specify:

-   PAN identifier of the selected network
-   A flag indicating whether it joins as a router or an end device.

If you join, you get two types of network addresses:

-   End device network address
-   Router network address

Before performing the JOIN request, you specify if you are executing as a router or an end device. The parent (being a router or the coordinator, from the topology) will decide for you the network address. Joining as a coordinator or not does not change much as JOIN.


## Using the network address instead of the MAC
When you transmit something:
* you have the headers for multiple levels.
The size of the headers are massive.
ZigBee does not use the **MAC addresses but just the Network address**, this comes at a cost to do this, which we see as we need a binding table in the coordinator, but it allows to send lighter weight messages.


# Application Layer
Components are:
Application framework: light TCP, includes the set of Application Objects APO.
* Zigbee device Object(ZDO):  manages the application services
* Application Support Sublayer: provides data, binding and discovery services

Zigbee Device Object: it includes the application logic, with device able to understand different logics.
Application Support Sublayer

![[Pasted image 20230311111459.png]]


### Application Framework
To address an Application Profile Object (APO), you need to give it an ID. There are 240 possible APO values, corresponding to an application endpoint. The value 0(0x0000) is reserved for ZDO (Zigbee Domain Object).


Each APO in the network is uniquely identified by its endpoint address and *the network address of its **hosting device**.

You can query APOs with the Key Value Pair (KVP) data service, which allows you to query the key or value from sensors. APOs may also allow for more complex states and interactions.
(The cluster library now includes KVP)


You may have devices with multiple switches (e.g. lights) and bulbs, and you need to decide how to connect them.

One approach is to create an APO for each switch (two APOs for each light switch) and an APO for the light bulb. Then, a switch can be connected to one or multiple other APOs. To implement this, communication for those devices must be implemented in the MAC layer, Network Layer, and Application Layer.



In this sample application, there are:
* APO 5B
* APO 6B
* APO 8B
Which have the single attribute:
* bulb status: on/off

Then we have APO 10 and APO 25 which are switches and are configured as *clients **at** the application layer*.
The attributes of APO 5B, 6B and 8B can be set remotely from the APO 10A and 25A.

![[Pasted image 20230311110353.png]]

# Transport Layer: APPLICATION SUPPORT SUBLAYER  (APS)

The APS is a lightweight transport layer that offers packet-level transport without creating channels, unlike TCP. It also provides an optional acknowledgment mechanism.
The acknowledgements are end to end.
Furthermore, the APS can filter out packets for non-registered endpoints. The local binding table, local groups, and local address map are managed by the management system.
So in general APS provides:
* Data service as a light transport layer,  filtering out the packet to non registered endpoints and profiles not matching and generating end-to-end acknoweledgements
* Management: with local binding table, local group table, local address map.
## Application Protocol Interface (APO): Endpoints

The APO allows applications that use different protocols to communicate with each other, enabling them to be part of the same larger application. Endpoint IDs range from 1 to 240.

A ZigBee device can run multiple applications, one for each APO, where endpoints are seen as virtual wires connecting applications, which are equivalent to Unix sockets.

The endpoint allow for several profiles, devices and control points to co-exist withing a single node.
### Clusters
Clusters are protocols at the application level that define specific device behavior. Although optional, to ensure device compliance with the Cluster Library and the standard, they must be implemented in accordance with the cluster specified in the cluster library. **Clusters can be messages in simpler cases, but in more complex cases, they can define specific device behavior.**

**Cluster defines an interaction protocol, so informally a cluster provides access to a service/functionality of an application object.**

A cluster defines a set of attributes to read or write and specifies commands and actions for the devices. Clusters can be combined to create a basic application that specifies a particular behavior.

* commands cause actions on a device
* attributes show the state of a device in a given cluster

To determine the actions to take when receiving a message, a cluster identifier must be provided. Cluster identifiers use 16-bit identifiers, and although they may seem large, they are extensively used within specific application areas such as industry or agriculture. The scope of the identifiers varies based on the application area.

For example, a cluster identifier can be used to specify the action of turning on a light.

**Cluster ID have a meaning withing a given profile**
### General domain 
This is a type of domain that is independent of the application being considered, whether in smart industry, smart city, or agriculture, etc. This cluster does not belong to a specific profile but rather a generic profile.

Basic Cluster, for example, determines the version of the ZigBee protocol being implemented.

Power Configuration Cluster 0x0001 provides information about the device, such as whether it has a battery or is plugged in. By connecting to this cluster of a device, one can obtain information about its power source.

Temperature Configuration Cluster 0x0002 is not a thermometer cluster, but rather is used to monitor the internal temperature and to read or set the temperatures of the specific cluster, as specified in the specification.
![[Pasted image 20230310171546.png]]
## Application Profiles
**Cluster ID have a meaning withing a given profile**
Application profiles are collections of clusters specific to certain application domains. There are parts of the specification that are specific to ZigBee, such as the join process. Additionally, to comply with the standard, there are other parts of the specification. Several documents (written by the ZigBee alliance) contain application profiles with cluster libraries, which are lengthy to write for all application domains. One example is home automation.

An identifier must be unique and be used to call the behavior of an application profile and its associated cluster.
Application profiles are represented by 16-bit numbers, but proprietary solutions are also possible.

A set of addresses:
* is used to specify standard profile
* can be used to define proprietary profile (non standard)

Connecting to a proprietary ZigBee network is possible if there are no security checks and they allow it. You may call general domain clusters and even interpret some behaviors, but if you receive packets with a proprietary application profile, you may not understand them. So while you can do some things as part of the network, you cannot do everything.

A ZigBee network may contain application objects with multiple profiles. In the standard, there is no limitation on the number of application objects and profiles that can be responded to, even multiple.


![[Pasted image 20230310171559.png]]


### Device IDS
From the perspective of the standard and the device, the Device ID is not necessary. However, for human operators, it is essential as the devices themselves cannot identify what they are
- the IDs are simply numbers mapped to descriptions of the devices
 Human operators rely on the descriptions provided by the IDs to identify the devices, but the devices themselves do not require this information.
ZigBee discovers services in a network based on *profile ID and cluster ID*, not on **device ID**.

# (Application Support Sublayer)APS services
APS: it is a software on a device. It provides services for:
* APOs
* ZDO: ZigBee Device Objects (which provide services to let the APOs to organize into a distributed application)

The APS data service enables the exchange of messages between two or more devices withing a network, where the data service is defined in terms of the primitives:
* request(send)
* confirm (returns the status of the transmission)
* indication (receive)

For example we have the APS of a device that is a switch, and sends an APS-DATA.request
![[Pasted image 20230310173413.png]]
An APS-Data.request is received and is sent until an APS-ACK is received.

There are some group table, where there is a forwarding to all APO in the group table.
There are APO to move and join a group as broadcast groups messaging basically.
The group management provides:
* services to build and maintain groups of APOs
Each APO in the group is identified by the pair:
* network address
* endpoint

The ADD-GROUP primitive is used to add an APO to a group.
The REMOVE-GROUP primitive to remove an APO from a group.
The primitives take the group number and the endpoint number, **in case the endpoint numbers does not exist, it creates it**. 
Information about groups is in a group table in the APS.


## Connection to a network
Once connected to a network, a device receives an address and uses it for communication. For example, a thermometer may receive address 100, while a thermostat receives address 200. If there is a power outage, the device goes down, and the coordinator creates a new network, the devices may receive different addresses, such as 70 and 220.

Since we do not have the MAC address, we cannot identify devices using the same address. This creates a challenge when managing power shortages. The ZigBee protocol addresses this challenge by using binding. Binding creates a permanent association between APOs during network configuration, which is then stored in the APS. By creating a bind between APOs and APS, the binding allows the source to connect to the destination.

The APO does not need to know which other APO it is connecting to. It only needs to know the value of the switch but not where it needs to connect. Binding allows the system to maintain connections and continue to function even in the event of power outages or device failures.

## APS binding

The APS uses the binding table, network address, and endpoint address to locate the destination endpoint and network address by referring to the binding table.
Binding allows an endpoint on a node to be connected (bound) to one or more endpoints on other nodes, **binding is unidirectional and can be performed by the ZDO of the coordinator**

![[Pasted image 20230311103547.png]]
The ZDO of the coordinator must create a bind of the network address with the network address of another device. This process is necessary to enable communication between devices. Once a bind is created, the devices can communicate with each other, and the APS uses the binding table to locate the destination device.

### Direct vs indirect addressing.

In direct addressing, you define the addresses pair \<destination endpoint, destination address\>, whereas in indirect addressing, the message is sent, and the network finds the receiver.
Direct addressing is not suitable for extremely simple devices
While Indirect addressing exploits binding tables

# Creating a bind
Initially bind are created when the network is deployed.
To create a bind, a person places the device in the environment and connects it to the ZigBee network. Then, they tell the APS to create a bind between the two devices.

## BIND and UNBIND primitives
* BIND: BIND.request creates a new entry in the local binding table, taking in the input table: \<source address, source endpoint, cluster identifier, destination address, destination endpoint\>.
* UNBIND: UNBIND.request deletes an entry from the local binding table


# Indirect addressing

Done using the binding table:
1) match source addr : \<network addr, endpoint addr\> and cluster identifier into the pair: 
	1) \<destination endpoint, destination network addr\>
## The binding table:
it is:
* stored in the APS of the ZigBee coordinator and of the router.
* it is updated on explicit request of **the ZDO in the routers or in the coordinator**
* it is usually initialise at network deployment


****

When an APO generates a message with a given cluster, the coordinator retrieves information from the binding table, including the:
* network address, endpoint of the source and clusterID of the message ("cluster")
Then, the coordinator uses this information to locate the destination device's network address and endpoint.

The binding table includes MAC addresses (IEEE address of 63 bits.), and the APS uses network addresses and map addresses to create a mapping between them. Ultimately, the mapping is done using the MAC address.


![[Pasted image 20230310175057.png]]

To retrieve the Source and Destination MAC addresses mapping to their Network addresses, we need the
**APS address MAP**
![[Pasted image 20230310232556.png]]
## APS address map
The map table is contained in the APS layer, it associates:
* 16 bit NWK(network) addresses with the 64 bit IEEE MAC addresses
**Zigbee end devices (ZED)** may change their 16 bit NWK addresses when they leave or join the network. If this happens the announcement is sent to the network and every nodes updates its internal tables accordingly to preserve the binding.


1) find a match for src addr
2) make a match for cluster id
3) make a match for source endpoint
4) then forward the messages to 3 destination 1 mac address (1 and dest ep 12), then 4 destination and dest ep 33.
If you specify dest addr 0x9999 you use multicast, to a group. Then you have another table with all the device in the broadcast.


### Incoming message.

The APS coordinator will obtain the MAC address and endpoint, then determine the network address before forwarding to the destination's network address.

When the coordinator receives the message, it includes the source network address, source endpoint, and cluster identifier.

The coordinator identifies the destination endpoint and network address by searching for the MAC address of the source in the Binding table. If a line match is found with the MAC address of the source, source endpoint, and cluster ID, the coordinator extracts the destination MAC address and endpoint.

However, the coordinator cannot use the destination MAC address alone and must consult the APS address map to determine the destination network address.

Once the network address is identified, the local network layer of the coordinator is instructed to send the message to the destination endpoint at that network address.

# Exercise
At the start, routers create a mapping between MAC addresses and network addresses, then we got the table with the mappings to use at time t.
![[Pasted image 20230310215453.png]]
Solution
1) 0000, 34
2) No message delivered as 0x0022 is disconnected
3) Message sent to  NWK Addr: 0x0001 and Dest EP: 
4) Message sent to 0x0003.

0000 is also the coordinator in ZigBee.


# ZDO

The ZDO implements the functionalities needed for any ZigBee devices. It is connected to endpoint 0 and implements:
* clusters for ZigBee
* in the ZigBee Device profile

Some of the functions are the device discovery functions.
There can be many devices in the enviroment, but you do not know what they are doing, so:
* mechanism to spot who are the device and how they describe themself.
Query the coordinator of the network, with a list of what are the devices that are placed.
This information it gets:
* network address of the device in a network. 

Over this there is a mechanism of **service discovery**, which should be used to get the full information about the network, where the network is created with a *parent/child building, as a tree, and the adresses are assigned according to the position on a tree.*
You respond to a network coordinator in the network, and the network coordinator knows about the parents (routers), but not about devices in the routers (which are its child).
The router child will respond based on its subtree. The routers will respond to the device discovery.
Then the person asking for network discovery will get the list of devices.

Then ask to the devices:
* **Service discovery***: directed to coordinator to get all services in a network
* directed to a single device, to find the services it offers.
Add the clusters to which the device will respond.

*To query an end device, its parent router will respond.* As the end device may be in power save mode, so the parent router will respond on behalf of it.

There may be some functionalities, such as flash, that allow to locate physically a device.
The ZDO may implement service discovery and the device discovery, forwarding the query to the ZDO of the routers.

The ZDO will also implement binding mechanism. The ZDO acts as a control layer that governs
the behavior and interactions of a Zigbee device within a Zigbee network.

APO may be local or one of your end device.

Message if cluster ID 4 and Endpoint 5, matches the second line, and it will match the device
with network adres O796F.

The message with Cluster ID 4 from endpoint 3 will match with line 1 and 4.

When you have 0x9999 **you send a multicast message, using the multicast function of the cluster library**.


# ZigBee Cluster Library

The cluster library defines the behaviours for multiple devices, *to have interoperability*.
This makes the device compatible at application level, as we want the device to be able to use each other (thermometer and thermostat for example).
Look at the cluster library before reinventing the wheel to implement a function.
![[Pasted image 20230314114126.png]]
Behaviours defined.


The cluster library use the paradigm:
* client: client that can read a value or **write an attribute on it**.
* server: sensors usually, which as an internal state

The server is basically a more complicated device, reading and writing a state.
![[Pasted image 20230314114306.png]]


### Functional domains
General: same for all domains
Closures
HVAC: pump system and cooling
Lighting
Measurement and sensing
Security and safety: description of the behaviours of the sensor for an alarm, such as a passive infrared
Protocol interfaces: made to ensure interoperability with other ZigBee protocol.

Commands: are messages at application layer, with an header and a payload.
The second is a parameter to the header.
e.g.: write(header) 1234(payload).

Commands can used about dynamic attribute reporting.
The server will for example return the temperature every X minutes.

There are commands to configure a periodic report.


#### Configuration commands
![[Pasted image 20230314114741.png]]
1) get basic information.
2) get power configuration.
3) Setup and read the temperature configuration, setting up alarms and behaviours to iti
4) Identify: flash a led function to make a human operator identify physically.

A configuration can be arbitrarily complex.
e.g. when having multiple lamps, with a dimmable one:
![[Pasted image 20230314114958.png]]
Place those in the environment and setup parameters, using a configuration tool. In this we setup the switches.
Setting up if a device is a router or a coordinator, or some other device is.
One ask to the coordinator to setup the binding between Dimmer Switch and Dimmable lamp and *what are the APO responding to On/Off and level control*.

To do so: on the configuration to have:
* define discovery
* service discovery
* identify
Then you have all the information to give to the binding table.
You may need multiple identifiers if you have more dimmable lamps.


The version of the ZigBee cluster library is mandatory, as we query to which device the application responds. So you need to get the specific cluster version. 

Mandatory/optional defines if it is obligatory to define the cluster library.

Power source= if it is on battery or plugged.

There are also for the attributes their type, if they are read only and if they have a default value.

So to get power source:
* basic cluster -> requesting for reading the power source

Temperature measurement cluster:
* it can be a reading and reporting with RO
* While the min and  measured values are only R.
We see there that the type are int16, so the thermometer is home automation, so they are less sophisticated.
Other systems industrial may have more precision.

### Temperature measurement cluster

It provides, read write, discovery and configure and report.
Any other cluster may provide functionalities to find each functionalities.

In general clusters are not a library, but allow to build increasingly complex applications. Or a lamp with colors and manufacturer specific features.
*Rather than defining libraries for all the possible lamp in the world, add more and more cluster to have all the possible behaviour.*
![[Pasted image 20230314120033.png]]

Also with manufacturer features, allow to have those, which will not be used by device of other manufacturer but at least the device are available.

If you are a company specialized in systems, with components integrated among themselves to make something more complex.
So when creating an IoT solution, buy HW from providers and see them.
See the implementation of the ClusterLibrary as a support.
Add sensor and actuators depending on your need, putting them into shells, then implement the APO and so setup the business logic of the device, then you are ready to go in the market.

If making a deployment to a customer, have your own deployments using configuration tools and complex things, spending less in other internal mechanism of the devices.
Add the software which makes you in a simple way pair your devices.


# ZigBee security

Security is not built in, but is optional.
It is light enough that device can afford it.
The security services include the four elements:
* key establishment (Authentication + mechanism of integraty done with keys/hashes): you need to provide and exchange to devices the keys, enabling the security mechanism
* key transport
* frame protection: use the keys to create frame encryption and integrity
* device management: device management mechanism

ZigBee makes several assumptions that limits the bahavior of the intruders.
As it assumes:
* device can keep in a safe place the keys
* There is a protection mechanism employed
* trust to someone that gives you the keys

Trust that the installation is secure, and so not compromising a secure network.

Suppose that:
* all security protocols were correctly implemented
* correct random generator, as it creates the key for encryption. Note that the ZigBee standard gives the specification, not the implementation
So implement correctly, deploy correctly, add limitations to intruders.

ZigBee suppose that the protection operates to the device level and network level.
The level of protection is the entire device.
For example on a PC, there may be multiple user, and if one is affected by weak password, the other may be safeguarded by the PC. 
The latter is not true here.

Those security mechanism are not resilient to the tampering of devices.
If someone takes them and tampers with them then it may compromise it.

The specification does not tell anything, but one could try to mechanism with anti tamper to protect it.

If there is tampering, then there may be ways to find it.


### Security Design Choice

* A single key: can operate with just one key for the whole network
* single key per link, end to end

The protection of the frame, is implemented at the network layer.
The APS provides the key to the network layer.
The ZDO provides the key to the APS.


The application profiles provides the cluster and specification to allow to connect to a secure network in a secure way, and obtain the encryption material.
The standard also has mechanism to detect that something were wrong, misuses of keys etc.**Allowing to re-synchronize keys and reestablish the network functions**.


ZDO, manages the security policy and configuration. Then the APS sets that up in the network layer.


## Keys

Both link or network keys can be obtained :
1) by transport: asking for it to a device centralized. It may be a problem, as you do not have a key, and so you must receive the key without encryption. This can be ok if you are in a place without anyone else there. 
2) key establishment: use protocols to generate keys
3) Pre-installation: the manufacturer insert the keys in the device
There is another key:
**Master key**: it can be used to create other keys, eg pre installed.
The device then uses it to generate new keys 
(diff helman). It allows us to obtain a link key or network key

Eg combine random number with master key pre installed.

# Trust-center
It may be implemented in the coordinator or have an ad-hoc functionality.
The trust center is the device trusted by the rest of the network, which allows to get keys, both network or link keys.

After you join a network you connect to it and then it allows us to communicate in the network.

 <div style='page-break-after: always'></div> 


# Chapter 6: High Tech Greenhouse and DOREMI
Several sectors to show different cultivate at the same time. As a consequence none of them will operate in ideal condition.


Two sectors:
1) conventional sensors: minimum temperature ensure, humidity sensor + moisture of the roots in the substrate. Automatic logic
2) Top sector: more modern control sectors.
![[Pasted image 20230618123327.png]]
There are also two sub sectors for different type of cultivation


Relate each sensor to its position, its type of transducer used with it.

![[Pasted image 20230618123420.png]]
Note how there are different type of sensors used.

**An IP network for sensors and plants was made, using LAN and Wi-Fi**. *There was a single point to govern the green house*.
**Sensors came from different manufacturers, making necessary calibrations**.
For each transducer make a calibration. Note that for each calibration it may be useful to keep data of the calibration. There were different standards and technologies involved, with several digital twins for sensors.


It may be see here the architecture of an Industrial IoT configuration:
![[Pasted image 20230618123719.png]]
We see how the sensor is connected to a gateway using TCP/IP. Furthermore the gateway connects to a MySQL DB internal and to a router.
Using [[IEEE 802.11]] they interacted with a touch screen for control and monitoring. The router would lead requests to the controller via Ethernet TCP/IP. The controller would control all sensors. There is also a Server, which may be local or remote, which is connected to a Router with Firewall if remote and accessed via internet.


This is the information system structure:
![[Pasted image 20230315162121.png]]
![[Pasted image 20230618142328.png]]
We may see for each transducer the sensors (a sensor is a bigger entity with one or more transducer) its paired with, its type, its measurements and its calibrations!


There is in general a digital twin, which allows to control devices from the controllers.
Models were made to get the need for fertigation depending on the actual needs of the crops.

There are parameters based in the growth of a plant. And create AI models for the growth prediction.

Lettuce grow:
* blue: actual growth
* black: what the model predicted
![[Pasted image 20230618142525.png]]
It is seen that more or less the predictions where accurate
The prediction may work in a short time. But difficult in the long time.


You now need a model to decide what to do with the parameters, as it can allow you to have a finer grain control of your fertilisation system.

The future is to have a decision system for all of that.

# DOREMI Project
Coaching system for old people at risk of cognitive decline, this happens with several different causes.
Produce knowledge and tools with protocol and methods to deal with cognitive decline, to reduce time to be hospitalise or need assistance.
Those problem also amplify themself in conjunction.

DOREMI LIFE-STYLE: it will advise people to have a good lifestyle.
![[Pasted image 20230315164414.png]]

The information are collected, then analysed and then to provide the feedback.
The feedback may be given to also increase the difficulty level, for example a physical exercise one.
They gamified lifestyle protocols and in three phase:
* engage in social game, exercise games and diet advice and cognitive game
* monitor the cases of nutrition, social activity and physical/cognitive activity
* Analyse: analysis on how the elderly respond to the proposed protocol
Consider that the gamification for physical activity is limited as they are elders with elderly problems after all.
![[Pasted image 20230315164717.png]]
A focus group was tasked to define the GUI which is see over there.
It has tree categories:
* Cognitive game
* Exercise area: show what exercise to execute and how to correctly execute it
* Social Area: social games area

## IoT part
Design of the IoT subsystem. With an hardware part developed by a Spanish Company. Software developed in IoT software by CNR.

* Wristband: developed a new one + assess of wristband in the market and compare their data with our models. Getting also estimation of the power consumption.
* Environmental Sensor: sense social interaction, providing some evidence of a possible social interaction. To do so they also use [[Indoor Localization]].
* Balance board: a copy of the Wii board, which assess user balance
* App for tablet: contains dietary data, allows to play games (social, cognitive, exercise games) and allows *to collect feedback*
The result of those sensor are checked by specialists for the particular type of sensors.

## Database
The database were made in Austria
The raw data go from sensor to a DB, then there is pre-processing.
According to a Config DB there is **Activity Recognition using Machine learning models**
Finally the data went to a database for processed data. Then the processed data go to a reasoner application, that is rule-based on rules configured by medical specialists.
Dashboards and Applications also were able to see the data from the processed data DB.
![[Pasted image 20230618155303.png]]

Using the dashboard, the medical personal is able to:
* adjust the protocol
* get data from the system to adjust the protocol.

## KPI
There were many Key performance indicators, for many different areas.
Many KPI depend on the subsystems to implement.
We have two types:
* Clinical, its KPI are:
	* Vital Parameters, 
		* the data it gathers
			* weight
			* balance
		* the device: the Balance Board*
	* Physical activity:
		* device: wristband, which collects as data:
			* **indoor position**
			* number of steps
			* wrist acceleration
		 * device 2: environmental Wireless Sensor Network (WSN), which allows to track physical activity with sensors activation data.
* Social, its KPI is:
	* Number of Interactions (social), using:
		* Environmental WSN here too, with the data of sensors activation
		* Smartphone with GPS.

Detection of interaction is complicated.
For example if people go out of a room, as a social interaction is dynamic and people may leave the conversation


There are different data flows for:
* sedentariness
* diet
* social area
![[Pasted image 20230315170424.png]]

1) First analysis
2) second analysand
3) third further high level analysis.

## Analyse

Activity Recognition, taking pre-process data and the information taken from the databases.
In each house they had sensors and we have have to relate them.
The Config-DB contains the information about the whole deployments.
The result of the activity recognition, goes in the Processed data Database, but the data processed there is too much.
You need a **REASONER** to give a better explanation to the medical specialists.


## Propose and validate a medical protocol

The medical protocol uses digital tools to obtain reliable information and take sensible decision.
Are our machine learning mechanism working correctly? Is the information reliable?
Or the number of times a person met another person.
This has to do with the correction of the models and the application.
The problem is:
* is our experimental methodology correct?
To meet those requirements:
* everything was subjected to the ethical committee.

Since the system did not have to last for a long time, they could use less durable components.
The tradeoff was to have limited reliability of the components, with the fault detection and on-site intervention from the technical staff.
Different tradeoff may make sense, something make a super efficient reliable system is not a solution.

Before of the pilot, we need to have the Machine Learning model already trained, to do this we needed to get datasets.
Also a living lab was used in of competition of indoor localization systems.

We may see here the flow for reliability requirements and the relative measures undertaken in the design/methodology
![[Pasted image 20230618162414.png]]
The process would then proceed to pilots and then the real study.

## System Architecture
![[Pasted image 20230315172533.png]]
Every user had a smartphone and tablet.
As the wristband connects to smartphone and the smartphone enables it.
The data pass to some processing steps, and are send to a dashboard.


To design fast use different gateways to combine devices.
DOREMI gateway for the balance board.
The localization sensors were using the home localization system of the shells of the wireless beacon.
The wristband was using as a gateway a smartphone.


## Balance Assessment

The Berg Protocol is difficult and require a medical specialist.
There is a threshold to get if one is independent or not on the Berg protocol, and it requires 30 minutes.
**They made an equivalent protocol, with 4 for force sensor and 1 neural network, with duration of just 10 seconds**

With the balancing board, the test could be done independent without a test. The balance board is the one of the Nintendo Wii.
Depending on the balance of your body, one will put more ore less pressure on one of the 4 force sensors of the board.

## Physical Activity Expenditure estimation

Color of the skin is what the sensors measure for heart rate.
My measuring the color of your skin, you measure with frequency, the heart-wave.
The heart beats 60 times per minutes, and so one looks at their frequencies with that. One determines caloric consumption using the parameters of:
* age
* sex
* weight
And there are models to determine the calories consumption.

Those device measurements are not accurate, a chest band are more accurate.
* Doremi wristband
* commercial wristband
* chest band

The metabolimeter is a better machine than those actually for heart rate. It uses the same mechanism of those.
You convert with oxygen and expelled oxygen, you find how much oxygen you burned, so the calories are the difference.

The metabolimeter is a mask.
Then they made the exercise to do in the app games.
From there a dataset was made for the wristband.
**By applying a model to the inputs of the sensors, would allow to get results near the metabolimeter.**


Red line: metabolimeter
Blue line: model over wristband data.
![[Pasted image 20230618163438.png]]
Not much of a distance.
The result at the end was better for DOREMI wristband than the commercial one.

## Socialization assessment

Outdoor: by means of GPS of people involved in the experiment
Indoor: environmental sensor to get how many people go out or stay in a room.

The problem may be that a person may only open the door.
Even a postman giving a packet is not a socializing event.

The idea at the end is:
* passive infrared to see if someone was outside
* passive infrared inside: Locate a person and discriminate their position, with indoor localization.

Train the neural network to discriminate 2-3 people in the room.

## Database
The measurements data go to MongoDB.
The deployment data went to SQL, as it was fixed (e.g. placement of sensors).

We may have streams of data, where we have a data feed collection describing each single measurements from a device, for example a balance measurements.

Each feed goes to an independent document, but there is a collection then of those document.

The data feed collection: contains information about the management. There may be a stream, with the message measurement field.
The message elements are comprised of signal measurements, and with the state of a button of the sensors, describing its state.

There are a data field, some meta data.
Those are a reference to the hardware running the measurement.
We may have specific boards, where one must keep a reference to what specific board.
The measurement will be the same for all balance boards and data field.

By expecting the NoSQL we get the measurements of the balance board.
With the SQL we get the pairing of the board to the user.
**This is done with a reference to the device ID, which is a primary key in a SQL Table**.
With the start time we may segment the time of the stream.
For example the pressure data to analyze will be done given the segment.
*The measurement start also when the board is activated from a procedure.*
![[Pasted image 20230321113038.png]]
Those data then associated with the person and be 
elaborated by machine learning.

**The queries look for:**
* data generated by a specific sensor
	* at a specific time frame

The DB grew vastly, for 20 users, 3 months data per user reached 30 GB per user! 

In the configuration, there was some redundancy in devices to monitor. 
The *configuration system used* enables some semi-automatic centralized configuration of the WSN (Wireless Sensor Network).
A graphical user interface annotates the sensors position and configuration.
All the kits were prepared in Valencia, and then they were send in the UK.
The kits were packed in the UK and send there.
It was seen that for the boards it was easier to buy a new one rather than sending back to Genoa.

## Pilots
There was the need to find people with moderate cognitive decline, able to use smartphones.
But at risk of having cognitive decline.
There was also the need of having them living independently, and they have to accept to be monitored.
At the end from 1000 people, only 32 users.
With two groups:
* intervention groups: 25 groups where the protocol where applied
* control group: 7 groups observed but without protocols applied, to see if the protocol brings benefits.

In UK, Shenley Wood the environment was ideal, as all the apartments were identical and they are close.
So the sensors placement were easily replicable.
Also the technical aid was given in the Shenley Wood, and there were people able to solve daily problems, for example wristband not working/charging.

The deployment required to get the blueprints before installation.

In Genoa the apartment are completely different and spread around in the city.
And they deployments had to be designed for all house, also they had thick walls preventing communication.
Also it was difficult to fix technical issues, as there was the problem of having appointments with users, which could forget the appointments as they were old.


From the medical point of view: large number of volunteers over a large period of time. So to spot a protocol over a long period of time efficiency, there is the need of long analysis.
In project like this one must account for what can be done.
So agree to organize pilots in sequence instead of parallel.
Also there was the problem of avoiding the summer break, as people in Genoa could leave the homes.


Every user had to do something daily and weekly.
The only technical interaction allowed was to have a specialist from Valencia installing the devices.
But only the medical specialist were allowed to instruct how to use the devices to the users.

Also each day the user were instructed to do exercises.
Also add data about food intake in the diet app.


## Data
Every week the user had to play a cognitive game three times. Also receive cognitive coaching on demand.

While in Italy there were more users. **The data from the UK were the double**.
On average the UK user produced more data.

### Issues
Medial issues:
1) In the UK from the technical point of view was optimal. But what happened is that the **users in the control group were in the control groups**. So they self organized sessions of exercising, socialisation and changed their diet. *Those are impossible to prevent*.  This was taken into account and had a limited impact.
2) Social protocol in the Italian pilot: there was the idea to create periodic meeting in the Italian pilot to enforce socialization. In the UK is easy as there were common space in the place. In Italy the problem was to ask user to go far from their home, and the care givers had to pick them up. So in Italy the social protocol was given up, so it had a medium impact.
3) The application of the diet intake did not have information about UK diet, as the app was made by an Italian company. Most of the food consumed in the UK was not present. So there was work to add pictures and details. Its impact is limited since it was fixed, adding new DB entries for food.
4) from the medical point of view also a user withdrew

Technical problems

1) It was seen that in the UK the balance board was "not working", basically it did not produce any data.  The idea was that the chain of data there was something broken. The problem was: *the method to activate the balance board there was a protocol*. The problem at the end was that the doctor instructing the patients failed to understand how to instruct the patients. So this was a  **communication problem, as different specialist may have a different "language"** (in the slides it is said diet)
2) Users with pet, and fortunately only 2 in the UK had them. Those are a problem with passive infrared, so the application for the socialization event. It was limited, since those users did not met in the apartment people as they had common space, so in the end no much people went in the apartments
3) Some users refused to install some of the sensors. As they did not want for example hole in the walls or a sensor could disturb them, as they could have leds disturbing them. In the end they were not installed in the place designed, or some were not installed at all. That had an effect on socialization system and indoor detection. A user did not want a sensor out of the door, as he did not want to be known as being involved in a medical pilot, 
4) **Lack of motivation of the user, especially in italy**. In the UK the people could be motivated daily and people supported each other. In italy they were difficult to keep in touch. They stopped using the system, which meant to lost data in italy.
5) Imposed user privacy: there was the need of completely anonymous data, so no infomation about the users in the database was to in the DB, (outside of the DB and on paper there were reference), there was a pseudo anonimzation. There were games that **needed to be social, to share the results in rankings. The users complained that they want to know the other users and they were not able to**

Data reliability and other problems
1) Blackout in Genoa: one day only battery device were able to send data, as there was a city wide blackout
2) lack of connectivity: it was guaranteed that residence in UK had wifi coverage, but it was not sufficient, so 4G gateways were installed to fix that.
3) Monitoring devices and unavibality of the system: the user themself may have been a problem, as users would hide passive infrared of a user.
4) User hacking the tablet: a tablet was configured only to run the games. In order to connect user to games, there was a specific profile user on Android. The problem than was that a user changed the profile.

Reason of data loss:
![[Pasted image 20230321121914.png]]

Violet: lack of motivation, which was the first cause of data loss.

### Final remarks

1) The management were totally different in the areas. The environment affect the solution at many different level
2) Very limited budget, required a tradeoff between reliability and device less reliable but having a detect and fix approach. Part of the diagnosis required ad hoc intervention so there were investment there
3) **Unexpected issues, since devices are in the wild, exposed to everything, the user itself is wild enough**

On site pilots are complex if *users/human are involved, as user add additional entropy in a system, difficult to consider.*

A problem was also having indirect communication with the users, so missing feedback as the mediator did not have the tech skills.

*Interacting with medical specialists is difficult as they have different languages and expectations*.
Medical specialist do not trust the computer scientists

*Misunderstand lead easily a system to underperform.*
**Main lesson:** be ready to the unexpected.

 <div style='page-break-after: always'></div> 


# Chapter 7: IoT Design Aspects
In IoT one has to deal with devices:
* low power
* small
* autonomous (operate in respect to anything that may happen around)

At the same time a device is a full micro system, with Processor, Memory, radio and sensing/actuator device.
**In general to deploy the device anywhere, the device are batter powered**.
In some other cases the devices may use energy harvesting protocols, such as solar panels.

Energy efficiency: the most important issue.
If devices are powered by battery, then the device will stop working when it is consumed. Only way to do it is to ask to someone to do it.
If a device is cheap, it is maybe not worth it to recharge it asking someone to do it.

Adaptability to changing condition: may bee needed since if the deployment is in several years, the device must be adapted and be able to be interoperable, for example allowing to upload  a new firmware to update it.
This is complicated and not always possible to all devices.
The device will come with limitations in term of processing also.

In ZigBee for example we may have nodes of a lot of devices. And those devices cannot be organized in a star topology.

Protocols may be organized with routing tables, and we could address any node with 2 bytes. 
30k of devices  * 2bytes would be **larger than 64kbytes**, while in arduino you have only 4kbytes.
So routing protocol do not scale with low power devices. So the network is multi-hop

Mobility: there may be sensors for example where one monitors cows in a very large farm, which move freely. End in end you may not have an infrastructure with coverage over there.
The network must be mobile too, which is a problem,

Then we have data storage and processing to implement intelligence in those devices.
Even Arduino may have tensor flow.



In Computer Technology, for multiple technologies, there was the sit and wait approach, to get powerful computer which can execute complex algorithms, so the problem of AI in part is solved by sitting and waiting.
Those issues of IoT devices one could think, that they will be solved.

Moore Law: computer technology and the business of computer grows exponentially, every 2/3 years technology must be renewed.

## IoT context Moore

1) Performance double every 2 years
2) Size of the chip halves every two year, using the effect of the doubling of transistor, to pack same in half space
3) The cost halve every two year


Depending on what applications we need:
* small sized sensors
* in some application you need lots of devices, so you prefer low cost
* or you may need high performance devices

Will the Moore law solve our problem? No, not on the short term.
**We need to rely on something else now, not the Moore law, so rely on:**

# Energy Efficiency

Smart solution in implementing IoT devices.
The battery capacity is the technology that improves really slows or nothing (flat improvement).
All other processor, HD and memory capacity frows exponentially. 
The battery is bound to physical property difficult to exploit.

Improve on design and software part instead of battery.
To do:
- Analyse problem and find were we waste more energy

Generally display spends more but IoT device do not have those, so it is not a problem. 
In general a smaller amount of energy is spend on sense and analog digital converter.
Then half and half on Processor and Wireless network interface:
*this is subject to your application, depending if you transmit more or process more.*
Note that transmitting consumes 1k more than processing, but since you do not transmit continuously, it is balanced.

Usually the activation of the sensing element of a device, is something that cannot be arbitrarily. As its power depends on the quantity of that that you can receive.

From a certain PoV a microprocessor knows about itself, so it is easier to develop strategy to save time.
Radio is used to transmit and receive to someone else, so you are not free to control it as you wish.
That has a strong impact in solutions to save energy.
Most solution are based on developing strategy to make energy consumption more efficient.

## Relative relationship of Energy Efficiency radio

Every radio have different states, for example for WiFi:
* sleep: radio is frozen, so does not send and receive, but it is not technically off. Freeze as much as possible, much more than transmitting less
* transmit: consumes more than all modes, so try to shrink it
* receive
* listen (ready to transmit and receive)

For 802.3.4 (ZigBee one)
There the transmit mode has different **energy power**.
More power means to transmit at  a farther distance, the more you amplify, the distant the signal will arrive.
With 0.1 power level, you send it as less far as possible.
In receive model you **need to also decode the from analog to digital, while in send it may be easier so in 0.1 power level it is faster**.

**Those data say that transmitting less is not a solution, as listen mode is still costly, while turning the radio off will be the best to save energy, but you will not hear from any one, as if you do not exist anymore in the network.**
How to turn the radio off while keeping device communication?
The MAC protocols have been redone for wireless networks to refactor it.


transmit < receive in some case.
listen power is equal to receive power
radio should be turned off as much as possible, while preserving network operativity.

Turning off a component and turning it on again, *consumes energy too, so when taking a decision like that, know that this component will remain off for a reasonable amount of time.*
Also turning on and off will reduce the component availability, so one has to wait before it becomes operative again.


# Duty cycle
It is a period of activity:
* when sampling a physical signal.

This sampling activity is more efficient if repeated periodically.
So on a loop, perform a set of activity and wait for another loop.
A laptop does not have those, it may have sensors, but it is not its main task.
In IoT devices the activity is periodic in most  of the case.

**Put components in deep sleep mode when not in use**.
So the **duty cycle represent the fraction of one operiod in which the system in active**
So there is a period with inactivity and activity.
Also on the *inactivity fraction on the period, you may need to do something to keep the radio active.*

# Arduino code of sensor with DC

In Arduino the code is written in a function called loop, called continuously.
What is done usually is: read data from a sensor, process, store and transmit.

analogRead: read analog value into digital value.
Serial.println means to transmit over a line.

1) Sensor board and microprocessor shall be active in first instruction
2) in second instruction, not using the sensor, only the microprocessor can be active
3) in the third instruction, both microprocessor and radio must be used.
4) delay: may have all component in idle state, in principle, in arduino all components do not go off. Arduino will not turn them off, but in principle delay means to turn off components (in the example) and not waste energy.
Duty cycle of a component: time where a component is active, in a cycle of activity.

Supposing to have calls to turnOn and turnOff given components.
And instead of delay we may have a function turning off a microprocessor for y millisecond.
If i decide to turnOff a component, and to turnOn a component *i need a microprocessor to turn on, but then it is impossible to have it off*.
**Idle serves to stop the microprocessor, while for example a line which send interrupt remains active and wakes up the micro-processor.**

Using that:
* turn on microprocessor
* read its data
* turn off

Microprocessor active in first 3 instruction:
20 ms.
Total cycle is 400.

So the microprocessor duty cycle is 
$20/400$.

Current absorbed by each component in each state.
Note that processor for example have different consumption depending on its state.


Logger are memory, permament storage to use as disk.
Take into account that you rely on a battery, which is charged with a given amount of energy, part of the energy then is lost while using.
**As the battery ages, you will lose capacity, even if it is not used, as it cannot maintain a level of charge**.


Model 1:
	100% duty cycle of microprocessor ratio of active period and total period is 1. This is achieved by having the micro processor always operating.
	logger write mode in 1% of the time and read 2% of the type

Model 2: 
	model that sleeps 99% of the time. 
	When we have 5% duty cycle in general we refer to the processing as it is the most used.

*Note that some component are active in parallel, for example processor and radio both active at the same time.*

Sum of all the activity periods of a component, even if in two different section will measure the duty cycle.

1W: measure the work performed by a current of 1 Ampere which flows through a electrical potential difference of 1 Volt.
**Voltage is constant as we are operating in DC**.

Only the **Ampere change over time, so we can measure energy in milliampere hour**,

You can obtain joule by multiplying milliampere hour by voltage (a very good approximation).


# From duty cycle to energy consumption

Given a period of 400 ms.
Microprocessor is active for a fraction of time, and inactive for another fraction.
The first is the duty cycle.

$C^{full}$ * duty cycle of microprocessor + $C^{idle}$ (1-duty cycle) 

$C^{full}$ is the energy cost measure when the microprocessor operates at maximum capacity.


Radio: more complicated, as we are splitting time when transmitting and receiving. So we must **define a transmit and receive duty cycle and consider the union of them for the duty cycle of the radio**.
So we account for the two duty cycle and the cost for each, and the idle by doing 1- duty cycle transmit - duty cycle receive.


Note that it is three order of magnituted less the cost of idle mode, but this factor will be accounted as it will be multiplied by a large quantity (as we want to be a lot of time in idle mode), so the measure will have comparable measure, we **cannot** *disregard the idle measure.*

Energy consumption per period: energy consumption for all components.

Lifetime: (initial battery charge - leaks in lifecycle)/total consumption per duty cycle
**Lifetime unit of measure is for duty cycle**.

For the entire lifetime, we have this L leak, which depends on the lifetime, so it is a recursive equation as it changes, there is more leak in the lifetime. So we should account for that. 

We could do that by accounting for one year of duty cycle, by counting the duty cycles possible in one year, to find after how many duty cycle the L increases.

Given $\epsilon$ loss per cycle, we can express
battery loss of cycle n, with  (battery loss at duty cycle n-1) * 1-$\epsilon$ - E(energy consumption of a cycle)

So you solve the recurrence equation to deal with the battery charge loss.


**The device does not stop working when the battery charge reach 0, but one finds a threshold from which the device stops working.**



![[Pasted image 20230324173926.png]]

milliampere hour in the x axis.
In a logarithmic scale.
On y the percentage the months.

Generally the device last much much more  if you shrink the duty cycle,.

The more you reduce the duty cycle, the more you last.

Exercise



processor dc = 4+1+15 /400= 20ms/400 = 0.05 ms
processor cost per duty cycle= 0.05 * 8mA + 0.95 * 15μA = 0.4 mA ms + 14.25 μA ms


Duty cycle in 1h
3600/0,4 = 9000
(0.4 = milliseconds in 1h).


Multiply duty cycle in 1h *to get the fraction of time the device is active*.


So for example Processor

(1 - dc) * 1 hour * P idle*
Allowing us to get the power consumption in 1h.



sensor dc = 1/400  =  0.0025 ms
sensor cost per duty cycle = 0.0025 * 1 mA+ 20 * 0.9975 μA = 


radio dc = 15 ms /400 =0.0375ms
radio cost per duty cycle = 0.0375 * 1 mA + 0.9625 * 20 μA 



Lifetime  = Battery charge/total battery consumption

1.243 =tot battery consumption.
Solution is wrong.
Battery charge was guessed and not given in the exercise


1609 is the **number of hours of lifetime**


## Constraints

Some constraints do not prevent us to reduce the duty cycle.

Radio is used to communicate with others, so taking a local decision to turn off the radio, means that the other will not be able to communicate with us.

Reduce radio duty cycle by *using a form of coordination with other device, this has impact at the MAC layer*

## MAC protocols
Typically they are used to decide who can communicate.
In those mobile devices, they are used to decide the duty cycle.
There is the need of communication to devise a strategy for energy efficiency, not only to communicate without interference.

[[Exercises on Approaches of Duty Cycle]]

 <div style='page-break-after: always'></div> 


# Chapter 8: Exercises on Approaches of Duty Cycle
![[Pasted image 20230328215626.png]]
20 Hz: period of sampling (requirement of sensor).
Sampling a sensor takes 0.5ms. 
**Having 20 Hz sampling period means that 20 samples will be produced in 1 second.**
(x Hz represents 1s/x = **time to get 1 sample**)
Doing 1/20 *we get a sample every* 0.05seconds, in milliseconds it is 50ms 
So the Period is 50ms, and within this period, there is the measurement in 5ms.

* sampling requires both processor and sensor to be active
* the computing will be done every 5 samples on a remote server
* The transmission time is 2ms and requires both processor and radio active.

Heart rate is computed every 2 seconds (on 40 samples).
The HR is computed by a server.
The transmission time is 2ms and requires bot processor and radio active.


5 samples at a time are send to the **server**.

Server will compute every 40 samples.


### Duty cycle of sampling

We have
* 0.5 ms: working time
Duty Cycle of sampling: 0.5 millisecond (sampling time) / 0.05 second (sampling period)  
In percentage 0.01 * 100 = 1%.

We get a sample every 50 ms.
We need 5 samples to get 5 SAMPLES

# Duty cycle of transmission

The transmission is done every 5 samples. 
To get 5 samples we need 5* 50ms = 250ms
or 0.25 seconds.
So every **250 ms we send the data in 2 milliseconds**.

Duty cycle transmission
2ms (transmission)/0.25 sec (transmission period) = 0.008
In percentage: 0.8%



**Duty cycle cannot be above 1, ever.**


# Duty cycle per component
Duty cycle of processor: *it is the sum of the two duty cycle of transmission and sampling, as it does both activity independently without intersection*. Consider the minimum common number of those elements, and find the time where this is active.

Microprocessor duty cycle: 5* duty cycle of sampling + duty cycle of transmitting

Pw consumption in 1h: multiply by 1 hour the calculations.

Sensor energy consumption per duty cycle: $5mAh*0.01 +5\micro Ah*0.99$  = 0.55mAh
(we can express the power consumption with mA**h** as the voltage is constant, so we avoid to use Joule)



For the processor we must sum both the duty cycles
Processor solution: 
$(0.01+0.008)*8mAh+ (0.982)* 15\micro Ah$ = $0.144 mAh+14.73 \micro Ah$ = $0.144 mAh+((14.73)/1000) mAh$ =$0.144 mAh+14.73 \micro Ah$ = $0.144 mAh+00.01473mah$ = 0,1587

Radio consumption(**Left as exercise before exam**) = 0,1798.


**Duty cycle of the processor must be the sum of the two sampling and transmitting dc.**

(Using the radio in receive mode, it means that we would have another duty cycle to sum to the radio, for transmitting and receiving)


Lifetime = Power capacity fully charged / total power consumption   =  $$\frac{2000mA}{(0.1798+0.1587+0.055)mA}=5087 h$$


-------------------
# Exercise 2
![[Pasted image 20230329095846.png]]

The computing is done every 2s, and for 4ms.
It follows that it is:
duty cycle of computing: (5 ms) / (2 seconds) = 0,0025 ms 
computing:0.25%


The transmitting is done every **10 seconds(having collected 5 values computed)**
duty cycle of transmitting :
2ms/10s = 0,0002ms
transmitting:0.02%


The sampling is as in the exercise befoe.
sampling : 1 sec => 1%



#### Component by component

Processor time (*sum duty cycle of computing, sampling, transmitting*) =
1.27%\ * 8mAh + 98.7% * 15 $\mu$Ah = 0.1164 mAh



Radio time: $0,0002ms*20mAh+0,9998*20\micro A h$ = $0,004mAh + (19.96/1000)=0,004mAh+ 0,019 mAh = 0,024 mAh$

Lifetime and sensing time left as exercise before the session.

**Do not sum to the whole period the active period, you must send every X, so account for the time to send.**

## Takeaway
You need to reduce the duty cycle to spend less energy.
Not always you can reduce enough to spend less.
But you may move freely from device to cloud computation, which opens a range of possibility on the design and duty cycle.
Reducing the duty cycle is possible, if you find among all possible implementations, the correct trade-off.
The problem here are the same, but we have two completely different implementations.
And we found different values.

 <div style='page-break-after: always'></div> 


# Chapter 9: Biologging
Sensor to keep track of animals, 24 h a day.
Tortoise case of the paper.
We can distinguish between two approaches:
* biotelemetry: attach a sensor without storage, whatever it samples, it should be transmitted immediately. There is no storage. For example a radio collar transmitting the presence of a bear, and its position, detecting the angle from where the collar transmit to find its position.
* biologging: with the ability to store information, and no ability to send information, but actually biologging. Attach the sensor ( with sleeping animal), and then retrieve by hand. **Biologging are invasive devices, which means to catch it, sedate it, add the sensor, catch it again to get the data, so reduce this activity**

Now sensor can collect parameters concerning the behaviour, so biologging.
Biologging allows to study the habits and the life of an animal.

Study on the seals, detecting their activities were done, other on penguins.

Procedure:
* collect data
* classify what the animal is doing

Biologging will produce values and store local.
IoT and artificial intelligence can be used to send few data to server and reconstruct a series.

# Device Perspective

You have a long time series. With telemetry, you may send all the data.
Transmitting everything is expensive. On the other hand, you may solve the problem of the transmission, storing data. But if the storage is damaged, then all is lost.
**Limitations on the device storage, may then obligate you to retrieve them (which is invasive)**.

We do not need a simple log, but a full micro controller, producing a huge amount of time-series data
then using on board an automatic classifier. Which means to have a semantic classifier, at this point the activity for an animal are a few, and are reduced from time to time.
That has an implicit effect of prolonging the lifetime of a device, considering also the size of the memory of the device.

# Tortoise

In this case, there is an adaptive duty cycle, depending on conditions and branches.

Tortoise are protected when the eggs hatch.
They are released in the wild when protected against predators.

The problem is:
*finding the nests*, it is not as easy as turtle which have fixed nests on beach.

Tortoise may spread in different places and in different periods their nests.
In the places where they make a nest, the tortoise will cover the nest and laid the eggs.
The researcher collect them when the mother tortoise hatch them.
This is easy in Galapagos.

In Tuscany not, because there are lots of trees and forests.
So track with a device if the tortoise is laying down the eggs.
Then with GPS the researcher finds mother tortoise.

The device does not have GPS actually, but it has a way to find where the tortoise is.

### Detecting excavation
The tortoise make a particular movement when excavating a nest.
It takes a couple of hours, and it may happen that the tortoise begins, then gives up, and moves somewhere else.

The tortoise will lay down eggs in 4 months in the summer.
Ideally add it in the back of the tortoise at the start.
Consider that 1 year is too much to keep on, and it is not invasive to remove and add on tortoise. The battery would not last 1 year.

**Accelerometer: if not going fast, then it measures the gravity**.
When the tortoise excavates, the accelerometers sees the negative or positive gravity depending on the inclination of the tortoise when it excavates.
* To detect laying of eggs, you use the accelerometer, which you sample at given frequency, usually high.
* To spend less, find the right environment to lay, so light and temperature, as to limit the use of accelerometer.
You may turn off the accelerometer.


For temperature and light, you may have a really tiny duty cycle. As temperature takes a lot to go high.
![[Pasted image 20230331164107.png]]

Accelerometer is sampled at 1 Hz.
And the accelerometer will be sampled in the time required to implement activity recognition with a good accuracy.
If nothing relevant is detected, go back with very low sampling of light and temperature.

If an activity that is compatible with nesting, to reduce false positive, have a sort of confirmation, by repeating the activity of monitoring.

We may detect that step 4 is done only 4 times a day.

Usually the lifecycle is on step 1. So you will have a very long lifecycle.

We like a device with a small battery, so that it fits on a tortoise easily.

### Activity Recognition

Activity recognition has the goal to automatically recognizing the actions of animals from the signals collected during its activity.
Biologging provides the data, that are fed to the activity recognition system, which processes the data:
* processed by human
* and processed by an Automatic System
Then the activity is labelled:
* as digging for example
![[Pasted image 20230621094556.png]]


### Sensors are good or bad?
The strengths of using sensor is that they give punctual observation in time and can be used both in:
* wild environment 
* domestic environment
They output large quantities of data in time-series form, which requires suitable data analysis algorithms

The weaknesses are the constraints given by the battery lifetime, for intensive monitoring we may need off-line analysis. When the memory fill up or in the worst case of battery usage the battery drains out,  we need to retrieve the sensor physically, as its attached to the subject.


### Device Perspective

#### Conventional Approach - Low power logger
The conventional approach is use a low power logger.  It collects the data and communicates it:
* as a time-series to a remote station.
* or by retrieving the logger on field and get the time-series data

**Which are problematic solutions, especially in the biologging case!**
![[Pasted image 20230621100007.png]]

1) requires a lot of power to use the radio for that huge amount of time series data
2) its intrusive, as you physically have to go there and retrieve the device
![[Pasted image 20230621100050.png]]
#### Novel Approach - low power micro processor
**The goal of the novel approach is to reduce the amount of data sent, basically not sending a hug time-series but an output that already processed it**.
*A classifier was embed on board, processing the data and storing the result, resulting in better memory usage and communication efficiency*.
![[Pasted image 20230621101021.png]]

# Tortoise@ project
What they did was to localize Tortoises Nests, by:
* recognizing the digging
* having GPS
Then sending to a remote station the position of the digging.

Given that Tortoise lay eggs for over 4 months in the spring, the device must work for at least 4 months, so the battery should not run out before.
Since tortoise dig to create a nest, they found that accelerometer was very well capable of recognizing it.
**But there must be also some precise conditions for temperature and light, so low energy sensors as light and temperature were used, to limit the accelerometer usage.**


### Datasets

The initial Dataset was created by recording the behaviour of tortoise in captivity at «Centro di protezione tartarughe Mediterranee» at Massa Marittima, Italy
Spot digging, like when a tortoise does it, can create a lot of noise. There is a 300-second window to spot patterns, which have a size of 90 seconds. Using an accelerometer, if it is inclined to the left or right, you can obtain numbers that allow you to identify digging behavior that must be studied.

**The accelerometer produced a raw time-series of value of the x axis (not required the y axis)**

The data collected at Centro di protezione tartughe Mediterranee was then divided in two sets for *training and test sets*.

There are two dataset:
* Sequence dataset:
	* made of sequences in the 300-second window.
		* in this window 1 Hz sampling (so 300 sample at window)
	* In total they made 126 sequences, where they provided positive and negative classification (for the digging activity)
	* 56 sequences of those **were reserved for the test set, the others for the training and validation set**.
* Patterns dataset
	* a sequence of 90 seconds (time window), sampled at 1 Hz (so 90 sample at window)
	* 67 patterns with positive classification
	* 67 negative for *model selection*, allowing to select the best machine learning model
	* 10 patterns with positive classification and 10 negative for **model validation**
**The activities detected are**:
* digging
* walking
* eating
All can be recognized by different patterns in the x axis.


### Windowing
The size of the window was selected because it depends on the shape of the digging activity signal.
They may see how a portion of the window is taken for pattern recognition.
![[Pasted image 20230621115639.png]]


## Processing
1) Fill a model with a windows: Asynchronous task, as you sample and then taking a window you compute. The whole output depends of the Neural Network depends on the entire window.
2) Fill a model with all the input arriving: Synchronous task, you classify a stream of data while arrives. **There is a state kept with different sample, there for any sample you get a result**. You need something to aggregate the results. The output of a neural network does not need an entire windows of sample in this case, so it each sample is based **on the last 90 seconds, which are sufficient to find a pattern**.

Keeping the neural network has some memory overhead.
A Supervised Machine learning model while having the best performance is the worst in terms of memory overhead.

![[Pasted image 20230621121347.png]]

The best tradeoff is to use ESN
![[Pasted image 20230621121338.png]]


They used ESN neural network, which are a type of recurrent neural network. A recurrent neural network (RNN) is a type of neural network that can process sequential data by maintaining an internal memory state.
ESN uses a large reservoir of fixed, randomly connected neurons to transform input into high-dimensional features. ESNs are easier to train than traditional RNNs and have been successfully used in tasks such as time-series prediction and image classification.

Asynchronous task: The ESN neural network has an accuracy rate of 55% and operates on a single pattern, which can be amplified. Additionally, ESN has low memory consumption, using only 0.1 kilobytes, making it suitable for devices such as Arduino with limited RAM. Even CNN, which requires 3.5 KB of RAM, may not be feasible due to the cost associated with processing new data. ESN can be re-iterated to enhance the results.

To optimize synchronous tasks, the ESN neural network can achieve an accuracy rate of 93% by voting for each pattern, while maintaining low memory usage of only 1KB.

## Energy Efficiency
Factors:
- Avoid sampling at night.
- Environmental conditions can be sampled at a rate of 0.01 Hz, very low rate (temperature and light).
- When the environmental conditions are suitable for laying eggs, sample every 5 minutes at 1 Hz.
- If there is a positive response, the accelerometer sampling is repeated 3 times, in this way you reduce the rate of false positive
- if there is a negative response **suspend for half an hour the sampling, noting that the digging lasts more than one hour**
- only when the device is sure of the tortoise excavation it transmits, limiting the energy consumed

## Memory Consumption

There are two data structures in memory:
* a vector of SVM (Support Vector Machine), a vector refers to a feature vector, which is a mathematical representation of a set of input data. For conventional neural network, keep a whole window before fitting.
	* Also you need to keep a buffer.
* A structure to store the acceleration samples, ***In the worst case the whole window of 300 samples, considering that it is an analog signal, and it is converted from analog to digital with ADC that will give a certain size to the sample.**.

An Arduino has 10 bits for digital input, and we can assume that 1 sample is stored in 2 bytes. If you have 300 samples, storing a window of samples occupies 600 bytes.
This is relatively low, consider that cellular can hold much more.
## Cloud-Based vs Local

_Sometimes, local processing is better_.

If all computation is done on the cloud, data must be transmitted continuously without storing much locally. However, it's crucial to have a way to program the device from the cloud. If the device only transmits data, it won't be able to decide when to switch from GPS mode sampling to accelerometer mode. Therefore, you must send GPS data continuously to trigger the accelerometer.

With cloud-based processing, the device needs to store and transmit GPS position data every half an hour. A GPS position consists of two 32-bit long integers for latitude and longitude. Additionally, data sampled at 1 Hz must be stored and transmitted. In this case, low-power sensing of light or temperature may not be available.

Working for 4 months means:
- 46 KBytes of GPS data transmission
- 13 MBytes of accelerometer data transmission

With local processing, only 32 bits of latitude and longitude are needed when detecting excavation. The storage would only require about 3 KBytes at most, even less using ESN. In this case, the GPS can be activated only when detecting an excavation.
With ESN, you can keep the data usage below 1KB.

The storage in the exercises is considered as **permanent storage, not RAM**. It's essential never to reach the point where a device has to discard memory. The information about the device's lifetime tells you the limit up to which the device can be used before needing to be replaced.

## Examples with totally wrong solution

### Ex 1
![[Pasted image 20230621155711.png]]

### Ex 2
![[Pasted image 20230621155727.png]]
### Ex 3
![[Pasted image 20230621155739.png]]
### Ex 4
![[Pasted image 20230621155751.png]]

### Solutions
![[Immagine 2023-06-24 143006.png]]
![[Immagine 2023-06-24 142941.png]]
![[Immagine 2023-06-24 125414.png]]

![[Immagine 2023-06-24 125341.png]]

 <div style='page-break-after: always'></div> 


# Chapter 10: MAC Protocols

## IoT Design Aspects

One of the key design aspects of IoT is to reduce energy consumption. One way to achieve this is by reducing the duty cycle, which can be done through planning the transmission to reduce the duty cycle. However, messages received asynchronously cannot be planned, and we must wait for them.

## Objective of MAC Protocol

MAC protocols do not aim to reduce collisions primarily but to implement a duty cycle of the radio so that each device can use the radio when it is convenient. This can be achieved through different ways such as distributed protocol, preamble sampling, and polling. For instance, S-MAC implements only local synchronization, which means that two nodes far away from each other may be desynchronized, but the local ones are synchronized. Hence, messages travel along a path.

## S-MAC

In S-MAC, each node has its own schedule of radio activity, which consists of a period of activity and a fraction of time where it's active. The schedule is advertised with a SYNC frame. By listening to its neighbors, a node can use their schedule. If two neighbors have different schedules, one must pick up one of them. If no neighbors are present, the node chooses its own schedule. A node may revert to someone else's schedule if its own schedule is not shared with anyone else.

To transmit to a distant node with a different activity period, a node must turn on the radio when the distant node is active. This can cause latency issues in a multi-hop network, which can be optimized by overhearing a packet transmitted to someone else and keeping the radio on to become the next hop.

To avoid collisions, S-MAC uses the Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) protocol, which is a protocol for carrier transmission in wireless networks. In terms of energy consumption, the measure of inter-arrival plays a significant role, and the bigger the smaller the load on the network. However, the real problem with S-MAC is desynchronization, which can result in increased latency compared to other protocols that do not use a sleep cycle.

Overall, S-MAC's local synchronization approach is useful for conserving energy, but it has its limitations, especially in large multi-hop networks.


## Keeping Synchronization

Usually, synchronization is maintained with clocks. In IoT devices, clocks are really cheap and are affected by environmental parameters like temperature. The clocks may then diverge between devices, and it is significant to note that using a device without a shell versus a device with a shell to protect it from temperature has an effect on the device clock. In minutes, there is a divergence. S-MAC has additional functions to re-sync the clocks.

What happens when a node B which uses the activity period of Node A as it is one of its neighbour, will need to wake up and send with the transmission radio the packet in the activity period of Node C.
This is the same for Node C if its wants to transmit to Node B.
![[Pasted image 20230404191403.png]]
There may be a mechanism of adaptive duty cycle, where a node will remain active after overhearing an RTS or CTS, keeping the radio on until it finds the end of transmission, in case it is the next hop of a communication.
This adaptability *comes with an higher energy consumption but with a bit better inter-arrival period for messages.*
![[Pasted image 20230414142318.png]]
# B-MAC

The transmitter and receiver are totally different. The sender can send whenever it wants, while the receiver uses:
-   low power listening (LPL) mode to do preamble sampling

The receiver may spot when there is a packet that may be transmitted. The receiver keeps the radio on to get packets when it sees that the transmitter may transmit.

The transmitter will transmit a very long preamble, which allows it to spot the packet to receive at the end of the preamble. The content of the preamble allows it to listen, and at the end, the transmitter will receive the data frame. It makes no sense to listen in the middle of the frame, but the preamble is long enough. The preamble will be so long that the receivers will listen for sure to the packet, having activated the receiver mode. The sleep period is the only parameter of the protocol, and the duration of the sampling is a property of the underlying technology that should be as small as possible to the underlying radio. It may be possible to create a model to discover the smallest sleep period. The idea is to give the transmitter more work rather than the receiver.
The process is as in picture: ![[Pasted image 20230414142709.png]]
- Receiver does Preamble sampling: turn on the radio and listen, having the constraints of the underlying the radio.
-   The radio has an initialization time.
-   When receiving, it uses more current as it activates circuitry rather than in sampling mode.
-   After receiving, the analog signal is transformed into digital, and then the radio sleeps.
In may be seen in the phases what is the cost: ![[Pasted image 20230414142838.png]]
The Radio cycle for Mica-Mote is:
a) sleep 
b) init. Radio on timer interrupt
c) startup: radio initialization and configuration 
d) enters receive mode 
e) radio receives a signal 
f) signal decoding and frame analysis g) radio off again

Turning on the radio takes time and energy, even the initialization and startup it can be seen to take time.

## Modeling lifetime
There are multiple duty cycles to consider, considering the receiver:
$E_{check}$ = duty cycle of checking for samples. = $t_{check}*p_{rx}$
**With $p_{rx}$ = power consumed by reception.**
Then there is a duty cycle for receiving, which must be considered as being:
$E_{rx}=(1/2t_{preamble}+t_{data})*p_{rx}$

Where we define the 1/2 $t_{preamble}$ of time to receive the preamble, as after the check we have to wait until the end of the preamble, but we suppose that after 1/2 of its length time and then we **listen for the data**.


Consider that there is also a cost on the sleep for the radio, so we have also:
$E_{sleep}=t_{sleep}*p_{sleep}$
![[Pasted image 20230414144604.png]]
Consider also the cost to send the preamble and the data, which is just one duty cycle $E_{tx} =(t_{preamble}+t_{data})*p_{tx}$


In order to model the lifetime, we need assumptions on Frequency of transmission and on Frequency of receiving
-   $f_{check}$: frequency of preamble sampling
- $f_{data}$ frequency of transmitted data (in hertz 1/sec)

We can then write two duty cycle for the receiver:

* Duty cycle data: $DC_{rec}=f_{data}*(1/2t_{preamble}+t_{data})$ where the second term is the activity
* Duty cycle check: $DC_{check}=f_{check}*t_{check}$
The frequency represents 1/period.
*The Duty cycle represents activity/period*.
So we have found correctly, by multiplying *the activities and 1/period*, a duty cycle.


To them get **the energy spent in t seconds (in Joule)**
We will multiply by the power in receive mode the DC of reception, and the power in receiving mode with the **duty cyle of checking the sample**.
$ER(t)=t*(p_{rx}*DC_{rec}+p_{rx}*DC_{check}+p_{sleep}*(1-DC_{rec}-DC_{check}))$

We may use ER(1) to get the battery charge which allows us to get the lifetime in seconds.

ER(1): energy consumption in 1 second.

In fact the formula for transmitter and receiver is:
* transmitter: lifetime = battery$_{charge}/ET(1)$
* receiver: lifetime = battery$_{charge}/ER(1)$


## Receiver Site Lifetime

The curves are all similar and show a tradeoff related to the size of the checking interval:

-   Small interval: energy consumption dominated by checking of the sample
-   Large interval: dominated by receiving very long preamble (as you wake up less, so to make sure the preamble time is bigger)
![[Pasted image 20230414150159.png]]
## Transmitter Site Lifetime

-   Frequently sampling: saves in transmission but spends a lot for sampling
-   Longer check: forces the transmitter to send a lot of preamble

The optimal check time for the transmitter and receiver are opposite, so you must decide what to favor. Depending on the number of nodes in the network, we may have different tradeoffs.

Long preamble derails the network, so the throughput of the network is really limited. Depending on the scenario to address, if the transmission rate is very low, B-MAC is okay. **If you need to transmit frequently, then B-MAC may be problematic.**
![[Pasted image 20230414150223.png]]
### How to Reduce B-MAC Preamble? X-MAC

Transmit a preamble and allow the receiver to send an acknowledgement; in that way, the receiver will allow the transmitter to know that the preamble was received. The transmitter will then send the packet directly after an acknowledgement. This solution is called X-MAC.

If there is a long preamble, it may be possible that someone else wanted to transmit, and it may not be possible as the channel was full (carrier sense in a certain sense). Wait before sending our own preamble. If all other nodes, after receiving a message, turn off the radio, one must transmit the whole preamble until they wake up.

It is better for the receiver, after receiving, to keep the radio on just to see if there is something else coming. That is precisely the result of the grey area, to see if there is something else coming.

Considering different transmitter and check intervals with LPL and X-MAC:

-   Blue line with "O" is B-MAC
-   Blue line with "X" is X-MAC
![[Pasted image 20230414150627.png]]
We may see a reduction of the duty cycle. The larger the duty cycle, the tinier the duty cycle. A big check interval, S-MAC is very good, while B-MAC is very bad.

### BoX-MAC

It is an evolution, where rather than having in the preamble just short messages for a node, as I have a message for node 10 and says the message.
In IoT the messages are short, it is different to say I have a message for NodeX, to then transmit it to node X.
So instead of sending the preamble:
* send frame
* wait for ACK

This protocol assumes small data frames being sent. The receiver must wait the next header and then send an ACK to stop the transmission.
![[Pasted image 20230414150806.png]]
It can work also with Multi-hop routing:
![[Pasted image 20230414150848.png]]
This had no success in the practical use. Instead what is being used is the mechanism of **Polling
# Polling

According to the 802.15.4 standard, polling and synchronization are two methods that can be used in wireless sensor networks.

1.  Polling: In this method, a central coordinator node takes on a larger burden, as it is responsible for initiating communication with other nodes in the network. The coordinator node sends a polling message to a specific node or group of nodes, asking them to send data. Once the data is received, the coordinator can then send a message to another node or group of nodes. While this method can be effective for small networks, it can be inefficient for larger networks and consume more energy due to the constant communication with the coordinator.
    
2.  Synchronization: This method involves synchronizing the sleep/wake schedules of nodes in the network. The coordinator sends a synchronization message to all nodes in the network, which sets their clocks to the same time. This allows nodes to sleep and wake up at the same time, reducing the time they spend listening for incoming messages and saving energy. However, this method can also be inefficient for larger networks, as it can require frequent synchronization messages.
    

Overall, the choice of method will depend on the specific requirements of the network and the trade-offs between energy consumption and network efficiency.
[[MPCS/pages/802.15.4]]


# Question 
The radio of a device using BMAC takes 4.0 E-04 seconds to check for the preamble. Assuming that the frequency of the preamble sampling is 5/sec (that is, preamble sampling is performed 5 times in a second). What is the duty cycle of the preamble sampling activity?

* Duty cycle check: $DC_{check}=f_{check}*t_{check}$
* where $f_{check}=1/5$
* where * Duty cycle check: $t_{check}=4.0 E-04=0.0732..sec$
So the Duty cycle of check is:
1/5 * 0.073 = 0.0146.
over the whole period from one check to another (0.2 sec from one sample to another, so 0.2-0.0146 of inactivity seconds).





 <div style='page-break-after: always'></div> 


# Chapter 11: 802.15.4
# ZigBee underlying layer

[[ZigBee standard]]
Oriented towards low-power networks, ZigBee allows the building of multi-hop networks, which is different from Bluetooth, which only allows communication with nearby devices.

Bluetooth Low Energy has a similar energy consumption, but it only supports communication with nearby devices, making it unsuitable for larger networks.

ZigBee is a specification for creating low-power personal area networks that can also support larger networks. It is infrastructure-less, meaning devices can be deployed in a field and they will work.

ZigBee devices are active even in short ranges, which is the range required to communicate with other devices (it doesn't make sense to have a wireless network that only works at long ranges).

ZigBee operates on license-free frequency bands:

-   860 MHz in Europe for 20 kbps
-   2483.5 MHz (2.4 GHz) worldwide, which is the most popular, with a maximum performance of 260 kbps.

## Physical layer

The physical layer provides two main services:

-   Data service: for transmission and reception of PHYSICAP PROTOCOL DATA UNIT (PPDU) through the physical medium
-   Management service: The management service allows devices to obtain the energy level in the channel to detect noise or to detect the carrier signal to determine if someone is transmitting. In ZigBee, you need to associate your network with a *channel that has a* low noise level. Parameters can be used to select the best channel for your network.

In the case of 2.4 GHz, channels are selected, in a way to avoid overlaps. ZigBee supports 11-26 channels of 2.4 GHz.
![[Pasted image 20230414153440.png]]

802.15.4 is designed to operate in non noisy channels. The higher the signal-to-noise ratio (SNR), the better it operates. The lowest SNR implies more noise and higher error rates, while the higher the SNR, the lower the bit error rate. For example, for ZigBee, there is a very low bit error rate for a low SNR.

**Signal to noise ratio higher means that more data can pass, without error made by noise.**
We can see in the graph how an high SNR means really low BER (bit error rate):
![[Pasted image 20230414153649.png]]
## Energy detection
There is the function of energy detection in the physical layer of ZigBee. This part is used to find a free channel and for carrier sense to find if someone else speaks in the channel. Also the estimation time for Energy Detection is equal to sending an average of an 8 symbols interval. The detection threshold is at 10 dB above the sensitivity level. The Energy result is given in byte. 

## Link Quality Indicator
This metric is used in multi-hop routing. 
The Link Quality Indicator (LQI) indicates the quality of the data packers received by a nodes. It is assessed each time a packet is received and it must have 8 different levels. *It is based on Energy Detection or SNR or both*

*The estimated value is then forwarded to the network and application layers*
## Channel Assessment
**The channel assessment function, checks if the channel is busy**
It has three modes:
* Mode 1: uses ED, finding a channel busy if the energy level exceeds *the detection threshold*
* Mode 2: Carrier Sense: finds that the channel is busy *if the detected signal has the same characteristics as the sender*
* Mode 3: combines the modes in an AND or an OR
## Data Services
In the Physical layer, a PPDU message will report on the above layer if a transmission was a success or a fail

The reason for failure may be:
* radio trans receiver is out of order (old packet or missing packet)
* radio trans-receiver is in receiver mode
* radio transceiver is busy


## Frame
The initial part of a ZigBee transmission includes:
-   Preamble: A special encoding is transmitted to allow the receiver to synchronize with the rest of the transmission. This synchronization continues until the end of the transmission.
-   SFD (start of frame delimiter): Tells the receiver when the real data will start.

The header includes the frame length which is 7 bits, meaning 128 bytes of payload. Not all bytes need to be used, as it is better to transmit short frames to reduce problems with carrier sense and collisions.
![[Pasted image 20230414154628.png]]
The frame length is encoded in 7 bits, and we have a payload of max 127 bytes.
# MAC Layer

Above the Physical Layer
-   Data Service: transmission and reception of MAC frames (MPDU) across the physical layer.
-   Management Service: For example, assigning transmission slots for transmissions that require synchronization and association and disassociation of devices.

## Device Types

There are two types of devices corresponding to the roles they play in the network:

-   FFD (Full-Function Device): A device that implements the full MAC protocol.
-   RFD (Reduced-Function Device): A device that implements only the mandatory part of the protocol.

These two device types are mapped to the [[ZigBee]] specification, with RFDs serving as end devices and coordinators and routers serving as FFDs. In some specific cases, such as in a star network, an RFD may be used at the MAC layer.

## MAC Layer Topologies

There are two main topologies in the MAC layer:
-   Star
-   Mesh/Peer-to-Peer

In ZigBee, all three topologies can be mapped to peer-to-peer because devices in the MAC layer only see their neighbors.

### Star Topology

In the star topology, we have an FFD at the center, which acts as the coordinator. From the 15.4 standard onwards, all devices are seen as behaving as reduced-function devices, even if routers are FFDs. In a star topology, a router will act as an FFD as its additional functionalities will not be used.

### Mesh/Peer-to-Peer Topology

In the case of the P2P topology, which supports the mesh and peer topologies of ZigBee, coordinators and routers are all full-function devices, while RFDs serve as endpoints.

## Type of frame
* Beacon frame
* Data frame
* Acknowledgement frame
* Command frame (MAC)
# Channel Access

The channel access can be done:
* with super-frame: used in star topologies or peer to peer organized in threes, it enforce synchronization of devices enabling power savings.
* without super-frame: here there cannot be coordination, so the energy efficiency optimizations cannot be done.

Channel access is implemented by means of a coordinator in a star topology. The coordinator will emit beacons, which define its activity period. If beacons are used, then a super frame structure is defined.

In 802.15.4, mechanisms are used to implement energy efficiency. The coordinator has a duty cycle of the radio, with a period where the coordinator is active. In the rest of the time, the radio will be off. The coordinator uses a period to state when the activity period will start. All the nodes can then be initialized in the star topology.

The network may operate without a superframe structure, which may save energy. In the past, it was used, and above the MAC layer, one could decide when to turn on or off the radio.

The super-frame structure has two parts: the activity period and the inactive period. Data is transmitted in the active period in one slot. The first part is transmitted by the coordinator, which states the network identifier, activity period start, length, and all parameters of the network.

To discover an existing network, you set up a radio on the channel and await the beacon. If no beacon is received, the channel s considered idle, and the device can set up its network.

![[Pasted image 20230618110055.png]]
**The beacon frames are send by coordinator in a star topology**

![[Pasted image 20230414155710.png]]
The active period is divided to up to 16 slots, in the example 14. Those slots are used:
* to communicate with the coordinator
* or from the coordinator to send a frame to a device

In the inactive period the devices can sleep. All the other node in the network must obey to the request of the coordinator to send messages.
## Contention or Contention free

Some slots may be reserved for some devices. In this way for a specific device the slots are guaranteed.
The active periods may be divided in:
![[Pasted image 20230414162516.png]]
* CAP(Contention Access Period): It is mandatory that at least one contention slots and must be available, as it is used *for the maintenance of the network*. A join requires the use of a contention slot also, so it is needed for that. All other may be the guaranteed time slots. There are at most 15 CAP slots. Any contention-based transaction must be completed before sending the Contention Free Period..
* Contention Free Period: means fixed for some devices, this is **for devices that require to be activated at a given time, which is fixed**. All device will know about those guaranteed time slots, and only authorized application will talk. In this case CSMA/CA may be not used, as all other device will be silent. Within the same slot of GTS (guaranteed time slot), there is the time to receive acknowledgement. A device that transmits in a GTS should finish its transmission within it.
If an application misses the GTS guarantee, then one must wait for the **next super-frame**.

*In a multi-hop path, one must ask to its own router, but it is unclear how it works*. The contention free slots are mostly thought about in start networks.
### CAP backoff
The end-devices will use CSMA-CA protocol
1)  at first they wait a random number of slots (so that they luckily do not rush together to occupy the same slot) 
2) if it is busy, they wait another random number of slots before trying again
3) if they find the channel idle, they can transmit and they do, **they will keep the medium until the end of the frame after gaining access, noting that they can transmit only on that slot** (they need to go to step 1 again at next slot). 


## Channel access with superframe (beacon enabled)
The coordinator of the PAN creates its own *superframe*.
The characteristics of channel access with superframe are:
* the active period of the superframes are always of the same length.
* it is the coordinator that *initiates* the superframe, composed of the Beacon frame and the frames sent in the CAP and CFP (which we see above).
### Channel access with superframe in P2P topologies
**Routers will synchronize with neighbours in a p2p network, by using the superframe emitted by the coordinator of their PAN.**


## Channel Access without Super-frame (non Beacon enabled)

The network is without instructions, so there are no slots. The communication is based on unslotted CSMA-CA protocol, so there are no slots like in CAP (which used CSMA-CA too).
*This PAN, where the coordinator decides not to use the super-frame structure* is called **non** beacon enabled.

This means that *the coordinator/router (referred both as coordinators) must be on anytime*, the RFD can *stay off and wake up only when they want to send something.*
The coordinators will stay active to receive data from end-devices.
Also the Coordinator and Router have a more complex protocol to message with a RFD, as they can be inactive.

### Poll-based data transfer in non Beacon enabled channels

The data transfer without superframes is poll-based. A device will periodically wake up and poll the coordinator for any pending message for which it is the destination.
The coordinator (router or PAN coordinator) can send two type of responses:
* the pending message
* a signal that no message is pending

# Data Transfer Modes
There are three types:
1) End-device to coordinator (PAN coordinator or router)
2) Coordinator(PAN coordinator or router) to end-device
3) Peer to peer (end device to end device may be possible, besides coordinators communication)

* star topology: uses only types 1 and 2, **because the data transfer can only happen between PAN coordinator and the other devices, as the PAN coordinator is at the center of the network**
* peer to peer topology (tree or mesh): all three type of data transfer mode may be possible, as data can be exchanged by any pair of devices

There are different implementation on Beacon enabled and non beacon enabled networks.

## Data Transfer in BEACON ENABLED NETWORKS

In this case there is a difference of the interaction in a  star topology or in a peer to peer (mesh and tree) topology, as we will see.
### From end device to coordinator (in star topologies)
In Beacon Enabled Networks, there may be problem when communicating from an end device to a router, as the end device needs:
* to own a GTS and be able to use it without contention to talk with the coordinator
* if it does not own a GTS to transmit the data frame to the coordinator by acquiring a CAP slot, during the CAP period **using the CSMA-CA protocol.**
We may see below how the Device listens to the beacon, then it the active period it sends Data to the coordinator,  optionally the Coordinator may send an ACK.


![[Pasted image 20230703175315.png]]
### From coordinator to end device (In star topologies):
We may see below the interactions of PAN Coordinator and Device.

![[Pasted image 20230703175333.png]]
	

1) A flag in a list on the Beacon, will state if a *pending message is available from a device in the Coordinator*.
2) the device wakes up to listen to the beacon. If the end device sleeps when there is the beacon frame, the coordinator will continue to advertise the available data.
3) In a free slot (Contention Access Period, accessed with CSMA-CA), the end device will send a Data request message to the coordinator. The request is *immediately acknowledged by the coordinator after receiving the the request*.
4) In a successive free slot (CAP), the coordinator sends the pending message data. 
5) The device will then send an ACK **on another slot!**.  The ACK is necessary in all those case, to allow reconfigurations internal.
6) the coordinator upon receival will in fact change its internal configuration by removing from the list of pending messages the pending message.



### P2P (tree and router) data transfer in BEACON ENABLED NETWORKS

In this case :
* coordinator devices (PAN coordinator or routers) will communicate with end devices **using the star topology interaction schema**
* end to end devices **will not be able to communicate directly and must forward their message to a coordinator (router or PAN coordinator)**, recursively reducing to the previous case


#### Coordinators communication

We have multiple Routers or the PAN coordinator which are are not synchronized, as they would collide. When one router wants to transmit to another router, it must find a *free contention slot in the other router activity period*. ****
**How to do this synchronization is beyond the scope of IEEE 802.15.4 standard, but must be defined by the programmer**
![[Pasted image 20230414164919.png]]


## Data transfer in NON BEACON ENABLED NETWORKS
Even in this case there is a distinction between star topologies and p2p
### From end device to coordinator (In Star topologies)
1) The communication from any device to the PAN coordinator is done by having the end device check with CSMA-CA that the link is idle, so "unslotted"
2) The device sends the data in the unslotted CSMA-CA. As a consequence  **the coordinator must always be active to receive the data**
3) the coordinator may send an optional ACK


![[Pasted image 20230703182808.png]]

### From coordinator to end device (in star topologies):
(In this case the coordinator considered is also a router, besides the PAN coordinator).

optional acknowledgement or the ACK if they are request.
There are no beacons advertising the pending messages to the device, the device must do polling to find if there are messages pending with it as destination

1) In this case, at any time, depending on CSMA/CA free slot the device sends a Data Request to the Coordinator
2) then the coordinator sends an ack (but not a response with data or empty)
3) the coordinator **transmits the data or an empty message if no message pending**
4) the device sends an obligatory ack
5) the coordinator discards the message
* .![[Pasted image 20230414165230.png]]


### P2P (tree and router) data transfer in NON BEACON ENABLED NETWORKS

In this case :
* all devices may communicate with every other device in their transmission range (using CSMA-CA to get an unslotted slot)
	* **but to do so all devices must be always active or be synchronized**
		* synchronization in this case too goes beyond the standard 802.15.4 and **it is said that is left to the upper layers!**

Question (missing in the published slides):
1) beacon (from coordinator)
2) data request (from end device)
3) ack (from coordinator): **immediately sent from coordinator**, allowing to state that it will sent in the next activity slot
4) data (from coordinator): sent in a free slot of the activity period during the CAP
5) ack (from end device): **immediately send from end device** from there the coordinator can now discard the data

# MAC Layer Services
The primitives to communicate with the Network layer from the  MAC layer are the same as [[ZigBee standard]]:
![[Pasted image 20230703184403.png]]

## MAC Layer: Data Service

It uses the primitives request, confirm and indication.
Where:
* Data.request: is invoked by the Network layer above with the objective to send a message to another device
* Data.confirm: reports the result (returns a success or an error code) of the transmission to the Network layer, it is send after a DATA.request and the attempt of data transmission
* Data.indication: it is a *receive* primitive, basically its generated by the MAC layer when receiving a message from the physical layer that came from another device, it allows to pass the message to the network layer


We may see here the exchange:
![[Pasted image 20230703184811.png]]

The Data confirm:
* instantly if there is no ACK to wait
* after ACK if it is optionally inserted.
In the latter case the originator device may wait a lot as to send a one must find a free slot (from a beacon or a CSMA-CA free slot), then also the receiver must find a free slot, which must be got by a beacon frame that may be awaited (in the next period), then only after this process the MAC layer sends a Data confirm.

The receive here is seen as a DATA.indication, the data goes up with *different possible implementations, not specified here*.

## MAC management service

The MAC layer services are offered to the above levels, to create a PAN and start transmitting beacons.
*Also it must provide the detection of existing PAN, with device association and disassociation of devices to an existing network.*
There may also be other services.
For completeness we may see Management services offered by the MAC layer and see that some may have or not additional primitives included, with a distinction from RFD and FFD.
![[Pasted image 20230703190326.png]]

In some case, the Indication and or Request may be optional or not.
For example ASSOCIATE, indication and response are optional, this is because there are two ways to connect on an existing network:
1) own will from a device: in this case ASSOCIATE needs to have Request, Indication, Response and Confirm for a FFD, because a FFD may receive a request actually, while there is no need for **request in RFD**, neither there is an Indication for RFD (as there just needs to be a confirm, no one will ask for an associate to an end device).
2) force a device, from coordinator to join an existing network here there needs to be an indication and response in the RFD to communicate the request from the coordinator to join with an indication to the upper layer and the response to the coordinator



Other  examples here:
* BEACON-NOTIFY: a service from MAC layer to advertise that it has received a beacon to **upper layer**.
* GTS: it is an optional service, to request a guaranteed contention slot.
* START: optional sued only by coordinator, to say that they start a PAN, it can be done to do service discovery.

# Associate Protocol
Protocol by an end device willing to join a network.

ASSOCIATE must specify channel it wish to connect and other parameters.
The MAC Address of the end device is the only one to communicate, as it is not on the network yet.

The association request is sent during the CAP, using a slotted CSMA-CA protocol.

The ack of the coordinator does not imply confirmation of the request.

On the joining device
![[Pasted image 20230414171015.png]]

When knowing the PAN adress. The MAC layer of the coordinator will receive a Associate.request.
![[Pasted image 20230414171116.png]]

Note that before sending ASSOCIATE request: MAC layer awaits a beacon, to get a free contention slots, the Coordinator MAC sends instantly a ACK after.
Meanwhile the MAC layer of the coordinator, sends an ASSOCIATE.Indication, the NWK chooses a Network address for the device.
From a indication to response, it takes time.
If it is a *router rather than a coordinator, than the response can be faster, without waiting for the coordinator*.


**The MAC layer, cannot answer directly the response of the associate request**.
We may even be in the inactive part of the network after the NWK layer computes what it did.
It makes a pending frame to respond,.

The MAC layer of the originator device, knowing the estimated time of the computation. **It waits a predefined period of time, define by the standard to take into account the time of a coordinator to produce a response, after such time a data request to end the pending frame to it**.
The request is immediately ACK.
Then the MAC layer of the Coordinator will send on a free contention slot the frame.
The ACK is received instantly from device.
**This ACK is important, as from there a COMM_STATUS.indication is forwarded from MAC to NWK layer, which must be used to say that the bind of address and device is successful**.
COMM_STATUS is a way to extend the type of requests, when REQUEST, INDICATION , RESPONSE were already used with a function, as happened with ASSOCIATE.

From there the [[ZigBee standard]] address map, from MAC addr to IP addr ill be updated.


 <div style='page-break-after: always'></div> 


# Chapter 12: Embedded Systems and Case study of Arduino

An embedded device is a computer designed specifically for one function, that is why it is designed specifically for IoT. An embedded device is different than general purpose device, as they have a specific purpose, with one specific function, e.g. sampling for environment, means to specify a particular Duty Cycle.

The design of hardware and software here is in conjunction. Your choices on HW impact on SW, on SW impact on HW. The decision on transducer may impact SW and vice-versa.

For example a light software with very good transducer can be done, or vice-versa a cheap transducer but with software layer you can make it just as good. **So we talk about hardware and software co-design**.


Microcontrollers are microprocessors with the management of input-output.
Arduino are configured with:
* ports connected with a microprocessor
Ports can be for in and out.

Sometimes manufacturer take a microprocessor and update it to make a microcontroller, so optimize and design it to interface with the physical world. Usually microcontrollers implement functionalities over real-time systems. Usually embedded systems are real-time systems.

Some embedded device may be implemented with ASIC, or other may be with System on a Chip (very generic term actually).
So they are two different categories. 


## Programming an embedded device

Doing so, has different constraints and requirements from a general purpose computer system.
One nowadays may rely on powerful microprocessors and systems.
In microprocessor one must keep under control all the resources. Some things to face are: how to deal program memory, to fit the memory on embedded device.

What happens is that the ***programs are written on a fixed memory, rather than ram memory***. When turning on an embedded device, it loads the program and starts what it is supposed to do. The program memory is up to 15KB in an Arduino.
The footprint of code + libraries should fit that amount in general purpose computer on does not care.
**When programming to ARDUINO, the compiler tells you what is the code size, because there it becomes  a problem**.

On Arduino the user interface become led or maybe LCD tiny display, so there are difficulties in debugging.

There usually are not file systems on flash memory (disk equivalent) or RAM. *The file system if it fits may be on a program memory, so also for OS*.
If one takes space of OS, the program memory is reduced.
Usually OS there are **libraries, with a set of functions**.

There may be some version of OS, with real time features, or have embedded versions of powerful OS, for powerful embedded devices.

**Without an OS, then one must compile on a workstation( a PC) and upload the code, libraries and the initial configuration of the device, such as MAC addr or NWK addr**.

*Feedback on execution*: it cannot be controlled, besides on *led* or tiny display, or radio message, or serial line messages.

**Response time, in embedded device, must be controlled**.
Not only the functionality but the timing must be implemented correctly, and it is difficult to test it. For example Failing to give information in time, may fail the **non functional requirement of time***.

Another challenge is also on reliability, which means that a programs should not fail for years. Improper management of memory cannot be afforded in embedded devices.

**Power management is also critical in this case.**
Arduino: an IDE which provides the run time support, that is basically the OS of Arduino platform.
TinyOS: first one OS for wireless sensor network (used only for research).


## Executable

The language code produced, will be linked by the platform libraries, along with constants needed and parameters defined in term of constraints of the device code. 

To provide ZigBee, one buys from manufacturer device, which also gives: 
* libraries
* environment
One writes *application objects code*, then it is linked with those provided, and configures the device (to say if it is coordinator or RFD).
Then all this is used to produce an executable, to upload on a device.
*Parameters will change for all device programmed (e.g. MAC address). The part of compiling can be done once, the assignment of parameters is done at uploading time, allowing to differentiate the parameters.*

Usually those low level device are programmed in C, as C code is very efficient and allows to program easily registers.

To program code in C, we usually code the main function, the first one executed when running the code usually, **here no, the programming environment provides the main function, we may think as if the OS provides the main**. The purpouse of the main is to initialise the embedded device, which writes a function defining the business logic of the device at runtime.

The main basically us not seen to us, but is there and it represent the piece of software booting the the embedded device. 
This is because those device have all the same initialization, so it is useless to make the programmer program there. In this case for those low end device, the run time support basically corresponds for the O.S.


Led or display are a form of actuators, you may also store on flash storage data, and may receive data. There there is a wait time to *sample again the next time the sensors*.
To make sense of the sensors data, we must sample at regular intervals.




## Interaction with HW on PC

While in PC, the OS abstracts the interaction with the HW, so sends at low level commands to the HW and receive communication when the instructions are executed. 

Commands in this case are a set to instruct the HW, they are aggregated for the more complicated one. 

There are interrupts send by the HW when operations are completed. 
There is the need to wait, before the HW op is completed. 
With threads, the function may request the OS to suspend a thread, keeping in a data structure (e.g. stack or processor and thread descriptor) the the thread state, so that the microprocessor may do what it wants.
The interrupt is detected by OS, allowing to resume the state of a thread to execute again. From the point of view of the thread, it never stopped and is transparent.

*All of this has a cost*:
* memory requirements to freeze the state and space on the stack to keep the thread state
## Interaction with HW on Device

Considering that you have 1KB of memory, where you need the memory for the stack.
In Arduino, you have only one thread.
When there is a wait, the thread is stopped and freeze, until the hardware finishes its job.

*Arduino has also an advanced mechanism, to use interrupts manually.*

The first solution is the:
* Arduino event loop
The second:
* event-based programming

**Delay**: if you need to wait, you have an active delay, without stopping the processor, to wait for something.

The flow:
* init: main of the runtime support + programmer configurations
* Main loop: control loop directly after init. It allows to send command on the HW, with invocation on the library of the runtime support. Send the command at low level to the hardware and freeze
* Main loop: wait until command has been completed, and then the return will **activate again the main loop**.  The delay is a command sent to the HW
* active wait for the processor
* Main loop: wake up from the delay

In Arduino, communication was not thought about at the initial design.
We have that communication is really asynchronous, so there was not effort as it was not thought to put support on it.
As time passed, the environment evolved to provide support for communication.

# TinyOS
It raises an event, which is an interrupt, managed asynchronously by an interrupt handler. 
We program handler and link them to the program to intercept, and the OS will automatically run the handler when an interrupt is intercepted.

**Consider that the system is not responding to other interrupts, and as such we turn them off when executing the code of an interrupt, or on other O.S. there must be taken care carefully, the first way is the easiest**. When managing the interrupts, the data structures are on the O.S. The values are temporally consistent when managing the interrupt, when another interrupt arrives, there will basically be a race condition within an operative system, by disabling interrupts and managing the concurrency in them.
That solution is also a good idea with scarce resource, but it means to execute all other interrupts are in a queue.
*So the program handler should be tiny and not do much*. Really long operations means to lose the ability of having asynchronous communications.


We may define tasks that are non-preemtable: if posting two tasks, they will execute in sequence one after the other.
When an interrupt is received during the execution of tasks, they have a *higher priority than tasks*.
**The tasks will be preempted when an interrupt arrives, but in general a task does not share state with another task, but the minimum overhead we have is this interrupt management**


# TinyOS flow
 
* init: set a timer, and wait until woken up by *interrupt*
* sleep until interrupt of the timer
* Timer handler: it sends a commands to start a transducer. Note that you must wait to the transducer completion, as it will not do it instantly. Right after sending the command Start read, you may not expect to have immediately the result, the device is frozen.
* Read handler: when the HW completes an operation, it sends an interrunpt, which is the event Read done. This other handler is linked to another event handler than the read handler. You have the value read for the sensor, but you cannot process it to the read handler as it should be fast. **What we must do is to post a task, which is postponed to a task that will be executed later and not in the event handler at OS level**. After that the Read handler must *set a new timer* to wake *up when the next read operation* must be performed. After this the read handler returns to the O.S
* Task execution: when there is nothing else to do, the O.S will execute the task. If after computing, there is the need to send. The task will send a command Send data, to send it. Send cannot be executed immediately, so the O.S. returns control to the task, accepting the task asynchronously, without completing it. Once you send something, you cannot expect that it has been already sent. Return to O.S without anything to do.

![[Pasted image 20230827103534.png]]

At this point you have:
* read by sensors
* send by radio interface*
Those will be executed with handlers as before.
We see that for example an upcall after the Start read command is done. And there may be the arrival in the middle of Send done upcall from HW to a Send Handler, then the Read done in the meantime to the Read handler.

What misses there is not having high level handlers but they are part of the interrupt handler.
When the HW raises up an interrupt, the O.S. will start executing an interrupt handler.
Then an invocation, is done at application layer to the event handler, which will return then to the Interrupt Handler the control when done.

One must be careful on the Interrupt Handler commands, as for example in the event handler one invokes a command: **the command operates at the OS level, if it uses the same data structure of the Interrupt handler, it will mess up the data structure.**
So the application runs at OS privilege, using OS commands, even if we code it.
For example, if the interrupt comes from the radio, it is not sensible to send set up in the command another radio instruction, or it may be messed up.

That is why, the task are posted, so that a task, will *safely send a command that will be executed by OS, as the Interrupt handler has finished.*

# Arduino interrupts
We can implement with libraries the interrupt.
We have a control loop to implement tasks.

## Arduino

Open Source Hardware example, as of today it is even using on business. 
Arduino concept will comprise three elements:
* Device
* IDE
* Forum: with examples, projects and documentation

Arduino cannot come with more than 32KB program, as it has 32KB flash memory.

With power 5 voltage of circuitry, and we have an analog to digital converter.
1 bit = 5V/224 .

The digital pin are 5V or 0 mapping the signal.
The pin may be used to connect an actuator. By giving current to a led we start it.
*Basically the digital pin can be used in input and output*, the analog cannot be used for output.
We may have complex controls in output over digital pins actually, this is implemented by the runtime support.
Two pins may be used to produce external interrupts.
Connect and use it .

Decide the port from which you are compiling and then connect the port to program and compile the program and load it in the flash memory.

That analog signal is transformed from 0 to 1023, operating at 10 bits.
While digital signal is 0 or 1.

The code that we have to write is:
* setup: called by the main, when initialising the device at boot
* loop: after the init is complete*

Not one must connect the code, but for example having a system with buttons.
We must match the button id and the pins with the led.
The serial line has several different speeds, and if they do not match, you will not read anything.
The pin number will be used in input or output with a function that specifies it at setup.

In the loop. You want to read the state of the button, connected to a digital pin, so a **digitalRead function is the one that we have to implement**.



With the function digital write, which means to put current onto a pin, we provide an **HIGH value, so provide the current**.
With LOW current, we turn off the led.


With `analogRead` we read a signal of an analog input, and we transform it into a 10 bit number that can be stored into an int. 
We can determine the pin voltage.
If the electronics are powered with 5V. Any step of increase is 5V/1023 because we suppose that **level 0 is 0**.

With `Serial.println()` we may print on IDE, note that we ma use it also to send on wireless device if it is connected.

# Interrupts 
Arduino offers an interface to interrupts, allowing to manage external interrupts to the runtime support. Two type of interrupts may be managed by runtime support.

* External: interrupt managed by Arduino, which are interrupt connected to pins, those pins are implementing an external interrupt lines

Timer: it is an abstraction of a timer, where we ask the Runtime for us to manage the time for use

The external device will actually be external basically, we can sleep for real rather than have the kind of delay wait which is active.

With `attacInterrupt` we can declare an interrupt.

We can give a mode to the Interrupt, defining:
* the signal to take a decision on what to do, so depending on how its raising signals to invoke the function

Suppose to attach an interrupt handler to INT0: if it raise **then active an interrupt, if it falls do not activate it**
Or we may say HIGH or LOW, in this case you must be careful as if the signal remains stable, then it will send interrupt at really fast.

Normal buttons have a state, while some push button emit a signal and turnoff again,a  mode low or high makes sense only for signals.

The interrupt is very fast in very low level instructions.

To control a led according to the interrupt of low level circuitry


# Breadboard

Those board may allow to prototype circuitry. Those boards can have on time cables. There are + and -.

Connecting the - signal of Arduino to the -, then all the - dots are connected in a row all together. 
Same form +.

The rest of the breadboard, the holes are connected in columns and disconnected by all others.
This allows to connect components, to make them connect automatically. The connections that cannot be done in this way, can be connected with wires.

If the current goes from + to - and gives current to a line. When pressing a button, which is connected to a line, from this line it goes back with the resister to the negative pool and returns to the negative pole of Arduino.
The resistor is needed to not burn arduino.

The signal of the press, may go also to pin 2. So that when pressing the button, the microcontroller finds the pit 2 power.

So the power pin, gives the power to the button, than can send it in a column up to the digital pin input 2..

On pin output 7,  connected to resistor with led and . connected to negative line,
By writing on 7 we can implement a digital write with a **high value to turn on the led**.
The pressing of the button is an interrupt on pin 2.


What the loop does is, just to turn off again the LED.


The interrupt only, happening asynchronously while executing the loop, will run the rising of the counter of the loop and turning it on.

Printing is not a good idea but it does it.


**Race condition**: there is a potential race condition on the variable count, it may be a chance that while reading count,  on the loop, we may write with the interrupt on count.

**in a certain sense we can prevent the interrupts when receiving them**.
In C we have registers and we overwrite the memory. The compiler may be optimized and is more efficient in read only once from memory and then read only from register. You may even have the idea of locating in the register directly and not in memory.
If the variable is in a register, when the interrupt arrive, all the registers are stored on the stack to manage the interrupt.
At this point the interrupt handler:
* read the variable count on memory
But after the interrupt handler finishes, the main loop should be restored, so the microcontrollers will take from the stack the registers, with the old value of the variable count. 

**By declaring volatile, we force the compiler to keep the variable count in memory at any time, so not on cache, consequently an interrupt does not create a problem.**
The variables in the control loop and the interrupts are generally made volatile (so greenLed too).

The interrupt handler should be void and be without parameters, for a precise reason.
It is not for security and race conditions.
It takes no parameters as:
* you do not know when this procedure will be called
* also there are no parameters associated to an interrupt, as it is made by a pin
So there is no parameter, as there is no input parameter, and there is no input parameter for the invocation.
Since no invocation, the output of the function cannot be received.
The handlers are executed with disabled interrupts, to have protection against race conditions, so they have no interrupts, as such keep it short.
During the interrupt handler the clock is stopped and the time is freeze.
*You cannot put a delay in the handler, as you are waken up with a delay by an interrupt, so in theory it should not work as you do not receive the wake up interrupt*.


`millis()` is not incremented during interrupt.
Count is declared as volatile as told before.

We may also stop receiving interrupts with:
* detachInterrupt
* interrupts():enables all interrupts
* noInterrupts(): disables all interrupts, for example when dealing with main loop parameters on the main loop. By default true when entering an handler.

## Energy Management in Arduino

In Arduino, even when delaying and waiting the microcontroller is frozen but it is is powered state.
The microcontroller is Arduino supports actually different states. Consider that Arduino is a platform, different implementation with different microcontrollers may have different states.
Refer to microcontroller documentation to get the states.


There is a low power library, which provides the calls to implement low powered states for the micro controllers.
Different microcontroller may be responding different to the library.

INTO -> mapped to PIN 2
INT1 -> mapped to PIN3 
in the board of Arduino.
That is why  the 0 in the registration of interrupt from pin 2 is 0 in the code.


## SLEEP MODES IN ATMEGA328P ARDUINO

In Idle mode: you stop the CPU, the SPI part of the microcontroller stays on for interrupts) It turns off the clock of the microcontroller CPU and the flash. The external components interrupts and internal interrupt are still activated.

ADC Noise Reduction Mode: it allows to stop the CPU but the ADC is on, allowing to have less noise to convert analog to digital

Power-down Mode: stop the clock and allows only operation from asynchronous modules. It can wake up with hard reset and other serial interface and special type of interrupt. **You can wake up with the timer***

Power-Save: turns off the timer too.

# Using idle mode: low power
* use the library with: `#include "LowPower.h"`
Check carefully the microcontroller, as it may not implement the call of the library, such as:
`LowPower.idle(SLEEP_8S, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_OFF, TWI_OFF);`

The first parameter is important as it: *states how much to sleep.*
After the time, it generates an interrupt and the microcontroller is turned on automatically.

For the parts of the microcontroller, you may decide the components to put on or off.
ADC_OFF / ADC_ONTIMER0_OFF/ TIMER0_ON

### Power Down:

Brown out detector: monitor to detect that you are burning something.

``#include "LowPower.h" //Note: no setup is required`

You have a small number of parameters as it powers down other components.


`LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);``

With `powerDOWN(SLEEP_FOREVER....)` you will not be waken up by the clock.
There may be an handler that *catches an interrupt and wakes up the device*.

 <div style='page-break-after: always'></div> 


# Chapter 13: Energy Harvesting IoT
Recharging or throwing away a device when the battery is out is costly. Energy Harvesting allows us to recharge the batteries and avoid such situations as much as possible.

In [[IoT Design Aspects]], we try to reduce the energy use at the microcontroller, sampling, and radio level. We can also consider using larger batteries with bigger capacity or rely on very low-powered devices.

In addition to reducing energy use, we can also use Multiple Access with Collision Avoidance (MACA) [[MACA Protocol]] protocols. These protocols help to reduce the energy consumption of devices by avoiding collisions and idle listening.

By implementing these design strategies, we can extend the battery life of IoT devices and reduce the need for frequent recharging or battery replacements. This, in turn, can help to reduce the cost of IoT maintenance and improve the overall sustainability of IoT systems.

### Hardware and software energy management

When it comes to managing energy for electronic devices, decisions need to be made for both hardware and software. Hardware decisions are typically made at the beginning of the device's design and cannot be changed easily. On the other hand, software energy management is more flexible and can adjust the device's behavior based on its energy consumption.

#### Duty Cycle Principle
The duty cycle principle is a common approach for managing energy in electronic devices. This principle involves trading lifetime with performance by slowing down the device. However, there is a limit to how much a device can be slowed down before it is no longer meeting its requirements. The speed of the device can be adjusted based on how long it needs to last on a battery.

## Energy Harvesting
Another approach to manage energy is through energy harvesting, which involves converting energy from various sources into power. The amount of energy that can be collected depending on the energy source, which may be periodic, intermittent, or unpredictable. Energy harvesting allows for more possibilities in device design, but it also makes the design process more complex.

The physical source from which we extract energy is called the **energy source**. Examples include solar energy, vibrations from the earth or the human body.

The component that extracts energy from the energy source and transforms it into electrical energy is called the **harvesting source**. This can be anything that extracts energy from the environment, such as solar panels or wind turbines.

### Modulating Load with Duty Cycle
The amount of energy that can be taken from the environment is variable over time, and the load (instantaneous power that the device consumes) is also not constant. The only element that can be controlled in energy harvesting is the load. By modulating the device's duty cycle, the load can be adapted to match the energy production.

### Adapt the load method
The key to successful energy harvesting is matching the load with the production and controlling it. One approach is to keep the device on when there is enough energy being produced and turn it off when there is not enough. This allows for the collection of excess energy during times of overproduction.

In some cases, an energy harvester can be connected directly to the source without a battery. However, abrupt power loss can cause issues with consistent operation. To address this, energy can be stored during times of overproduction to resume operation later without issue.

##### Challenges without battery
There are challenges to energy harvesting, particularly when the amount of energy being produced is minimal. In these cases, it may be difficult to switch the device on and off without affecting its operation.

$P_s(t)$ --> power produced by harvester from source S. 
$P_c(t)$ --> power consumed by the load at any time t.

We have lines representing both. The device is operative if the power produced is above the consume and we do not have a buffer then we lose the charge. On the other hand if we go below $P_c$, we will lose the device as it goes off until the S increases.

![[Pasted image 20230426192241.png]]

### Energy buffer method

![[Pasted image 20230508153219.png]]
We may have a device that takes the power from battery or the source. and **the energy harvester giving energy to buffer.**

If going below $P_c$ with the energy coming from $P_s$, the device may still be operative, in principle, in practise it is not like this as there are energy constraints on the battery. There are technological constraints on the energy buffer, as we may not have device that can store and inline amount of energy, beyond that they cannot be charged so there is a waste.
Also real battery leak energy over time and they lack charge just idling.

Producing 10 energy, you do not charge **10, the charging efficiency eta $\eta$ can be 1, but usually it is not and we lose some charge**.

#### Ideal buffer
In an ideal buffer we don't have any lack of energy in charging and all the energy harvested is used to recharge the battery so hasn't a capacity limit. In any time interval we need the relation:
	* left: amount of energy consumed (load), that the device consumed on time T : $\int_0^T P_c(t)dt$ 
	* right the energy produced from time 0 to time T. The multiplication of power by time is a measure of energy. The amount of energy taken from the source, the instantaneous power * time + $B_O$ the battery level at the start. Which is $\int_0^TP_s(t)dt+B_0$ $\forall t\in(0,\infty]$
If right > left: then the device will be operational.

#### Non-ideal buffer
In this real model we have leaks of energy, limited storage capacity, limited power capacity.
* *$B_{max}$= maximum battery capacity (energy buffer size)
* *$B_t$: battery charge at time t
* *$P_{leak}(t)$ the leakage power of battery at time t
* $\eta$<1 the charging efficiency
* $P_s$(t): power harvested at time *t
* $P_c(t)$: load at time *t
* $B_0$: initial charge of the buffer

We have more power than the consumed one, on the left. The excess is represented by the dashed blue line, which is the excess energy available from the device. We can estimate this excess energy using the upper integral.

We use the rectified function to nullify the differences $x^+$.
$$x^+=
\begin{cases}
      x \hspace{0.5cm} x>0 \\
      0 \hspace{0.5cm} x\leq 0
    \end{cases}\
    $$
    
In the integral, we consider the difference between the power produced and consumed, and multiply it by the amount of time for which this holds when it is above 0. **This represents the amount of energy produced that goes into the battery**.

Given the graph:
![[Pasted image 20230426223832.png]]
-  If the instantaneous power produced is below the instantaneous power that we are consuming, that means there is more consumption than production. There is insufficient power and we draw from the buffer.
- We consider the integral, only taking into account power consumed - produced when it's > 0, and the time during which this is true.

We create a model based on the instantaneous battery charge $B_t$:

$B_T$ = what you put in up until time T - what you take out - leak up until time T  $$=B_0 + \eta\int_0^T[P_s(t)-P_c(t)]^+dt -\int_0^TP_{leak}(t)dt\geq0$$
* first integral: energy produced in excess and that go to the buffer
* second integral: energy consumed from the buffer

#### Model with No Charge Limit

What you put in excess = production - consumption = excess in the period

**We have to multiply the excess by Eta to account for the battery efficiency**

We assume that taking energy from the battery has 100% efficiency, so we do not multiply. The amount of power consumed more than produced is what you take out when we consume more than production, integrating it over time from 0 to T.

The leak is just an integral of the leak from 0 to T. **This gives us the charge in the battery at time T**.
Suppose that the excess goes above the energy that we can put in the battery.

_To model this, we need the constraint that the battery is always below $B_{max}$
We can say that the previous equation holds if $B_t$ is less than $B_{max}$. If it does not happen, **there is a loss (because of less battery capacity)**.

So we get finally the formula: 
$$B_{max}\geq B_0 + \eta\int_O^T[P_s(t)-P_c(t)]^+dt -\int_0^tP_{leak}(t)dt\geq0$$


* right: sufficient and necessary to guarantee **energy conservation**
* left: sufficient to guarantee the **buffer capacity limit**, but it is not necessary. It may be necessary if *waste is not possible*, but it is allowed to waste battery capacity. 


# Question

![[Pasted image 20230426225915.png]]

Energy Produced(4)$\int_0^4P_s(t)dt=\int_0^480mA$ $dt$ $= 80mA\cdot 4s = 320 mAs$ (milliAmpere per second).

Note that graphically for the integral, it is 4 * 80, as we have 4 = base of the rectangle, and 80 is the height.

Consider the interval [0, 4 sec].

The energy produced is 80 mA. To get the energy, we multiply by time, and we want milliampere-hours. So we multiply 4 / 36000.
Given the result in milliAmpere per second, we do:
320mAs/3600 =0.088 mAh

To get the energy stored then do: 0.088*95/100 = 0.0836 mAh

We calculate the **energy consumption** similarly: 150 * 4 / 3600 = 0.16 mAh

We are in a situation where the production is smaller than consumption.

Charge = 400mAh + (energy produced - energy consumption) = 400 mAh + 0.0836 mAh - 0.16 mAh = 399.9236 mAh

(The integral is calculated by multiplying by 4)

### Second question:
**Use the initial energy calculated, and go in the interval 4 to 10, so multiply by 6 instead than by 4.**
Energy Produced at time 10 = 80mA \*6s/3600 = 0.13 mAh.
Energy stored at time 10 = 0.13 * (95/100) = 0.126
Energy Consumed at time 10 = $20*6/3600$ 0.033 mAh 

The Battery charge at time 10 is:
$B_t(10) =$ 399,9236 mAh + 0.126 mAh - 0.033 mAh  = 400.0166 mAh

# Energy sources and storage technologies
In nature we have different phenomenon from which we can harvest energy, for example we have: sun, wind, vibrations, thermal, radioactivity, motion, radio frequencies...

We can classify these energy sources based on their controllability:
- fully controllable: energy source that we can control and produce it only when we need. 
- partially controllable: energy sources may be influenced by system design but the result might not be deterministic.
- non controllable: energy sources are uncontrollable such as wind, sun... The energy harvest have to be done when it is possible.

But other that controllability we have predictability:
- uncontrolled but predictable: you can build a precise forecast model in which you know when the energy source will be available. For example sun, day/night and winter summer.
- uncontrolled and unpredictable: you can't construct a forecast model in which the energy source will be available, such as the vibration of earth or wind.

Here in table, there are some energy source and their main features:
![[Pasted image 20230508160937.png]]

### Radio frequency sources
There is an antenna coil attached to a TAG and when it is moved near an electromagnetic radio frequency (RF), this pass inside the coil and generate an AC voltage. 
We have an RF TAG that have a passive behaviour and an RF energy transmitter that have an energy source. 
Can be used as identifier RFID TAG, to locate and track object. The RF TAG is entirely powered by the energy transmitted by source and can send a reply, that is ever the same, in fact the particular data is done by the particular construction of the antenna.

![[Pasted image 20230508161838.png]]

### Piezoelectric
It composed by a piezoelectric material and a metal back plate, when it is compressed by a mechanical force it results in a electrical potential difference.
There are two type of piezoelectric components: PDVF (Polyvinyl Fluoride) and PZT (Lead Zirconate Titanate) which is more rigid.

![[Pasted image 20230508170559.png]]

Two type of implementation of this energy source are:
- shoe powered RF tag system: active RFID tag wireless transmitter that
sends a 12-bit identification code over short distances, while the bearer walks.
- Push button controller: can wirelessly transmit a digital code to a distance of 15 meters on a single button push.

### Wind turbines
There are many different types of wind turbines, with different form factor, energy production, scales and operative range of wind speed.
In particular those used for IoT are small, with low height and operative range with weak wind. Below there are some data form a micro wind turbine generator:
![[Pasted image 20230508171446.png]]

The turbine reach the maximum efficiency when the load resistance matches the internal resistance of the generator. Here an example of a turbine that have different type of power generation in according to the load resistance and the wind: more wind generate more power, but more resistance doesn't generate more power. But it has to taken into account also the mechanical resistance of the blades (can turn only to a maximum speed).
![[Pasted image 20230508171809.png]]

### Solar energy
To get energy from sun we need solar panels, but the production depends on different factors such as:
- irradiance: with which the sun rays hit the surface of the panels. It depends also on the seasons of the year and the geographical position and the direction of exposure of the panel.
- size of the panel.
- charging efficiency: how much the solar energy can recharge the battery, it depends on the materials and the surface of the panels.

An example of sun exposition and the power generated in Madrid and in Hamburg:
![[Pasted image 20230508172839.png]]

Given the fact that the power production varies a lot in the year, through the months, an usual solution is to oversize the harvesting subsystem and the battery to match with the worst conditions.
The provisioned expectations of the solar production is very far from the real one, taking in example the below chart we can see that there a big discard between the twos, because you have to take into account also the clouds...
![[Pasted image 20230508173759.png]]

Finally we have a comparison chart between solar and wind production over 12 days:
![[Pasted image 20230508173918.png]]

Obviously with the natural source of power we cannot have them 24/7 so, there will be a period in which there will not be an energy provision, and in that case the device will take energy from the battery, if there is yet, otherwise it will switch off, and it will turn when the source became available.

# Storage technologies
The energy storage are composed by cells of different materials, they provide with anode an cathode a difference in electrical potential that provide energy. The storage cells can be recharged by reversing the internal chemical reaction of anode and cathode. Depending on the materials a battery can be more or less dense, can have different type of charge method, different degradation, different maximum recharge cycles and different nominal voltage.
![[Pasted image 20230508175141.png]]

### Supercapacitors
![[Pasted image 20230508175626.png]]

They are very efficient when there isn't need complex charging circuit, where ample energy is available at regular interval and can be used to buffer energy if energy source is jittery because it needs of trickle charge: when no-load, allows to charge at the same rate of discharge to keep the capacitor at full charge level.

### Measuring the battery capacity
This is not a trivial calculus; all methods for power management assume to have fresh information about the battery charge and the actual energy from the harvesting source. 
Most of devices don't have the capacity to measure this information and the same hold both for charging and consumption.

We may define:
* $E_b(t)$ representing the **battery charge** at time t.
* $p_c(t)$ representing the power consumption at time t
* a specific time frame to measure where $t\in[t_1,t_2]$ 

A simple method to measure the energy production $E_e$ is derived by this formula:  $$[E_e=\int_{t_1}^{t_2}p_c\cdot dt + E_b(t_2)-E_b(t_1)]^+ $$Where $[x]^+$ is the rectifier function, making the value 0 if negative, else returning the value.
**This formula is a consequence of the energy conservation principle**, as the energy is consumed and produced by converting energy of the source, but not destroyed of created from nothing.

But if the interval is too big errors may occurs, the estimation of the energy consumption is not easy to do and errors could occur for the the battery charge, also the estimation of the energy consumption may be difficult.

* A better method may be to use the electronic circuits and measured the current and the voltage flowing out the harvesting source. 

### Measuring the battery level
To measure the battery charge we may measure the voltage.
Battery charge and voltage are correlate, as the voltage drops down with the charge. Often this relationship can be assumed linear, but depends on the specific technology.
That is clearly seen here:
![[Pasted image 20230629162455.png]]


**We want to compute a representation on the device of the current voltage, to then define battery levels**.
Considering a device with a minimum and maximum battery charge $B_{min}$ and $B_{max}$ respectively and $v_{min}, v_{max}$.
Given an ADC of d-bits, we can **define** the bounds of the presentation of  $v_{min}, v_{max}$. 
$$x_{max}=2^d - 1 $$
$$x_{min}= ROUND[\frac{v_{min}}{v_{max}}\cdot (2^d -1)]$$
So, given $v$ the current battery voltage then the value $x$ read from the ADC is:
$$x=ROUND[\frac{v}{v_{max}}\cdot (2^d -1)]$$
and the corresponding current battery level $B$, assuming a linear scale, is:
$$B=B_{min}+ \frac{B_{max}-B_{min}}{x_{max}-x_{min}}\cdot (x-x_{min})$$

(Here we assume a linear scale voltage/charge, so they correspond to each other)

An example of energy consumption of some platform, where $B_{min}= 300mAh$: 
![[Pasted image 20230628100424.png]]

### Exercises
![[Pasted image 20230629163252.png]]
![[Pasted image 20230629163304.png]]


# Energy Neutrality
Load modulation is an action to reduce the amount of work to reduce the energy consumption. Some device actions such as transmitting or receiving, activate sensors with high frequency and therefore consume more battery, but this frequency can be reduced in order to consume less.

A device is neutral if it can keep the desired energy level "forever".  An operation is considered energy-neutral if the energy used is always less the energy produced.
Some question rise at this moment: what is the maximum performance level can be supported in a given harvesting environment?
How can be an estimation computed of energy production considering the forecast and other parameters?
![[Pasted image 20230628103913.png]]

To achieve this two different approach can be used: 
- adapt the load: if there is a energy production the device is ON otherwise is OFF. In this case if there is a energy production higher than ones consumed there is a energy loss.
- energy buffer: the energy production is stored in a battery to provide energy to the device even if there is no production. Also in this approach we have a energy loss: both in charging mechanism but also when the battery is at the maximum level and there still an energy production.

### Harvest-Store-use to Energy Neutrality
**The goal becomes to modulate the energy consumption to archive energy neutrality**.
The modulation is based on:
* the amount of energy already harvested in the past from one or multiple sources
* *the current charge of the battery*
* the *future energy production*
	* this is estimated using forecasts, such as weather forecast for sun and wind. *Consider those forecasts are likely subject to error so* **a pessimistic approach with the minimum energy production is considered** (that could lead to wastes)

*The approach of Harvest-Store use* is to use the energy harvested when:
* there is no source producing energy at the moment
* the energy produced by the source is not enough for the *sensor task* required energy
We may see how a Scheduler in the device will use the data produced by an Energy predictor to create a Task energy model to manage the load.
![[Pasted image 20230629101952.png]]
 
## Kansal's approach
Consider the case in which there are predictable but not controllable sources, such as solar energy. The objective is to keep the system energy neutral, maximizing the node performance and ensure the system never fail due to energy depletion.
To achieve this the approach makes sure the device neither operates below minimum performance levels nor switches OFF before the next recharge cycle, tuning dynamically the device performance.

Considering the linearity of both energy production and load 
![[Pasted image 20230628110820.png]]
Amount of energy produced in an interval $[0, T]$ is defined as
$$E_T=\int_{0}^{T}P_s (t) dt$$
where $p_s \cdot T - \sigma \leq E_t \leq p_s \cdot T + \sigma$
($P_s$ is a real number denoting energy produced at time t and $\sigma$ is a real number)
![[Pasted image 20230628110832.png]]
Amount of energy consumed in an interval $[0,T]$ is defined as
$$L_T=\int_{0}^{T} P_c(t)dt$$
where $0 \leq L_t \leq p_c \cdot T + \delta$
($P_c$ is a real number denoting energy consumed at time t,  a real , and $\delta$ is a real number)

the Kansal's theorem says that the system's energy neutrality if this conditions hold (as a sufficient condition, not necessary):
$$
\begin{equation}
    \begin{cases}
      \eta \cdot p_s \geq p_c + p_{leak} \\
      B_0 \geq \eta \sigma + \delta \\
      B_{max} \geq B_0
    \end{cases}\
\end{equation}
$$
Where  $\eta$ is the charging efficiency and $p_{leak}$ is the battery leakage and the three conditions respectively says:  
- The trend of production (considering the charging efficiency) should exceed the trend of load and the leak together
- The initial battery charge should be sufficient in the worst case
- The required initial battery charge should be admissible (less than the battery capacity)
### Utility and duty cycle 
Kansal **makes** sure that the system must meet two conditions:
* Condition 1 on power production: for the power production must be enough, and this is taken as an assumption by Kansal
* Condition 2 on load: it adjusts the duty cycle dynamically, increasing or decreasing the load
	* A duty cycle reduces has a **linear relationship with the the power consumption reduction (almost linear)**
	* the conditions as it stands would be met with a duty cycle of 0%, but the device would be doing nothing. To prevent this, we introduce utility.


Make a relationship between duty cycle $dc$ and utility $u(dc)$ of the application: 
$$\begin{equation}
    \begin{cases}
      u(dc) = 0 \hspace{2,75cm} if\space dc < dc_{min} \\
	  u(dc) = \alpha \cdot dc + \beta \hspace{1cm} if\space  dc_{min}\leq dc \leq dc_{max} \\
      u(dc) = u_M \hspace{2,3cm} if\space dc > dc_{max}
    \end{cases}\
\end{equation}$$

So there is a linear relationship between utility and duty cycle, that we may see in the graph:

![[Pasted image 20230629180430.png]]

Given:
* $u_m$ the minimum utility 
* $u_M$ the maximum utility 
* $dc_{max}$ maximum duty cycle
* $dc_{min}$ minimum duty cycle
**We define $\alpha$ in relation to the differences between maximum and minimum of utility to represent and duty cycle:
$$\alpha=(u_M-u_m)/(dc_{max}-dc_{min})$$
and $\beta$** as the difference between the minimum utility and the minimum duty cycle but multiplied by $\alpha$:
$$\beta=u_m-\alpha\cdot dc_{min}$$
To finally obtain represent with the equation the utility for a given duty cycle$$u(dc) =\alpha\cdot dc + \beta  $$an example showing this with 
* *$u_m$ = 10 
* $u_M$ = 100 
* $dc_{max}$ = 90%
* $dc_{min}$ = 50%

![[Pasted image 20230629181343.png]]
#### Example with energy consumption
Assuming:
* $p_{max}$= 5 mA
* $p_{min}$= 1 mA
* $d_{c_{max}}$ = 10%
* $d_{c_{min}}$ = 100%

In this example, where is a linear relationship between the **average power consumption and the duty cycle**, denoted by 
$p(dc)=\rho*dc+\sigma$
and we denote:
$$\rho=\frac{p_{max}-p_{min}}{dc_{max}-dc_{min}}$$
as it was done for the utility.
Then we denote $$\sigma=p_{min}- \rho\cdot dc_{min}$$

We may see in the graph the relationship between **power consumption, utility and duty cycle**.

![[Pasted image 20230629182415.png]]
This correlation of utility and duty cycle enable a modulation of the load on the energy harvesting, this correlation brings to the correlation between the utility and **the energy consumption**, as seen in the graph.

Depending on the domain, going beyond $dc_{max}$ would be not useful as its a waste to increase the sampling rate. Going below $dc_{min}$ means that the system would not function.
Moving in the bounds an higher sampling frequency means less quality results but power consumption.
# Kansal Approach as optimization problem

"Since the **energy source is predictable**, we have to find the load so that the **system is energy neutral** and the **overall utility** is maximized."
This approach work well if the source is **predictable** such as the sun light. 
Furthermore, the optimization problem can be done only if the sample taken are observed in constant period and not a random one.
This because the duty cycle is constant, so Kansal operates dividing the working time in slots and assigns them a fixed duty cycle so, having a fixed and constant one can be calculated the Fourier analysis and so a precise forecast.

*For example the sun has a natural cycle of 24 hours, so the sample can be taken at each hours*, *using as sample the forecasts to estimate the day production*. 
*Each day after 24 hours the optimization is run again to account for the changes in forecasts*.
![[Pasted image 20230629102851.png]]


*We may see the allocation for each slot and how we store power when we have a bigger production than consumption*.
In this graph:
* the power production is **constant in a slot**
* the power consumed in idle mode is 0
* $p_s(i)$: the power harvested in slot i
* $p_c(i)$: the power load in slot i, *which depends on the duty cycle used in the slot, decided by the Scheduler solving the optimization problem*

![[Pasted image 20230629110239.png]]


The estimation is build over three components:
- forecast future power consumption based on the past production
- uses a simple polynomial algorithm to solve the problem
- performs a re-optimization if the actual production deviates from the expected one.

## Kansal formally
Let
$k=$ numbers of slots in a day
$B(i)=$ battery charge at beginning slot i
$B(k+1) =$ battery charge at the end of slot k, means at the end of the day
$p_s^j$ = measured energy production in slot i in day j
$\tilde{p_s}^j$ = estimated energy production in slot i in day j
$p_{max}=$ power consumption when operates at maximum in duty cycle
$p_{min}=$ power consumption when operates at minimum in duty cycle


where estimated energy production is calculated as: $$\tilde{p_s}^{j+1} (i)= \alpha \cdot \tilde{p_s}^j (i) + (1-\alpha)p_s^j$$ and $\alpha<1$ is a parameter; so the average of power production in a slot is the weighted average of the past power.

## Kansal's algorithm 
Considers two type of sets 
$S={i \in [1, k]: \tilde{p_s}(i)\geq p_{max}}$ is a set where there is overproduction -> sun slots
$D={i \in [1, k]: \tilde{p_s}(i)< p_{max}}$ is a set where there is underproduction -> dark slots

### Case one
*If at the end of the day there is a surplus of energy ($p_r$)*
$p_r=B(k+1)-B_1 > 0$. Take one random slot **from the Dark Slots** and bring it to maximum, if there is residual take another until energy finishes. If the residual energy is not sufficient to bring to the maximum, then bring one random slot to the maximum possible with that amount of energy.

![[Pasted image 20230628150145.png]]

### Case two
*There is a underproduction of energy ($p_u$) at the end of the day.*
$p_u=B(k+1)-B_1<0$. If the maximum power consumption minus the underproduction divided by the sun slots is less than the minimum power consumption there is no feasibility solution.
Otherwise decrease all the sun slot by the same quantity, equals to maximum power consumption minus the underproduction divided by the sun slots number ($p_{max}-p_u/|S|$). 

![[Pasted image 20230628150122.png]]
We see how from the dark orange, the reduction is to the yellow, to get an admissible solution.
#### Why it is not admissible
The idea of the algorithm is to reduce evenly, for all *Sun Slots* their power consumption.
*If the condition* $p_{max}-p_u/|U|$ does not hold, then there is not an admissible solution, there will be one slot that will have less power available than the minimum required.

### Algorithm code
#### overproduction case
* overproduction case, surplus of $p_r$ power production at the end of the day
* We have an array $dc_i$ of assigned duty cycle for the slot (note it is d_c\[i\] in the code below).
* **consider that $p_{max}-p_{min}$** represents the *increment in power to add to a slot that allows to go from minimum duty cycle to maximum duty cycle.*
	* We implicitly assign this unit when we bring the slot to maximum duty cycle
	* we reduce the residual power by this unit in the last line of the while
``` C
// p_r is the surplus of energy: p_r = B*(k+1) - B_1 > 0
while p_r > p_max - p_min { // p_r can power up a slot to the max utility
    let i in D be a slot with d_c[i] == d_cmin // let i be the minimum index
    d_c[i] = d_cmax;
    p_r = p_r - (p_max - p_min); 
}

if p_r > 0 { // p_r is insufficient to maximize the utility of another slot
    let i in D be a slot with d_c[i] == d_cmin // let i be the minimum index
    d_c[i] = DutyCycle(p_r + p_vmin); // increases the DC of the slot as possible
}
```
#### underproduction case
* We have an array $dc_i$ of assigned duty cycle for the slot (note it is d_c\[i\] in the code below).
``` C
// p_u is negative, it's the underproduction: p_u = B*(k + 1) - B_1 < 0
if p_max - p_u/S < p_min {
    return(-1); // no admissible solution, too much underproduction
} else {
    // for each i in S, i.e. for the slots with dc_r = dc_v
    for each i in S {
        // decreases the duty cycle of the sun slot by the same quantity
        dc[i] = DutyCycle(p_max - p_u/S);
    }
}
```
### Dynamic adaptation
Can happen that during day the actual production differs from that expected.
A dynamic adaptation of duty cycle is applied by Kansal, looking at the actual production and applying changes to the remaining slots.
* for example increase their duty cycle if there is over production
* or decrease their duty cycle if there is underproduction to guarantee the device operation.
The algorithm is similar to the basic algorithm (we did not see it).
#### PRO of Kansal
- reach the optimum
- does not need of linear programming
- can be implemented in IoT devices with low computational power
- does not have strong memory requirements

#### CONS of Kansal
- based on linear scaling of duty cycle, **this means that devices *will have* irregular sampling frequencies**. That is not the best solution for some applications that require a precise regular sampling frequency
- use of duty cycle adaptation to adapt the load production, hence it is suitable only for simple behaviour, you cannot chose for example what type of transducer to activate if having many with different power consumption or to chose different algorithms with different power consumption for the the same task.
### Exercise 1
![[Pasted image 20230629120839.png]]


### Exercise 2
![[Pasted image 20230629120809.png]]


# Task based model 
An IoT device operates in 4 type of task:
- sensing
- storing
- processing
- transmitting
And the works for every phase during an IoT device life may change. As consequence even servers or gateway in the IoT network re-modulate their works, for example changing the sampling frequencies, storing more data on device, transmitting less but compute more on server side.
We may have transducer with different utility levels, meaning that they use higher or lower frequencies to get more precise or less precise data.
Therefore, the requirements does not change but system functionality, the implementation of those changes a lot (we may see those as non-functional characteristics). These implementations are called tasks, each has:
* a power consumption (cost) per unit of time 
* a utility (what they archive and with what quality)

### Load Modulation with Tasks
By Scheduling the tasks to execute, based on the utility and power consumption targeted.
*The server receiving data must be informed of the task being executed, to adapt itself (process the data or just store them if processed by the device)*.

![[Pasted image 20230629142208.png]]
We may see how *on the Internet, there is the Energy Predictor, which has an internal Energy Source model*, this receives from the Solar panel information about the produced energy and *gives to the Scheduler of the device the energy produced and forecasts*.
The device receives energy from the energy buffer and also directly from the Solar panel.
Internally the Scheduler will schedule tasks, using the Task model with information given by the Energy predictor.


### A case of Task-based model
In the Task-based model that we see below, the the energy production is already **considered** in energy cost value. The operation of an IoT device is divided into time slots and each is filled with a task.

Given $k$ slots, and $n$. tasks.
A scheduler has a matrix $x[k,n]$ where
* $x_{i,j}=1$* iff task j is assigned to slot i

**The scheduler is set to run once a day at a certain time (e.g. midnight)**.


We may see how each task has a certain utility and Energy cost:
![[Pasted image 20230629144238.png]]

![[Pasted image 20230628153605.png]]


$p_s(i)=$ expected energy production at slot i(e.g. by weather forecast)
$p_c(i)=$ energy consumption in slot i
$p_s^{+}(i)=[p_s(i)-p_c(i)]^+=$ expected power produced and not consumed at slot i (recharging battery in the slot if not 0)
$p_c^{-}(i)=[p_c(i)-p_s(i)]^+=$ expected power consumed from battery in slot i
$\eta =$ charging efficiency

The battery level at the end of slot i is:
$$B(i+1)=min\{{B_{max}, B(i)+\eta \cdot p_s^+(i)-p_c^-(i)}\}$$
There is $min$ because the battery level cannot be above $B_{max}$
* $\eta\cdot p_s^+(i)$ is the battery charge produced at slot i
* $p_c^-(i)$ is the battery consumed

### Optimization problem formalization
The problem can be formalized as a linear integer programming problem and it becomes:
$$max \sum^{k}_{i=1}\sum^{n}_{j=0} x_{i,j} \cdot u_j$$
where $u_j$ is the utility of the task assigned in that slot
Given:
- $\sum^{n}_{j=1} x_{i,j} = 1 \hspace{0,5 cm} \forall i \in [1,k]$ 
- $B(1) \leq B(k+1)$
- $B_{min} \leq B(i) \hspace{0,5cm} \forall i \in [1,k]$ 
- $B(i+1)=min\{{B_{max}, B(i)+\eta \cdot p_s^+(i)-p_c^-(i)}\}$
Where the constraints mean:
1) one task per slot
2)  we want energy neutrality, at the start of the next cycle we did not consumed more than the initial batter level (we actually are enforcing an equality)
3) We cant have a slot with battery charge lower then the minimum or the device stops
4) *at the end of a slot and start of another slot, the charge depends on the initial charge and what was produced and consumed*

The problem is NP-hard and can be reduced as a version of knapsack; some implementation are pseudo-polynomial  based on dynamic programming; and even in low-power IoT can be executed, under some realistic restrictions.

### Dynamic Programming pseudo-polynomial solution
Given:
* i : the slot up to which the system has been optimized, so slots (1,2,..,i-1,i) are optimized
* b *the battery level at the beginning of slot 
Denoting the System state as **(i,b)**
The optimal utility defined as opt(i,b) (so the optimal system state) can be found using backward recursive rule:
- base:
	$opt(k,b)=max_{j=1..n}\{u_j:b+\eta \cdot p_s^+(k)-p_s^-(k)\geq B(1)\}$ 
	where results from assuming task j assigned to slot k
- recursive step: 
	$opt(i,b)=max_{j=1..n}\{u_j+opt(i+1, B^j(i+1)):B^j(i+1)\geq B_{min}\}$ 

Finally, the complexity is $O(k \cdot battery\_level)$ and given $k$ is a constant and with some optimizations the final complexity will be $O(battery\_level)$ 

**But the battery level is a real number ranging from $B_{min}$ to $B_{max}$ ... is it?**

The Battery Level is not clearly a real number but rather function of the quantization levels $d$, the voltage at a certain moment and the maximum and minimum voltage, as it depends on the ADC (analog to digital converter) precision. Given that we cannot reduce the complexity to O(1) but have to make it depend on that variable.
#### Simulations on Arduino UNO
**Arduino UNO has a complexity of O($k\cdot$** Battery levels), without optimization for execution time of the scheduling algorithm.
To reduce the complexity, we may *chose*:
* number of slots
* battery level
So that the algorithm can be executed by the target platform.

For example with an Arduino UNO this means an execution time of 0,8 seconds for 96 slots to fill with tasks, due to its tiny memory.
![[Pasted image 20230629154447.png]]
An experiment show how the battery level changes along days over the months, having application with different duty cycles.
We may see how in august we may always use the maximum duty cycles for the best utility, while the utility is much lower in January. On the x axis we represent he *number of slots to fill with tasks*. An **increase** in the number of slots means an increase in the utility that can be obtained in any month, but keeping in mind that the scheduling algorithm complexity will then increase.

![[Pasted image 20230628163716.png]]

Here the representation is for average remaining battery level. We see how in cold months we are dangerously close to B1, the initial level. While in summer we go above.
![[Pasted image 20230628163740.png]]

Daily we may see for each slot the battery level.
![[Pasted image 20230628163756.png]]


# Extra Exercise
![[Pasted image 20230629183537.png]]

 <div style='page-break-after: always'></div> 


# Chapter 14: Hands-on on Thingspeak
Thingspeak is a platform which allows to setup IoT communication channels.
It is a free web service to which daily up to 8200 may be sent, the maximum frequency of upload is 15 seconds, so you cant upload at faster frequency.
It has a REST/HTTP interface for data upload and has a MQTT broker.
It has tools for data processing and visualization.
# Thingspeak channel

A channel is for Thingspeak its basic abstraction, it represented values up to:
* 8 time-varying parameters
**A channel as an identifier and is protect by**:
* API keys that must be added to the URL or in an header field
There are two distinct keys:
* Write API key: to upload data
* Read API key: to access data, as a channel may be private or public.
More than one device could contribute to putting values on a the channel.
We get from the Website the keys.
## Field

**A channel may have multiple field**s.
A field represents a variable, with a fixed identifier.
Uploading one or more values in a channel is called **feed**. With just one feed several fields may be updated.

## How to implement a feed
* HTTP:
	* GET: containing the request URL and the pairs field=value
	* post: with pairs field=value in the body of the request
* MQTT: a **publish()** of the pair field=value
# Representation

In the channel dashboard there is a diagram for each field:
* horizontal axis: time
* vertical axis: measured parameter

# How to use
1) you may test with the browser and HTTP requests
2) use Python and HTTP
3) MQTT: by creating a MQTT device in thingspeak, in this way there is access for MQTT in the channel.
# What we did
We used Thingspeak with Arduino and MQTT publish the data of a sensor attached to the Arduino which measured the electric charge.




 <div style='page-break-after: always'></div> 


# Chapter 15: Arduino and TinyML Hands-on
The goal of the hands-on was design a small size neural network, able to run in a resource constrained device, then optimize it.
After Design: Train and then Upload to the device.

Train the neural network to: recognize the activity you want to recognize.
Using the division:
* Training set: train network to recognize the gesture
* Validation set: to optimize the network, you use the validation set, adjust some configuration on the neural network to get some results on those
* Test set: use some part of the set to test, **using some new data not already seen or you are cheating**
We will just train the network, as we suppose that Google Efficiently trained it.


Through Chrome, you can pair with a BL device.
We train the system to recognize a gesture by making it record us doing it.
Then when we execute it, we will the what gesture it recognize and will give also a confidence band.
The more samples we give, the better is the training.



 <div style='page-break-after: always'></div> 


# Chapter 16: Indoor Localization
When we use position to provide to users some context awareness. For example giving them a service for monitoring their position.
For example for navigation indoor too, as used in [[High Tech Greenhouse and DOREMI]].

# Classification
We can classify the types of location information according to how its presented and relative to what
We may have physical location or symbolic location.
* Physical referring to a map in 2D or 3D. **Latitude and Longitude for example are physical locations
* Symbolic: location expressed a natural language such information about proximity to an object or placement in a room. 
We also have for positions
* Absolute location: uses **a shared reference system**
* Relative location: **has its own frame as a reference**, for example position relative to an access point or for a moving object to the destination.
A relative location can be converted on an absolute location, knowing the relative position to a absolute position known point. 
It requires multiple relative readings available, needed for a fusion strategy.


# Outdoor Localization Scenario

Using the GNSS, Global Navigation Satellite Systems. Some of GNSS systems are GPS by USA and Galileo by EU.
Some of those systems used in Outdoor localization are also used in Indoor Localization.
The process is that a signal is sent from a satellite, in response a unit send information. We have for each receiver, a calculation saying how long it takes from the receiver to get the signal, which allows to tracker the receiving unit.
![[Pasted image 20230618183926.png]]
GNSS satellite systems consist of three major components:
* Space Segment: Multiple Satellites
* Control Segment: Base Stations, Master Stations and Stations for Data upload to satellites.
* User Segment: Moving objects

All the signal is sent in broadcast from satellite to devices, except the Data Uploading stations, used only for uploading data. The Data Uploading stations use the GNSS Control Channel to communicate.

Two satellites are not enough for **determining the position of one unit, there is the need of Range measurements from 4 satellites**.
For each tracker satellite, the *receiver itself calculates*:
* the time the satellite signal needed to reach it, **that allows to determine the distance to the satellite**
Given
* Propagation time = Time for the signal reached to receiver - Time signal Left satellite.
The distance to the satellite is defined as:
* Distance to Satellite = Propagation Time $*$ Speed of Light
The receiver knows *at a specific time, where the satellite was at time of transmission, using the orbits epidermises*
The orbits are is a very big table, which contains of orbits of the satellite and time where they reach a certain point. The table allows to know when at a certain time a satellite is. 
Those pre-calculated orbits for satellite, with their time are called orbits families.

## Trilateration
We may not know precisely where we are, as we may be in the middle of two satellites.
Also considering the difference in clocks precision for satellite and unit, which contribute both with their data to calculate the and the propagation time. 

We may have a big error, for example a 1 km of error can be generated.
**A third satellite is needed to reduce this error**, By adding a third satellite, the number of possible positions is reduced to one.

If you have two satellites, there are two points instead which are the intersection points of three spheres (one is contained in the other twos), the true position is likely to be closer to one of these two points than to any other location within the circles of possible positions.

With three satellite we reduce by much the error, getting one point!.
![[Pasted image 20230618210221.png]]



*Since we want to converge the coordination to a single point* but that point is not the precise point, ***there is no intersection because of the clocks differences**, to receive an accurate position we can iterate.
*The receiver know the pseudo-ranges to the three satellites and that they do not intersect due to errors of the clock*.
![[Pasted image 20230618210428.png]]
The receiver can advance or delay the clock **until the pseudo-range of the three satellite converge at a single point**.
The *satellite clock is transferred in a certain sense to the receiver clock, doing that, gives a very accurate time, eliminating clock errors*.

This is the result:![[Pasted image 20230618211247.png]]
Note that **we said 4 satellites because, if we want to extend this principle to the three dimension world, we need a fourth satellite to compute a position**.


# Indoor Localization
Indoor is different, as we do not receive indoor the GPS signal.
We need a new kind of matrix that maps an area.
## Topologies 

There are two main topologies:
* Remote positioning: the target unit to localize acts as a transmitter and is mobile. The measuring units called **anchors** are fixed in a position. There is a location manager (or may be called beacon), which may be an anchor , that executes the localization algorithm
* Self-positioning: the unit to be localized is mobile, *it makes the measurements necessary and runs the localization algorithm, without a location manager*. The unit receives from the *fixed anchors* signals. The unit knows the position of the anchors. The anchors are only transmitters.

There also is indirect self-positioning if the location manager sends back the position to the *mobile unit*.![[Pasted image 20230618215507.png]] The mobile device will measure, localize and use localization data.
Or there is Indirect remote positioning: opposite, the mobile send its location to a remote location manager (beacon). This may be seen here: ![[Pasted image 20230618215446.png]]
The anchors will measure, localize and use localization data.

One must chose the kind of device to chose. Where an accuracy of 15-20 meters is fair.
There are various ranging approaches, based on time, angle and indicators. The most simple measure is the time of arrival, measuring with the time that the signal use to arrive to the mobile target.
The unit of measure to use, depend on the accuracy required.
![[Pasted image 20230618215921.png]]
The propagation formula of the GPS is used too to measure the distance from the beacon.
When receiving the signal you use the time of transmission.


Having three different angles, you do thrilateration. You can then use some formula to minimize the error.
Having the known coordinates and time, we may minimize the formula to detect ranges, which is not easy to do on a low computation device. We may combine radio signal and acoustic signals too, exploiting their speed difference.
There are tradeoffs between different metrics.
We may have:
* infrared: only for line-of sight devices, you cant see around corners or if there is an obstacle
* ultrasound: no line of sight problem, precise accuracy with 10-20 cm error but so may be used only in short range
* UWB (ultra wide band): accuracy to 10-20 cm, but need costly specialized hardware
* WiFi: accuracy of 3-5m, bigger error but low cost


# Signal Metric

There are three ranging approaches:
* Time: Time of Arrival, Roundtrip Time of Flight, Time Difference of Arrival
* Angle: angle of arrival
* Received Signal Indicators: such as received signal strength and received signal phase.


# Time Of Arrival (TOA)
Measure the distance with the:
* propagation time
	* as there is a proportion for the distance between the measuring unit and the mobile target with the propagation time.
### How it works

* Mobile emits a radio signal at time **t**
* Measuring unit receives it at **t'**
	* Measuring unit computes the distance as (t'-t)$*p$, with **$p$ being the propagation speed of the signal**

The issues it has is that: *there is the need of a tight synchronization between transmitter and receiver and the *signal sent by the Mobile* must encode the transmission time t.

**Anchors are needed and as in GNSS we need for a 2F position of a mobile target at least 3 anchors**.
We may use then different methods to compute the position. For example below they use the intersection of circles.
![[Pasted image 20230618222214.png]]

## Linear Equation
This other methods solves a **non-linear optimization problem, the least squares**,
It has as unknown variables, 3 (or 2 as you want to see it):
* t: **time of signal emission**
* **(x,y)**: coordinates of the mobile target
* coordinates of the anchors $(y_1,y_1),(x_n,y_n)$ which are well known
* the times of arrival of the signal at anchors $t_1$,...,$t_n$ which are known.
* c: light speed
The formula of the optimization problem is then:
$min\sum_{i=1}^n|c*(t_i-t)-\sqrt{(x_i-x)^2+(y_i-y)^2}|$
So we multiply the **propagation time by the speed of light, as in GNSS**. Then we subtract the square root of the squared difference between the coordinates summed up.



We implement ToA by using *different signals in some applications*. Mixing signals of different nature, for example radio and acoustic. The *radio signal* has a specific use:
* to **synchronise the measuring units.**

The difference in time between the arrival of the signal is almost proportional to the distance.
You may see that **we consider the time $t_1$** as the time where we sent the full radio message, and include in the interval the ultrasound time.
**t_2 is the time to receive both!**


![[Pasted image 20230618224500.png]]

We may see how the $t_{sound}$ represents the time to transmit fully the sound and $t_{radio}$ the time to transmit fully the radio signal.
The difference in time of transmitting radio and ultrasound, is bigger than the time to receive both.
Consider that radio is order of magnitudes **faster than acoustic signals**.
Also note that $v_{radio}>>v_{sound}$ so the velocity of radio signal is faster as said.

**We then define the distance as**:
* $(t_2-t_1)*v_{sound}$ 

The proof will make us see why we isolate $v_{sound}$
and in general show the correctness of the mechanism.

Given:
* d:distance
* $t_1$: time of radio signal full arrival
* $t_2$: time of ultrasound full arrival
* $t_r$: time of radio signal start
* $t_s$: time of ultra **s**ound start
* $t_w$: difference between time of ultrasound send start and time of radio send start: $t_s-t_r$
* $t_w$: sum between of time radio send start + that difference : $t_r+t_w$ $(=t_r+t_s-t_r=t_S$ actually)
* ![[Pasted image 20230619095504.png]]

We can define d in two ways:
1) $d=(t_1-t_r)*v_r$
2)  $d=(t_2-t_s)*v_s$
We can expand $t_s$ in the second
$d=(t_2-t_r-t_w)*v_s$
$d=t_2*v_s-t_r*v_s-t_w*v_s$
**we solve for $t_r$, dividing all by $v_s$**
$t_r=((t_2-t_w)-d/v_s)$
We than plug that it in the first formula
$d=(t_1-((t_2-t_w)-d/v_s))*v_r$
We place on the left the factors with d.
$d-(d*v_r/v_s)=(t_1*v_r-t_2*v_r+t_w*v_r)$
operating on the left side
$(d*v_s-d*v_r)/v_s=d*(v_s-v_r)/v_s$
**dividing all by $v_s$**
$d*(v_s-v_r)/(v_s*v_r)=(t_1-t_2+t_w)$
**using the fact that $v_s$<<$v_r$**, we consider only $v_r$ in the difference at the left side
$d*(-v_r)/(v_s*v_r)=(t_1-t_2+t_w)$
easily simplified to
$-d/(v_s)=(t_1-t_2+t_w)$
$d/(v_s)=(t_2-t_1-t_w)$
**Using the fact that $t_2-t_1$>> $t_w$** as the difference between the signal of the sound is received and the signal of the radio is received is much bigger than the difference the signal of the sound is sent than the signal of the radio is sent.
As such the formula becomes
$d/(v_s)=(t_2-t_1)$
**we finally reach the result:**
$d=(t_2-t_1)*v_s$




## Time Difference Of Arrival Hyperbolic location theory


In this case, the difference used is at *arrival time at the measuring units (anchors)**rather than the absolute time of arrival of two signals of different type(or just one)**
In hyperbolic location theory, the difference in arrival time is measured at the receiving end rather than at the anchor end.
Given an Hyperbola,the difference $t_1-t_2$ is always the same on the hyperbola.

Given:
* M the mobile
* $t_1$ the time of arrival at anchor $A_1$
* $t_2$ the time of arrival at anchor $A_2$
*Then we can state*
$d_{diff}=d(M,A_1)-d(M,A_2)=(t_1-t_2)*c$
So its a multiple of the difference in time of arrival at two points the distance measured as difference.
Basically based on 2 or three sensors, we can estimate **at the hyperbola** **intersection** the position of the mobile.
![[Pasted image 20230619104808.png]]
Given the intersection of hyperbolas, we may have then a formula.
Each sensor pair **gives an hyperbola on which the emitter mobile lies***.
With the intersection of all hyperbolas we estimate the location.
**The hyperbola is the set of points that are at a constant range-different $c*t_2-t_1=c*\Delta t$** from two foci


For Time Difference of arrival TDOA, given its measurement $d_{diff}$ the transmitter must lie *in a hyperboloid, that has a constant range distance between any two measuring units*.
A hyperboloid is a quadric surface generated by rotating a hyperbola around its axis.

*![[Pasted image 20230619105827.png]]. When 0, the unit has the same distance, the hyperbola is a straight line
	* ![[Pasted image 20230619105913.png]]when < 0, it means that $A_2$ is farther than $A_1$, note that the curve will be internal to $A_1$ then
	* 	* ![[Pasted image 20230619105913.png]]when > 0, it means that $A_2$ is closer than $A_1$, note that the curve will be internal to $A_2$ then
* ![[Pasted image 20230619110047.png]] By trilateration, we find in the intersection of hyperbolas the pint




# Roundtrip Time Of Flight (RTOF)


Here the transmitter and the measuring unit are the same.
Where the *mobile device does not measure the time difference in arrival*. Instead the device to be localized is a transponder, receiving the signal and *sending it back.*


The measuring unit is the difference between:
* time of transmission $t_1$ from the measuring unit
* time of reception $t_2$ of the measuring unit for the signal sent back!
So the distance is:
* d=$c*(t_1-t_2)/2$
	* Since the signal does twice the same path
The advantage here is that the need of synchronization is reduced with respect to Time Of Arrival. In Time of Arrival (TOA) localization, the mobile device and the receiving units need to be synchronized in order to accurately measure the difference in arrival time between the signals. This is because the difference in arrival time is very small (in the order of nanoseconds), and any inconsistency in the clocks of the mobile device and the receiving units can lead to errors in the localization.

In Roundtrip Time of Flight (RTOF) localization, the need for synchronization is reduced because the same clock (anchor one) is used for both the transmission and reception of the signal.
Furthermore, *in small range also the processing time for measuring unit and transponder are not negligible, they must be estimated correctly*.
![[Pasted image 20230619114238.png]]

As in the given the figure:
At $t_1$ the measuring unit transmit the signal, at $t_2$ it is received by the mobile, $t_3$ the signal is sent back and $t_4$ is received back by the measuring unit. The time of flight is unknown $T_f$ but can be calculated. 
* $T_f$: time to fully send a signal from A to B and from B to A
* $T_d$: processing time before the mobile sends back
d = c*$T_f$
We can write, by modelling the image situation:
$t_4-t_1=2*T_f+T_d$: two times the time to do A<->B and including the computation time on the transponder.
**We then solve by $T_f$**
$T_f=1/2*(t_4-t_1-T_d)$

Then we can plug this onto d.

$d=c*(1/2(t_4-t_1-T_d))$
Consider that the time when signal back is sent- time first signal is sent will be much more higher than $T_d$
usually.
	If $t_4-t_1>>T_d$ then:
		$T_f=1/2*(t_4-t_1)$
			d=$c*(1/2)*(t_4-t_1)$ 
So we obtained the formula of the distance!



# Angle of Arrival (AOA)
The target location is obtained by *the intersection of several pairs of angle direction lines*

We may compute the angle of the receiver signal, and we know it with the antenna that measures it. Knowing the angle, in 2D environment we need 2 reference point, in 3D, 3 reference point.
*In 3D we also need 3 dimensional antennas.

In 2D the example is:
![[Pasted image 20230619121430.png]]
Two reference points and their respective angle measurements are needed.
In 3D we need as said, three.

## Problem
We need *directional antennas as said, to understand from where the signal is received, those are not available in sensors usually, are large and expensive*.
**To solve that, they implemented this recently with arrays of antennas**.


## But it is the best for accuracy
It is very accurate, at the same time there are error cause by:
* reflection (on surfaces of the signal)
* multipath (signal may arrive from different directions). We may have an effect of multipath, where one does not understand from what direction the signal is received. The array of antennas allows to understand better from where the signal comes.
Which may affect the measurement.

# Remarks
* TOA
* TDOA
* AOA
(NOT RTOF)
They work well only when transmitter and measuring unit are in Line Of Sight (LOS)**. If not, the signal is affected by multipath, affecting the time of arrival and angle.

The Received Signal Strength: focus on the power of the signal.
Consider that all measures with time need hardware that can perfectly synchronize the time, so we need a good accuracy clock and synchronisation.

For angle arrival: we need phase and angle measuring devices.


# Received Signal Strength (RSS)


*The radio signal attenuates with distance*.
There is an exponential rule, that the power of the signal decay when being far from the source.

Assuming that we received a signal on z and w (anchors!) from v(mobile). The main assumption is that the farthest is the device transmitting a signal the lower is the power. The basic formula is the Friis equation, which has the assumption to be on an open field! So without trees and any building. The equation allows to compute the power of the receiver signal strength and with that the distance as the power reduced with the distance.

![[Pasted image 20230619124251.png]]
v receives a signal from z.
The power of transmission P will be greater than the power of the incoming signal.
For w, since its farther away than z, the power of its incoming signal will be even less than then one on w.

Depending on the received signal phase, we may have different wavelengths, for a distance larger than a wavelengths this approach does not work. 

**Fris equatio will give the relationship**:
* transmission power and
* distance between transmitter and receiver

Given:
* $P_r$: the signal power at the receiver in Watt
* $P_T$: the signal power at the transmitter in Watt
* $\lambda$:the wave length
* d: distance **between transmitter and receiver**
* n:**the path loss, which is usually between 2 and 4, that is related to environmental conditions**
* $G_T$: antenna gain at the transmitter
* $G_R$: antenna gain at the receiver
Antenna gain shows how well an antenna focuses radio signals in a particular direction, compared to an ideal antenna that radiates evenly in all directions. The higher the gain, the more focused the signal becomes in a specific direction.

*We define the power at the receiver*:
* $P_R=P_T*((G_T*G_R*\lambda^2)/((4*\Pi)^2*d^n))$

There is an exponential relation ($e^{-x}$) for power and distance.
![[Pasted image 20230619125549.png]]


RSS is available in all antennas, but its not very accurate. We can still exploiting this information that available on those device for localization.
**Note that RSS, in indoor condition worsen significantly, as there is no LOS given that there are obstacles.**
The ideal behaviour is to have **homogenous differences in signal strength decay, as can be seen here**
![[Pasted image 20230619145703.png]]
Instead the real behaviour is more similar to that:
![[Pasted image 20230619145744.png]]
**This is because of 3rd order reflection, which refers to a radio signal reflecting off of 3 surfaces before reaching the receiver.**

# Received Signal Phase
The estimation of the distance is **made by a measurement unit (anchor), which estimates the distance by the phase of the received signal**.
It is said that this holds within a wave length
This is because the phase of the signal repeats after each wavelength, so any phase measurement beyond one wavelength is ambiguous and cannot be uniquely resolved.

Then knowing the distance, the **algorithm of triangulation of ToA is used to localize the mobile unit**.
![[Pasted image 20230618222214.png]]
*It may be possible to use different signals with different wave lengths, as in ToA we used different signals with different speed*.
The problem is also that LOS is needed between transmitter and receiver.
# Signal Metrics final remarks

|          | TOA/TDOA/RToF                                                                                                        | AoA/RSP                                                       | RSS                                  |
|----------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------|
| Hardware | Requires special HW for synchronization, not available in commercial products                                        | Requires special hardware for angulation or phase measurement | Integrated in all antennaso          |
| Software | Requires special SW for synchronization not available in commercial products.  It needs complex routing algorithms   |                                                               |                                      |
| Issues   | Suffers Multipath  Needs accurate clock, with the issue that the accuracy also depends on the temperature for clocks | Suffers Multipath                                             | Suffers Multipath  Not very accurate |
| Positive |                                                                                                                      | Accurate                                                      | Available in off-the shelves devices |
# Processing Methods
We have two types of processing methods, using RSSI (Received Signal Strength Indicator), that is a standardized method. RSSI specifically refers to a standardized measurement of received signal strength that is commonly used in wireless communication systems. In contrast to RSS, which can vary depending on the specific implementation and device, RSSI is typically measured in a consistent manner across different devices and systems.

Here are the types:
* range-free approach: avoid to detect the distance using ranging by direct comparison of RSSI samples.
	* it is independent of channel parameters
	* its localization is imperfect **even with the ideal channel**. That is also because the algorithm is really simple.
range-based approach: detect the position using RSSI ranging:
* it depends on channel parameters
* potentially it may give a **perfect localization, if having the ideal channel**.

We may see that the localization algorithm finds the position of the Node using **the known anchor positions and the RSSI samples.**
![[Pasted image 20230619161526.png]]



## Algorithms per type:

### Range free
* Centroid: needs anchor placement done correctly
* DV-HOP: *works poorly if nodes move or are **unevenly distributed***
* APIT:
	* requires approximation *for being used in practise*
	* **it recognizes direction of departure via neighbor exchange of RSSI**
		* that is a problematic assumption
**Those have all low accuracy in general.**

# Range-based

* Multilateration: simple and scalable but noisy samples will affect it a lot
* Min-Max: simple and with limited performance. The minimum and maximum RSSI values correspond to the closest and farthest distances between nodes. The actual distance is estimated between these bounds. 
* Maximum likelihood: The most likely distance is estimated based on the RSSI value and signal propagation model that maximizes the probability. This one is **asymptotically optimum, but complex**

# Range-Free: Centroid
Periodically the anchor are saying: i'm here, in broadcast.
The anchor receive periodically positions, covering devices.
Then from all anchors for a user, it uses their average position to spot where they are.


You do not use ranging but *just deploy enough anchors.*

The algorithms in the mobile unit does:
* a loop where it listens for anchors
* calculates the average locations of all anchors that are in range
* returns as result the location estimate
We need coverage by the anchors!
![[Pasted image 20230619171928.png]]



# Range-Free: DV-HOP
Here we see the behaviour of the Anchors and Nodes.

Anchors:
* Flood the network with 
	* *known positions*
	* **average hop distance**
In turn the Nodes:
* Count the *number of hops to anchors*
* To determine their own positions, the nodes multiply the number of hops with the average hop distance

In the image we can see:
![[Pasted image 20230619172814.png]]
That there are:
* 3 hops from A to B
* We have avg hop distance 4.
**With that information we can know the distance A from B**
You have an average hop distance of 4 and you know that the distance between node A and B is 3 hops, you can estimate the distance between node A and node B to be approximately 12 units of distance (4 x 3).
# Range-Free: APIT
*The anchors divide an environment in triangular regions*.
![[Pasted image 20230619173318.png]]

*If an element, as seen the red, is inside a triangular region, we can narrow the area where it may reside*.
*The name of APIT* comes from
Approximate Point In Triangle test.

# Range-Base: MULTILATERATION

The algorithm is as follow:
1) Node (mobile) collects beacons (messages), with the beacon it estimates its distance from each beacon(anchor). It iterates over all the beacons it can collect****
2) The node will compute its position:
	1) It intersects all the circles that are **centered around the positions occupied by the beacons**. The radius of the circle is **equal to the estimated distance**
3) *The result from the intersection of the circles, which may be seen below, is an area where the node is likely to be found*

![[Pasted image 20230619180044.png]]

# MIN-MAX

The position **of a node in coordinates on a cartesian plane is* defined by this formula:
$d =[max(x_i-d_i),max(y_i-d_i)]*[min(x_i+d_i),min(y_i,d_i)]$ 
Here is the algorithm:
1) The node(mobile) associates
	* each anchor to 
		* **the signal strength of said anchor**
2) If the power decreases as the node is farther from the signal source, then if the node is closer it increases, basically **inverting the nominal distance-power loss law, the node estimates his distance from each beacon*
3) The node draws around each beacon:
	1) a pair of horizontal lines
	2) a pair of vertical lines
		1) It does so to express the fact that calculating minimum distance between:
			1) each line
			2) the beacon position
				* the minimum distance equals the **estimated node-beacon instance**. These lines are drawn in such a way that the minimum distance between each line and the beacon position is calculated. These minimum distances are used to estimate the distance between the node and the beacon.
			3) Consider that the anchor will be at the center of the rectangle, with distance **$d_i$** from the mobile as "radius".
1) The node localize itself **at the center of the rectangular area which**
	1) considers the innermost horizontal and vertical lines, meaning that is included in other areas, but that is the one *that is included and tinier, considering that its the intersection of multiple anchors lines*
That may be seen here:![[Pasted image 20230619182105.png]]

We may base on the recess, the min-max to find the location.

## Example
Given A1(0,4)
Given A2(3,3)
Given A3(1,0)
From A1 to A3

$d_1(A,m)=3meters$
$d_2(A,m)=2meters$
$d_3(A,m)=3meters$



This will be the situation graphically after we make the lines around each beacon
![[Pasted image 20230620100437.png]]
Based on distance and the pointers, we apply the min max formula. To get the x of the square and the y of the square.
![[geogebra-export (1).ggb]]
A1 taking 0 and doing -3 for the first element.
\[max(-3,1, -2),max(1,1,-3)\] *  \[min(3,5,4),min(7,5,3)] =$[x=1,y=1]*[x=3,y=3]=[x=3,y=3]$
**That is the position of the point**:
![[Pasted image 20230620100800.png]]


The point will be in the inner most "rectangle", in this its placement corresponds to point (3,3).

We may make squares, along with A1 and A2, and A3 a square of 3 meters as the distance. We will get an overlapping area with the distance over the points, getting at the center of the overlapping area the point searched.



# Maximum Likelihood.

A very difficult algorithm which mathematically is the optimum. 
We compute the probability of **the values r** received by RSSI.
Then maximize the probability that the one we chose is the actual position. We will arrive to the final matrix, which can be then used to solve a system.

In steps and formally:
1. **Data collection:**
    
    - Collect RSSI values from n beacons to create a vector r = {$r_1, r_2, ..., r_n$}.
    - The beacons have known coordinates in the x and y axes:
        - $x_B$ = {$x_1, x_2, ..., x_n$}.
        - $y_B$ = {$y_1, y_2, ..., y_n$}.
2. **Compute a priori probabilities:**
    
    - For each potential position $[x, y]$ of the mobile node, calculate the probability of receiving the RSSI values in vector r to get that position.
3. **Estimate the position:**
    
    - The estimated position of the mobile node will be the one that maximizes the probability obtained in step 2. This can be achieved by solving the corresponding system with the final matrix after computing probabilities.

We use r in two ways:
1) calculate the probability distribution for step 2
2) **determine the position estimate with higher probability at step 3**


We may see in depth

To minimize the MSE, which stands for Mean Squared Error, which is a commonly used metric to measure the difference between a predicted value and the actual value.
Create equations for each anchor.
$f_i(x_0,y_0)=d_i-\sqrt{(x_i-x_0)^2+(y_i-y_0)^2}$
We may try solve it by equaling it to 0, so
$f_i(x_0,y_0)=0$
**doing the square of both terms we may reach this point**:
* $-x_i^2.y_i^2+d_i^2=(x_0^2+y_0^2)+x_0*(-2x_i)+y_0*(-2y_i)$
* removing $(x_0^2+y_0^2)$ as it is possible to do so (they probably are a constant value)
* we ma subtract the n-th equation
* $-x_i^2.y_i^2+d_i^2 - (-x^2_n-y_n^2+d_n^2)$ obtaining
* $2x_0(x_n-x_i)+2y_0(y_n-y_i)$
**We obtain the system y=Xb** which can be solved doing b = $(X^TX)^{-1}X^Ty$
We may see how the matrix and vectors are organized:

![[Pasted image 20230620103847.png]]
In reality we have only 2 incognita, $x_0$ and $y_0$
X corresponds to the right side of the equation
y corresponds to the left side.

**It is much more complex than others, but the variance of the estimation error is minimizes as the number of observations grows to infinity, so if the number of reference beacons grow to infinity**.

***The Maximum Likelihood performance is limited by the fact that in realistic situation the number of beacons is very limited.***


# An analysis on Range-Based Algorithm performance

We may see, *how much the average localization error is reduced by using more anchors*.
![[Pasted image 20230620111812.png]]
* ML: the best, it shrinks a lot by adding anchors
* Min-Max: it starts with the lower error and improves but not by much
* Multilateration: it improves as its the worst with few nodes, but it does not reach minmax.
In general we can say that ML benefits from increasing beacons, the others not.


# Scene analysis



Using a couple of RSS measurements **it makes a map, with respect to anchors**.
The anchors may be different access points.
Using the access points, we get their measure of the RSS, then when we want to get the actual position at runtime using the measurement.
**A grid of points is made in a map to "divide it", a tuple of measurement is made for each point i in the map, the tuple of RSS measurements is defined as $R_i$ and defines the point distance in respect to the anchors**.
We will locate the mobile using the points RSS and the mobile measured RSS.

![[Pasted image 20230620112356.png]]
We see the anchors $A_i$ and the yellow points are the points . For each points **we will** have tuple of RSS measurements, as may be seen below.
![[Pasted image 20230620112826.png]]


The idea is match the measured RSS values to the RSS tuples associated with each grid point in the map.
We try to find the most similar points with the RSS measurement similar to the RSS measurement of the mobile, that allows to say where we are at runtime.
We see how **at runtime the mobile and the anchors produce new tuples**.
![[Pasted image 20230620113425.png]]


The algorithm works in this way:
**The position of the target in respect to the anchors produces**:
* a new tuple R made of RSSs
	* we compare R against all tuples $R_i$
	* *Mobile target position is approximated with the position of one or more points who have a tuple that is the most similar to R


The problem here is to find the best matrix, meaning the optimal set of tuples associated with a point. This may be done with neural networks, probabilistic methods or the KNN (k-nearest neighbors algorithm).

### Training the model
There are two phases:
1) Offline phase
	1) Collect fingerprints to train the network
	2) Construct fingerprint vectors $[(x,y),SS]$
2) Online phase:
	1) Match the RSS to existing fingerprints, doing so using:
		*  probabilities
		* or use a distance metric


We may see in the image the vectors of fingerprint, the anchors with their fingerprints and the position of the node.
![[Pasted image 20230620115816.png]]



Training a machine learning algorithm, with a target and so on, then one trains the network to associate a position to the RSS collected before, to then detect the target position.
We try to match the RSS with the existing fingerprint phase.



You may see here the phases in depth. With Access point giving samples for the points location. Those points locations, processed by the Machine Learning machine will be then stored in the DB and the algorithm will give the location of a moving object, using the database data and the fingerprint of the moving object.
![[Pasted image 20230620120344.png]]
We need to retake the fingerprint, if some object is moved in the online phrase.



# K NEAREST NEIGHBORS
We may have the KNN: K nearest neighbours.



The goal of the algorithm is to find k points for which the mean square error is minimized:
	* given $R=<r_1,...,r_n>;\forall_iR_i=<r_{i,1},...,r_{i,n}>;$R is the RSS sample for the mobile, $R_i$ corresponds to the one of the points.
* the mean square is of point $i$ = $\sqrt{1/n*((r_1-r_{i1})^2+k*(r_n-r_{in})^2)}$, we want to find k points where its minimum
**The position of the target can be estimated as the average position among the coordinates of the k points, which correspond to the best matching tuples**.
With WiFi access points, 3 or 4 five errors in meters were made. 
It may be good in big environment to know where something is in a room


# Neural Networks
It is similar to KNN.
Here the signal strength in that case are implicitly stored in a neural network.
We train the NN with:
* x,y as a target
* for each input tuple, the NN will output a pair of coordinates.

**The accuracy depends on the quality of the training, having home environment only 2-3 meters error were made, it is said to be the same for KNN**.

# Costs and Conclusions on Fingerprint

It has a cost to setup those type of localisation.
* Configuration costs: as you have to construct the DB or train the NN at deployment
* Maintenance cost: you need to **reconstruct the DB or re-train the NN at every environment change**
Basically they are good when used in static environment and is better to use for a long time, else its a waste to construct.

# Device-Free Localization
Device Free localization is another processing method, different than the previous ones.
*It allows to track humans without a device*.
It exploits RSSI degradation under the influence of the human body.


There is a DOPPLER effects, which is a change in wavelength of frequency of a signal receiving by a **moving observer receiving the signal from a base station (an anchor in our case**. 
The signal that is affected by that and is used is a MIMO CSI signal.
* MIMO: it uses multiple input and output antennas to better transmit and receive the information 
* CSI: Channel State Information, its the information that about the wireless channel condition that both transmitter and receiver exchange
* MIMO CSI is the **phase information** of the received signals captured by the receiver antenna. *MIMO uses the phase of the received signal to enhance the signal strength, basically suppressing interference from other directions.



To do Device-Free localization, we need Massive MIMO;
* Massive MIMO (Multiple Input Multiple Output) is an advanced wireless communication technology that utilizes a large number of antennas at the base station (also known as the access point or transmitter) to serve multiple users simultaneously. It is an extension of traditional MIMO technology that typically employs a smaller number of antennas.

**This works in both small and big areas and is capable of doing gesture and activities recognition!**
In an experiment they put a lot of ZigBee devices outside, and they were transmitting to each other a message. In a kind of circle, the human user placement created a sort of cloud, where the RSS was much lower than before. The user had no device at all, but it moved on the environment, modifying the signal from there, allowing to the detect the user in the field.









# Radio Tomography

Radio Tomography is a wireless sensing technique that utilizes signal strength measurements from a network of radio transceivers to create a tomographic image. It enables the detection and tracking of objects, as well as monitoring changes in an environment without the need for visual or physical contact.
The nodes are disposed in a way to make a squared area.
![[Pasted image 20230620145940.png]]

We can see in the image how we have nodes with unique links, that are specific paths or connections between pair of nodes in the wireless network, directly communicating.
**Each device will measure for each pair of nodes the signal strength between them**.
We see how an object attenuates them!


# CSI-based
In Orthogonal Frequency Division Multiplexing (OFDM), multiple sub-carriers are used for data transmission. These sub-carriers are carefully designed to be orthogonal, meaning they do not overlap in frequency. On the other hand, in Frequency Division Multiplexing (FDM), different channels can be exploited since they occupy separate frequency bands.
![[Pasted image 20230620151824.png]]
We use OFDM systems, as data are modulated on multiple subcarriers (carrier = a base frequency) that are in different frequencies (so they use different base frequencies) and they are transmitted simultaneously.
Channel State Information (CSI) is crucial for optimizing wireless communication systems. In OFDM, by leveraging the CSI obtained from the overlapping sub-carriers, one can access information at the network interface level, requiring lower-level access for obtaining this data. However, not all network interfaces provide access to CSI, limiting its usability.

You get a lot of information from each packet send, and one can use this information to detect how a body impacts a signal.
In this case case the user must move or its not spotted, it the user does not move, then there is no information on the position. 
It may be useful to use CSI-based localisation for gesture recognition.

**We use for each carrier, the information it gives about phase and amplitude, to get**:
* fingerprints
* to do Multilateration
* to use MIMO Arrays and understand from where the signal comes.
![[Pasted image 20230620152147.png]]
You see in the image the distance d from the first and second antenna in the antenna array, and how the way form has a phase difference on both.
An incident wavefront is the leading edge of a wave as it interacts with a medium or object. It determines how the wave is reflected, refracted, or diffracted.
# Proximity

We may not need to know the position, but just be know if we are near something, a reference point for example.
In this case Proximity techniques are optimal.
Using the power, since the distance makes it exponentially decrease.
If there is an high power, then you are near that object. 
**We will have low precision but this technique is very cost effective, as there is not special hardware required for finding the ranges**.

This technique may be implemented in two ways:
* *topology based*, as we count the hops. 
* RSSI: setting a threshold on them
Obviously you have a low precision.
# Location error: Performance Metrics
We want to compute and measure the error.
For that we have two metrics:
* Accuracy(location error)
* Precision
## Accuracy
It may be done with accuracy checking the distance between real position and **estimated position of the target**. 
The distance between real and calculated position may be seen as the hypothenuse of a triangle, which is calculated with the following formula.
$d(p,q)^2=(q_1-p_1)+(q_2-p_2)^2$
![[Pasted image 20230620154513.png]]

## Precision
**We use that to measure the self-consistency of the system, as it may give different result for the same situation.**
Precision is *an indication on the variation of accuracy*. We check basically in different trials *how the acucracy varies*.
**What is measures is:**
* the distribution of the localization accuracy

## Goal
We want basically a system that is both precise and accurate.
**The mobile unit is at the center of the cross**
![[Pasted image 20230620155023.png]]

The points are all scattered, some even outside of the circle, in the worst case:
![[Pasted image 20230620155056.png]]
If we have accuracy but not precision, then we give results that are near the correct point, but *not the same results*:
![[Pasted image 20230620155221.png]]
Having precision but not accuracy **we constantly give the wrong answer :)**:
![[Pasted image 20230620155306.png]]
Then with precision and accuracy we **have a really low error for every position estimation, correctly guessing the point location or really being close to it/touching it**.
![[Pasted image 20230620155358.png]]


# Other measures
Other than precision and accuracy, we may have other measures.
We may have the measures for:
* resolution: the level of detail, limiting the error
* scale: how big is the deployment.

We may say that:
* large resolution is ok, for guiding, tracking and routing
* tiny resolution is **required for automation and control, for example in industrial system**.
ZigBee, Bluetooth, WLAN technologies, are good indoors and have a resolution of less than 10 meters, around 10.
**GPS is good for outdoor and has a resolution of 10 meters, with GPS assisted by Wireless, we get less than 10meters, around 5meters**.


## Complexity, Robustness, Scalability

* Complexity: the complexity based on
	* hardware
	* algorithms
	* deployment maintenance
	* communications (number of them required and their complexity)
* Robustness: related to
	* noisy signals
	* failure of anchors
	* susceptibility to missing LOS.
* Scalability:
	* the cost to cover an increasing large area
* Costs(monetary):. which are effected by the type of deployment, we have costs initially and for maintenance


# Future Directions




As of now information about location can be obtained from multiple devices and the trackers may be of different type. 
As can be seen here we can have for a smartphone:
* internal sensors, accelerometers, gyroscope, digital compasses and even the camera
* the may track it with satellites using the GNSS
* RF (Radio Frequency) Signals; using RFID/NFC, Bluetooth to connect to devices such as smartwatches, WLAN and using **the cellular network** or even Digital TV.


As such we can fuse together those sources, to really improve the tracking.

## Data Fusion
The research focus today changed to Data Fusion.
Not only understand where a mobile device is using signals on a map, but use location, proximity and inertial systems (gyroscope and proximity sensor) to improve its localisation. 
We may also use images and visual computing.
There could also be running ILS(Incident Light sensors) simultaneously

There are state of the art algorithms such as:
* Kalman Filter
* Particle Filter


Using geofencing we may for example reduce the area of interest, then we may use the particle filter
In this way we have a narrower area where its possible to find an object.
In the context of a particle filter, geofencing can be used as a means to constrain the search space and focus the estimation process. By setting up geofences around relevant areas or regions where the user is likely to be located, you can limit the particles' movement or resampling process to within those boundaries.


# Bluetooth AOA
There is a field of research of Bluetooth, to get the angle of arrival of Bluetooth, allowing to put Bluetooth beacons to detect the angle of the antenna to cover a large area. 

Given a tag, which is a device that is equipped with **a Bluetooth transmitter**.
There is a Angle of Arrival locator that calculates and obtains:
* the heading angle of the tag
* pitch angle of the tag
* a unique ray
Then according to the *tag height, the AoA can calculate and obtain a unique spatial* **absolute** coordinate.
![[Pasted image 20230620165515.png]]
We may see that there is a precision of 0-1-0.5 m for objects really close.


If AoA locators are **combined strap-down, meaning that the AoA locator is attached to the object being tracked, allowing the locator to move with the object, then the AoA locator obtain a larger positioning coverage space**.
It also obtain multiple anchor course angle calculations, which means the measurements between each anchor and the tag being localized.
In general this improves the global spatial accuracy level!


# Ultra Wide Band Time Of Flight, Time Difference of Arrival, AoA

There are device that allow to a use of ultra wide band. With that its possible to use the Time Of Flight algorithms.
We may also use the time Difference of Arrival paired with Ultra Wide BAAND.



, and ultra wide band uses the time of flight and the time difference of arrival.
With TIME OF FLIGHT: (hyperbola one) you may manage walls, with time distance of arrival instead its tough.
Time of Flight (TOF) based algorithms, such as UWB TOF, can be advantageous in scenarios where obstacles like walls are present, so we may use that in this case.
While Time Difference of Arrival may struggle with walls.

**For close-in applications, the TDOA(Time Difference of Arrival**) methodology is the one used.

![[Pasted image 20230620173229.png]]
We may see in this table the comparison of ToF and TDoA
![[Pasted image 20230620173257.png]]
We see that we have different advantages and disadvantages in both.
TAG capacity refers to the number of devices  that can be tracked. *simultaneously by the system*.
## Using AoA
For *long range application we may use a* two cluster AoA tracking method.
**Note that if we want the angle of arrival, there is the probable that  we need the phase of the signal, so low hardware access is needed. In the new Android OS, they will allow this possibility to the network interface, opening a lot of scenarios with localization systems that are low cost.**


## Bluetooth AoA vs UWB


![[Pasted image 20230620173558.png]]
**Comparing Ultra Wide Band vs Bluetooth AOA, more or less Bluetooth is better, but Ultra Wide Band is more robust.** So you may use one or the other depending on the case.



For example AoA is compatible with multiple devices, while UWB requires specific UWB Tags and has an higher cost and power consumption.
The accuracy is a bit better for UWB.




 <div style='page-break-after: always'></div> 


# Chapter 17: Wireless Sensor Network
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


 <div style='page-break-after: always'></div> 


# Chapter 18: The ZigBee Network Layer

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

 <div style='page-break-after: always'></div> 


# Chapter 19: Wireless networks
Cyber-physical systems embed software and have hardware but are defined by their place in the environment, so we need wireless because of their placement. The hosts are often mobile and battery-powered, such as smartphones and sensors.

We are not sharing cables, so those nodes must coordinate themselves with the shared medium, using an **infrastructure such as a base station, which will be linked to wired access points**. The infrastructure networking will have a **coordinator**.
Instead, ad hoc networking does not have a coordinator, so the devices must coordinate themselves.

The devices communicate in a wireless networking, and we have the base station where devices can communicate with each other. To make them communicate outside of the networking, we may have from the base station:

-   a wired link
-   or wireless link

The end devices are connected wirelessly to the base station, those can be mobile. Sometimes we may deploy cables but have a wireless link as a redundancy, wireless doesn't mean mobile, so a device can have a wireless connection without moving itself.


# Problems

One problem of a wireless access point is how we access the medium and how to coordinate the device is addressed by multiple access protocols. Also, the problem may be handoff if a user moves from a base station to another, then the communication must move from BS1 to BS2, and the BS1 sends info to BS2 some control messages to also seamlessly do this handoff. It is ok with cells of the same operator, difficult with cells of another operator.

## Evolution of wireless standard 802.11

Some standards have different **data rates** and different coverage for WiFi. 802.11af, for example, is made for the internet of things and can go up to 200, to 4 Km almost. When speaking about these **data rates, we have both theoretical measures and throughput measured in different environments**. The values can change depending on how they were measured.

4G gives a longer coverage with ok bandwidth, and 5G has a shorter coverage than 4G but with more bandwidth.

## Infrastructure Single Hop

An infrastructure wireless network, where a host makes a _**single hop**_ to connect to an access point. This is the case of the mobile network or WiFi, you connect to an access point and then have the support of the infrastructure.
The central coordinator usually is the base station, all communication must traverse the base station, managing the **resource of the physical medium**. In a wireless network, we have an access point, and in mobile, we have **cell towers**.

## Infrastructure Multiple Hops

You have one access point, but you have a relay node that the devices reach, and from there, the communication is forwarded to the access point. This is the case of a mesh network.

## No Infrastructure and One Hop

No base station, but connect directly nodes.

## No Infrastructure and Multiple Hops

Networks must coordinate so that each node makes routing decisions to forward packets in a path.

Some examples: VANET: Vehicular networks, ZigBee networks: different nodes that communicate, with one node that may be connected and elected to do it, as a relay to the internet.

## Problem of Wireless

We have electromagnetic waves going in the free atmosphere. So, the signal strength:

1.  Reduce as the distance goes, since some obstacles can block the waves.
2.  Experience interference from other sources. We not only have cables isolated with other specific material, but we have frequencies. Other frequencies in the environment may be mixed, either by other devices emit signals and there is noise in the environment, so the signal received can be the sum of those.
3.  Experience multi-path propagation. We may have radio signals that are reflected by different surfaces, and we need to reconstruct the signals as they are combined and have different magnitude and different phases.
4. Limited knowledge: a terminal cannot hear all others, and there are hidden exposed terminals. Mobility or failure of terminals may make us lose a terminal. Terminals may be dynamically connected and disappear, so the network must cope with this.
5. Coordination of access: CSMA/CD cannot be used in the wireless channel. In physical layer we can find CSMA/CA or at network layer usage of IP but different routing and can be without infrastructure.
6. Obstacles: given that there may be a wall, which prevents two devices from detecting each other, while they can talk with a central host. According to how those hosts are positioned in distance:

	-   A has a large signal strength to B, but when we arrive at B the energy of the signal decreases, and B can detect it.
	-   With higher distance, A is not able to detect C signal.

	Also, since B may receive two different signals at the same time, there will be a collision.


# Metric on Communication Environment

Metric to evaluate the quality of communication: SNR: energy signal / noise, measured in dB. A large SNR is better, it means that there are a low noise respect to the overall signal. We compare that with modulation, being how you imprint information on electromagnetic waves, send a series of bits, which are information and must be sent with amplitude and phase frequency, in the medium of the hair.

Bit error rate (BER): probability that information is transmitted with an error.

With different modulation techniques, we may have higher or lower data rates. E.g. BPSK has a lower data rate, and if we increase the signal-to-noise ratio it  increases the energy of the signal, we lower the BER.
For QAM16: you need more energy to get the same BER than BPSK at a certain level, as you send more information.


# MAC Layer

Assumption: for all communication, we have a single channel that may be shared by more than one node. All the station use the channel to transmit and receive data. Some communication may overlap, so the receiver may not be able to reconstruct the signal from the signal received. **All stations may detect collision**, so the receiver may not be able to reconstruct the signal from the single received.
**All stations may detect collision**.


## CSMA/CD

CSMA/CD is a protocol that was developed for Ethernet networks with a hub at the center of a star or shared bus topology. In this protocol, a station must first sense if the channel is idle before transmitting. If the channel is busy, it waits until it detects that it is idle before starting transmission. At time $t_0$, the channel is idle and the station starts transmitting.

However, collisions can occur during transmission, and station B may detect the collision only at a certain point, t2. When a collision is detected, the station that detected the collision stops transmitting.

To prevent collisions, there is a random interval of time where a node sleeps. The time interval is random, and if it is not long enough, there is a higher probability of having a collision again.

The minimum unit of time to wait is one contention slot, which is equal to 2T, where T is the time it takes to reach the farthest station in the network. The collision slot corresponds to the minimum Round-Trip Time (RTT),**the RTT represent the minimum time to detect a collision.**

The collision takes time to be noticed, as it must reach a node that receives two signals before being detected.

![[Pasted image 20230302100358.png]]
Diving in mini slots a system, where a mini slots has duration 2t (equal to 2T), when a node start to transmit at the beginning of a mini-slot, what happens at the end of the mini slot is:
* no collision occurred, so no interruption to the transmission
* a collision occurred by the end of the mini slot, so the channel would be idle again.


A collision at most affects a mini slot:

![[Pasted image 20230302100439.png]]

The algorithm used in CSMA/CD has binary exponential backoff. After the first collision, each station waits for 0 or 1 slots before trying again. After collision i, the station chooses x at random in the range \[0, 2^i - 1\] and skips x slots before retrying.

After 10 collisions, a random interval is chosen and frozen at 0-1023. After 16 collisions, the protocol reports the collisions to upper levels and takes action to prevent further collisions.


# Why does this approach not work with wireless networks?

1) The transmitted sides is sensing if there is another sending a signal in the channel. In wireless is not possible to both transmit and receive(at least with 1 antenna), the problem is that you transmit your signal with high energy, the one you receive has low energy, so it happens that you do not recognized the other. With wireless trans-receiver you cannot detect collision
2) If a node is out of range, it may not note a collision, this problem is a hidden terminal.
3) If a node senses two different nodes (that don't senses each other) and want to send a message to one, it have to check if the third isn't transmitting. Otherwise it will create a collision, but without interference. This problem is called exposed terminal

# Hidden terminal problem

A can receive and transmit to B.

* A sends to B.
* C can send to B and D (not A).

If C wants in the meantime to transmit to B, then it does not sense any signal from A, it starts transmitting, so we have a collision on B.

So the problem is defined as:
C is not able to detect a collision **at B the receiver**
A doesn't too, as they are out of their range.
So **C is HIDDEN with respect to THE COMMUNICATION FROM A TO B**.
![[Pasted image 20230301103651.png]]

# Exposed terminal Problem


B can transmit to C and A.
C cannot transmit to D.


C cannot transmit to D, as there **it senses that the physical medium is occupated, so it cannot transmit to D**.
It is a problem as B is transmitting to C but not receiving, while C could transmit to D, and there would not be interference to D.


**Problem: cannot send data as there is the interference from another transmitting station, even if the receiver is out of the interference.**

![[Pasted image 20230301104148.png]]
# Solution MACA

MACA: Multiple Accesses with Collision Avoidance.
Ideally avoid collisions, trigger an exchange of sender and receiver to see that channel is free and advertise to other that communication will happen.

A wants to transmit to B, check the channel and it sends a **REQUEST TO SEND(RTS), with the information of length of the following information**.
All nodes in the range will receive this RTS.
B which is a recipient sends a reply: (CTS) Clear To Send, with the data length copied by the RTS (in this mode even who has not eared the RTS know how much time have to wait).

The CTS arrives to A, which sends the data frame.
C has heard the RTS in the range of A, but it did not receive the CTS from B. So C is in the position that *it may be exposed to their communication*.
Giving that C doesn't hear the CTS, means that it is exposed so it may send transmissions (as B is just sending not hearing, and A is not in range).

Since D receives a CTS, and B receives data, it cannot start transmitting as its transmission is in the range of B.

If both are received such as E, it have to wait.

If we want to transmit from C and B to A, both C & B send an RTS, then A does not recognize the RTS due collision, so no CTS send by E. Basically, if there is a collision of RTS, then there is no CTS. So both nodes that send the colliding frame will wait with Exponential Backoff.

# MACAW
This is a fine tune of the original MACA.
ACK frame: add acknowledge reply to a data frame.
Carrier Sensing: station recognize if there is a signal in a nearby station, so to prevent that it sends an RTS when a nearby station is *transmitting to the same destination*.
Then there is the exponential backoff, run for separate pairs of *source and destination, instead of being run for the whole station communications*.
Stations have ways to recognize temporary congestion problems.
CSMA/CA is used in [[IEEE 802.11]] and it is based on MACAW

## Question 3
![[Pasted image 20230302095038.png]]

B did not receive the RTS and CTS, and D is receiving data, but B did not receive the CTS, if B sends a RTS, there a collision in D

 <div style='page-break-after: always'></div> 


# Chapter 20: Mobile Network

## Evolution of Cellular Networks

In the past, there were a low number of devices connected with wires. However, the current state of cellular networks is vastly different. There are now 10 wireless devices for every one fixed wire phone,so we have a rate of 10-in-1 subscribers for wireless devices. Additionally, there is now a 5 to 1 ratio of mobile broadband-connected devices to fixed broadband-connected devices.

With the advent of 4G/5G cellular networks, Internet protocol stacks, including Software Defined Networking (SDN), are being embraced. Mobility has become a significant consideration for users and operators, who now advertise connection services for users on the move. Operators must manage user authentication, verifying the user's identity and checking whether the requested service is within the user's service realm.


## Components of Cellular Network Architecture:
![[Pasted image 20230302151031.png]]

Base Stations are similar to Access Points (AP), which cover a specific area and operate in conjunction with other functions within the remaining infrastructure. From 1G to 5G, the Base Station has undergone a few changes. The Mobile Switching Center handles setting up connections between end-user devices, authentication, and resource localization. Usually, a Mobile Switching Center handle tens Base Stations, and some may serve as a gateway to the Public Telephone Network. There can be multiple levels of Mobile Switching Centers within a network.

![[Pasted image 20230302151143.png]]

***1G networks*** used Frequency Division Multiple Access (FDMA) and only analog signals. FDMA consist in divide spectrum in channels and divide them in time slots (TDMA). Combining these twos is possible to have a division that allow multiple access to the station.    

***2G networks*** introduce digital signal called Global System for Mobile Communications (GSM), focusing on voice communication. The mechanism used here is the code division multiple access (CDMA) that is a partitioning of code space, since digital signal are used.   The introduction of text messaging surprised many since it was not expected to be as popular as it has become. 2G introduced significant changes to the architecture compared to 1G.

***3G networks*** included data and voice communication with the internet, extending the architecture further from 2G. There is the parallel usage of both previous voice network and the new one. The partition of code is done by Wideband CDMA (WCDMA), an evolution of CDMA.

***4G networks*** introduced significant changes to the architecture, introducing principles of software defined approach with virtualization technology inside. The network architecture became like a distributed data center, with links and processing resources. Here, is used Orthogonal Frequency Division Multiple Access (OFDMA) to partition the communication.

***5G networks*** are similar to 4G in the architecture but is used OFDMA or Non-Orthogonal Multiple Access (NOMA)

![[Pasted image 20230302151212.png]]


### Techniques to Access

***FDMA*** the basic idea is to divide a frequency band into sub-frequencies and assign each sub-frequency to a different node. In Time Division Multiple Access (TDMA), time slots are assigned to nodes. Combining FDMA with TDMA allows a frequency channel to be divided into time slots to serve more stations.
![[Pasted image 20230302151248.png]]

***CDMA*** uses codes rather than dividing frequencies or time. A code is a sequence of bits sent at a higher data rate than the information sent. Each station transmitting has a code that is distinct from another node code. The receiver receives a sum of the multiplication of data and code, creating an average to get the data. If the receiver receives multiple messages from different senders, the data is decoded using the summation operation on the receiver.
![[Pasted image 20230302151514.png]]

## 2G Voice Network Architecture
The Base Station Controller (BSC) decides how the medium's resources should be used, and both the sender and receiver must be aware of the code to use. The Mobile Switching Center (MSC) is used for circuit switching.

2.5G added data management to the network.
![[Pasted image 20230302151753.png]]

It uses in GSM:
* TDM (time division multiplexing)+FDM (frequency division multiplexing): using the 200 Khz frequency band, where each band supports **8 TDM calls**. FDM  allows the sharing of multiple low bandwidth signal with high bandwidth frequency range in the physical layer.
In the 2.5G (GPRS - GeneralPacketRadioStation). where *data transfer besides voice was enabled*:
*  uses CDMA to access the data link layer.
* it reserves automatically time slots for data transfer of 40-60 kbps

## 3G Network Architecture

There are local resources assigned to manage data communication. The MSC has a parallel branch to the Public Telephone Network. The Serving GPRS Support Node (SGSN) connects mobile devices to the Public Internet via the Gateway GPRS Support Node (GGSN). The radio network controller is the actor that manage the communication between the radio station.

What happens in this layer is that, the **cellular data network operates in parallel with the existing voice network, only at the edge they share the radio network controller**.
The voice network is unchanged in the core, with circuit switching.

While the data network operates in parallel, with Packet switching the SGSN (Serving GPRS Support Node) represents the access router, from there the packets will be routed in the internal domain of the provider, until they reach the Gateway GPRS Support Node, that connects to the public internet.

![[Pasted image 20230302153658.png]]


## 4G-LTE
4G may change depending on release, for example LTE is one release.

![[Pasted image 20230315094613.png]]

For access, we have a set of base station, forming a radio access network.
For the links:
* dashed lines mean control, the messages exchanged to signal and management, for example authentication and attaching to a network so associate with it, the message go through it. MME and Home Subscriber server are involved in the control plane.
* The continuous link are the links in the data plane, S-GW, P-GW serve that plane.

In this standard, there is no separation between data and voice plan, all traffic is carried over IP core to gateway.
So **the datagram switching is also used for voice calls,** and the voice calls traffic goes through the internet services, using the same paradigm, allowing to simplify the management of services.

##### Similarities to wired Internet
* With 4G/network  **as we have IP as a common protocol to forward information**
* The difference between wired internet and 4G/5G networks are: the edge **terminal part of the network, on one side mobile devices and other application servers. Then the core is different, which forwards packets and in the case of a 4G operator have also the role of authenticating the devices**.
* Mobile operator have their own network, with datacenters, but we have also a  global cellular network which is  a networks of networks, so there is an interconnection for mobility in different country..
* Mobile networks are also interconnected to the wired internet, allowing to access the wired internet services (youtube, google etc...)

##### Differences to wired internet
- different wireless link layer: AP on one part and BS on the other
- users are identified with the SIM card. So there is an authentication, and since there is this authentication, the mobile operator is able to allow mobility, this functionality for example is not possible with WiFi.
- The business model is different, as there can be roaming and mobility into this case., there is an inter-carrier settlement for all users.

### 4G architecture in depth
We do not have as in 3G the Radio Network Controller managing the base stations.
Here have **base stations,called eNodeB and Mobile Core that splits the Radio Network controller Functionalities**.

![[Pasted image 20230315100240.png]]
#### Mobile core:
* it provides IP connectivity for data and voice services
* it ensures QoS requirements are met
* It tracks *mobility of the user to allow for uninterrupted service*
* it handles the billing and charging

##### RAN: radio access network:
It consist of the distributed collection of Base Stations, it *manages the radio spectrum*.

##### Backhaul Network
Connection between the base station, usually in wired mode with fiber optic or sometimes even with a wireless link.
It also interconnects the RAN with the mobile Core.
For instance, Integrated Access Backhaul (IAB), allows to use the backhaul network in wireless mode, using the same frequencies of user equipment or different.

#### Network architecture control path
![[Pasted image 20230308163515.png]]

- UE: *user equipment*
- eNode-B: base station
- HSS: The Home Subscriber Service has information about **subscribers, so have information and credential of the information relevant for the** authentication part. It is basically a database, it stores information about mobile devices, for which the *HSS network is their home network, it will work with the MME device to enable authentication*.
- MME: the Mobility Management Entity is a third party between **base station and HSS**, when the UE provides information from SIM, the MME receives it. The HSS, MME, Base Station and Mobile device will exchange message, to make a mutual authentication between mobile device and network.
	MME allows to do:
	* device handover between cells
	* tracking the movements of the device. 
	* *Paging*: ask the BaseStation for the presence of a device, to find if it went out of the network. 

	A data path, to exchange data is **setup** by the MME.
	
* Serving Gateway (S-GW): it forwards IP packets to/from the RAN. **It handles inter-eNode-B handovers and provides mobility between 4G and other type of networks**.  So it must be placed before P-GW to facilitate the handover to a 2G/3G network. A group of base stations are management by a single S-GW. We have a remote subscribing network.
* PDN Gateway (P-GW): *it represents a gateway to the mobile cellular network, similar to any other internet gateway routers*. It provides NAT services and support additional access-related function, including policy enforcement, traffic shaping and charging.
* generic routers: *there are other routers in the architecture which forward packets.

### 4G architecture flexibility

Mobile core components may be flexibly deployed to serve a geographic area.
![[Pasted image 20230315103744.png]]

A *single pair of MME and P-GW may server a metropolitan area*. Using 10 S-GW deployed through the city and with 100 base stations. There can be alternative deployment configuration by the specification of 3GPP

#### Plane separation
We have separation of data plane and control plane on routing.

In the **control plane** we have protocols for:
* mobility management, security and authentication
In the data plane we have protocols at link and physical layers, with extensive use of tunneling to facilitate mobility.

In the **data plane**, the data path is setup by realizing two tunnels:
1) First tunnel from base station to S-GW (terminal point)
2) Grom S-GW to P-GW.

![[Pasted image 20230315105149.png]]

The Base Stations forward both control and data plane packets between Mobile core and UE. Can see how the Mobile Core will support both Mobile Core Control Plane and Mobile Core User Plane:
![[Pasted image 20230315184828.png]]


#### Control Plane
The control plane packets are tunnel over SCTP/IP, where the **Stream Control Transport Protocol**, is an alternative and reliable transport to TCP.
Which is made for **carry signaling** (to send **control** information) information to telephony services.
Also the UE authentication, registration and mobility tracking are tracked in the control plane.

#### User Plane
The user plane packets are tunneled over the **General Packet Radio Service Tunneling protocol**. GGTP is a 3GPP-specific tunneling protocol, it runs over UDP.


## LTE data plane Protocol Stack

![[Pasted image 20230308165126.png]]

We see how from the Base Station, the GTP (**G**eneral Packet Radio Service **T**unneling **P**rotocol ) sends, over UDP, to the S-GW(serving gateway), the **encapsulated mobile datagram**.
S-GW re-tunnels the datagrams to the **PDN Gateway(P-GW)**.

Serving gateway is a fixed point, needed as we have the tunnel if we change base station or S-GW, we can just change the S-GW.
**So to support mobility, basically only tunneling endpoints change when the user moves.**

At the fist hop:
* UE has a datagram and sends it to the Base Station, under IP there is the Packet Data Convergence, Radio Link and Medium Access protocols.
* The Base Station has from the physical, to the Link and up to the IP layer, since it isn't involved in application layer.
![[Pasted image 20230315190044.png]]
- Packet Data Convergence has header compression/decompression and header encryption/encryption
* Radio Link Control (RLC) is the protocol for fragmentation and reassembly of transfer units, enabling reliable data transfer.
* Medium access: it is the protocol to request and use radio transmission slots.

### Channels

LTE radio access network has two streams:
* downstream: Orthogonal frequency division multiplexing OFDM (frequency and time multiplexing, guaranteeing the minimal interference)
* upstream: there is a combination too of FDM and TDM similar but not OFDM.

**Depending on the release, the frequencies are allocated in time slots of 0.5 ms.**
The scheduling algorithm is not standardized with operators, but by this time slots, but can reach 100 Mbps per device.

### Associating with a BS
![[Pasted image 20230316094820.png]]
1) BS broadcasts a **primary sync** signal. It does so for every 5 ms and on all the frequencies. It must be accounted that multiple carriers broadcast sync signals.
2) The UE finds a primary sync signal and locates a second sync signal on its frequency. The UE may find information broadcasted by the BS, such as channel bandwidth, configurations and BS **cellular carrier info**. The UE may get information from multiple BS of multiple cellular networks.
3) The mobiles selects to which **BS to associate, favoring its home carrier**.
4) subsequent steps to authenticate, set up a state and set up the control plane.

#### Save energy with Sleep Mode
The LTE module may go to sleep to preserve battery. There are two possible sleep phrase:
* light sleep after 100msec of inactivity:
	* periodically wake up, with a rate of 100msec to check for downstream transmission
* deep sleep: after 5-10 seconds of inactivity
	* then it means that if the device changes cell, it must re-establish a connection to another base station.There may be paging coming from the BS and send by the MME where it is asked about the mobile device.

## 5G
New frequencies ranges, new antennas, use of millimeter range frequencies. Millimeter wave frequencies allows for higher data rates, but over shorter distances.

* 5G New Radio:
	* has millimeter waves frequencies
	* it is not backward compatible with 4G
	* MIMO: there are multiple directional antenna
* millimeter wave frequencies: much higher data rates over short distances.
	* The cells are pico-cells, large 10-100 m (not much)
	* there is the need of having a massive and dense deployment of new base stations.

(List of 5G functions will not be asked at the exam, but the principle will be)

#### 5G use cases:
![[Pasted image 20230316101636.png]]

We can categorize it into multiple parts.
* extreme mobile broadband: high peak rate in the order of Gigabit/s, having 100 Mbit/s everywhere and much more traffic than 4G
* Massive machine communication: give long battery life so less energy consumption, with ultra low cost and have a real big sensitivity of devices per kilometers square.
* Critical Machine communication: zero mobility interruption, low radio latency and ultra reliability so really low end point to endpoint errors.

#### 5G architecture
The 5G Core network is:
* designed to be integrated with the internet and cloud-based services
* It has a ***complete control and user  plane separation***. It does it with virtualised software network functions.
* network slicing allows to flexibly meet the diverse requirements of the different 5G applications.
![[Pasted image 20230316102555.png]]
The dashed lines are for the *control plane*, the plain lines are for the *user plane*.

### UPF User Plane Function

This function is a microservice (so it can be scaled), where a user plane function have the task of:
* packet inspection
* application detection
* trace and reporting
* QoS management
Those task are in microservices, where they can be scaled up and deployed freely.
The User plan functions **forwards traffic between RAN (radio access network)** and the Internet. 
It maps to the *combination of S-GW and P-GW of the 4G (EPC: evolved packet core)*

The UPF can be put both close to the base station, thus have better latency so they are be co-located in the edge, or they can be in the network core, in central data centers.

The UPF allows then for: [[Multi-Access Edge Computing]], which can be done by using base station.

![[Pasted image 20230316103235.png]]
It can be seen how the UE goes through the gNodeB (BS) and then directly to the UPF, which in turns connects to the Data Network.

### Control plane

#### Inherited from 4G
In the control plane we have a stateless functions, so there is better scalability. The solution is a *cloud native solution*.

![[Pasted image 20230316103955.png]]
* AMF (Access Mobility Function): directly connected to the base station. It allows for connection, reachability, mobility management, access authentication and authorization, then for location services. **It servers part of  purpose of the MME of 4G**.
* SMF (Session Management Function): it manages each UE session, including IP address allocation, selection of associated UP function, control aspects of QoS and control aspect of IP routing, **it performs part of the purpose of the MME and the control aspects of P-GW of 4G**.
* PCF(Policy Control Function): it manages the policies of charging and billing rules.
* UDM (Unified data management): it manages user identity:**including credential authentication, doing the same task as the HSS of 4G in conjunction with the AUSF**:
* AUSF(authentication server function): an authentication server, doing the task of HSS.

#### Non-Existing for 4G
![[Pasted image 20230316150135.png]]
* SDFS: Structured Data Storage Network Function, it is an **helper service** used to *store structured data*.
* UDSF(Unstructured Data Storage Network Function): a means to **expose selected capabilities to third-party services**
* NRF(Network Repository Function): a means to **discover available services**
* NSSF (Network Slicing Selector Function): A means to select a Network Slice, to serve a *given UE*. Where network slices are a way to partition network resources in order to differentiate service given to different users.

## Types of 5G

We can have:
* Non-Standalone 5G
* Standalone 5G. In this case the base stations are all 5G stations and the control plane and data plane go through them, the core is the 5G Mobile Core (New Generation-Core)

In the non Stand-alone 5G, the mobile provider have their 4G mobile core network, then they deployed 5G Base station, which are using the 4G mobile core.
This leads to an improved data rate, but the control plane is still managed by the 4G, while the data rate may be managed by the 5G stations.
The stand alone 5G is much rarer, as it is costly.

![[Pasted image 20230316153242.png]]
The choicest is a mix of 4G and 5G base stations.

### Global Cellular Network: a network of IP networks
Having the HSS being the one to identify UE and give service info while roaming in the home network. The P-GW will have a link to the public Internet and **inter carrier IPX** meaning that **carriers interconnect withing each other at exchange points**.
This interconnection allows via connect other P-GW that *visited mobiles network for the UE*.
So with a SIM, a UE is identified globally, identified also by its home network. The SIM can then allow the UE to connect then to its home network or to a BS of another network in Roaming.

![[Pasted image 20230316153700.png]]

![[Pasted image 20230316153957.png]]


# Mobility

Devices can move between different access points in one provider network, and they can move among other provider network, but they maintain their ongoing connections.

**In order to have mobility, there is the need of having an home, which allows to get source about you and who you are, so the Home network is fundamental**.
It is possible to have a notion of visited networks, where we can share credentials from the home network.

* *Home network*: it provides a paid service plane with a cellular provider, in it there is the HSS which identifies a user and its services.
* *Visited network*: any network that has an agreement with other networks to provide access to visiting mobile.

In the case of an Internet Service Provider and Wifi, there is not the notion of global home. The device and user store the credentials, and different networks have different credentials (there are some exception: shared distributed wi-fi network, like eduroam).

### How can the mobile network support device mobility? (incorrect approach)

1.  Assign an IP address.
2.  Allow the mobile device to move between visited networks.
3.  Use a private address with NAT IP or an IMSI.

Handling directly by routers: this is not the correct way. Routers advertise the well-known name, address, or number of the visiting mobile node through a routing table exchange. Internet routing can already do this without any changes, using routing tables to indicate where a mobile device is located, using the longest prefix match. **However this approach cannot scale to billions of mobile devices.**

## Correct mobility approach
We cannot use the aggregated address of routers. We do not want to handle tables of millions of mobile device, given that mobility is a key property of the device. The idea is that the mobility is managed at the edge by the mobile network:
1) **Indirect routing**: is a method of communication in a mobile network where data is first sent from the correspondent (External sender) to the home network of the mobile device and then forwarded to the device. In this method, the home address of the mobile device is used as the destination of the packet. The process of indirect routing involves the border network gateway receiving the datagram from the correspondent and forwarding it to the visited network. The datagram is then forwarded to the mobile device in the visited network using the home address as the destination. This method of routing is commonly used in mobile networks as it provides a way for mobile devices to maintain a consistent address even when they move between different networks but another pro is that the correspondent hasn't to know the actual address of receiver but only the home address. However, it _can introduce additional latency and complexity_ compared to direct routing, where data is sent directly to the mobile device without passing through its home network.
2) **Direct routing**: the correspondent gets the foreign address of the mobile UE from the home network, then send directly to actual visited network. This mechanism is non-transparent to the host, but the manage of data loss is better.

## Indirect routing

### Registration 
The mobile device **needs an IP address in the visited network**. In the **home network** there is a **Permanent address associated with the mobile device**.

In the visited network there are Transient identifiers:
one is new address in the range of the visited network and the other is IP address provided via NAT.

Indirect routing: always go through the home network, also called triangle routing.
 1) Mobile **associates** with the visited network mobility manager. 
 2) The mobile mobility manager **registers** the mobile location with the home HSS.

![[Pasted image 20230316163217.png]]
We see how:
* the device has a permanent IP in its home network
* in the Visited Network the device has a NAT IP.
* Visited and Home Network have different Network Address
* The IMSI of the UE is always the same (As its like a network interface address.)

The registration allows to forward from the Home Network the ***datagrams*** to the Visited Network and so, to the UE.

### Mobility
Given a **corresponded, being someone that wants to reach a UE**.

1) Corresponded uses the *home* address as the datagram address
2) The *home network gateway (which is the border gateway of the home network) receives the datagram and it tunnels it to the remote gateway*
3) The Visited network gateway forwards the datagram to the UE (it handles it as appropriate) in internal network.
4) The visited gateway router will forward the reply either:
	1) Directly to the *correspondent* (local blackout)
	2) To the home network, which will then forward to it

### Requirements
1) A mobile device to visited network association protocol: as the mobile device needs to associate with visited network and disassociation.
2) a protocol to associate the **visited network to the home network HSS** *registering where is the UE* (mobile device). This subscribing protocol is needed to connect the network, and also to know for the visited, what are the services the mobile can consume. Then the home will update its database of the placement of the mobile device. **1 and 2 are controls messages/protocols**.
3) A datagram tunneling protocol between the network gateway of home and visited networks. Tunnels are also within the visited network.
	1) The home gateway will encapsulate and forward the corresponded original datagram. Encapsulation allows to maintain the original datagram, and add an additional header, with new src and dst address, as it is more appropriate to perform a task.
	2) The gateway router of the visited network decapsulates it, **it performs NAT translation to then forward the original datagram to the mobile device**

### Properties

#### Cons
There is a triangle inefficiency, as it may be possible that correspondent and UE may be in the same visited network, but we must go through the home network.
One consumes resources of the home network and increases the latency of the communication between the mobile device and server in its same network.
 
#### Pros
**Transparency:** The moving from one visited network to another is *totally transparent to the corresponded, as the HSS of home will record where the UE is and forward there the packet that receives from the correspondent.*
The correspondent does not need to know *where the mobile device is*.

**Data Loss**: Even if some packets may be lost, when there is an interrupted flow of datagrams between network, the on-going TCP connections between correspondent and mobile can be maintained. Or other reliable services of transport allow to sustain the data loss, in any case it is a bit better solution.

If the mobile changes the visited network then:
- update the HSS in the home network
* change the tunnel endpoint to terminate at the gateway router of the new visited network
This can be done without additional complexity, the HSS is queried by the correspondent only once at the beginning of the session.

## Direct Routing

### Mobility
In this case the corresponded will find the position of the UE and then will go to the visited network to send the datagram.
The HTTP datagrams will not go to the home network gateway to send data, but directly to the visited network gateway. It is direct routing in the sense of sending data directly.
1) Correspondent communicate with home network HSS and gets the UE visited network.
2) The correspondent sends the datagram to the visited network address of the UE.
3) the visited network gateway router will forward the datagram to the UE.

### Properties

#### Pros
**Simplicity**: The triangle inefficiency is not a problem anymore.
**Data loss:** The change of visited network it easily managed by updating HSS in the home network and then changing the tunnel endpoint to the new border gateway. 

#### Cons
There is **no transparency of the UE mobility for the correspondent**, it must take care-of-address from the home agent, so ask for the new visited network of the UE.

## Mobility in 4G networks
BS sends a sync signal and selects one, then there is association between mobile and BS.
1) ***Base Station association*** is done with a BS in a visited network, the UE sends the IMSI identifying itself and stating its home network. IMSI: International Mobility Subscriber Identity, identity of the mobile.
2) There is a ***control plane configuration*** with the MME of the visited network, which will contact the HSS of the **home network**. It does this to authenticate the mobile device.
3) The ***data plane configuration*** is performed by the MME of the visited network, creating a forwarding tunnel for mobile. The Visited and home networks establish tunnels from the home network P-GW **that goes to the Serving Gateway of the Visited network, then to the BS and ultimately to the UE**. We need this setup for the forwarding of the packets, as we said doing it with the tunnel.
4) ***Mobile handover***: the devices changes its point of attachment to the visited network, the handover occurs when the device changes its association from one base station to another. Basically, the termination of the Service gateway to BS will change to do this handover, if the mobile device is in the same visited network.

![[Pasted image 20230316180203.png]]

### Configuring the LTE control plane

The mobile communicates with the local MME of visited network, using the **BS control plane**.
The MME uses the IMSI and contacts the mobile home HSS to:
* retrieve authentication, encryption and network service information. This authentication is performed by the HSS with the Mobile device.
* the home HSS knows the UE, and knows that it is *resident in the visited network*
The BS and the UE mobile will select the parameters for BS-mobile data-plane radio channel, the final linking between BS and mobile device.
![[Pasted image 20230316180640.png]]


### Configuring the data-plane tunnels

The MME(of visited) configures the data plane for the mobile (UE) devices.
All the traffic to and from the mobile device will be tunneled through the **device home network**.
- The MME of the visited network sets up the first tunnel between BS and serving gateway of the visited network.
- Then there is a termination from P-GW of the home network to the S-GW of the visited network, any packet follow this patch from the P-GW of home, to S-GW of visited to then BS and ultimately UE.
The Streaming server in the image will send to the P-GW of the home network datagrams, in turn the P-GW sends the datagrams to the Serving-Gateway of the Visited Network.

There are two tunnels:
1) S-GW to BS tunnel: when a mobile (UE) changes BS, then **just change the endpoint IP address of this tunnel, but keep the same S-GW with its address**
2) S-GW to home P-GW: implementing indirect routing

The tunneling is done using GTP, so the datagrams are encapsulated into it, allowing to specify different IP source and destination addresses.

### Handover between BS in the same cellular network

![[Pasted image 20230316182829.png]]

1) There may be an handover of UE: starting from the current BS (the BS currently serving the mobile device, which monitors the quality of the link and may decide to initiating it either for degradation of signal strength or since it is being overloaded), that selects a target BS (best BS to move the mobile device, selecting it), using a *Handover Request message to the target BS*, informing it to handle the new mobile device.
2) The Target BS pre allocates the radio time slot for the mobile UE device, and it responds with an **Handover Request ACK, that contains additional info for the mobile**.
3) The source (current but not anymore) BS informs the mobile of new BS, the mobile UE can now send datagrams via the new BS. So for the UE mobile *handover looks complete*. There is asked to change the mobile connection, to change the radio link to the **Mobile device** to target.
4) Until the new tunnel isn't created, target BS will need to forward the packet of the mobile device to the source base station, as the old current forward the packets to new target.
5) The target BS informs the MME that it is the new BS for mobile UE. The MME then instructs the S-GW to change the **tunnel endpoint to be the new target BS**.
6) The target BS sends an ACK to the source BS **making the handover complete and allowing the source BS to release sources**.
7) The mobile UE datagrams now flow through the tunnel from target BS to S-GW. Now the source Base Station is completely released from handling the mobile device.

![[Pasted image 20230316182840.png]]

All this mechanism is possible thanks to the overlapping area of different base station, so in this way cells talk with each other and they can find the best one.

### Mobile IP
It is possible to handle mobility with the public internet.
Mobile IP is an architecture to handle addressing of devices on the move. It was not successful, as the mobile network evolved rapidly.
The idea of it is to sue:
* indirect routing with IP
There is the possibility to try and do it with direct routing.

Is is merely academic research.

### Impact of wireless and mobility to higher layer protocols

There is the big goal of supporting mobility of user, but Performance wise: **there is an light packet loss and delay due to bit errors and handover loss**. For example an handover may cause a loss, which *TCP interprets as a congestion, so it will decrease the congestion window unnecessarily*. As said TCP and UDP can go on mobile network, logically the impact is minimal, the best effort service model remains unchanged, and TCP and UDP can and will run over wireless and mobile.
UDP does not care about packet loss, but for example TCP will degrade its performance, as it may increase the congestion window and will then slowdown the throughput. This is a compromise to handle the low level requirements.

There may be delay and impairments for real time traffic and bandwidth is also a scarce resource for wireless link.

Quiz:
![[Pasted image 20230621204627.png]]
1) Source Base station
2) Source Base station

 <div style='page-break-after: always'></div> 


# Chapter 21: IEEE 802.11
IEEE 802.11 operates at the Physical Layer and at the Data Link Layer.
![[Pasted image 20230302101521.png]]


![[Pasted image 20230302095641.png]]
# Versions
802.11a: Throughput: 23 Mbps (must take into account the overhead and loss of packets) while the bandwidth of 54 Mbps is a theoretical measurement.

IEEE 802.11n: MIMO (multiple input multiple output) is used to improve the throughput and performance of the wireless network.

WiFi 5: Also known as 802.11ac, this standard can work both on 2.4 and 5 GHz frequency, as the previous edition of Wi-Fi, obviously 5 GHz has more bandwidth.

WiFi 6: Also known as 802.11ax, this standard includes even more improvements in power consumption and security compared to previous Wi-Fi standards.

Frequency and coverage overview of 802.11: The first release had a low coverage of up to 30 meters, but subsequent releases improved coverage up to 70 meters. The latest frequency, 802.11af, uses lower frequencies (previously assigned to television) which allows for higher coverage, up to 1 kilometer. With lower frequencies, the wavelength is higher, so the signal can travel further.

802.11ah: This standard has more than enough bandwidth for sending sensor information and a coverage about 1 kilometer.



# Infrastructure
Infrastructure-based architecture: Wireless networks using this architecture include an access point, which is used to transmit data from the transmitter to the receiver and can also connect devices to the internet.

Transmission: is done with carrier sense multiple access with collision detect.

Single Coordination function: This function is distributed throughout the network and controls all the stations.

Spectrum: The range of frequencies available for wireless communication is divided into channels at different frequencies, with administrators assigning a channel to a frequency.

Channel association: A node receives beacon frames from access stations and selects which access point to use. The node then authenticates to the access point and starts DHCP.

## Type of scanning

![[Pasted image 20230302101827.png]]

Passive Scanning: This method involves the access point sending beacon frames to nodes, which must scan the frames and select an access point. The node then sends an association request to one specific AP, and that responds with an association response. Access point selection is based on signal strength, but sometimes an access point may be overloaded even if it has a better signal strength with many devices.

___________________________________________________


![[Pasted image 20230302101801.png]]

Active Scanning: In this method, the node takes the initiative by sending a beacon frame in broadcast to other access points (probe request). The access points respond with probe responses, and the node selects an access point and sends an association request. The access point responds with an association response, and confirmation of the assignment occurs.


## Coordination

![[Pasted image 20230302102014.png]]
DCF and PCF can *also be active in the same station at the same time*.

## PCF
It uses a base station to control all activity in its cell, it is *thought to delay sensitive traffic*.
AP *will poll station for transmission, but under the hood it is based on DCF.*

# Distribution Coordination Function

DCF is completely decentralized and thought for best effort asynchronous traffic. **DCF must be implemented by all stations**. 

MACAW is implemented in this function, which is decentralized and must be implemented by all stations.

Carrier Sensing: Two types of carrier sensing are used: physical CS, which checks if another station is transmitting on that channel, and virtual CS, which also considers the time duration in the headers of RTS, CTS and also of a data frame. *In this way the channel is virtually busy until the end of the data transmission*.
* A channel is declared as busy if both the *physical and virtual carrier sensing detect it as busy*.
### Priorities and Coordination

Interframe Space: This is the time between two frames, and one node must wait for another before transmitting. 
Different IFS values can be used, such as a short one of a few microseconds, and then we have the Point Coordination Function IFS.


SIFS (Short IFS) < PIFS(Point Coordination Function IFS) < DIFS (Distributed Coordination function IFS).
**The station with highest priority are the ones what only have to wait for a SIFS**

Priority: Nodes with higher priority wait less time than nodes with lower priority.


In a communication:
- When the **sender** can transmit, it **waits for a DIFS**, sends an RTS, and **waits for an SIFS** before receiving a CTS. 

- Meanwhile, **given the RTS and CTS**, other stations **calculate a NAV (network access vector)** as an implementation of virtual carrier sensing, so it is an estimation of the interval to wait when ear a RTS.

- After the NAV, nodes wait for **DIFS** and then may wait for the backoff if necessary before trying to send data.

- SIFS values are typically 16 ms for 5 GHz and 10 ms for 2.4 GHz.


 <div style='page-break-after: always'></div> 


# Chapter 22: Software Defined Networking
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


 <div style='page-break-after: always'></div> 


# Chapter 23: Network Function Virtualization
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






 <div style='page-break-after: always'></div> 


# Chapter 24: ComNetsEmu - Hands On

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

 <div style='page-break-after: always'></div> 


# Chapter 25: Hands-on Network slicing
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



 <div style='page-break-after: always'></div> 


# Chapter 26: An Introduction to the Theory of Signals
Sensors measure continuous physical quantities in the real world and sample them into discrete digital signals for processing and transmission. These signals are mathematical functions that map from a domain (often time) to a codomain (the signal values). The domains and codomains can be either continuous (real numbers, R) or discrete (integers, Z) depending on the signal.

Deterministic signals follow definite rules and are different from random signals. Deterministic signals can be analyzed using deterministic methods, while random signals require probabilistic methods.

When sensors sample a continuous physical quantity, they convert the infinitely variable real-world quantity into a finite set of numbers that represent the quantity at discrete points in time or space. This results in a discrete signal that can be processed digitally. For example, a temperature sensor may sample the continuous temperature fluctuations in a room into a set of numbers representing the temperature every minute. This discrete set of temperature values over time forms a discrete signal.

The discrete signals from sensors must then be transmitted, often as electromagnetic waves. The transmission medium converts the discrete signal into electromagnetic waves that propagate to a receiver. The receiver then converts the waves back into the original discrete signal for further processing.


### Deterministic Signal definition
Function f(t) with a real value such as time, where
$f(t):D$ -> ℭ
Where D and ℭ may be:
* $\mathbb{R}$ real numbers
* $\mathbb{Z}$ a discrete set, such as integers
* $\mathbb{C}$ a set of complex number, allowing to represent two independent signals together if used as codomain
 
# Classification
We take signal as a real function of time. We may have for domain and codomain:
* time continuous(D=$\mathbb{R}$) and amplitude continuous signals (ℭ=$\mathbb{R}$)![[Pasted image 20230610125345.png]]
* Time continuous(D=$\mathbb{R}$) and quantized signals(ℭ = $\mathbb{Z}$)![[Pasted image 20230610125402.png]]
* Time-discrete(D= $\mathbb{Z}$) and amplitude continuous signals (ℭ=$\mathbb{R}$)	![[Pasted image 20230610152341.png]]
* Time-discrete(D= $\mathbb{Z}$) and quantized signals (ℭ=$\mathbb{Z}$)
	![[Pasted image 20230610152945.png]]
Note that quantized signals may be also refereed as discrete amplitude signals

### Discrete-time signals in depth (D = $\mathbb{Z}$)
We can have a signal that is discrete in time but continuous in amplitude. This type of signal is often found in digital audio, where the amplitude of the audio signal is sampled at discrete points in time but the amplitude values themselves are continuous.

In contrast, an image is typically considered a discrete signal (digital signal), meaning that it is discrete both in time and amplitude. In digital image processing, an image is represented as a grid of pixels, each with a discrete amplitude value that represents the brightness or color of that pixel.

In formula, the domain is  D=$\mathbb{Z}$(T) which is a set of integers defined as:
$\mathbb{Z}$(T) = {nT, $\forall n\in\mathbb{Z}$ and $T\in \mathbb{R}$}.
In this way we have a multiplication between an integer and a real value.
We may have as an example
$\mathbb{Z}(2)$={${..,-4,-2,0,2,4}$}, so we multiply by $2\in \mathbb{R}$ any integer number. 


### Digital Signal (D= $\mathbb{Z}$, C= $\mathbb{Z}$)
A discrete signal is called digital when the codomain is a finite set of symbols. Its called also a "symbolic sequence". 

We may have an alphabet, a set of symbols allowed to represent some signals.
A = \{a,b,c,...,x,y,z\}
A symbolic signal is for example a sequence abababac.. as it transmits the set of symbols to

Furthermore we can reduce to another alphabet that one, having B={0,1} alphabet we can represent any symbol in A with a sequence in B.
We may have a custom encoding of letters.
We may use the rules of representation to represent the signal as a sequence of binary symbols. For example
a= 0000, b = 00001 and so on, making the code 

«ababfxje»  into a series of those symbols: 
0000000001000000000100101101110100100100

# Frequency
We want to find the duration of a transmission given a source that transmits f symbols/second (symbols per second) which is the symbol frequency. 
* We have that for an alphabet of 8 symbols, defined as A. The transmission will last 8/f seconds
* We have that for an alphabet of 40 symbols, defined as B. The transmission lasts 40/f seconds.

The symbol frequency is called binary frequency, if a binary alphabet is used. For binary frequencies we define the measure throughput, which is expressed in bits per second. To calculate the throughput, we need to know the binary frequency that produces $f_c$ samples/second. 

Assuming that a source samples an analog signal with $f_c$ samples/seconds.
That we need M bits per sample to represent a value, the formula for calculating the throughput is
* $f_c\cdot M$ bit/second

Furthermore we can define M as being $log_2$(alphabet_size) where alphabet_size is the number of symbols in the alphabet.
The formula will then become:
* $f_c \cdot log_2$(alphabet_size)


#### Exercise
![[Pasted image 20230610162729.png]]
1. Determine the number of bits needed to represent each symbol. Since there are 8 symbols in the alphabet, we need 3 bits to represent each symbol (2^3 = 8). M = $log_2$ bit/symbol (alphabet_size)

2. Since the symbol frequency is 10 symbols per second, we can calculate the throughput by multiplying the symbol frequency by the number of bits needed to represent each symbol:

Throughput = $f_c \cdot M$
Throughput = 10 symbols/second * 3 bits/symbol  
Throughput = 30 bits/second


## Periodic Continuous Signal
A continuous signal $s(t): R\rightarrow R$ is *periodic* with period $T$ if $s(t) = s(t+T)$ $\forall t\in R$ 

> For example $sin (nt)$ and $cos(nt)$, are periodic, with period $T =2\pi/n$  $\forall n\in Z$

We may have non-periodic signal **which we can make period, by studying them in the period \[0,T]\, since their behaviour remains the same in all its existence domain.

We may see how for periodic signal, it holds that
$s(t+T)=s(t+2T)=s(t+nT)$ $\forall t\in \mathbb{R},n\in{Z}$ here the domain is $\mathbb{R}$, $\mathbb{T}\in{R}$ and $t\in R$ 
*The frequency is $f=1/T$*

### Example of periodic continuous signal
$s(t) = cos 2t + 4 \cdot sin 2t - cos 5t+ 4 \cdot sin 6t$ has a period of $2\pi$ 
The frequency is $f = 1/T$.

![[Pasted image 20230610170646.png]]

### Aperiodic signal
We define in the domain \[a,b) a **periodic signal s with limited support**, limited support means that where outside of this domain, the signal is not supported. This limited support is defined as $s(t) = 0$ $\forall t\in[a,b)$

We can define the periodic extensions $s^\star$ of $s$ as
$$s^*(t)=\sum_{n=-\infty}^\infty s(t-nT)$$
where $T = b-a$
![[Pasted image 20230610171709.png]]

We are summing all the multitude of periods (the multiple repetitions or cycles of the periodic signal), covering the entire domain.  
By shifting the signal this way, the signal becomes periodic, with a period of $T = b-a$.

This infinite sum, allows to make the periodic function, where we replicate this same shape of curves. This periodic extension, which starts from a signal with limited support, sampled and trying to reconstruct it. We re-construct a complete signal by summing all of its individual cycles, where each cycle is a shifted version of the original signal s(t) over the interval $[a,b)$.

Basically we increase $t$, and we subtract a value $nT$, with $n$ growing, to make the periodic effect shaped.

# Transmission
Typically, our problem is to transmit any information produced by a source as this information has to be transmitted to the medium.
The signal must change depending on the channel.

There is a transducer, that converts a message to a signal, which can be transmitted to a medium.
A transducer converts an electrical signal into an electromagnetic wave.

The electromagnetic wave will then travel by destination during transmission. During the transmission, noise may be "added" to the signal, or the signal may have some distortion. Noise is typically an external and random signal that represents the movement of electrons.
The signal received at the destination will not be identical to the original signal due to the presence of added noise, which is inherent to the nature of the channel.
Furthermore, other effects may cause variations in the signal, such as distortion, resulting in a signal composed of different frequencies. When the signal propagates through the air or a medium, it may experience frequency-dependent attenuation, causing different frequencies to be attenuated in varying ways.

At the destination, the transducer will convert a signal into a message.
The transducer for electromagnetic signals is an *antenna*. A *channel* may be electromagnetic, sound, optical waves etc.
![[Pasted image 20230610183417.png]]


The attenuation of the signal will vary accordingly, as the attenuation characteristics differ for these frequencies.

The primary objective of the transmission process is to minimize noise and distortion, aiming to enhance the signal while mitigating the impact of noise.

To assess the quality of the communication channel, the Signal-to-Noise Ratio (SNR) is utilized, representing the ratio between the signal strength and the level of noise present.


#### Analog Transmission
In the figure below we have different block to represent the various phases of the analog transmission, we can see:
* source: who emit the signal
* adaptor: for noise and distortion, those devices will reduce the effects of those unwanted changes, with equalizers, amplifiers( mitigate the effect of noise). This phase transforms the signal to make the transmission more efficient. We enter the real analog channel
* transducer: hardware component emitting the signal
* transmission medium: the medium in which the signal travel
* transducer: in this case the receiver does the task of transforming electromagnetic waves (or other type of physical signal) into electrical signals
* adaptor: the same as the other adaptor, to reduce noise and distortion

![[Pasted image 20230610183834.png]]

#### Digital Transmission
Digital transmission: the source is emitting digital signal, discrete sequence of symbols, for instance a sequence of bit. Basically creating an exchange of discrete messages.

We have:
* source: who emit the signal
* modem: (modulator/demodulator) convert the signals from discrete to continuous, in this way the signal can be sent over an Analog channel
* adaptor: same as before
* analog channel (same as before)
* adaptor: same as before
* modem: demodulates to get the source, with some error probability, as there are many steps from transmission to receiver side, that makes it difficult to reconstruct the signal as the original one. One of the goal is to make the error probability as minimal as possible. Do channel decoding, adding information, such as redundancy bit, to make some checks, detecting errors during transmission and correcting them
![[Pasted image 20230610183844.png]]


## Sampling and quantization for Digital Transmission
The source produces a digital message, this digital message can be produced from an analog signal, for instance, the source may be a sampling messages.
To do this, it converts the continuous signal with an ADC, being an analog to digital converter. The analog signal will be represented as a sequence of symbols, if the symbols are {0,1} then into bits of 0 s and 1 s.

Those are sent on a Digital Channel. Furthermore, the DAC converts from digital to the analog signal.
![[Pasted image 20230610190159.png]]

At the receiver site, the signal is converted again into an analog signal, using a DAC, *digital to analog converter*.

### How to sample
When transmitting speech, a certain number of samples must be generated and transmitted. However, due to limitations in efficiency, we may not be able to transmit a large amount of data. Additionally, since the medium may be shared with other communications and conversations, errors are likely to occur during transmission, which can affect the signal reconstruction.

Having a high resolution and high sampling rate can reduce quantization errors as more samples are taken. However, it is important to note that even with these improvements, the reconstructed signal may not be as precise as the original signal that was produced.

In order to better understand the signal, particularly its frequency components, it is necessary to analyze it thoroughly.

Consider that sampling and quantization introduce a distortion in the signal, called **quantization noise**, which is added to the channel noise.
This quantization noise is dependant on:
* the frequency of sampling rate
* resolution of the digital symbols, meaning how many different symbols are used to **represent a single analog value**
Consider that:
* higher resolution and high sampling rate = small quantization error but = a larger number of symbols to transmit (higher bandwidth required)


# Fourier series and Frequency Domain Analysis
We use Fourier series and Frequency Domain Analysis to understand how a signal can be composed of base signals at given frequencies. They were been the cornerstone of signal and system analysis.

We have a combination of different frequencies. We may have a sinusoid oscillating at different frequencies. There could be, for example, a sum of two sine waves with different amplitudes.

Here, we see the general expression for a sinusoid at frequency $\omega$. We may also see it at frequency f in Hertz.
$$x(t)=a \cdot sin(\omega t+\phi) = a \cdot sin(2\pi ft+\phi)$$

![[Pasted image 20230611094316.png]]  
We then have another example of combining two sinusoids.  
![[Pasted image 20230611094337.png]]  
Given by the formula:  
$$x(t)=sin(2\pi t)+sin(4\pi t)$$

We may have a specific sound made up of signals at specific frequencies. As we can see here, there is an analogy with audio signals, showing the US telephony line.  
$$x(t)=sin(2\pi\cdot 350 \cdot t)+sin(2\pi\cdot 440 \cdot t)$$

![[Pasted image 20230611094648.png]]

In general, this type of assumption can be made for a series of signals that are constant in time. We may have signals at fundamental frequencies. With $f_0=1/T$, we have sinusoids that are multiples of these frequencies.
**We have a fundamental harmonic, and then we have the 2nd, 3rd, etc. harmonics**.
We may sum all these components, and we obtain a final signal that is continuous in time and amplitude.  
We can assign a weight to each harmonic, with different weights by summing a portion of the components.  
We get different signals in this way.

![[Pasted image 20230611094740.png]]

We generally define the k-th harmonic as:

- $s_k(t)$: k-th harmonic (frequency $f_k = k/T = k \cdot f_0$)  
    So, we may see how all harmonics are defined based on the fundamental harmonic, and their frequency is a multiple of $1/T$ (its period).

See how by changing the weights, we can get a different signal:  
![[Pasted image 20230611095115.png]]

What is more interesting is the opposite.  
**Can we have a continuous and periodic signal expressed as a sum of trigonometric functions, such as sine and cosine oscillating in multiples of a given frequency?**  
If we can:
	How do we compute the weights to combine the sinusoids to obtain said signal?
		The answer is that we can analyze and decompose the continuous and periodic signal and compute the waves at specific frequencies for the signal.


# Fourier series
Allows to decompose the signal as a infinite number of continuous function, oscillating at different frequencies.
We start from signals whose domain is the time, and we analyse it from time to frequency domain shift.
There is a change of domain from the previously discussed, now $D=$ frequency domain.

Those continuous functions, are the base of the decomposition.
Formally the base are the set of functions $\phi_n(t),n\in\mathbb{Z}$. So they are a numerable and infinite set of functions.
In the Fourier series, those functions are trigonometric functions, which are orthogonal. 

## Fourier series formally
Given a continuous signal $s(t):R \rightarrow R$ periodic in the interval \[-$\pi$,$\pi$\] **(so $T=2\pi$ period)**. 

$$s(t)=1/2*a_0+\sum_{n=1}^\infty(a_n*cos(nt)+b_n*sin(nt))$$

The Fourier series is defined as a function over time.
Its composition is:
* $a_0\cdot 1/2$ is the constant components, where $a_0$ is defined as: $$a_0=\frac{1}{\pi}\int^{\pi}_{-\pi}s(t)dt$$
The integral of the continuous signal, over the interval $-\pi$ to $\pi$ 

Hence we do an infinite sum of trigonometric functions.
Note that sine and cosine oscillate at different frequencies.
We start from $cos(t)$ and $sin(t)$.
* $a_n \cdot cos(nt)$: where $a_n$ is an amplitude of the n-th harmonic, while $cos(nt)$ is the n-th harmonic with fundamental harmonic cos(t) We define $a_n$ as: $$a_n=\frac{1}{\pi}\int^{\pi}_{-\pi}s(t)\cdot cos(nt)dt$$
* $b_n\cdot sin(nt)$ where $b_n$ is amplitude of the n-th harmonic, while $sin(nt)$ is the n-th harmonic with fundamental harmonic sin(t). We define $b_n$ as $$b_n=\frac{1}{\pi}\int^{\pi}_{-\pi}s(t)\cdot sin(nt)dt$$
The decomposition is general, with a constant component, an infinite sum and we compute the value of those weight.


There are math demonstration, to define the condition under which a signal may be developed in a Fourier series.
*We make a conservative assumption, which were established by Dirichlet*.
IF:
	 $s(t)$ is periodic
	 $s(t)$ is piecewise continuous, then it implies that the Fourier series of $s(t)$ *exists* and converges in $R$.

#### Remembering Sine and Cosine
* Sine is an even function, meaning that $sin(-x)=-sin(x)$
* Cos is an odd function, meaning that $cos(-x)=cos(x)$


## Example

Given a signal we need to develop the signal into a Fourier series.
$$s(t)=\begin{cases} 
2 \hspace{0.4cm} if \hspace{0.2cm} -\pi<t<0 \\ 
1 \hspace{0.4cm} if \hspace{0.8cm} 0\leq t \leq \pi \\ 
\end{cases}$$
periodic signal function with period $2\pi$
![[Pasted image 20230611122521.png]]

We apply the formulas to get  $a_0$, $a_n$, $b_n$

We have a base s(t). We may have a non continuous function with two co-domains depending on the definition of the function.
We may check what happens, if we sum just a finite number of the components.
For example summing only the first 20 harmonics, we reconstruct our signal, it is not the same as our original signal. This approximation will improve, by summing more harmonics.

**Split the intervals, make the integrals based on s(t) which is defined as its values in different intervals.**
Make the integral, by plugging the intervals value of s(t) and splitting in the two domains of the functions with different values.

Make sure to divide the integral in the various interval where it has some value.
**Note that n is a constant inside cos and sin, we cannot leave it as that to solve it, we must make the integrals by substitution!**

$a_0=1/n \int_{-\pi}^\pi s(t) dt= 1/\pi(\int_{-\pi}^{0}2dt +\int_{0}^{\pi}1dt = [2t]_{-\pi}^0 + [t]_{0}^{\pi}$

= $(2\pi+\pi)/\pi = 3$


$a_n=1/\pi \int_{-\pi}^\pi s(t) cos(nt) dt$

$= 1/\pi(\int_{-\pi}^{0}2cos\cdot t(nt)dt +\int_{0}^{\pi}cos(nt)dt)$

we will use the substitution $u = nt$, so $du/dt = n$ and $dt = du/n$.
We redefine the integral in the form of having the derivative of the element substituted in the integral:

$1/\pi(1/n\int_{-\pi}^{0}2cos(nt)*n*dt +1/n\int_{0}^{\pi}cos(nt)*n*dt$

$=1/\pi(1/n\int_{-\pi}^{0}2cos(u)du +1/n\int_{0}^{\pi}cos(u)du$

$=1/\pi[1/n * 2 * sin(u)]_{u(-\pi)}^{u(0)} +[1/n * sin(u)]_{u(0)}^{u(\pi)}) = 0$ 

where $\forall n, sin(n\pi)=0$. So the final result, substituting $u(\pi)= n\pi$ will result in a $=0$.


$a_n=1/n \int_{-\pi}^\pi s(t) sin(nt) dt= 1/\pi(\int_{-\pi}^{0}sin(nt)dt +\int_{0}^{\pi}sin(nt)dt$

We will use the substitution $u = nt$, so $du/dt = n$ and $dt = du/n$.
We redefine the integral in the form of having the derivative of the element substituted in the integral:
$1/\pi(1/n\int_{-\pi}^{0}2(sin(nt)*n)dt +1/n\int_{0}^{\pi}(sin(nt)*n)dt$

$=1/\pi(1/n\int_{-\pi}^{0}2(sin(u))du +1/n\int_{0}^{\pi}(sin(u))du$

$=1/\pi[1/n * 2 * -cos(u)]_{u(-\pi)}^{u(0)} +[1/n  -cos(u)]_{u(0)}^{u(\pi)})$ = 0

the formula will become, extended, bearing in mind that $cos(-x)=cos(x)$

$1/(n*\pi)*(-2+2cos(n\pi)-cos(n\pi)+1)$
$=1/(n*\pi)*(-1+cos(n\pi))$ 

We make the cases:
* $n$ is odd, then we have $cos(\pi)$, $cos(3\pi)$ and so on, always equal to $-1$, meaning that $b_n=0$ when n is odd.
* $n$ is even, we have $cos(2\pi)$,.. and so on, where its always equal to $+1$, meaning that $b_n=-2/(\pi*n)$ when n is even
The absolute value decreases to $0$.

The coefficient can be seen here:
![[Pasted image 20230611123807.png]]


We may make an example by letting $n = 2k - 1$, and plugging the coefficients in the Fourier Series. For all k>0, in such way we get just n odd numbers!
$$s(t)=\frac{3}{2}-\sum^{\infty}_{k=1}(\frac{2}{(2k-1)\pi}\cdot sin((2k-1)\cdot t)))$$

We can plot a finite sum of harmonics. Plotting an increased number of harmonics, we approximate better the functions.
The discontinuity are hard to handle. It is close to those, you have the oscillation behaviour. With more harmonics, you reconstruct better the signal at those points. As it may be seen here in this comparison:
![[Pasted image 20230611124013.png]]


# Exercise 2

![[Pasted image 20230611124200.png]]
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{0.2cm} -\pi<t<-1 \\ 
	0 \hspace{0.4cm} if \hspace{0.2cm} -1\leq t < \pi \\
	1 \hspace{0.4cm} if \hspace{0.8cm} 1 \leq t \leq \pi
\end{cases}
$$

Instead than substitution, we may also use the well known integrals, to solve directly: 
$$\int sin(t)dt=-cos(t)$$
$$\int cos(t)dt=sin(t)$$
$$\int sin(nt)dt=-\frac{cos(nt)}{n}$$
$$\int cos(nt)dt=\frac{sin(nt)}{n}$$


In this case we will split in 3 parts the integrals but its the same procedure. We may then plot the first n harmonics and see the difference:
![[Pasted image 20230611125041.png]]


# Fourier series with arbitrary period
**We can generalise, to not just the harmonic with period of 2$\pi$**. by applying the theorem which in a more generic form.
Periodic in a period $T$. We can have a signal, continues and periodic in time in the interval $-T/2$, $T/2$.

Formally:
Given a continuous signal s(t): $\mathbb{R} \rightarrow \mathbb{R}$, periodic in the interval $[-\pi,\pi]$, using the substitution $y = 2\pi t/T$ to get

$$f(y) = s(\frac{T}{2\pi}\cdot y)$$ that is periodic in the interval $[-\pi,\pi]$ 

We can define the Fourier Series
$$f(y) = s(\frac{T}{2\pi}\cdot y) = \frac{1}{2}\cdot a_0+ \sum_{n=1}^\infty(a_n \cdot cos(ny)+b_n \cdot sin(ny))$$

Then we may return to the initial variable and obtain the formula:
$$s(t)=\frac{1}{2}\cdot a_0+\sum_{n=1}^\infty(a_n\cdot cos(2\pi nt/T)+b_n \cdot sin(2\pi nt/T))$$

We consider that in $a_n$ and $b_n$ we have $2/T$ instead of $\pi$ in the integral intervals. Therefore, instead of $nt$ inside the cosine and sine harmonics, we have $(2\pi \cdot n \cdot t)/T$

![[Pasted image 20230611144337.png]]


# Energy of a continuous signal

Given a signal s(t) defined in the interval $[-T/2,T/2]$ , its **energy** defined as:
$$E_s(T) ≜ \int_{-T/2}^{T/2}|s(t)|^2dt$$
Which has the meaning in physics that if s(t) represents the voltage, applied to a $1\ohm$ resistor, then $E_s(T)$ is the energy dissipated in the period T.

## Energy Signal
A signal with finite energy is defined as **energy signal**.
We have an energy signal if we have the following limit greater than 0.
$$E_s=lim_{T \rightarrow\infty}E_s(T) = \int_{-\infty}^{+\infty}|s(t)|^2dt > 0 \land E_s<+\infty$$

(I would say that in an infinite period the energy dissipated is more than 0 and less than infinity, meaning finite number for the signal $s(t)$ and then the signal is an energy signal).

That definition includes:
* finite duration signals
* infinite duration signals
	* if the signal has infinite duration, then $E_s \rightarrow 0$ as fast as $1/t$ or even faster

**In the physical world, all signals have finite energy, as no signal will last forever**.

# Power of a signal

We define the **average power of the signal** given $s(t)$ defined in the interval $[-T/2,T/2]$
$$P_f(T)≜ \frac{1}{T} \int_{-T/2}^{T/2}|s(t)|^2dt=\frac{E_s(T)}{T}$$
So we average the energy of the signal over the whole period.

## Power Signal
A signal, with finite power, also defined as *power signal*, is a power signal if the following limit is greater than 0

$$P_s=lim_{T\rightarrow \infty}\frac{1}{T}\cdot E_s(T) = \frac{1}{T} \cdot \int_{-\infty}^{+\infty}|s(t)|^2dt > 0 \land P_s<+\infty$$
(Basically, if the average of the energy of the signal, with the limit of the period to infinity is greater than 0 and less than infinity meaning that its finite then its a power signal)

### Periodic signal
Periodic signal are a class of signals important because, **given that** they have *finite power* so they are power signal, they also have:
* infinite energy
* *their average power is equal to the average power computed in a period (the same from a period to the whole duration)*



# Energy and Power

**If a signal has finite energy, then it has an average power of $0$**.
So we have the classification of:
* finite energy signal (energy signal), with their power being $0$
* finite average power signal (power signal) $>0$, with their energy being infinite
**Those are two disjointed sets**
![[Pasted image 20230611155155.png]]
Power signals contain periodic signals. While energy signal contain Pulse signals, where they contain limited duration signals.


# Example
Having an exponential signal:
$$
s(t)=\begin{cases} 
	0 \hspace{0.9cm} \forall \hspace{0.1cm} t < 0 \\
	ae^{bt} \hspace{0.4cm} \forall \hspace{0.1cm} t\geq 0
\end{cases}
$$
It has finite energy, so its an energy signal, as we may see up to infinity

$$E_s = \int_0^\infty|s(t)|^2dt= \int_0^\infty|ae|^{-bt2}dt$$
we can remove the absolute value, as we have defined the signal as 0 in the case $t<0$.

$\begin{align*} & \int_0^\infty (a \cdot e^{-b \cdot t})^2 dt \\ & = \int_0^\infty a^2 \cdot e^{-2b \cdot t} dt \\ & = a^2 \int_0^\infty e^{-2b \cdot t} dt \\ & = a^2 \left[ -\frac{1}{2b} \cdot e^{-2b \cdot t} \right]_0^\infty \\ & = a^2 \left[ -\frac{1}{2b} \cdot (e^{-2b \cdot \infty} - e^{-2b \cdot 0}) \right] \\ & = a^2 \left[ -\frac{1}{2b} \cdot (0 - e^{-2b \cdot 0}) \right] \\ & = a^2 \left[ -\frac{1}{2b} \cdot (-1) \right] \\ & = \frac{a^2}{2b} \end{align*}`$

where at step 3 we computed the integral of e, in the format:
$$\int e^{cx}dx=\frac{1}{c}e^{cx}$$
Furthermore, we proceeded with the substitution, knowing that $e^{-\infty}=0$ and that $e^0=1$, obtaining $+1/2b$ which is then multiplied with $a^2$

We may see that it has null power since, taking the average over a period T going to infinity, the power is 0.

$$P_s=\lim_{T\rightarrow\infty}\frac{1}{T}\int^{T/2}_{0}|s(t)|^2dt=lim_{T\rightarrow \infty}\frac{a^2}{2bT}=0$$

### Power signal example
A periodic signal, such as cos or sin, are power signal.
Given $s(t)=cos(t)$ $\forall t$ considering its period $2\pi$ from 0 to $2/\pi$ 
We may see that for sure since the function is bounded between $0$ to $2\pi$, in the values 0 and 1, the average power will be limited in those and so finite.
**You may notice that the integral of the energy is undefined, but consider that we know that the set of power signal and energy signal are disjointed, we can say that the energy is infinite!**

![[Pasted image 20230611170731.png]]

To do the integral, the half angle identity was used as
$\int cos^2(x)dx=\int 1/2(1+cos(2x))dx$.

Then this was split into two intervals, note that in the right interval, there is a bit of an error in the slide. What happens is that we need to make the substitution $u=2t$. So we multiply the integral outside by $1/2$ and inside by $2$.
Thus at the end we will obtain for the right side, $[1/(4\pi) sin(2t)]_0^{2\pi}$

### Question 2

$$
s(t)=\begin{cases} 
	3 \hspace{0.4cm} -2<t < 0 \\
	0 \hspace{0.4cm} otherwise
\end{cases}
$$
We try to understand if this is a power signal or an energy signal

$E_s$=$lim_{T\rightarrow\infty}E_s(T)$ = $\int_{-\infty}^{+\infty}|s(t)|^2dt > 0$ && $E_s<+\infty$ 
so we write
$\int_{-2}^{-1}|3|^2dt= [9*t]_{-2}^{-1} = -9+18 = 9$ 

Since the energy is $>0$ and $<\infty$ we can say that this is an energy signal, not a power signal since the two sets are disjointed, so the power will be zero.

### Question 3
$$
s(t)=\begin{cases} 
	3/t \hspace{0.4cm} 1<t < 10 \\
	0 \hspace{0.8cm} otherwise
\end{cases}
$$

$E_s$=$lim_{T\rightarrow\infty}E_s(T)$ = $\int_{-\infty}^{+\infty}|s(t)|^2dt < 0 \land E_s<+\infty$ 
so we write
$\int_{1}^{10}|3/t|^2dt = 9*\int_1^{10} 1/t^2 = -9*1/t|_1^{10} = -9/10 +9= 81/10$

here too the energy is finite. So its an energy signal.

 <div style='page-break-after: always'></div> 


# Chapter 27: Fourier Transform

## Complex Numbers

$\overline{x} = a + jb$ is a complex number, composed of the real part a and the imaginary part $jb$, j is the imaginary number, $j=\sqrt{-1}$ .

We may also define the conjugate of $\overline{x} = a + jb$  being  $\overline{x}^* = a - jb$ 
We may **represent the number in the imaginary plane, using the vector with $|x|$ as modulo and phase $\phi$**

![[Pasted image 20230611184040.png]] ![[Pasted image 20230611184057.png]]
On the right we can see it with its conjugate.
Consider that we can also obtain the single components:
* $|x|=\sqrt{a^2+b^2}$
* $\phi=tan^{-1} b/a$
* $a= |x|cos(\phi)$
* $y= |x|sin(\phi)$
then we can also **write into an alternate form the complex number**
$\overline{x} = a + jb = |x|*cos(\phi)+j|x|*sin(\phi)$


## Euler exponential
We can define the Euler exponential, which is a complex number, defined as:
* $e^{\pm j\phi}=cos(\phi)\pm j*sin(\phi)$

We can derive then the Euler formulas
* $cos(\phi)=(e^{j\phi}+e^{-j\phi})/2$
* $sin(\phi) = (e^{j\phi}-e^{-j\phi})/2j$

$\overline{x}=a+jb$ can be rewritten then as  $\overline{x}=|x|\cdot e^{j\phi}$ 
which fits into the definition of $\overline{x} = a + jb = |x| \cdot cos(\phi)+j|x|\cdot sin(\phi) = |x|\cdot e^{j\phi}$

We then may represent the conjugate $\overline{x}^*=|x|\cdot e^{-j\phi}$


# Fourier series with exponential base
As seen in the introduction of signals([[An Introduction to the Theory of Signals]]), the formula of the Fourier series may be rewritten according to the Euler exponential

Formally, the Fourier series is **expressed in the complex numbers domain, allowing to represent signals s(t):$\mathbb{R}$->$\mathbb{C}$**
Since  $\mathbb{R}\subseteq \mathbb{C}$, that definition includes also signals  $s(t):\mathbb{R}$->$\mathbb{R}$

The following form, is a generalization of the Fourier series for real functions, this form is the one generally used and allows to generalize Fourier series for real functions using the complex exponential.

Given a continuous signal $s(t):R \rightarrow R$ periodic in the interval $[-\pi,\pi]$ (so $T=2\pi$ period).
$s(t)=1/2*a_0+\sum_{n=1}^\infty(a_n*cost(nt)+b_n*sin(nt))$

We may redefine using as base of Fourier, the set of functions:
* $e^{j\cdot 2\cdot \pi\cdot n\cdot F\cdot t}\forall{n}\in\mathbb{Z}$, where there is defined $\phi=2\cdot\pi\cdot n\cdot F\cdot t$. 
* $n$ is also called the weight
* The complex exponential $e^{x+jy}$ can be decomposed into $e^{x+jy}$ = $e^x\cdot e^{jy}=e^{x}\cdot(cos(y)+jsin(y))$ as we substituted the $e^{\pm j\phi}=cos(\phi)\pm j\cdot sin(\phi)$ and add the x component with $e^x$, here $y=\phi$

**This results in the base of Fourier set of functions to be**:
* $e^{j\cdot 2\cdot \pi\cdot n\cdot F\cdot t}=cos(2\cdot\pi\cdot n\cdot F\cdot t)+j\cdot sin(2\cdot\pi\cdot n\cdot F\cdot t)$
(note that $e^x= 1$ here and $x=0$)

## Formally Fourier with exponential base
Given a **periodic** signal:
* $s(t)=s(t+T)\forall t$
* $s(t)$ is defined as a power signal (infinite energy and finite power)
The frequency $F = 1/T$ is the *fundamental (first) harmonic, expressed in Hertz*

The signal can be represented with the linear combination

$$s(t) = \sum_{n=-\infty}^\infty S_n\cdot e^{j\cdot 2\cdot\pi\cdot n\cdot F\cdot t}$$

which then can be expanded with the previous result for the base of Fourier set of functions:
$$\sum_{n=-\infty}^\infty S_n\cdot(cos(2\cdot\pi\cdot n\cdot F\cdot t)+j\cdot sin(2\cdot\pi\cdot n\cdot F\cdot t))$$

In those cases the harmonics are:
* $e^{j2\pi nFt}$
* $(cos(2\pi nFt)+j\cdot sin(2\pi nFt))$

While the amplitude of the harmonic is:
$$S_n = \frac{1}{T}\int^{T}_{0}s(t)e^{-j2\pi nFt}$$

**Dirichlet theorem states that the Fourier series give the same values of $s(t)$ where $s(t)$ is continuous but not in discontinuities**. That expresses the fact that $s(t)$ is fully represented by ${S_n}$, meaning that the knowledge of the series $S_n$ is equivalent to the knowledge of $s(t)$
*The periodic signal $s(t)$ can be tough as being composed by an infinite number of periodic signal.*

The idea is that the Fourier base, have frequency $nF$, which is a multiple of the fundamental harmonic $F = 1/T$.

* For $n>1$:
	* The terms $S_n\cdot e^{j2\pi nFt}$ are called **the harmonic components of $s(t)$** each of those with frequency $nF$
* For $n=0$
	* The coefficient $S_0=1/T\int_0^Ts(t)dt$ is the "constant" component, as it is the average value of $s(t)$
* For $|n| = 1$:
	* there is the fundamental frequency $f_0=F$ with period $T=1/F$
	* $S_1$ and also $S_{-1}$ are the amplitudes of the fundamental frequency (consider that we start from $-\infty$ so of course we will have also $S_{-1}$)
* For $|n|>1$ (same as first):
	* the harmonics of frequency $f_n=nF$ with period $T/n$
	* $S_n$ are the amplitude of the harmonics, whenever the value is different than -1 and 1, the harmonics after the fundamental are the one represented

# Fourier series of aperiodic signals using limited support
Consider limited support, where the signal is not defined out of the bounds $[a,b]$.
Furthermore, we can obtain the Fourier series **for an aperiodic signal with limited support**, as the series assumes that the signal is periodic,**taking as period the entire duration of the signal**.

As a consequence, you may revert from $S_n$ to s(t) and obtain **the periodic extension of the signal**
As can be seen in the image:

![[Pasted image 20230612102804.png]]

## Example
Consider the signal with period T and frequency $F= 1/T$
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{1.75cm} |t|\leq T/4 \\ 
	0 \hspace{0.4cm} if \hspace{0.3cm} T/4 < |t| \leq T/2 \\
\end{cases}
$$

![[Pasted image 20230612114552.png]]
The coefficient of the Fourier series are

$$S_n=1/T\int_0^T s(t)\cdot e^{-j2\pi nFt}dt = 1/T\int_{-T/4}^{T/4} 1\cdot e^{-j2\pi nFt}dt$$
expressing to the period where the signal is defined and using the value of $s(t)$ for the interval.
This integral has two values, $1/2$ if $n=0$, while $\frac{sin(n\pi/2)}{n\pi}$ if $n\neq0$. 

The resolution is done by doing the integral with substitution, then it solves the integral by plugging the intervals, at the end it equalizes the result to this one:
![[Pasted image 20230612112549.png]]
Since there is a sine, it can have two possible values. As we saw in [[An Introduction to the Theory of Signals]] the function can be decomposed in odd ($2k-1$) and even values.

We may see the formula in its full form, by using said n:
$$s(t)=\frac12+\sum_{k=-\infty \ \& \ k\neq 0}^{k=\infty}(-\frac{(-1)^k}{(2k-1)\pi}(cos(2\pi(2k-1)Ft)+j\ sin(2\pi(2k-1)Ft)))$$

**Using the fact that sin is an odd function and $sin(x)=-sin(-x)$**:

The formula becomes for the **complex part** becomes, *also by taking out t*
$\sum_{k=1}^{k=\infty}j*sin(2\pi(2k-1)Ft)=$
$-\sum_{k=1}^{k=\infty}j*sin(-2\pi(2k-1)Ft)=$
$-\sum_{k=1}^{k=\infty}j*sin(2\pi(-2k+1)Ft)=$
$-\sum_{k=-1}^{k=-\infty}j*sin(2\pi(2k-1)Ft)$ 

What we basically stated is that the part from $-\infty$ to $-1$ will be the negative of the part from 1 to $\infty$ so they will null each other.
*The complex terms are null in this example.

Furthermore the formula becomes:
$$s(t)=\frac{1}{2}+ \sum^{k=\infty}_{k=-\infty}-\frac{(-1)^k}{(2k-1)\pi}cos(2\pi(2k-1)Ft)$$

So only the real part of the cosine remains.
We can see an approximation, with period $T = 4$. Which means that at $F=1/4$ Hertz, we have that representation of the signal.
![[Pasted image 20230612120249.png]]
**We can see how there are different approximation depending on the range from which k is iterated!**

Consider that the original signal is:
![[Pasted image 20230612120338.png]]
Taking 200 of k values, yields the blue that is exactly the same signal with some noise


# Spectrum of a signal
Given a signal $s(t)$ and using Fourier it can find the coefficient $S_n$ of the series, given it we can reconstruct the signal $s(t)$.
The sequence of order coefficient, $S_n$ with $n=-\infty$ to $+\infty$ is called **spectrum of $s(t)$**.
*The spectrum itself can be seen as a discrete signal* (a digital signal).

The spectrum of:

$$
S_n=\begin{cases} 
	1/2 \hspace{1.5cm} if \hspace{0.3cm} n=0 \\ 
	0 \hspace{2cm} if \hspace{0.3cm} n \hspace{0.3cm} even \\
	-\frac{(-1)^k}{(2k-1)\pi} \hspace{0.4cm} if \hspace{0.3cm} n=2k-1
\end{cases}
$$
is
![[Pasted image 20230612124245.png]]
In $n=0$ we have the constant signal.
In $n=1$ and $n=-1$ we have the fundamental harmonic.

So without knowing $s(t)$, but just by knowing $S_n$ we can reconstruct the signal. The spectrum $S_n$ as may be seen in the image, is a set of values, which are discrete values

## Fourier Transform
*Having s(t)* which is a continuous signal, we can transition to its spectrum, which is its discrete signal $S_n$.
**The transition is called Fourier Transform (FT)**.

That is denoted in such way:
$$s(t) \underset{FT}{\iff}S_n$$
We may even represent it with:
$$S_n=\mathcal{F}(s(t)) \hspace{1cm} (transform)$$
$$s(t)=\mathcal{F}^{-1}(S_n) \hspace{1 cm} (inverse\hspace{0.2 cm} transform)$$


With the transform the domain changes from **the time domain of $s(t)$** to the *frequency domain* of $S_n$

$S_n$ is a function of n, that identifies an harmonic and that harmonic identifies a frequency.
That is because $S_n$ is the amplitude of the harmonic of frequency $nF$ and period $T=1/nF$.

*The frequency domain in this case is the discrete frequency domain.* This is because we have a discrete set of frequencies.
In conclusion the Fourier Transform is a transform to the **discrete frequency domain**.

## Spectrum of a signal in complex dimension

In general $S_n$ is a complex number, while there may be some lucky cases where both $S_n$ and s(t) are real.
It is not always possible to represent the spectrum with a 2D diagram as before.
*We can use the Euler exponential, to represent $S_n$*.
$$S_n=|S_n|\cdot e^{j\theta_n}$$
Where:
* Phase of the harmonics = $e^{j\theta_n}$
* Amplitude of the harmonics $|S_n|$

*So the representation of $s(t)$ has two diagrams*:
* phase spectrum diagram
* amplitude spectrum diagram

### Example
Given this signal:
$$
s(t)=\begin{cases} 
	-1 \hspace{0.4cm} if \hspace{0.91cm} 0< t\leq T/2 \\ 
	1 \hspace{0.75cm} if \hspace{0.4cm} T/2 < t \leq T \\
\end{cases}
$$

We have those coefficients for the Fourier series
(again the resolution is done by doing the integral with substitution, then it solves the integral by plugging the intervals, at the end it equalizes the result to this one):
![[Pasted image 20230612153735.png]]

So as result the coefficients are
$$
S_n=\begin{cases} 
	0 \hspace{1.cm} if \hspace{0.55cm} n \hspace{0.2cm} even\\ 
	j\frac{2}{n\pi} \hspace{0.4cm} if \hspace{0.55cm} n \hspace{0.2cm} odd \\
\end{cases}
$$

#### Using the complex numbers representation
Recalling the following statements from the start of this note
* $|x|=\sqrt{a^2+b^2}$
* $\phi=tan^{-1} b/a$
* $a= |x|cos(\phi)$
* $y= |x|sin(\phi)$
then we can also **write into an alternate form the complex number**
$\overline{x} = a + jb = |x|*cos(\phi)+j|x|*sin(\phi)$

Such that:
* if n is odd:
	$S_n=j*(2/n\pi)$ where $a=0$ (as there is no real part), $b=2/n\pi$, $\theta_n=tan^{-1}b/a$ can be written as: $$S_n=|S_n|\cdot e^{j\theta_n}$$
Furthermore we have two cases.
* when a>0, then $\theta_n=tan^{-1}b/a=\pi/2$
* when b<0, then $\theta_n=tan^{-1}b/a=-\pi/2$

As such the representation of the coefficient $S_n$ is:
$$
S_n=\begin{cases} 
	0 \hspace{2.3cm} if \hspace{0.3cm} n \hspace{0.2cm} even\\
	\frac{2}{n\pi}e^{j\pi/2} \hspace{1cm} if \hspace{0.3cm} n>0 \land n \hspace{0.2cm} odd \\
	-\frac{2}{n\pi}e^{-j\pi/2} \hspace{0.35cm} if \hspace{0.3cm} n<0 \land n \hspace{0.2cm} odd
\end{cases}
$$
Here, we isolate the amplitude as:
$$
S_n=\begin{cases} 
	0 \hspace{1.05cm} if \hspace{0.3cm} n \hspace{0.2cm} even\\
	\frac{2}{n\pi} \hspace{0.7cm} if \hspace{0.3cm} n>0 \land n \hspace{0.2cm} odd \\
	-\frac{2}{n\pi}\hspace{0.35cm} if \hspace{0.3cm} n<0 \land n \hspace{0.2cm} odd
\end{cases}
$$
**We represent the amplitude in the spectrum**
![[Pasted image 20230612155937.png]]
Furthermore the phase is:
$$
S_n=\begin{cases} 
	0 \hspace{1.2cm} if \hspace{0.3cm} n \hspace{0.2cm} even\\
	\pi/2 \hspace{0.7cm} if \hspace{0.3cm} n>0 \land n \hspace{0.2cm} odd \\
	-\pi/2 \hspace{0.35cm} if \hspace{0.3cm} n<0 \land n \hspace{0.2cm} odd
\end{cases}
$$
which is represented by 
![[Pasted image 20230612160013.png]]
With the previous found coefficient, we can represent the signal:
![[Pasted image 20230612160100.png]]

# Fourier Transform for non-periodic signals
It is possible to apply the transform to *finite signals* not just to periodic signals. The signals are finite in a time frame of length $T$. Hence, the counter-transform will instead return a periodic signal with period $T$.

When $T \rightarrow \infty$ then the Fourier Transform interprets the signal with a fundamental frequency $F=1/T$ that tends to 0 ($F\rightarrow 0$). What happens is that the harmonic tend to become infinitely close to each other. The periodicity will disappear progressively.

So, a non periodic signal s(t) can be expressed as:
$$s(t)=\int_{-\infty}^{\infty}S(f)e^{j2\pi ft}df$$
*where f is the continuous frequency*, which ranges in $[-\infty,+\infty]$
$S(f)$ is **the amplitude** of the frequency $f$. In this case, we have that $S(f)$ is given:
$$S(f)= \int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}dt$$
and $S(f)$ is the spectrum. 

Unlike the continuous signals that produce a discrete spectrum, these finite signals produce a spectrum as a continuous function. This can be seen in the next example, compared to the previous the difference is well visible. 
A continuous and aperiodic signal can have energy concentrated in a continuous range of frequencies rather than only in specific frequencies. This can make the frequency spectrum of a non-periodic signal more difficult to interpret.

The passage from the non-periodic signal to its spectrum is called **Continuous Fourier Transform* (CFT).
We denote it in two ways:
$$s(t)\underset{CFT}{\iff}S(t)$$
Or also with:
$$S(f)=\mathcal{F}_c(s(t)) \hspace{1cm} (transform)$$
$$s(t)=\mathcal{F}_c^{-1}(S(f)) \hspace{1cm} (inverse \hspace{0.2cm} transform)$$

## Example

Given the pulse signal, which has finite energy and power equal to zero, but being a pulse is not continuous.
$$
s(t)=\begin{cases} 
	-1 \hspace{0.4cm} if \hspace{0.2cm} |t|\leq T/2 \\ 
	0 \hspace{0.75cm} otherwise \\
\end{cases}
$$
Which is represented as:
![[Pasted image 20230612165543.png]]

The coefficients of the Fourier series are:
$S(f) = \int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}dt=$
by dividing in the intervals with different values of $s(t)$ 
$\int_{-T/2}^{T/2}e^{-j2\pi ft}dt$ = 
performing the integral by substitution of $u = -j2\pi ft$, we get the final result
$[e^{-j2\pi ft}/(-j2\pi f)]^{T/2}_{-T/2}$ we then plug the values:

To obtain:
$$S(f)=\frac{e^{\frac{j2\pi fT}{2}}}{j2\pi f}-\frac{e^{-\frac{j2\pi fT}{2}}}{j2\pi f}=\frac{sin(\pi fT)}{\pi f}$$

Furthermore, by considering different values of T, we can obtain different approximation,
*It has to be noted that in this particular case $S(f)$ is real, with no imaginary part*.
The phase of the spectrum is constant and is not represented.

Original signal:
![[Pasted image 20230612171659.png]]

Spectrum with T=5
![[Pasted image 20230612171717.png]]
The backward transformation of it
![[Pasted image 20230612171745.png]]
Spectrum with T=10
![[Pasted image 20230612171818.png]]
Its backward transformation:
![[Pasted image 20230612171846.png]]

**We may see that by increasing the period, we increase the length of the pulse in the signal, giving it a length of T**.

With $T=20$
![[Pasted image 20230612171948.png]]

![[Pasted image 20230612172003.png]]


# Band of a signal

Whenever the signal is periodic, the spectrum contains only the harmonics of the main frequency (it being the fundamental frequency,  F = 1/T) with different amplitudes (its multiple frequencies). In general the spectrum of a signal spans across all frequencies in $(-\infty, +\infty)$.

*We may filter some of the frequencies of the spectrum*.
In such way we may obtain a *signal limited in bandwidth*.

The signal can:
* exclude high frequencies, those are called **low-pass filter**
* exclude low frequencies, those are called high-pass filter
* exclude low and high frequencies, keeping the intermediate frequencies, those filters are called **band-pass filter**.

## Example
Considering the pulse signal , which was then transformed into the spectrum, and then obtain in the new form by the reverse transform.
With T=20.
It became:
![[Pasted image 20230612173835.png]]
The new signal became:
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{0.2cm} |t|\leq 10 \\ 
	0 \hspace{0.4cm} otherwise \\
\end{cases}
$$
Its spectrum is then:$$S(f)=\frac{e^{\frac{j2\pi fT}{2}}}{j2\pi f}-\frac{e^{-\frac{j2\pi fT}{2}}}{j2\pi f}=\frac{sin(\pi fT)}{\pi f}$$
By plugging $T=20$
$$S(f)=\frac{sin(20\pi f)}{\pi f}$$
The spectrum is:
![[Pasted image 20230612174036.png]]

### Apply a low-pass filter
By applying a low pass filter for frequency below $0.5$. We can obtain a different spectrum, where the little points which are not very near to 0 will be erased:
![[Pasted image 20230612174250.png]]
This will then get us this new digital signal:
![[Pasted image 20230612174305.png]]


### Apply an high-pass filter
By applying an high pass filter for frequency above $0.5$.
We increase the values in the range distant from the very near of 0.
![[Pasted image 20230612174448.png]]

### Apply a band-pass filter
By applying an band pass filter for frequency in range $[0.1,0.5]$.
We increase the values in the range distant from the very near of 0.
This will erase the very very near values in 0. But it will keep the values up to $0.5$.
![[Pasted image 20230612174622.png]]


## But what is a band for a signal
A band represents the range of frequencies within a signal.
Where Bandwidth represents the range of frequencies over which the signal can operate effectively.
A signal is said band-limited if the **frequency content** is **limited to a certain range**.
For humans the audible frequency range is limited between 20 Hz and 20 kHz. Here **the band is the range of frequencies within that range**.

# Question
![[Pasted image 20230612182834.png]]
Consider that f is a continuous frequency ranging from $-\infty$ to $\infty$. Consider that the period here is $T=5$.
This signal is ***not limited*** in band, this is because it has infinite support in the frequency domain. That means that it contains contribution from all frequencies, which are both the positive and negatives.

By applying a low pass filter with threshold frequency set to 1. We need to remove all the frequency going above this line:

![[Pasted image 20230704120451.png]]As such the frequencies remaining are:
![[Pasted image 20230704120802.png]]

### An example of a signal with limited band

The signal
$$
s(t)=\begin{cases} 
	A \cdot sin(2πf_0t) \hspace{0.4cm} if \hspace{0.2cm} \leq T/2 \\ 
	0 \hspace{3.1cm} otherwise \\
\end{cases}
$$
where $A$ is the amplitude of the signal, $f_0$ is the center frequency, and $T$ is the duration of the signal.
The signal is non zero only in the interval $[-T/2,T/2]$.
Since it contains a single component, only the frequency component at $f_0$, the bandwidth of the signal is equal to the frequency range which is significant for it, that is of size $2f_0$.
The signal is band-limited to frequency range $[-f_0,f_0]$


# From FT do DTF
We may define for discrete signal a Fourier Transform, which represents signals only at *N* instants, which are *separated by sample times T*. Basically the sample are a finite sequence of data.

*Continuous signals are reduced to discrete time signal, by applying a domain restriction, from $\mathbb{R}$ into $\mathbb{Z(T)}$.

Sampling is the operation that performs this restriction, it is stated by the relationship:
* $sc(n\cdot T)=s(n\cdot T), n\cdot T\in \mathbb{Z(T)}$
**Where**:
* $s(t), t\in \mathbb{R}$ is the reference to the continuous signal, and  $sc(nT),nT\in \mathbb{Z(T)}$ is the discrete signal **obtained by the sampling operation**.

## Discrete Time Signal
A discrete-time signal is a ***complex function***, **of a discrete variable**.
It is defined as:
* $f(t):\mathbb{Z}(T)\rightarrow$ℭ
	* the domain is $\mathbb{Z}(T)$, which represent the of multiples of $T$, being $\mathbb{Z}(T)=${$...,-T,0,T,2T,..$} for $T>0$.
The signal can be denoted in two forms:
* $s(nT)$, $nT\in\mathbb{Z}(T)$
* $s(t$), $t\in\mathbb{Z}(T)$

## Onwards to discrete Fourier transform
Having defined $s(t)$, $t\in\mathbb{R}$ to be the continuous signal that is the **source of the data**. Letting the $N$ samples to be denoted by $s(0),s(1),....s(N-1)$

The Discrete Fourier Transform will consider each sample as **an impulse having area $s(t)$**.
The integral exists only at the sample points. What the amplitude of frequency $f$ will become is:
$$\displaylines{
S(f)= \int_{-\infty}^{\infty}s(t)e^{-j*2\pi ft}dt=\\
s(0)\cdot e^{-j2\pi f0}+s(1)\cdot e^{-j2\pi f1}+s(2)\cdot e^{-j2\pi f2}+...+s(N-1)\cdot e^{-j2\pi f(N-1)}
}$$

In short, the formula becomes:
$$S(f)=\sum_{k=0}^{N-1}s(k)\cdot e^{-j2\pi fk}$$
*The DFT treats the data as if they were periodic, this is because there is a finite number of input data points*. So what happens is that:
* $s(N)$ to $s(2N-1)$ is equal to $s(0)$ to $s(N-1)$.
**Given this, we can evaluate the DFT equation for the fundamental frequency which is $(1/NT)$** and its harmonics, *since the operation treats the data as periodic.*
So $f = 0,\frac1{NT},\frac2{NT},...,\frac{N-1}{NT}$
What happens is that the DFT computes a finite number of DFT coefficient, just $N$.

# Discrete Fourier Transform
We can further improve the formulation and state:
* given a finite length sequence composed of $N$ values, $s_n$ with $n=0,1,...,N-1$. We can calculate the Discrete Fourier Transform
	$$S_f = \sum_{n=0}^{N-1}s_ne^{j\frac{2\pi f}Nn}$$
with $f=0,1,...,N-1$
* we divide by $N$ to normalize the scale. As said before we take into account the fundamental frequency and its harmonic. Without the normalization factor their magnitude would be scaled by $N$,
	* fundamental frequency would have a magnitude $N$
	* the second harmonic would have magnitude $2N$
	* so on..
* those do not represent the actual amount of each frequency in the signal, instead they are artificially boosted by a component $N$
Furthermore, the anti-transform, capable of returning the temporal series of samples $s_n$, is defined as:
$$s_n=\frac1N\sum_{f=0}^{N-1}S_fe^{j2\pi f\frac nN}$$
The computational complexity of the Discrete Fourier Transform is $O(N^2$) with $N$ being the data set of samples. We can have a faster version called the [[Fast Fourier Transform]] reducing the complexity to $O(Nlog_2N)$


## Computing the DFT
Given 
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{0.2cm} n=0,1,2,3 \\ 
	0 \hspace{0.4cm} if \hspace{0.2cm} n=4,5,6,7 \\
\end{cases}
$$
Having $N=8$ samples the computation of DFT is:
1) Calculate the formula of the summation for a generic $f$.
2) For all the $f\in[0,N-1]$ plug the value and calculate their amplitude

The result is as follow:
![[Pasted image 20230613112950.png]]
**Note that the calculation of $S_2$ and the other even frequencies are not reported, equaling to 0.** 
Further more the amplitude of the DFT can be seen here as follows:

![[Pasted image 20230613113140.png]]

 <div style='page-break-after: always'></div> 


# Chapter 28: Fast Fourier Transform
The Discrete Fourier Transform (DFT) is $O(N^2)$ with N being the data set of samples.

The Fast Fourier Transform FFT is a **class of algorithm for the calculation of the DFT** and also for its inverse.
*The number of operations is reduced a lot, making the numerical processing of the signals to be computationally feasible*.

The time complexity is shrink to $O(N log_2 N)$


 <div style='page-break-after: always'></div> 


# Chapter 29: Analog to digital conversion
Sensors must take values from physical quantities, which are physical quantities and we want to take values in a specific time interval. 
Then we want to represent the values in a digital form to process them with a computer device. That has many useful properties, including the processing of a value without needed special purpose numbers. Why? Because you have numbers, with whom you may work. Also the data may be managed and transmitted without altering the signal.
If condition changes, you do not have to alter the signal, the signal is robust over some specific conditions.

What we can do when sampling from a sensor is to sample an analog signal. We have for sample a value and then transmit it after passing into a analog to digital conversion on a channel that sends a signal. 
But also we may need to reconstruct a signal from digital to digital. It is important that the A/D process does not lose much information from the initial signal.

![[Pasted image 20230613123856.png]]
The process can be seen in the image above.
A/D will transform the analog signal $s(t)$ into a sequence of integer, then the sequence can be ***stored, processed and transmitted by a digital device***. 
To apply those operations, the numeric sequence is transformed into a binary stream.

The main elements of analog to digital are:
* sampling: pick values of a continuous signal
* quantization: represent a value using the representation specification of our system.

### Sampling
Input: a continuous signal $s(t)$
Output: a stream of real numbers

The sampling of a Signal $s(t)$ means to extract a sequence of numeric values that the signal **assumes at discrete time intervals**.
When we sample a signal we consider the value is a instance of time, we consider the sampling period and take the value of the signal at multiples of the signal.
*Sampling is performed at uniformly spaced time intervals*. Those intervals are spaced of **$T_c$** that is the sampling period.

### Quantization
Input: a stream of real numbers produced by sampling
Output: a stream of numbers (integers)

We may have in quantization:
* float representation: just a finite number of bits, to represent a continues domain you can only do a subset of values of the real domain, according to the bits we have you have different quantization solution. The value you can represent from a smaller value of a subset that you can represent.
* integer representation

### Losses for sampling and quantization
In theory, sampling may allows to preserve the *original signal*, under some hypothesis, so without loss. We need to sample correctly to represent well the signal and to reconstruct well the original continuous signal from the samples obtained.

Quantization instead implies to have a loss of information, there will be an error in the representation of the sampled signal. We do not represent exactly the sample value but the goal must be to make the reconstruction of the original signal feasible rather than perfectly. 
There is a trade-off on how well will be the sampled quantized with how much time this process requires.


# Sampling Continuous signal
Sampling allows to obtain from an analog signal, being a continuous signal s(t) a discrete signal $g(n\cdot T$), $n\in\mathbb{Z}$.
Where we can see that there is an equality for the signal in points n of the samples.
$$g(n\cdot T)=s(nT)$$
We have a period and a frequency here for **sampling** too.
* $T_c$ is the sampling period
* $1/T_c$ is the sampling frequency

Given this continuous signal
![[Pasted image 20230613151556.png]]

With sampling we get a discrete signal with points in time. We see on x the *samples at points that are* multiples of our sampling period.
![[Pasted image 20230613151732.png]]

## Example for sin(t)
Given $s(t) = sin(t)$ and **having frequency** $f=1/(2\pi)\approx0.159$, a sample will be the value of a signal at precise time.

**A sample is a value of signal itself, which is defined as $s(nT_c)$**, taking a value for every multiple of the sampling period $T_c$.

So we approximate $s(t)$ with another signal.
We can decide the sampling period $T_c$ and then see what is the value of the sampling frequency:
	if $T_c=3.09$
	then it implies that $f_c=1/ {T_c} \approx0.324>2f$
We have a simple signal and it is enough here to sample with double the signal frequency; but in general, we will see that it is  enough to sample double the frequency for sampling frequency to *approximate well the signal*. The continuous signal can be seen here:
![[Pasted image 20230613152853.png]]
We get then the approximation points as we can see in the bottom graph:

![[Pasted image 20230613152913.png]]

We get only information related to the dots, but we lose some information.


# Reconstruct a Signal - Interpolation

**We apply interpolation to reconstruct the continuous signal.**

There are several ways to do this, such as using the sample value to reconstruct a continuous signal.

There are several methods:
- **Piecewise-constant signal**: This can be done, for instance, by building a zero-order hold, nearest neighbor.
    - **Zero-order hold/Nearest neighbor**: Using a sample, this method decides the value of the curve of a signal from 0 to T. Basically zero-order hold means to assume that the signal assumes a constant value, which is the value of a sample, until the next sample is reached, then it will be the value of that other sample.  
    - **Nearest neighbor** refers to the fact that the reconstructed signal value at any point in time is the one of the nearest sample value.
- **Piecewise linear**: For example, by using first-order hold reconstruction. 
	- First-order hold reconstruction: it approximates a continuous signal, by connecting adjacent samples with straight line segments. it can be seen mathematically as having piecewise linear interpolation between adjacent samples (get the value of a point which is unknown by using other points). The continuous signal will have less discontinuity using piecewise interpolation than other methods for piecewise linear reconstruction. Basically this method involves drawing a line between two consecutive samples. Here, you do not reconstruct the original signal, but something close to it.

Zero Order Hold Interpolation can be seen here:
![[Pasted image 20230613155941.png]]
It can be seen how the values of the reconstructed signal will have the value of the last sample at each point.

# Sampling Theorem
The basic assumption is that if you have a signal that changes rapidly you need to have an high number of samples.
If it changes slowly, you need a low number of samples to represent its variations.
A fast changing signal must be sampled faster than one changing slowly.

**The sampling theorem suggests the minimal sampling frequency required to reconstruct the original signal but that  is only valid in *ideal* conditions** (infinite samples).

Given a sinusoid. We may get a lot for samples for a period, there we sample at high frequency.
Intuitively we will have enough info to reconstruct the signal, whenever $f_c>>1/T$ so if the sample frequency is much greater than the signal frequency (defined as $1/T$ Hertz).
$$x(t)=sin(\frac{2\pi}T)t$$

![[Pasted image 20230613163155.png]]

## Sampling at low rate
In the following image we may see in blue the **original signal**.
![[Pasted image 20230613163344.png]]
If we sample at a frequency that is too low, we may see that the dots do not represent well the original signal. As such we end up reconstruction **a lower frequency signal, which is the one in red**.
The problem there is that the sample does not represent our signal. If we over impose a graph over the points, the red sinusoid matches the samples, which is at a lower frequency.

### Aliasing
The effect where we reconstruct a low frequency signal is called **aliasing**. 
Aliasing is has the effect of making **different signals become indistinguishable when they are sampled**.
Aliasing depends on:
* sampling rate
* frequency content of the signal


## Theorem
The sampling theorem is a fundamental theorem that gives us the sampling frequency required to get enough sample to reconstruct signals and avoid the effect of aliasing.

Given a signal $s(t)$, which is limited in band, which is an important assumption. The spectrum is defined for a range of frequencies up to $f_M$ maximum frequency, after which **the spectrum is null**.

When the signal respect the condition that the spectrum is null above the frequency $f_M$  then we can say *formally*:
$s(t)$ **is completely represented** by its sampled taken:
* at regular intervals $t_n=n\cdot T_c$  where $(n\in \mathbb{Z})$
* with a sampling period $T_C<=1/(2f_M)$. Meaning that we are sampling two times at minimum the double of the maximum frequency.

**With those samples it is possible to reconstruct** $s(t)$ for any $t$.

## Nyquist frequency
So we define the Nyquist frequency.
$$f_{c_{min}}=1/T_{c_{max}}=2\cdot f_M$$
This is obtained by maximizing the sampling period, which allows to obtain the minimum sampling frequency.
**The Nyquist frequency is the minimum frequency at which a signal $s(t)$ limited in band must be sampled*** to be able to reconstruct well the original signal.

**$f_{c_{min}}$ ultimately corresponds to the double of the maximum frequency in $s(t)$.**


### Reconstructing the signal.
We have to do interpolation to reconstruct the signal, there are several ways from sample. One interpolation starting from the samples is the one using the cardinal sin.
This can be seen here in formula:
$$s(t)=\sum_{n=-\infty}^\infty s(n\cdot T_c)\cdot \frac{sin(\pi f_c(t-nT_c)}{\pi f_c(t-nT_c)}$$

We reconstruct signal by using multiples of the period of sample.
By shifting the argument of the cardinal sine function, we can estimate the signal value at any time, not just at the times where we have samples. The shift is a multiple of the sampling period and is determined by the frequency of the signal.
We shift by multiple of the sampling period the argument of the sin, which is ultimately produced by  $\pi$ * frequency of sampling * shift of the multiple of the sampling theorem!

When evaluating the reconstructed signal at a time that is a multiple of the sampling period, such as $2T_c$, the value of the cardinal sine function becomes centered at 0, e.g. $2T_c$
you will get the multiplication of $s(nT_c)\ sin(\pi  fc$) which not shifted but centered at 0.

The ripples around infinity can cause some distortion in the reconstructed signal, which is why other interpolation methods may be preferred in some cases.
So it will be 1 at the center and 0 everywhere else.
You sum the cardinal sin at different point to reconstruct the signal..
To get the value of the signal between two samples, we need to take into account the contribution of the sampling period. This is because the cardinal sine function assumes that the signal is periodic with a period equal to the sampling period. By including the contribution of the sampling period, we can estimate the value of the signal at any point in time.

# FT of a band limited signal
Given a signal $x(t)$ **which is a band limited signal as defined before**, **the Fourier transform of the signal will consist of shifted and scaled copies of $X(f)$**. Where $X(f)$ correspond to the coefficients of the harmonics composing the signal $x(t)$ (the amplitudes). 

The Fourier Transform of a band limited signal can be seen here:
![[Pasted image 20230524163958.png]]

The Fourier transform for a continuous signal is different than the discrete one as we have seen in [[Fourier Transform]].
We make the Fourier of the samples and we obtain the spectrum regards to the transformation. The result is basically a spectrum made of a set of distinct frequencies composing the sampled signal.
The spectrum itself is repeated multiple times in the plane, as it is centered around multiples of the sampling frequency.
So we have spectral replicates also called aliases that are centered around $f_s$.  You can imagine an infinite number of replicas.

### Spacing between the replicas
The replicas of $X(f)$ are spaced depending *around the sampling rate* $f_s$. They are centered around 0 with spacing $f_s$ from their central point.

There is the problem that *if sampling at a too low frequency, we may have overlapping between replicas as it may be seen below*

![[Pasted image 20230524164154.png]]
If you sample at frequency $f_s$ greater than the maximum of the signal. You increase the distance of the replicas, so not overlapping!

![[Pasted image 20230524164238.png]]

*If we sample every T second, the spacing between the replicas in the frequency domain is equal to the sampling frequency $f_s=1/T$*.

**Ignoring what there is between samples, there is the fact that the sampling process throws away lots of information, but since the signal is perfectly band limited, there is no information lost**. *You must account for this in system design!*
*Then take the spectrum and taking the blue part being the original spectrum and having the replicas without overlapping, you have all the information to reconstruct this continuous in time signal*.

With the Fourier transform the signal can be both be represented in the time domain and in the frequency domain, allowing us to convert between them. Using the spectrum you may approximate the signal which is continuous in time, but with discrete samples.
What happens when you sample at a lower frequency, the resulting samples will not contain enough information to reconstruct the signal accurately. This can result in aliasing, distortion, and loss of information.

### Aliasing in depth
Appreciate the aliasing effect you may see that for instance: if you have a signal and know its frequency, you may sample the signal and be able to reconstruct it. But without knowing the frequency *you may reconstruct the wrong signal*.

* Given a sinusoidal signal of frequency $f= 1/2\pi$ which is band limited
	![[Pasted image 20230613183103.png]] 
	**if you know its frequency you can predict precisely the sampled signal.**

There is the problem that **from the sampled signal you cannot find necessarily the frequency of the original signal.**
As it may be seen here:
![[Pasted image 20230613183216.png]]
If you do not **have enough sample** you may construct over the same samples the green signal besides the blue signal.
In this example the sinusoid was taken at a frequency $f'=f/6$, so $1/6$  of the original signal frequency $1/2\pi$.
**This means that the samples will represent more than one signal, which is totally wrong and does not allow to reconstruct the blue signal**.
We may see also how a red signal as below, with an higher frequency may fit in the samples:
![[Pasted image 20230613184056.png]]

This problems holds for all signals.

#### Overlapping example
It can be seen in the images how the spectrum of the sampled signal $s_c(t)$ consist of infinite replicates of the spectrum $s(t)$, those are centered at frequencies multiple of in this examples $f_c=3$

Given the spectrum of $s(t)$:
![[Pasted image 20230613184355.png]]

Then spectrum of $s_c(t)$:
![[Pasted image 20230613184431.png]]

The requirement of Nyquist to have the signal $s(t)$ *be limited in band* is for this reason. As if the signal in the example can be limited at frequency $f_M=1.5$, we can disregard all replicas that have higher frequencies than it!
It can be seen here:
![[Pasted image 20230524164645.png]]

We want most energy of the signal to be limited in the end.
The ideal spectrum of the sampled signal is as follow:
![[Pasted image 20230524164719.png]]
Basically they are not overlapping and when one replica ends, the other starts.

The sampling theorem gives us an hint on the minimum frequency of sampling, providing a proof to reconstruct as most as possible exactly the signal.
Using the Nyquist frequency, we can choose $f_c$ to ensure the above case, so that the replicas of the spectrum of $s(t)$ do not overlap.

## Some sampling frequencies examples
Given a sinusoid, it is supposed to sample it at a frequency $f_c>2f$, saw there
![[Pasted image 20230524164831.png]]
**As we may see here, we sampled at a frequency that is higher than double the signal frequency**

***But the result of the interpolation of the samples, to reconstruct the signal is as follow***
![[Pasted image 20230524164934.png]]
This one is not accurate and does not *reconstruct well the signal*.

By Increasing the sampling frequency and getting it higher than signal frequency, we still may have a problem in the reconstructed signal
![[Pasted image 20230524165005.png]]



![[Pasted image 20230524164903.png]]
As it can be seen here **while the situation improves, and the reconstruction is good for a short interval, the whole result is not a sinusoid!**

## WHY
The problem is that we need:
* limited in band
* sampling at a frequency double the frequency of the signal ($2*f$)
* you need a number of samples that are **infinite in number**
What happens is that even if we satisfy the first two points, by sampling only a finite number of points, the result will include error in reconstructing the original analog signal. *The continuous signal contains an infinite amount of information that a finite set of sample cannot contain*.
**The more sample we acquire, the less is the error in signal reconstruction, but it will never reach 0 with a finite number of samples**.

## What Nyquist did say
Nyquist requires a signal that is limited in band, but not all signals are limited in band.
A finite duration signal will have a spectrum that extends over a range of frequencies. The spectrum is the distribution of the signal's energy over different frequencies.
To have a signal limited in bandwidth then it is necessary that *the signal does not have energy going beyond a frequency band*. For this is necessary that the signal extend infinitely in time.
We can have signal whose higher frequency have low energy or high energy.

What Nyquist stated:
* The boundary is on the frequency of sampling

What Nyquist did not say was:
* the boundary on the number of samples, the **theory works on an infinite number of samples**.

**But we can in any case sample the signal, in finite time and reconstruct it reasonably well.**
No signal is strictly limited, in bandwidth meaning that is unlimited in time this has no physical meaningfulness. Because in practise *they are* ***almost*** limited in band, so their spectrum beyond their band is small, meaning that their energy beyond the band is small.

*There will be little distortion due to this limitlessness* but with good sampling it will be negligible.

### Cutoff Filter
We can apply a cutoff filter to signals that are unlimited in band and focus our attention on a spectrum part. This spectrum part corresponds to the part where most of the energy is concentrated. The cut off signal cuts out components of the signal by **cutting frequencies above a threshold** and then sample the signal. Thus, allows to meet the Nyquist requirement.
You can also use cutoff filter with limited band signal, because these signals are not really limited in band, but they have little energy behind the band limitation. To cancel this little part of signal use cutoff, and this result also having a better signal.

Low pass filter with a cutoff at half the sampling frequency $f_s/2$, but an ideal filter cannot be realised, as you would then attenuate high frequency content. To solve this, you use oversampling and then a cutoff filter, to reduce the loss of attenuated frequencies.

## What Nyquist did not say

«I am going to sample at 8 KHz, so I need to use a filter with a 4 KHz cutoff»
* Sampling at rate $N$ samples per second **Nyquist did not say that you can use an anti-aliasing filter with a cutoff at frequency $f=N/2$.**
* The filter applied to the signal, does not put to $0$ the frequency higher than the limit that we give, it just attenuates its component frequency. Basically *there is no analog filter that is perfect*, there is a **significant amount of frequencies above 4 KHz** that pass, although they are attenuated.
* The aliased signal is not negligible and seriously disturbs sampling.

Meaning that just sampling with a signal with a cutoff half of the frequency cutoff is not enough.
If you want to apply the theorem the solutions are:
* use a more complex anti-aliasing filter, which anti alias filter, without resampling but getting a filter that has a steep slope, so a filter that has a fast transition from passing frequencies to attenuating frequencies. In this way one can cutoff the signal to satisfy the limited band to apply the Nyquist theorem.
	![[Pasted image 20230524165433.png]] 
* You oversample, we may also increase the sampling frequency, as by increasing it, we consider different in replica of the spectrum for example. In this way the replicas do not alter the signal, we move the replica further from each other.

#### Telephone companies solution's
The method is to used as filter to resolve this situation was to use a stronger cutoff  with a low pass filter which filters anything in the band between 0 and 3 KHz.
The frequency that pass are over 3 KHz, than sample at a frequency of 8 KHz, **more importantly they oversampled at 8 KHz**.

So limit the band of the signal, than oversampling at a higher frequency. **It is impossible to give general rules for all cases, but it gives example to study your specific signal.**

#### Another case
«I need to monitor the 60 Hz power line, so I need to sample at 120 Hz»
«We have a signal at 1 kHz we need to detect, so I need to sample at 2 kHz»

**Nyquist did not say that a signal that repeats $N$ times a second, has a bandwidth of $N$ Hertz**. Basically a power line of 60 Hz would mean that the signal repeats every $T=1/60$ Hz. But this does not correspond to the bandwidth. That is because the powerline is nominally at 60 Hz, but there is a lot of distortion, as it may be seen in the figure below, so there are many frequencies involved!

![[Pasted image 20230524165706.png]]
The main signal is of 60 Hz but it is not true that it is limited in bandwidth at 60 Hz.
It does not work just sampling 120 Hz, as you see the ripples, a component is at higher frequency, up to 300 Hz, the 2°, 3°, 4°, 5° harmonic must be considered with their variation (the latter is to 300 Hz).
You need to sample at least at 600 Hz, as this is the maximum frequency that you want to consider. **But in reality even more, because you do not know the phase of the signal, if you want to have accurate sampling in a short time, you need to oversample accurately**.

#### Rephrasing the question
«I need to monitor the 60 Hz power line, so I guess need to sample at well over 120 Hz».

**Not even that, in some case it may be even better to downsample, which means to at first oversample, then waiting long enough with patience to connect enough sample at an high rate before decimating (removing) some of the sample to archive a lower effective sampling rate.***
Or just to sample at a lower rate at the start but wait long enough to get enough information to reconstruct the original signal.

You may discard the effects of the other Harmonics and only care about the main frequency of the power line signal, so discarding the harmonic which are greater than the fundamental harmonic, **if you have as in this case** a steady signal, which has a known and steady frequency, you may need to sample the signal only on some part, and you may discard the transient phase.
You can reconstruct the signal, by reconstructing it at a lower frequency, for example a frequency slightly over 20 Hz.

The sinusoid at different period, given there, if our device cannot sample at a certain frequency.
You have a sampling period = signal period + a small interval.

So we may get a sample in different part of the signal period. **What we see is that the signal phase, within a cycle will advance a little bit for each new sample**.
This allows us to reconstruct the signal, once we wait enough sample, in the required time.
**We need the signal to be stead, repetitive and with a steady frequency to do that**.
![[Pasted image 20230524170148.png]]

This works only for AC/DC signal.
What you do is to make an analysis of the signal and its nominal frequency, which is different from what we did before, as we need to consider (want) also the 5° harmonic.
This shows how the theorem can be applied in different way.

Now we cant get infinity, but when you see the sampling of 20, you know that you approximate well the curve for a bit, after that, you will lose in the middle and after that.
You cant do better than going to infinity, at least us as much samples as possible to approximate better the signal.


# Quantization
In general the values obtained with sampling are Real numbers, but in some applications, even a representation in floating point (32/64 bits) is considered prohibitive (e.g. in IoT).

For example in Arduino Uno ([[Embedded Systems and Case study of Arduino]]), there are only 10 bits per integer, which can be used to represent a sample.

We may see below how the quantized value and the sampled value may be different, because the quantized value may be rounded to the nearest value in the quantized representation, rather than the continuous value.
![[Pasted image 20230614120952.png]]

Given k bits, we can represent integers in the range: \[0, $2^{k-1}$\]
We can represent the integer closer to a sample in that range.

# Doing quantization from a signal
Given a signal sampled at a frequency $f_c$.  This means that the samples are taken at intervals $T_c=1/f_c$

Letting $x_k\in\mathbb{R}$ be the sample read at the time interval $I_k$. This is uniform quantization where the input range is divided into uniformly spaced quantization levels, this means the intervals between quantized values are all the same size.

The quantization will encode $x_k$ in an integer value $y_k\in[0,2^R-1]$. Then we use a R-bit scalar quantized. It is said scalar because the samples are quantized individually.
There is the requirement of R bits per sample, those R bits per sample are defined as the **quantization rate**.
The bit rate for a signal sampled at frequency $f_c$ is $R_b=R\cdot f_c$ bit/sec.

Keep in mind:
	$R_b=R\cdot f_c$ bit/sec bit rate for a signal sampled at frequency $f_c$

When we represent the signal as the quantized signal, you introduce an error, as in the different than sampled in time t instance, you represent the quantized value

For example this is the signal sampled
![[Pasted image 20230614122405.png]]
This is the quantized signal:
![[Pasted image 20230709153652.png]]
$s(t)-y_k$ error, with y being the k-th quantized value.
You do not represent exactly the signal value.
You represent a value on the subset of number that can be represented with your system of representation of bits.
There are errors in the difference between signals and quantized values.
As it may be seen here:
![[Pasted image 20230614122434.png]]


# Quantization noise

## Overload 
**You may have an overload with uniform quantization, which happens whenever** have some points at the same distance, and you are not be able to represent a signal, because it is above the maximum value you can represented correctly, as it will have a lower resolution. This happens formally when:
* $s(t)>2^R-1$
This can be faced with non uniform quantization.
Non-uniform quantization can provide higher resolution for certain input ranges dividing bits for higher ranges, meaning that it allocated more bits for certain higher input ranges.
![[Pasted image 20230709154002.png]]

## Granular noise
If all the values in an interval $I_k$ are represented with a unique $y_k$, meaning that if the signal changes, you are not capturing changes. This is called granular noise and you lose the spacing between points.
Basically you have a piece-wise constant signal, meaning that a signal takes a constant value at different intervals of time, there it can happen that phenomenon.
This process of approximating a continuous signal by a piece-wise constant signal can introduce errors and distortions, which can be seen as a type of granular noise.
![[Pasted image 20230614125302.png]]

### Example
As Humans we can hear in the frequency of 20 to 20.000 Hz (20 kHz).
This is too much, what is really needed and acceptable as degradation in quality can be around 4 kHz usually, or even 3 kHz sometimes. That is the level accepted at phone.

### Solution
We apply a sampling rate, twice the 4 kHz frequency that we want to send.
The sampling rate taken is $f_c=8$ kHz. Each sample is quantized on 8 bits (R=8).
So we sample at 8 kHz and not for example 40 kHz (double of maximum).
We get a bit rate of $R_b=64Kb$ ($R*f_C$)


# Exercise on sampling
Consider that the period, is the point where a trig function returns to its starting initial position. Which may be shifted right by adding $-1$ or shifted left by adding $+1$

Given 4 signals, find the Nyquist sampling frequency, by applying the sampling theorem.

Always check if the band is limited, **if the band is not limited then you cant apply the theorem, you would need to apply a cut-off filter**.
- $s(t)=sin(3t)$
- $s(t)= \begin{cases} 1 \hspace{0.5cm} -2<t<2 \\ 0 \hspace{0.5cm} otherwise \end{cases}$
- $s(t)=sin(2t+5)+sin(8t-1)$
- $s(t)=7+sin(2t-1)$ 

#### $s(t)= sin(3t)$
It is limited in bandwidth as its a sin limited in $-1$ to $+1$ and its a periodic function so its a energy signal.
1) Period is 2$\pi/3$,
2) given the period, we find the signal frequency $f=$ $3/(2\pi)$ 
3) We find the maximum frequency, which is  $f_m$ = $f$ $3/(2\pi)$:
5) Then we calculate the Nyquist sampling frequency $f_c$ = $2 \cdot 3/2\pi$ = $3/\pi$ 

#### $s(t)= \begin{cases} 1 \hspace{0.5cm} -2<t<2 \\ 0 \hspace{0.5cm} otherwise \end{cases}$
This signal is not limited in band, as its maximum value is 1.

That is because the signal is limited in time **but its not limited in band**. If we make the Fourier transform of this, we get contribution in frequencies that go up to the infinite frequencies contributing. So we cant have a Nyquist sampling frequency.

#### $s(t) =sin(2t+5)+sin(8t-1)$

The signal is limited in band.
The period of this one is $T=2\pi/8$
(as $sin(8*(2\pi)/8-1)=sin(-1)$))

The maximum frequency is $f_m= 8/2\pi$.
You have two sinusoid, but you consider just the second to calculate 7 the maximum sampling frequency, because it has higher frequencies

As such we cant calculate the Nyquist frequency:
$f_c= 2* 8/2\pi$.

#### $s(t) =7 + sin(2t-1)$
This signal is limited in band, as we just sum a constant term to a sinusoid function.
In reality the period is $2\pi/2$ as for the argument of the $sin$ function $2t$.
7 will influence the frequency but the influence of sin gets higher values.
The maximum and unique frequency of the signal is then $f_m=2/2\pi$. 
The sampling frequency is then $f_c=4\pi$ being its double.


# Exercise on Quantization
Consider an analog to digital converted ADC, which performs Q-bits quantization of signals. Using Q bits for signals in the range \[0,M\],
Compute the resolution of quantization and the maximum absolute quantization error.

Represent a range and divide in by using q bits.
What is the resolution of the quantization, meaning the distance between two points, and then the absolute quantization error!

We represent a range and divide in by using Q bits.
The quantization resolution is the distance between two points. We represent a range using Q bits, so the quantization resolution is M/$2^Q$, 
Given that we may calculate the absolute quantization error.

![[Pasted image 20230614183156.png]]

* If Q = 10. the quantization resolution is 5/$2^{10}$ = 0.0049.
	* The resolution is the distance between two values.
* The maximum quantization error is **at most half the resolution, because by rounding a value, we may at most most miss half of the interval in precision**. So it is at most 0,0049/2.
		* **The error is the distance of two adjacent values**


So on for all other cases
![[Pasted image 20230614190943.png]]

How a controller can build up a topology and communicate with switches to construct a topology.
At the exam even the scheme and interaction may be to do.
The generations changes must be studied!
The architectural schema are not required!

## Summary 
Sensors produce analog signals that need to be converted to digital form for processing by computers. Sampling involves taking discrete samples of the analog signal at a certain rate. While sampling allows us to represent the analog signal in digital form, it does not necessarily provide all the information required for perfect reconstruction.

The Nyquist sampling theorem states that to perfectly reconstruct a continuous-time signal from its samples, the sampling frequency must be at least twice the highest frequency in the signal, known as the Nyquist frequency. This ensures each cycle of the highest frequency is sampled at least twice.

Aliasing occurs when a signal is sampled below the Nyquist rate, causing different signals with frequencies above the Nyquist frequency to become indistinguishable in the sampled signal. Anti-aliasing filters can be used to remove frequency components above the Nyquist frequency before sampling to prevent aliasing.

In practice, the sampling theorem is applied to signals that are effectively band limited, meaning most of the signal energy is contained below a cutoff frequency. The theorem also strictly requires an infinite number of samples; in practice we use a finite but sufficiently large number of samples to approximate it.

Higher sampling rates and more bits of quantization provide higher resolution and accuracy but at the cost of larger data volumes and higher computational requirements. Non-uniform quantization assigns more bits to higher value ranges for higher resolution.
