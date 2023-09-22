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
