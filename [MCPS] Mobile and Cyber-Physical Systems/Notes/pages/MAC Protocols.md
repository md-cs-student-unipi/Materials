
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



