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