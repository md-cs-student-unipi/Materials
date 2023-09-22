![[Pasted image 20230328215626.png]]
20 Hz: period of sampling (requirement of sensor).
Sampling a sensor takes 0.5ms. 
**Having 20 Hz sampling period means that 20 samples will be produced in 1 second.**
(x Hz represents 1s/x = **time to get 1 sample**)
Doing 1/20 *we get a sample every* 0.05seconds, in milliseconds it is 50ms 
So the Period is 50ms, and within this period, there is the measurement in 5ms.

* sampling requires both processor and sensor to be active
* the computing will be done every 5 samples on a remote server
* The transmission time is 2ms and requires both processor and radio active.

Heart rate is computed every 2 seconds (on 40 samples).
The HR is computed by a server.
The transmission time is 2ms and requires bot processor and radio active.


5 samples at a time are send to the **server**.

Server will compute every 40 samples.


### Duty cycle of sampling

We have
* 0.5 ms: working time
Duty Cycle of sampling: 0.5 millisecond (sampling time) / 0.05 second (sampling period)  
In percentage 0.01 * 100 = 1%.

We get a sample every 50 ms.
We need 5 samples to get 5 SAMPLES

# Duty cycle of transmission

The transmission is done every 5 samples. 
To get 5 samples we need 5* 50ms = 250ms
or 0.25 seconds.
So every **250 ms we send the data in 2 milliseconds**.

Duty cycle transmission
2ms (transmission)/0.25 sec (transmission period) = 0.008
In percentage: 0.8%



**Duty cycle cannot be above 1, ever.**


# Duty cycle per component
Duty cycle of processor: *it is the sum of the two duty cycle of transmission and sampling, as it does both activity independently without intersection*. Consider the minimum common number of those elements, and find the time where this is active.

Microprocessor duty cycle: 5* duty cycle of sampling + duty cycle of transmitting

Pw consumption in 1h: multiply by 1 hour the calculations.

Sensor energy consumption per duty cycle: $5mAh*0.01 +5\micro Ah*0.99$  = 0.55mAh
(we can express the power consumption with mA**h** as the voltage is constant, so we avoid to use Joule)



For the processor we must sum both the duty cycles
Processor solution: 
$(0.01+0.008)*8mAh+ (0.982)* 15\micro Ah$ = $0.144 mAh+14.73 \micro Ah$ = $0.144 mAh+((14.73)/1000) mAh$ =$0.144 mAh+14.73 \micro Ah$ = $0.144 mAh+00.01473mah$ = 0,1587

Radio consumption(**Left as exercise before exam**) = 0,1798.


**Duty cycle of the processor must be the sum of the two sampling and transmitting dc.**

(Using the radio in receive mode, it means that we would have another duty cycle to sum to the radio, for transmitting and receiving)


Lifetime = Power capacity fully charged / total power consumption   =  $$\frac{2000mA}{(0.1798+0.1587+0.055)mA}=5087 h$$


-------------------
# Exercise 2
![[Pasted image 20230329095846.png]]

The computing is done every 2s, and for 4ms.
It follows that it is:
duty cycle of computing: (5 ms) / (2 seconds) = 0,0025 ms 
computing:0.25%


The transmitting is done every **10 seconds(having collected 5 values computed)**
duty cycle of transmitting :
2ms/10s = 0,0002ms
transmitting:0.02%


The sampling is as in the exercise befoe.
sampling : 1 sec => 1%



#### Component by component

Processor time (*sum duty cycle of computing, sampling, transmitting*) =
1.27%\ * 8mAh + 98.7% * 15 $\mu$Ah = 0.1164 mAh



Radio time: $0,0002ms*20mAh+0,9998*20\micro A h$ = $0,004mAh + (19.96/1000)=0,004mAh+ 0,019 mAh = 0,024 mAh$

Lifetime and sensing time left as exercise before the session.

**Do not sum to the whole period the active period, you must send every X, so account for the time to send.**

## Takeaway
You need to reduce the duty cycle to spend less energy.
Not always you can reduce enough to spend less.
But you may move freely from device to cloud computation, which opens a range of possibility on the design and duty cycle.
Reducing the duty cycle is possible, if you find among all possible implementations, the correct trade-off.
The problem here are the same, but we have two completely different implementations.
And we found different values.