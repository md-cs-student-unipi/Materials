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


