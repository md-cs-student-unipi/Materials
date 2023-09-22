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
