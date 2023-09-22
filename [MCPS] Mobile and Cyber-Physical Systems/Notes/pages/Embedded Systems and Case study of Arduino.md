
An embedded device is a computer designed specifically for one function, that is why it is designed specifically for IoT. An embedded device is different than general purpose device, as they have a specific purpose, with one specific function, e.g. sampling for environment, means to specify a particular Duty Cycle.

The design of hardware and software here is in conjunction. Your choices on HW impact on SW, on SW impact on HW. The decision on transducer may impact SW and vice-versa.

For example a light software with very good transducer can be done, or vice-versa a cheap transducer but with software layer you can make it just as good. **So we talk about hardware and software co-design**.


Microcontrollers are microprocessors with the management of input-output.
Arduino are configured with:
* ports connected with a microprocessor
Ports can be for in and out.

Sometimes manufacturer take a microprocessor and update it to make a microcontroller, so optimize and design it to interface with the physical world. Usually microcontrollers implement functionalities over real-time systems. Usually embedded systems are real-time systems.

Some embedded device may be implemented with ASIC, or other may be with System on a Chip (very generic term actually).
So they are two different categories. 


## Programming an embedded device

Doing so, has different constraints and requirements from a general purpose computer system.
One nowadays may rely on powerful microprocessors and systems.
In microprocessor one must keep under control all the resources. Some things to face are: how to deal program memory, to fit the memory on embedded device.

What happens is that the ***programs are written on a fixed memory, rather than ram memory***. When turning on an embedded device, it loads the program and starts what it is supposed to do. The program memory is up to 15KB in an Arduino.
The footprint of code + libraries should fit that amount in general purpose computer on does not care.
**When programming to ARDUINO, the compiler tells you what is the code size, because there it becomes  a problem**.

On Arduino the user interface become led or maybe LCD tiny display, so there are difficulties in debugging.

There usually are not file systems on flash memory (disk equivalent) or RAM. *The file system if it fits may be on a program memory, so also for OS*.
If one takes space of OS, the program memory is reduced.
Usually OS there are **libraries, with a set of functions**.

There may be some version of OS, with real time features, or have embedded versions of powerful OS, for powerful embedded devices.

**Without an OS, then one must compile on a workstation( a PC) and upload the code, libraries and the initial configuration of the device, such as MAC addr or NWK addr**.

*Feedback on execution*: it cannot be controlled, besides on *led* or tiny display, or radio message, or serial line messages.

**Response time, in embedded device, must be controlled**.
Not only the functionality but the timing must be implemented correctly, and it is difficult to test it. For example Failing to give information in time, may fail the **non functional requirement of time***.

Another challenge is also on reliability, which means that a programs should not fail for years. Improper management of memory cannot be afforded in embedded devices.

**Power management is also critical in this case.**
Arduino: an IDE which provides the run time support, that is basically the OS of Arduino platform.
TinyOS: first one OS for wireless sensor network (used only for research).


## Executable

The language code produced, will be linked by the platform libraries, along with constants needed and parameters defined in term of constraints of the device code. 

To provide ZigBee, one buys from manufacturer device, which also gives: 
* libraries
* environment
One writes *application objects code*, then it is linked with those provided, and configures the device (to say if it is coordinator or RFD).
Then all this is used to produce an executable, to upload on a device.
*Parameters will change for all device programmed (e.g. MAC address). The part of compiling can be done once, the assignment of parameters is done at uploading time, allowing to differentiate the parameters.*

Usually those low level device are programmed in C, as C code is very efficient and allows to program easily registers.

To program code in C, we usually code the main function, the first one executed when running the code usually, **here no, the programming environment provides the main function, we may think as if the OS provides the main**. The purpouse of the main is to initialise the embedded device, which writes a function defining the business logic of the device at runtime.

The main basically us not seen to us, but is there and it represent the piece of software booting the the embedded device. 
This is because those device have all the same initialization, so it is useless to make the programmer program there. In this case for those low end device, the run time support basically corresponds for the O.S.


Led or display are a form of actuators, you may also store on flash storage data, and may receive data. There there is a wait time to *sample again the next time the sensors*.
To make sense of the sensors data, we must sample at regular intervals.




## Interaction with HW on PC

While in PC, the OS abstracts the interaction with the HW, so sends at low level commands to the HW and receive communication when the instructions are executed. 

Commands in this case are a set to instruct the HW, they are aggregated for the more complicated one. 

There are interrupts send by the HW when operations are completed. 
There is the need to wait, before the HW op is completed. 
With threads, the function may request the OS to suspend a thread, keeping in a data structure (e.g. stack or processor and thread descriptor) the the thread state, so that the microprocessor may do what it wants.
The interrupt is detected by OS, allowing to resume the state of a thread to execute again. From the point of view of the thread, it never stopped and is transparent.

*All of this has a cost*:
* memory requirements to freeze the state and space on the stack to keep the thread state
## Interaction with HW on Device

Considering that you have 1KB of memory, where you need the memory for the stack.
In Arduino, you have only one thread.
When there is a wait, the thread is stopped and freeze, until the hardware finishes its job.

*Arduino has also an advanced mechanism, to use interrupts manually.*

The first solution is the:
* Arduino event loop
The second:
* event-based programming

**Delay**: if you need to wait, you have an active delay, without stopping the processor, to wait for something.

The flow:
* init: main of the runtime support + programmer configurations
* Main loop: control loop directly after init. It allows to send command on the HW, with invocation on the library of the runtime support. Send the command at low level to the hardware and freeze
* Main loop: wait until command has been completed, and then the return will **activate again the main loop**.  The delay is a command sent to the HW
* active wait for the processor
* Main loop: wake up from the delay

In Arduino, communication was not thought about at the initial design.
We have that communication is really asynchronous, so there was not effort as it was not thought to put support on it.
As time passed, the environment evolved to provide support for communication.

# TinyOS
It raises an event, which is an interrupt, managed asynchronously by an interrupt handler. 
We program handler and link them to the program to intercept, and the OS will automatically run the handler when an interrupt is intercepted.

**Consider that the system is not responding to other interrupts, and as such we turn them off when executing the code of an interrupt, or on other O.S. there must be taken care carefully, the first way is the easiest**. When managing the interrupts, the data structures are on the O.S. The values are temporally consistent when managing the interrupt, when another interrupt arrives, there will basically be a race condition within an operative system, by disabling interrupts and managing the concurrency in them.
That solution is also a good idea with scarce resource, but it means to execute all other interrupts are in a queue.
*So the program handler should be tiny and not do much*. Really long operations means to lose the ability of having asynchronous communications.


We may define tasks that are non-preemtable: if posting two tasks, they will execute in sequence one after the other.
When an interrupt is received during the execution of tasks, they have a *higher priority than tasks*.
**The tasks will be preempted when an interrupt arrives, but in general a task does not share state with another task, but the minimum overhead we have is this interrupt management**


# TinyOS flow
 
* init: set a timer, and wait until woken up by *interrupt*
* sleep until interrupt of the timer
* Timer handler: it sends a commands to start a transducer. Note that you must wait to the transducer completion, as it will not do it instantly. Right after sending the command Start read, you may not expect to have immediately the result, the device is frozen.
* Read handler: when the HW completes an operation, it sends an interrunpt, which is the event Read done. This other handler is linked to another event handler than the read handler. You have the value read for the sensor, but you cannot process it to the read handler as it should be fast. **What we must do is to post a task, which is postponed to a task that will be executed later and not in the event handler at OS level**. After that the Read handler must *set a new timer* to wake *up when the next read operation* must be performed. After this the read handler returns to the O.S
* Task execution: when there is nothing else to do, the O.S will execute the task. If after computing, there is the need to send. The task will send a command Send data, to send it. Send cannot be executed immediately, so the O.S. returns control to the task, accepting the task asynchronously, without completing it. Once you send something, you cannot expect that it has been already sent. Return to O.S without anything to do.

![[Pasted image 20230827103534.png]]

At this point you have:
* read by sensors
* send by radio interface*
Those will be executed with handlers as before.
We see that for example an upcall after the Start read command is done. And there may be the arrival in the middle of Send done upcall from HW to a Send Handler, then the Read done in the meantime to the Read handler.

What misses there is not having high level handlers but they are part of the interrupt handler.
When the HW raises up an interrupt, the O.S. will start executing an interrupt handler.
Then an invocation, is done at application layer to the event handler, which will return then to the Interrupt Handler the control when done.

One must be careful on the Interrupt Handler commands, as for example in the event handler one invokes a command: **the command operates at the OS level, if it uses the same data structure of the Interrupt handler, it will mess up the data structure.**
So the application runs at OS privilege, using OS commands, even if we code it.
For example, if the interrupt comes from the radio, it is not sensible to send set up in the command another radio instruction, or it may be messed up.

That is why, the task are posted, so that a task, will *safely send a command that will be executed by OS, as the Interrupt handler has finished.*

# Arduino interrupts
We can implement with libraries the interrupt.
We have a control loop to implement tasks.

## Arduino

Open Source Hardware example, as of today it is even using on business. 
Arduino concept will comprise three elements:
* Device
* IDE
* Forum: with examples, projects and documentation

Arduino cannot come with more than 32KB program, as it has 32KB flash memory.

With power 5 voltage of circuitry, and we have an analog to digital converter.
1 bit = 5V/224 .

The digital pin are 5V or 0 mapping the signal.
The pin may be used to connect an actuator. By giving current to a led we start it.
*Basically the digital pin can be used in input and output*, the analog cannot be used for output.
We may have complex controls in output over digital pins actually, this is implemented by the runtime support.
Two pins may be used to produce external interrupts.
Connect and use it .

Decide the port from which you are compiling and then connect the port to program and compile the program and load it in the flash memory.

That analog signal is transformed from 0 to 1023, operating at 10 bits.
While digital signal is 0 or 1.

The code that we have to write is:
* setup: called by the main, when initialising the device at boot
* loop: after the init is complete*

Not one must connect the code, but for example having a system with buttons.
We must match the button id and the pins with the led.
The serial line has several different speeds, and if they do not match, you will not read anything.
The pin number will be used in input or output with a function that specifies it at setup.

In the loop. You want to read the state of the button, connected to a digital pin, so a **digitalRead function is the one that we have to implement**.



With the function digital write, which means to put current onto a pin, we provide an **HIGH value, so provide the current**.
With LOW current, we turn off the led.


With `analogRead` we read a signal of an analog input, and we transform it into a 10 bit number that can be stored into an int. 
We can determine the pin voltage.
If the electronics are powered with 5V. Any step of increase is 5V/1023 because we suppose that **level 0 is 0**.

With `Serial.println()` we may print on IDE, note that we ma use it also to send on wireless device if it is connected.

# Interrupts 
Arduino offers an interface to interrupts, allowing to manage external interrupts to the runtime support. Two type of interrupts may be managed by runtime support.

* External: interrupt managed by Arduino, which are interrupt connected to pins, those pins are implementing an external interrupt lines

Timer: it is an abstraction of a timer, where we ask the Runtime for us to manage the time for use

The external device will actually be external basically, we can sleep for real rather than have the kind of delay wait which is active.

With `attacInterrupt` we can declare an interrupt.

We can give a mode to the Interrupt, defining:
* the signal to take a decision on what to do, so depending on how its raising signals to invoke the function

Suppose to attach an interrupt handler to INT0: if it raise **then active an interrupt, if it falls do not activate it**
Or we may say HIGH or LOW, in this case you must be careful as if the signal remains stable, then it will send interrupt at really fast.

Normal buttons have a state, while some push button emit a signal and turnoff again,a  mode low or high makes sense only for signals.

The interrupt is very fast in very low level instructions.

To control a led according to the interrupt of low level circuitry


# Breadboard

Those board may allow to prototype circuitry. Those boards can have on time cables. There are + and -.

Connecting the - signal of Arduino to the -, then all the - dots are connected in a row all together. 
Same form +.

The rest of the breadboard, the holes are connected in columns and disconnected by all others.
This allows to connect components, to make them connect automatically. The connections that cannot be done in this way, can be connected with wires.

If the current goes from + to - and gives current to a line. When pressing a button, which is connected to a line, from this line it goes back with the resister to the negative pool and returns to the negative pole of Arduino.
The resistor is needed to not burn arduino.

The signal of the press, may go also to pin 2. So that when pressing the button, the microcontroller finds the pit 2 power.

So the power pin, gives the power to the button, than can send it in a column up to the digital pin input 2..

On pin output 7,  connected to resistor with led and . connected to negative line,
By writing on 7 we can implement a digital write with a **high value to turn on the led**.
The pressing of the button is an interrupt on pin 2.


What the loop does is, just to turn off again the LED.


The interrupt only, happening asynchronously while executing the loop, will run the rising of the counter of the loop and turning it on.

Printing is not a good idea but it does it.


**Race condition**: there is a potential race condition on the variable count, it may be a chance that while reading count,  on the loop, we may write with the interrupt on count.

**in a certain sense we can prevent the interrupts when receiving them**.
In C we have registers and we overwrite the memory. The compiler may be optimized and is more efficient in read only once from memory and then read only from register. You may even have the idea of locating in the register directly and not in memory.
If the variable is in a register, when the interrupt arrive, all the registers are stored on the stack to manage the interrupt.
At this point the interrupt handler:
* read the variable count on memory
But after the interrupt handler finishes, the main loop should be restored, so the microcontrollers will take from the stack the registers, with the old value of the variable count. 

**By declaring volatile, we force the compiler to keep the variable count in memory at any time, so not on cache, consequently an interrupt does not create a problem.**
The variables in the control loop and the interrupts are generally made volatile (so greenLed too).

The interrupt handler should be void and be without parameters, for a precise reason.
It is not for security and race conditions.
It takes no parameters as:
* you do not know when this procedure will be called
* also there are no parameters associated to an interrupt, as it is made by a pin
So there is no parameter, as there is no input parameter, and there is no input parameter for the invocation.
Since no invocation, the output of the function cannot be received.
The handlers are executed with disabled interrupts, to have protection against race conditions, so they have no interrupts, as such keep it short.
During the interrupt handler the clock is stopped and the time is freeze.
*You cannot put a delay in the handler, as you are waken up with a delay by an interrupt, so in theory it should not work as you do not receive the wake up interrupt*.


`millis()` is not incremented during interrupt.
Count is declared as volatile as told before.

We may also stop receiving interrupts with:
* detachInterrupt
* interrupts():enables all interrupts
* noInterrupts(): disables all interrupts, for example when dealing with main loop parameters on the main loop. By default true when entering an handler.

## Energy Management in Arduino

In Arduino, even when delaying and waiting the microcontroller is frozen but it is is powered state.
The microcontroller is Arduino supports actually different states. Consider that Arduino is a platform, different implementation with different microcontrollers may have different states.
Refer to microcontroller documentation to get the states.


There is a low power library, which provides the calls to implement low powered states for the micro controllers.
Different microcontroller may be responding different to the library.

INTO -> mapped to PIN 2
INT1 -> mapped to PIN3 
in the board of Arduino.
That is why  the 0 in the registration of interrupt from pin 2 is 0 in the code.


## SLEEP MODES IN ATMEGA328P ARDUINO

In Idle mode: you stop the CPU, the SPI part of the microcontroller stays on for interrupts) It turns off the clock of the microcontroller CPU and the flash. The external components interrupts and internal interrupt are still activated.

ADC Noise Reduction Mode: it allows to stop the CPU but the ADC is on, allowing to have less noise to convert analog to digital

Power-down Mode: stop the clock and allows only operation from asynchronous modules. It can wake up with hard reset and other serial interface and special type of interrupt. **You can wake up with the timer***

Power-Save: turns off the timer too.

# Using idle mode: low power
* use the library with: `#include "LowPower.h"`
Check carefully the microcontroller, as it may not implement the call of the library, such as:
`LowPower.idle(SLEEP_8S, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_OFF, TWI_OFF);`

The first parameter is important as it: *states how much to sleep.*
After the time, it generates an interrupt and the microcontroller is turned on automatically.

For the parts of the microcontroller, you may decide the components to put on or off.
ADC_OFF / ADC_ONTIMER0_OFF/ TIMER0_ON

### Power Down:

Brown out detector: monitor to detect that you are burning something.

``#include "LowPower.h" //Note: no setup is required`

You have a small number of parameters as it powers down other components.


`LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);``

With `powerDOWN(SLEEP_FOREVER....)` you will not be waken up by the clock.
There may be an handler that *catches an interrupt and wakes up the device*.