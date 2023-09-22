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