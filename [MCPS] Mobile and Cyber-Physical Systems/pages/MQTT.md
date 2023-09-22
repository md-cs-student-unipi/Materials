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