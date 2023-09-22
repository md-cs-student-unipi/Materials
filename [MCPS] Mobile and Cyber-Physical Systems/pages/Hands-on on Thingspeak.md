Thingspeak is a platform which allows to setup IoT communication channels.
It is a free web service to which daily up to 8200 may be sent, the maximum frequency of upload is 15 seconds, so you cant upload at faster frequency.
It has a REST/HTTP interface for data upload and has a MQTT broker.
It has tools for data processing and visualization.
# Thingspeak channel

A channel is for Thingspeak its basic abstraction, it represented values up to:
* 8 time-varying parameters
**A channel as an identifier and is protect by**:
* API keys that must be added to the URL or in an header field
There are two distinct keys:
* Write API key: to upload data
* Read API key: to access data, as a channel may be private or public.
More than one device could contribute to putting values on a the channel.
We get from the Website the keys.
## Field

**A channel may have multiple field**s.
A field represents a variable, with a fixed identifier.
Uploading one or more values in a channel is called **feed**. With just one feed several fields may be updated.

## How to implement a feed
* HTTP:
	* GET: containing the request URL and the pairs field=value
	* post: with pairs field=value in the body of the request
* MQTT: a **publish()** of the pair field=value
# Representation

In the channel dashboard there is a diagram for each field:
* horizontal axis: time
* vertical axis: measured parameter

# How to use
1) you may test with the browser and HTTP requests
2) use Python and HTTP
3) MQTT: by creating a MQTT device in thingspeak, in this way there is access for MQTT in the channel.
# What we did
We used Thingspeak with Arduino and MQTT publish the data of a sensor attached to the Arduino which measured the electric charge.


