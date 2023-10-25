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