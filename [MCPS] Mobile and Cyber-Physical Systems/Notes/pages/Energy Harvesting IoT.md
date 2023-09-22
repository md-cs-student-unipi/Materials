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