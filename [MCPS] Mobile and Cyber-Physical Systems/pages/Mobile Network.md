
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