Several sectors to show different cultivate at the same time. As a consequence none of them will operate in ideal condition.


Two sectors:
1) conventional sensors: minimum temperature ensure, humidity sensor + moisture of the roots in the substrate. Automatic logic
2) Top sector: more modern control sectors.
![[Pasted image 20230618123327.png]]
There are also two sub sectors for different type of cultivation


Relate each sensor to its position, its type of transducer used with it.

![[Pasted image 20230618123420.png]]
Note how there are different type of sensors used.

**An IP network for sensors and plants was made, using LAN and Wi-Fi**. *There was a single point to govern the green house*.
**Sensors came from different manufacturers, making necessary calibrations**.
For each transducer make a calibration. Note that for each calibration it may be useful to keep data of the calibration. There were different standards and technologies involved, with several digital twins for sensors.


It may be see here the architecture of an Industrial IoT configuration:
![[Pasted image 20230618123719.png]]
We see how the sensor is connected to a gateway using TCP/IP. Furthermore the gateway connects to a MySQL DB internal and to a router.
Using [[IEEE 802.11]] they interacted with a touch screen for control and monitoring. The router would lead requests to the controller via Ethernet TCP/IP. The controller would control all sensors. There is also a Server, which may be local or remote, which is connected to a Router with Firewall if remote and accessed via internet.


This is the information system structure:
![[Pasted image 20230315162121.png]]
![[Pasted image 20230618142328.png]]
We may see for each transducer the sensors (a sensor is a bigger entity with one or more transducer) its paired with, its type, its measurements and its calibrations!


There is in general a digital twin, which allows to control devices from the controllers.
Models were made to get the need for fertigation depending on the actual needs of the crops.

There are parameters based in the growth of a plant. And create AI models for the growth prediction.

Lettuce grow:
* blue: actual growth
* black: what the model predicted
![[Pasted image 20230618142525.png]]
It is seen that more or less the predictions where accurate
The prediction may work in a short time. But difficult in the long time.


You now need a model to decide what to do with the parameters, as it can allow you to have a finer grain control of your fertilisation system.

The future is to have a decision system for all of that.

# DOREMI Project
Coaching system for old people at risk of cognitive decline, this happens with several different causes.
Produce knowledge and tools with protocol and methods to deal with cognitive decline, to reduce time to be hospitalise or need assistance.
Those problem also amplify themself in conjunction.

DOREMI LIFE-STYLE: it will advise people to have a good lifestyle.
![[Pasted image 20230315164414.png]]

The information are collected, then analysed and then to provide the feedback.
The feedback may be given to also increase the difficulty level, for example a physical exercise one.
They gamified lifestyle protocols and in three phase:
* engage in social game, exercise games and diet advice and cognitive game
* monitor the cases of nutrition, social activity and physical/cognitive activity
* Analyse: analysis on how the elderly respond to the proposed protocol
Consider that the gamification for physical activity is limited as they are elders with elderly problems after all.
![[Pasted image 20230315164717.png]]
A focus group was tasked to define the GUI which is see over there.
It has tree categories:
* Cognitive game
* Exercise area: show what exercise to execute and how to correctly execute it
* Social Area: social games area

## IoT part
Design of the IoT subsystem. With an hardware part developed by a Spanish Company. Software developed in IoT software by CNR.

* Wristband: developed a new one + assess of wristband in the market and compare their data with our models. Getting also estimation of the power consumption.
* Environmental Sensor: sense social interaction, providing some evidence of a possible social interaction. To do so they also use [[Indoor Localization]].
* Balance board: a copy of the Wii board, which assess user balance
* App for tablet: contains dietary data, allows to play games (social, cognitive, exercise games) and allows *to collect feedback*
The result of those sensor are checked by specialists for the particular type of sensors.

## Database
The database were made in Austria
The raw data go from sensor to a DB, then there is pre-processing.
According to a Config DB there is **Activity Recognition using Machine learning models**
Finally the data went to a database for processed data. Then the processed data go to a reasoner application, that is rule-based on rules configured by medical specialists.
Dashboards and Applications also were able to see the data from the processed data DB.
![[Pasted image 20230618155303.png]]

Using the dashboard, the medical personal is able to:
* adjust the protocol
* get data from the system to adjust the protocol.

## KPI
There were many Key performance indicators, for many different areas.
Many KPI depend on the subsystems to implement.
We have two types:
* Clinical, its KPI are:
	* Vital Parameters, 
		* the data it gathers
			* weight
			* balance
		* the device: the Balance Board*
	* Physical activity:
		* device: wristband, which collects as data:
			* **indoor position**
			* number of steps
			* wrist acceleration
		 * device 2: environmental Wireless Sensor Network (WSN), which allows to track physical activity with sensors activation data.
* Social, its KPI is:
	* Number of Interactions (social), using:
		* Environmental WSN here too, with the data of sensors activation
		* Smartphone with GPS.

Detection of interaction is complicated.
For example if people go out of a room, as a social interaction is dynamic and people may leave the conversation


There are different data flows for:
* sedentariness
* diet
* social area
![[Pasted image 20230315170424.png]]

1) First analysis
2) second analysand
3) third further high level analysis.

## Analyse

Activity Recognition, taking pre-process data and the information taken from the databases.
In each house they had sensors and we have have to relate them.
The Config-DB contains the information about the whole deployments.
The result of the activity recognition, goes in the Processed data Database, but the data processed there is too much.
You need a **REASONER** to give a better explanation to the medical specialists.


## Propose and validate a medical protocol

The medical protocol uses digital tools to obtain reliable information and take sensible decision.
Are our machine learning mechanism working correctly? Is the information reliable?
Or the number of times a person met another person.
This has to do with the correction of the models and the application.
The problem is:
* is our experimental methodology correct?
To meet those requirements:
* everything was subjected to the ethical committee.

Since the system did not have to last for a long time, they could use less durable components.
The tradeoff was to have limited reliability of the components, with the fault detection and on-site intervention from the technical staff.
Different tradeoff may make sense, something make a super efficient reliable system is not a solution.

Before of the pilot, we need to have the Machine Learning model already trained, to do this we needed to get datasets.
Also a living lab was used in of competition of indoor localization systems.

We may see here the flow for reliability requirements and the relative measures undertaken in the design/methodology
![[Pasted image 20230618162414.png]]
The process would then proceed to pilots and then the real study.

## System Architecture
![[Pasted image 20230315172533.png]]
Every user had a smartphone and tablet.
As the wristband connects to smartphone and the smartphone enables it.
The data pass to some processing steps, and are send to a dashboard.


To design fast use different gateways to combine devices.
DOREMI gateway for the balance board.
The localization sensors were using the home localization system of the shells of the wireless beacon.
The wristband was using as a gateway a smartphone.


## Balance Assessment

The Berg Protocol is difficult and require a medical specialist.
There is a threshold to get if one is independent or not on the Berg protocol, and it requires 30 minutes.
**They made an equivalent protocol, with 4 for force sensor and 1 neural network, with duration of just 10 seconds**

With the balancing board, the test could be done independent without a test. The balance board is the one of the Nintendo Wii.
Depending on the balance of your body, one will put more ore less pressure on one of the 4 force sensors of the board.

## Physical Activity Expenditure estimation

Color of the skin is what the sensors measure for heart rate.
My measuring the color of your skin, you measure with frequency, the heart-wave.
The heart beats 60 times per minutes, and so one looks at their frequencies with that. One determines caloric consumption using the parameters of:
* age
* sex
* weight
And there are models to determine the calories consumption.

Those device measurements are not accurate, a chest band are more accurate.
* Doremi wristband
* commercial wristband
* chest band

The metabolimeter is a better machine than those actually for heart rate. It uses the same mechanism of those.
You convert with oxygen and expelled oxygen, you find how much oxygen you burned, so the calories are the difference.

The metabolimeter is a mask.
Then they made the exercise to do in the app games.
From there a dataset was made for the wristband.
**By applying a model to the inputs of the sensors, would allow to get results near the metabolimeter.**


Red line: metabolimeter
Blue line: model over wristband data.
![[Pasted image 20230618163438.png]]
Not much of a distance.
The result at the end was better for DOREMI wristband than the commercial one.

## Socialization assessment

Outdoor: by means of GPS of people involved in the experiment
Indoor: environmental sensor to get how many people go out or stay in a room.

The problem may be that a person may only open the door.
Even a postman giving a packet is not a socializing event.

The idea at the end is:
* passive infrared to see if someone was outside
* passive infrared inside: Locate a person and discriminate their position, with indoor localization.

Train the neural network to discriminate 2-3 people in the room.

## Database
The measurements data go to MongoDB.
The deployment data went to SQL, as it was fixed (e.g. placement of sensors).

We may have streams of data, where we have a data feed collection describing each single measurements from a device, for example a balance measurements.

Each feed goes to an independent document, but there is a collection then of those document.

The data feed collection: contains information about the management. There may be a stream, with the message measurement field.
The message elements are comprised of signal measurements, and with the state of a button of the sensors, describing its state.

There are a data field, some meta data.
Those are a reference to the hardware running the measurement.
We may have specific boards, where one must keep a reference to what specific board.
The measurement will be the same for all balance boards and data field.

By expecting the NoSQL we get the measurements of the balance board.
With the SQL we get the pairing of the board to the user.
**This is done with a reference to the device ID, which is a primary key in a SQL Table**.
With the start time we may segment the time of the stream.
For example the pressure data to analyze will be done given the segment.
*The measurement start also when the board is activated from a procedure.*
![[Pasted image 20230321113038.png]]
Those data then associated with the person and be 
elaborated by machine learning.

**The queries look for:**
* data generated by a specific sensor
	* at a specific time frame

The DB grew vastly, for 20 users, 3 months data per user reached 30 GB per user! 

In the configuration, there was some redundancy in devices to monitor. 
The *configuration system used* enables some semi-automatic centralized configuration of the WSN (Wireless Sensor Network).
A graphical user interface annotates the sensors position and configuration.
All the kits were prepared in Valencia, and then they were send in the UK.
The kits were packed in the UK and send there.
It was seen that for the boards it was easier to buy a new one rather than sending back to Genoa.

## Pilots
There was the need to find people with moderate cognitive decline, able to use smartphones.
But at risk of having cognitive decline.
There was also the need of having them living independently, and they have to accept to be monitored.
At the end from 1000 people, only 32 users.
With two groups:
* intervention groups: 25 groups where the protocol where applied
* control group: 7 groups observed but without protocols applied, to see if the protocol brings benefits.

In UK, Shenley Wood the environment was ideal, as all the apartments were identical and they are close.
So the sensors placement were easily replicable.
Also the technical aid was given in the Shenley Wood, and there were people able to solve daily problems, for example wristband not working/charging.

The deployment required to get the blueprints before installation.

In Genoa the apartment are completely different and spread around in the city.
And they deployments had to be designed for all house, also they had thick walls preventing communication.
Also it was difficult to fix technical issues, as there was the problem of having appointments with users, which could forget the appointments as they were old.


From the medical point of view: large number of volunteers over a large period of time. So to spot a protocol over a long period of time efficiency, there is the need of long analysis.
In project like this one must account for what can be done.
So agree to organize pilots in sequence instead of parallel.
Also there was the problem of avoiding the summer break, as people in Genoa could leave the homes.


Every user had to do something daily and weekly.
The only technical interaction allowed was to have a specialist from Valencia installing the devices.
But only the medical specialist were allowed to instruct how to use the devices to the users.

Also each day the user were instructed to do exercises.
Also add data about food intake in the diet app.


## Data
Every week the user had to play a cognitive game three times. Also receive cognitive coaching on demand.

While in Italy there were more users. **The data from the UK were the double**.
On average the UK user produced more data.

### Issues
Medial issues:
1) In the UK from the technical point of view was optimal. But what happened is that the **users in the control group were in the control groups**. So they self organized sessions of exercising, socialisation and changed their diet. *Those are impossible to prevent*.  This was taken into account and had a limited impact.
2) Social protocol in the Italian pilot: there was the idea to create periodic meeting in the Italian pilot to enforce socialization. In the UK is easy as there were common space in the place. In Italy the problem was to ask user to go far from their home, and the care givers had to pick them up. So in Italy the social protocol was given up, so it had a medium impact.
3) The application of the diet intake did not have information about UK diet, as the app was made by an Italian company. Most of the food consumed in the UK was not present. So there was work to add pictures and details. Its impact is limited since it was fixed, adding new DB entries for food.
4) from the medical point of view also a user withdrew

Technical problems

1) It was seen that in the UK the balance board was "not working", basically it did not produce any data.  The idea was that the chain of data there was something broken. The problem was: *the method to activate the balance board there was a protocol*. The problem at the end was that the doctor instructing the patients failed to understand how to instruct the patients. So this was a  **communication problem, as different specialist may have a different "language"** (in the slides it is said diet)
2) Users with pet, and fortunately only 2 in the UK had them. Those are a problem with passive infrared, so the application for the socialization event. It was limited, since those users did not met in the apartment people as they had common space, so in the end no much people went in the apartments
3) Some users refused to install some of the sensors. As they did not want for example hole in the walls or a sensor could disturb them, as they could have leds disturbing them. In the end they were not installed in the place designed, or some were not installed at all. That had an effect on socialization system and indoor detection. A user did not want a sensor out of the door, as he did not want to be known as being involved in a medical pilot, 
4) **Lack of motivation of the user, especially in italy**. In the UK the people could be motivated daily and people supported each other. In italy they were difficult to keep in touch. They stopped using the system, which meant to lost data in italy.
5) Imposed user privacy: there was the need of completely anonymous data, so no infomation about the users in the database was to in the DB, (outside of the DB and on paper there were reference), there was a pseudo anonimzation. There were games that **needed to be social, to share the results in rankings. The users complained that they want to know the other users and they were not able to**

Data reliability and other problems
1) Blackout in Genoa: one day only battery device were able to send data, as there was a city wide blackout
2) lack of connectivity: it was guaranteed that residence in UK had wifi coverage, but it was not sufficient, so 4G gateways were installed to fix that.
3) Monitoring devices and unavibality of the system: the user themself may have been a problem, as users would hide passive infrared of a user.
4) User hacking the tablet: a tablet was configured only to run the games. In order to connect user to games, there was a specific profile user on Android. The problem than was that a user changed the profile.

Reason of data loss:
![[Pasted image 20230321121914.png]]

Violet: lack of motivation, which was the first cause of data loss.

### Final remarks

1) The management were totally different in the areas. The environment affect the solution at many different level
2) Very limited budget, required a tradeoff between reliability and device less reliable but having a detect and fix approach. Part of the diagnosis required ad hoc intervention so there were investment there
3) **Unexpected issues, since devices are in the wild, exposed to everything, the user itself is wild enough**

On site pilots are complex if *users/human are involved, as user add additional entropy in a system, difficult to consider.*

A problem was also having indirect communication with the users, so missing feedback as the mediator did not have the tech skills.

*Interacting with medical specialists is difficult as they have different languages and expectations*.
Medical specialist do not trust the computer scientists

*Misunderstand lead easily a system to underperform.*
**Main lesson:** be ready to the unexpected.