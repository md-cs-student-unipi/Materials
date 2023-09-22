Sensor to keep track of animals, 24 h a day.
Tortoise case of the paper.
We can distinguish between two approaches:
* biotelemetry: attach a sensor without storage, whatever it samples, it should be transmitted immediately. There is no storage. For example a radio collar transmitting the presence of a bear, and its position, detecting the angle from where the collar transmit to find its position.
* biologging: with the ability to store information, and no ability to send information, but actually biologging. Attach the sensor ( with sleeping animal), and then retrieve by hand. **Biologging are invasive devices, which means to catch it, sedate it, add the sensor, catch it again to get the data, so reduce this activity**

Now sensor can collect parameters concerning the behaviour, so biologging.
Biologging allows to study the habits and the life of an animal.

Study on the seals, detecting their activities were done, other on penguins.

Procedure:
* collect data
* classify what the animal is doing

Biologging will produce values and store local.
IoT and artificial intelligence can be used to send few data to server and reconstruct a series.

# Device Perspective

You have a long time series. With telemetry, you may send all the data.
Transmitting everything is expensive. On the other hand, you may solve the problem of the transmission, storing data. But if the storage is damaged, then all is lost.
**Limitations on the device storage, may then obligate you to retrieve them (which is invasive)**.

We do not need a simple log, but a full micro controller, producing a huge amount of time-series data
then using on board an automatic classifier. Which means to have a semantic classifier, at this point the activity for an animal are a few, and are reduced from time to time.
That has an implicit effect of prolonging the lifetime of a device, considering also the size of the memory of the device.

# Tortoise

In this case, there is an adaptive duty cycle, depending on conditions and branches.

Tortoise are protected when the eggs hatch.
They are released in the wild when protected against predators.

The problem is:
*finding the nests*, it is not as easy as turtle which have fixed nests on beach.

Tortoise may spread in different places and in different periods their nests.
In the places where they make a nest, the tortoise will cover the nest and laid the eggs.
The researcher collect them when the mother tortoise hatch them.
This is easy in Galapagos.

In Tuscany not, because there are lots of trees and forests.
So track with a device if the tortoise is laying down the eggs.
Then with GPS the researcher finds mother tortoise.

The device does not have GPS actually, but it has a way to find where the tortoise is.

### Detecting excavation
The tortoise make a particular movement when excavating a nest.
It takes a couple of hours, and it may happen that the tortoise begins, then gives up, and moves somewhere else.

The tortoise will lay down eggs in 4 months in the summer.
Ideally add it in the back of the tortoise at the start.
Consider that 1 year is too much to keep on, and it is not invasive to remove and add on tortoise. The battery would not last 1 year.

**Accelerometer: if not going fast, then it measures the gravity**.
When the tortoise excavates, the accelerometers sees the negative or positive gravity depending on the inclination of the tortoise when it excavates.
* To detect laying of eggs, you use the accelerometer, which you sample at given frequency, usually high.
* To spend less, find the right environment to lay, so light and temperature, as to limit the use of accelerometer.
You may turn off the accelerometer.


For temperature and light, you may have a really tiny duty cycle. As temperature takes a lot to go high.
![[Pasted image 20230331164107.png]]

Accelerometer is sampled at 1 Hz.
And the accelerometer will be sampled in the time required to implement activity recognition with a good accuracy.
If nothing relevant is detected, go back with very low sampling of light and temperature.

If an activity that is compatible with nesting, to reduce false positive, have a sort of confirmation, by repeating the activity of monitoring.

We may detect that step 4 is done only 4 times a day.

Usually the lifecycle is on step 1. So you will have a very long lifecycle.

We like a device with a small battery, so that it fits on a tortoise easily.

### Activity Recognition

Activity recognition has the goal to automatically recognizing the actions of animals from the signals collected during its activity.
Biologging provides the data, that are fed to the activity recognition system, which processes the data:
* processed by human
* and processed by an Automatic System
Then the activity is labelled:
* as digging for example
![[Pasted image 20230621094556.png]]


### Sensors are good or bad?
The strengths of using sensor is that they give punctual observation in time and can be used both in:
* wild environment 
* domestic environment
They output large quantities of data in time-series form, which requires suitable data analysis algorithms

The weaknesses are the constraints given by the battery lifetime, for intensive monitoring we may need off-line analysis. When the memory fill up or in the worst case of battery usage the battery drains out,  we need to retrieve the sensor physically, as its attached to the subject.


### Device Perspective

#### Conventional Approach - Low power logger
The conventional approach is use a low power logger.  It collects the data and communicates it:
* as a time-series to a remote station.
* or by retrieving the logger on field and get the time-series data

**Which are problematic solutions, especially in the biologging case!**
![[Pasted image 20230621100007.png]]

1) requires a lot of power to use the radio for that huge amount of time series data
2) its intrusive, as you physically have to go there and retrieve the device
![[Pasted image 20230621100050.png]]
#### Novel Approach - low power micro processor
**The goal of the novel approach is to reduce the amount of data sent, basically not sending a hug time-series but an output that already processed it**.
*A classifier was embed on board, processing the data and storing the result, resulting in better memory usage and communication efficiency*.
![[Pasted image 20230621101021.png]]

# Tortoise@ project
What they did was to localize Tortoises Nests, by:
* recognizing the digging
* having GPS
Then sending to a remote station the position of the digging.

Given that Tortoise lay eggs for over 4 months in the spring, the device must work for at least 4 months, so the battery should not run out before.
Since tortoise dig to create a nest, they found that accelerometer was very well capable of recognizing it.
**But there must be also some precise conditions for temperature and light, so low energy sensors as light and temperature were used, to limit the accelerometer usage.**


### Datasets

The initial Dataset was created by recording the behaviour of tortoise in captivity at «Centro di protezione tartarughe Mediterranee» at Massa Marittima, Italy
Spot digging, like when a tortoise does it, can create a lot of noise. There is a 300-second window to spot patterns, which have a size of 90 seconds. Using an accelerometer, if it is inclined to the left or right, you can obtain numbers that allow you to identify digging behavior that must be studied.

**The accelerometer produced a raw time-series of value of the x axis (not required the y axis)**

The data collected at Centro di protezione tartughe Mediterranee was then divided in two sets for *training and test sets*.

There are two dataset:
* Sequence dataset:
	* made of sequences in the 300-second window.
		* in this window 1 Hz sampling (so 300 sample at window)
	* In total they made 126 sequences, where they provided positive and negative classification (for the digging activity)
	* 56 sequences of those **were reserved for the test set, the others for the training and validation set**.
* Patterns dataset
	* a sequence of 90 seconds (time window), sampled at 1 Hz (so 90 sample at window)
	* 67 patterns with positive classification
	* 67 negative for *model selection*, allowing to select the best machine learning model
	* 10 patterns with positive classification and 10 negative for **model validation**
**The activities detected are**:
* digging
* walking
* eating
All can be recognized by different patterns in the x axis.


### Windowing
The size of the window was selected because it depends on the shape of the digging activity signal.
They may see how a portion of the window is taken for pattern recognition.
![[Pasted image 20230621115639.png]]


## Processing
1) Fill a model with a windows: Asynchronous task, as you sample and then taking a window you compute. The whole output depends of the Neural Network depends on the entire window.
2) Fill a model with all the input arriving: Synchronous task, you classify a stream of data while arrives. **There is a state kept with different sample, there for any sample you get a result**. You need something to aggregate the results. The output of a neural network does not need an entire windows of sample in this case, so it each sample is based **on the last 90 seconds, which are sufficient to find a pattern**.

Keeping the neural network has some memory overhead.
A Supervised Machine learning model while having the best performance is the worst in terms of memory overhead.

![[Pasted image 20230621121347.png]]

The best tradeoff is to use ESN
![[Pasted image 20230621121338.png]]


They used ESN neural network, which are a type of recurrent neural network. A recurrent neural network (RNN) is a type of neural network that can process sequential data by maintaining an internal memory state.
ESN uses a large reservoir of fixed, randomly connected neurons to transform input into high-dimensional features. ESNs are easier to train than traditional RNNs and have been successfully used in tasks such as time-series prediction and image classification.

Asynchronous task: The ESN neural network has an accuracy rate of 55% and operates on a single pattern, which can be amplified. Additionally, ESN has low memory consumption, using only 0.1 kilobytes, making it suitable for devices such as Arduino with limited RAM. Even CNN, which requires 3.5 KB of RAM, may not be feasible due to the cost associated with processing new data. ESN can be re-iterated to enhance the results.

To optimize synchronous tasks, the ESN neural network can achieve an accuracy rate of 93% by voting for each pattern, while maintaining low memory usage of only 1KB.

## Energy Efficiency
Factors:
- Avoid sampling at night.
- Environmental conditions can be sampled at a rate of 0.01 Hz, very low rate (temperature and light).
- When the environmental conditions are suitable for laying eggs, sample every 5 minutes at 1 Hz.
- If there is a positive response, the accelerometer sampling is repeated 3 times, in this way you reduce the rate of false positive
- if there is a negative response **suspend for half an hour the sampling, noting that the digging lasts more than one hour**
- only when the device is sure of the tortoise excavation it transmits, limiting the energy consumed

## Memory Consumption

There are two data structures in memory:
* a vector of SVM (Support Vector Machine), a vector refers to a feature vector, which is a mathematical representation of a set of input data. For conventional neural network, keep a whole window before fitting.
	* Also you need to keep a buffer.
* A structure to store the acceleration samples, ***In the worst case the whole window of 300 samples, considering that it is an analog signal, and it is converted from analog to digital with ADC that will give a certain size to the sample.**.

An Arduino has 10 bits for digital input, and we can assume that 1 sample is stored in 2 bytes. If you have 300 samples, storing a window of samples occupies 600 bytes.
This is relatively low, consider that cellular can hold much more.
## Cloud-Based vs Local

_Sometimes, local processing is better_.

If all computation is done on the cloud, data must be transmitted continuously without storing much locally. However, it's crucial to have a way to program the device from the cloud. If the device only transmits data, it won't be able to decide when to switch from GPS mode sampling to accelerometer mode. Therefore, you must send GPS data continuously to trigger the accelerometer.

With cloud-based processing, the device needs to store and transmit GPS position data every half an hour. A GPS position consists of two 32-bit long integers for latitude and longitude. Additionally, data sampled at 1 Hz must be stored and transmitted. In this case, low-power sensing of light or temperature may not be available.

Working for 4 months means:
- 46 KBytes of GPS data transmission
- 13 MBytes of accelerometer data transmission

With local processing, only 32 bits of latitude and longitude are needed when detecting excavation. The storage would only require about 3 KBytes at most, even less using ESN. In this case, the GPS can be activated only when detecting an excavation.
With ESN, you can keep the data usage below 1KB.

The storage in the exercises is considered as **permanent storage, not RAM**. It's essential never to reach the point where a device has to discard memory. The information about the device's lifetime tells you the limit up to which the device can be used before needing to be replaced.

## Examples with totally wrong solution

### Ex 1
![[Pasted image 20230621155711.png]]

### Ex 2
![[Pasted image 20230621155727.png]]
### Ex 3
![[Pasted image 20230621155739.png]]
### Ex 4
![[Pasted image 20230621155751.png]]

### Solutions
![[Immagine 2023-06-24 143006.png]]
![[Immagine 2023-06-24 142941.png]]
![[Immagine 2023-06-24 125414.png]]

![[Immagine 2023-06-24 125341.png]]