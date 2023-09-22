Sensors measure continuous physical quantities in the real world and sample them into discrete digital signals for processing and transmission. These signals are mathematical functions that map from a domain (often time) to a codomain (the signal values). The domains and codomains can be either continuous (real numbers, R) or discrete (integers, Z) depending on the signal.

Deterministic signals follow definite rules and are different from random signals. Deterministic signals can be analyzed using deterministic methods, while random signals require probabilistic methods.

When sensors sample a continuous physical quantity, they convert the infinitely variable real-world quantity into a finite set of numbers that represent the quantity at discrete points in time or space. This results in a discrete signal that can be processed digitally. For example, a temperature sensor may sample the continuous temperature fluctuations in a room into a set of numbers representing the temperature every minute. This discrete set of temperature values over time forms a discrete signal.

The discrete signals from sensors must then be transmitted, often as electromagnetic waves. The transmission medium converts the discrete signal into electromagnetic waves that propagate to a receiver. The receiver then converts the waves back into the original discrete signal for further processing.


### Deterministic Signal definition
Function f(t) with a real value such as time, where
$f(t):D$ -> ℭ
Where D and ℭ may be:
* $\mathbb{R}$ real numbers
* $\mathbb{Z}$ a discrete set, such as integers
* $\mathbb{C}$ a set of complex number, allowing to represent two independent signals together if used as codomain
 
# Classification
We take signal as a real function of time. We may have for domain and codomain:
* time continuous(D=$\mathbb{R}$) and amplitude continuous signals (ℭ=$\mathbb{R}$)![[Pasted image 20230610125345.png]]
* Time continuous(D=$\mathbb{R}$) and quantized signals(ℭ = $\mathbb{Z}$)![[Pasted image 20230610125402.png]]
* Time-discrete(D= $\mathbb{Z}$) and amplitude continuous signals (ℭ=$\mathbb{R}$)	![[Pasted image 20230610152341.png]]
* Time-discrete(D= $\mathbb{Z}$) and quantized signals (ℭ=$\mathbb{Z}$)
	![[Pasted image 20230610152945.png]]
Note that quantized signals may be also refereed as discrete amplitude signals

### Discrete-time signals in depth (D = $\mathbb{Z}$)
We can have a signal that is discrete in time but continuous in amplitude. This type of signal is often found in digital audio, where the amplitude of the audio signal is sampled at discrete points in time but the amplitude values themselves are continuous.

In contrast, an image is typically considered a discrete signal (digital signal), meaning that it is discrete both in time and amplitude. In digital image processing, an image is represented as a grid of pixels, each with a discrete amplitude value that represents the brightness or color of that pixel.

In formula, the domain is  D=$\mathbb{Z}$(T) which is a set of integers defined as:
$\mathbb{Z}$(T) = {nT, $\forall n\in\mathbb{Z}$ and $T\in \mathbb{R}$}.
In this way we have a multiplication between an integer and a real value.
We may have as an example
$\mathbb{Z}(2)$={${..,-4,-2,0,2,4}$}, so we multiply by $2\in \mathbb{R}$ any integer number. 


### Digital Signal (D= $\mathbb{Z}$, C= $\mathbb{Z}$)
A discrete signal is called digital when the codomain is a finite set of symbols. Its called also a "symbolic sequence". 

We may have an alphabet, a set of symbols allowed to represent some signals.
A = \{a,b,c,...,x,y,z\}
A symbolic signal is for example a sequence abababac.. as it transmits the set of symbols to

Furthermore we can reduce to another alphabet that one, having B={0,1} alphabet we can represent any symbol in A with a sequence in B.
We may have a custom encoding of letters.
We may use the rules of representation to represent the signal as a sequence of binary symbols. For example
a= 0000, b = 00001 and so on, making the code 

«ababfxje»  into a series of those symbols: 
0000000001000000000100101101110100100100

# Frequency
We want to find the duration of a transmission given a source that transmits f symbols/second (symbols per second) which is the symbol frequency. 
* We have that for an alphabet of 8 symbols, defined as A. The transmission will last 8/f seconds
* We have that for an alphabet of 40 symbols, defined as B. The transmission lasts 40/f seconds.

The symbol frequency is called binary frequency, if a binary alphabet is used. For binary frequencies we define the measure throughput, which is expressed in bits per second. To calculate the throughput, we need to know the binary frequency that produces $f_c$ samples/second. 

Assuming that a source samples an analog signal with $f_c$ samples/seconds.
That we need M bits per sample to represent a value, the formula for calculating the throughput is
* $f_c\cdot M$ bit/second

Furthermore we can define M as being $log_2$(alphabet_size) where alphabet_size is the number of symbols in the alphabet.
The formula will then become:
* $f_c \cdot log_2$(alphabet_size)


#### Exercise
![[Pasted image 20230610162729.png]]
1. Determine the number of bits needed to represent each symbol. Since there are 8 symbols in the alphabet, we need 3 bits to represent each symbol (2^3 = 8). M = $log_2$ bit/symbol (alphabet_size)

2. Since the symbol frequency is 10 symbols per second, we can calculate the throughput by multiplying the symbol frequency by the number of bits needed to represent each symbol:

Throughput = $f_c \cdot M$
Throughput = 10 symbols/second * 3 bits/symbol  
Throughput = 30 bits/second


## Periodic Continuous Signal
A continuous signal $s(t): R\rightarrow R$ is *periodic* with period $T$ if $s(t) = s(t+T)$ $\forall t\in R$ 

> For example $sin (nt)$ and $cos(nt)$, are periodic, with period $T =2\pi/n$  $\forall n\in Z$

We may have non-periodic signal **which we can make period, by studying them in the period \[0,T]\, since their behaviour remains the same in all its existence domain.

We may see how for periodic signal, it holds that
$s(t+T)=s(t+2T)=s(t+nT)$ $\forall t\in \mathbb{R},n\in{Z}$ here the domain is $\mathbb{R}$, $\mathbb{T}\in{R}$ and $t\in R$ 
*The frequency is $f=1/T$*

### Example of periodic continuous signal
$s(t) = cos 2t + 4 \cdot sin 2t - cos 5t+ 4 \cdot sin 6t$ has a period of $2\pi$ 
The frequency is $f = 1/T$.

![[Pasted image 20230610170646.png]]

### Aperiodic signal
We define in the domain \[a,b) a **periodic signal s with limited support**, limited support means that where outside of this domain, the signal is not supported. This limited support is defined as $s(t) = 0$ $\forall t\in[a,b)$

We can define the periodic extensions $s^\star$ of $s$ as
$$s^*(t)=\sum_{n=-\infty}^\infty s(t-nT)$$
where $T = b-a$
![[Pasted image 20230610171709.png]]

We are summing all the multitude of periods (the multiple repetitions or cycles of the periodic signal), covering the entire domain.  
By shifting the signal this way, the signal becomes periodic, with a period of $T = b-a$.

This infinite sum, allows to make the periodic function, where we replicate this same shape of curves. This periodic extension, which starts from a signal with limited support, sampled and trying to reconstruct it. We re-construct a complete signal by summing all of its individual cycles, where each cycle is a shifted version of the original signal s(t) over the interval $[a,b)$.

Basically we increase $t$, and we subtract a value $nT$, with $n$ growing, to make the periodic effect shaped.

# Transmission
Typically, our problem is to transmit any information produced by a source as this information has to be transmitted to the medium.
The signal must change depending on the channel.

There is a transducer, that converts a message to a signal, which can be transmitted to a medium.
A transducer converts an electrical signal into an electromagnetic wave.

The electromagnetic wave will then travel by destination during transmission. During the transmission, noise may be "added" to the signal, or the signal may have some distortion. Noise is typically an external and random signal that represents the movement of electrons.
The signal received at the destination will not be identical to the original signal due to the presence of added noise, which is inherent to the nature of the channel.
Furthermore, other effects may cause variations in the signal, such as distortion, resulting in a signal composed of different frequencies. When the signal propagates through the air or a medium, it may experience frequency-dependent attenuation, causing different frequencies to be attenuated in varying ways.

At the destination, the transducer will convert a signal into a message.
The transducer for electromagnetic signals is an *antenna*. A *channel* may be electromagnetic, sound, optical waves etc.
![[Pasted image 20230610183417.png]]


The attenuation of the signal will vary accordingly, as the attenuation characteristics differ for these frequencies.

The primary objective of the transmission process is to minimize noise and distortion, aiming to enhance the signal while mitigating the impact of noise.

To assess the quality of the communication channel, the Signal-to-Noise Ratio (SNR) is utilized, representing the ratio between the signal strength and the level of noise present.


#### Analog Transmission
In the figure below we have different block to represent the various phases of the analog transmission, we can see:
* source: who emit the signal
* adaptor: for noise and distortion, those devices will reduce the effects of those unwanted changes, with equalizers, amplifiers( mitigate the effect of noise). This phase transforms the signal to make the transmission more efficient. We enter the real analog channel
* transducer: hardware component emitting the signal
* transmission medium: the medium in which the signal travel
* transducer: in this case the receiver does the task of transforming electromagnetic waves (or other type of physical signal) into electrical signals
* adaptor: the same as the other adaptor, to reduce noise and distortion

![[Pasted image 20230610183834.png]]

#### Digital Transmission
Digital transmission: the source is emitting digital signal, discrete sequence of symbols, for instance a sequence of bit. Basically creating an exchange of discrete messages.

We have:
* source: who emit the signal
* modem: (modulator/demodulator) convert the signals from discrete to continuous, in this way the signal can be sent over an Analog channel
* adaptor: same as before
* analog channel (same as before)
* adaptor: same as before
* modem: demodulates to get the source, with some error probability, as there are many steps from transmission to receiver side, that makes it difficult to reconstruct the signal as the original one. One of the goal is to make the error probability as minimal as possible. Do channel decoding, adding information, such as redundancy bit, to make some checks, detecting errors during transmission and correcting them
![[Pasted image 20230610183844.png]]


## Sampling and quantization for Digital Transmission
The source produces a digital message, this digital message can be produced from an analog signal, for instance, the source may be a sampling messages.
To do this, it converts the continuous signal with an ADC, being an analog to digital converter. The analog signal will be represented as a sequence of symbols, if the symbols are {0,1} then into bits of 0 s and 1 s.

Those are sent on a Digital Channel. Furthermore, the DAC converts from digital to the analog signal.
![[Pasted image 20230610190159.png]]

At the receiver site, the signal is converted again into an analog signal, using a DAC, *digital to analog converter*.

### How to sample
When transmitting speech, a certain number of samples must be generated and transmitted. However, due to limitations in efficiency, we may not be able to transmit a large amount of data. Additionally, since the medium may be shared with other communications and conversations, errors are likely to occur during transmission, which can affect the signal reconstruction.

Having a high resolution and high sampling rate can reduce quantization errors as more samples are taken. However, it is important to note that even with these improvements, the reconstructed signal may not be as precise as the original signal that was produced.

In order to better understand the signal, particularly its frequency components, it is necessary to analyze it thoroughly.

Consider that sampling and quantization introduce a distortion in the signal, called **quantization noise**, which is added to the channel noise.
This quantization noise is dependant on:
* the frequency of sampling rate
* resolution of the digital symbols, meaning how many different symbols are used to **represent a single analog value**
Consider that:
* higher resolution and high sampling rate = small quantization error but = a larger number of symbols to transmit (higher bandwidth required)


# Fourier series and Frequency Domain Analysis
We use Fourier series and Frequency Domain Analysis to understand how a signal can be composed of base signals at given frequencies. They were been the cornerstone of signal and system analysis.

We have a combination of different frequencies. We may have a sinusoid oscillating at different frequencies. There could be, for example, a sum of two sine waves with different amplitudes.

Here, we see the general expression for a sinusoid at frequency $\omega$. We may also see it at frequency f in Hertz.
$$x(t)=a \cdot sin(\omega t+\phi) = a \cdot sin(2\pi ft+\phi)$$

![[Pasted image 20230611094316.png]]  
We then have another example of combining two sinusoids.  
![[Pasted image 20230611094337.png]]  
Given by the formula:  
$$x(t)=sin(2\pi t)+sin(4\pi t)$$

We may have a specific sound made up of signals at specific frequencies. As we can see here, there is an analogy with audio signals, showing the US telephony line.  
$$x(t)=sin(2\pi\cdot 350 \cdot t)+sin(2\pi\cdot 440 \cdot t)$$

![[Pasted image 20230611094648.png]]

In general, this type of assumption can be made for a series of signals that are constant in time. We may have signals at fundamental frequencies. With $f_0=1/T$, we have sinusoids that are multiples of these frequencies.
**We have a fundamental harmonic, and then we have the 2nd, 3rd, etc. harmonics**.
We may sum all these components, and we obtain a final signal that is continuous in time and amplitude.  
We can assign a weight to each harmonic, with different weights by summing a portion of the components.  
We get different signals in this way.

![[Pasted image 20230611094740.png]]

We generally define the k-th harmonic as:

- $s_k(t)$: k-th harmonic (frequency $f_k = k/T = k \cdot f_0$)  
    So, we may see how all harmonics are defined based on the fundamental harmonic, and their frequency is a multiple of $1/T$ (its period).

See how by changing the weights, we can get a different signal:  
![[Pasted image 20230611095115.png]]

What is more interesting is the opposite.  
**Can we have a continuous and periodic signal expressed as a sum of trigonometric functions, such as sine and cosine oscillating in multiples of a given frequency?**  
If we can:
	How do we compute the weights to combine the sinusoids to obtain said signal?
		The answer is that we can analyze and decompose the continuous and periodic signal and compute the waves at specific frequencies for the signal.


# Fourier series
Allows to decompose the signal as a infinite number of continuous function, oscillating at different frequencies.
We start from signals whose domain is the time, and we analyse it from time to frequency domain shift.
There is a change of domain from the previously discussed, now $D=$ frequency domain.

Those continuous functions, are the base of the decomposition.
Formally the base are the set of functions $\phi_n(t),n\in\mathbb{Z}$. So they are a numerable and infinite set of functions.
In the Fourier series, those functions are trigonometric functions, which are orthogonal. 

## Fourier series formally
Given a continuous signal $s(t):R \rightarrow R$ periodic in the interval \[-$\pi$,$\pi$\] **(so $T=2\pi$ period)**. 

$$s(t)=1/2*a_0+\sum_{n=1}^\infty(a_n*cos(nt)+b_n*sin(nt))$$

The Fourier series is defined as a function over time.
Its composition is:
* $a_0\cdot 1/2$ is the constant components, where $a_0$ is defined as: $$a_0=\frac{1}{\pi}\int^{\pi}_{-\pi}s(t)dt$$
The integral of the continuous signal, over the interval $-\pi$ to $\pi$ 

Hence we do an infinite sum of trigonometric functions.
Note that sine and cosine oscillate at different frequencies.
We start from $cos(t)$ and $sin(t)$.
* $a_n \cdot cos(nt)$: where $a_n$ is an amplitude of the n-th harmonic, while $cos(nt)$ is the n-th harmonic with fundamental harmonic cos(t) We define $a_n$ as: $$a_n=\frac{1}{\pi}\int^{\pi}_{-\pi}s(t)\cdot cos(nt)dt$$
* $b_n\cdot sin(nt)$ where $b_n$ is amplitude of the n-th harmonic, while $sin(nt)$ is the n-th harmonic with fundamental harmonic sin(t). We define $b_n$ as $$b_n=\frac{1}{\pi}\int^{\pi}_{-\pi}s(t)\cdot sin(nt)dt$$
The decomposition is general, with a constant component, an infinite sum and we compute the value of those weight.


There are math demonstration, to define the condition under which a signal may be developed in a Fourier series.
*We make a conservative assumption, which were established by Dirichlet*.
IF:
	 $s(t)$ is periodic
	 $s(t)$ is piecewise continuous, then it implies that the Fourier series of $s(t)$ *exists* and converges in $R$.

#### Remembering Sine and Cosine
* Sine is an even function, meaning that $sin(-x)=-sin(x)$
* Cos is an odd function, meaning that $cos(-x)=cos(x)$


## Example

Given a signal we need to develop the signal into a Fourier series.
$$s(t)=\begin{cases} 
2 \hspace{0.4cm} if \hspace{0.2cm} -\pi<t<0 \\ 
1 \hspace{0.4cm} if \hspace{0.8cm} 0\leq t \leq \pi \\ 
\end{cases}$$
periodic signal function with period $2\pi$
![[Pasted image 20230611122521.png]]

We apply the formulas to get  $a_0$, $a_n$, $b_n$

We have a base s(t). We may have a non continuous function with two co-domains depending on the definition of the function.
We may check what happens, if we sum just a finite number of the components.
For example summing only the first 20 harmonics, we reconstruct our signal, it is not the same as our original signal. This approximation will improve, by summing more harmonics.

**Split the intervals, make the integrals based on s(t) which is defined as its values in different intervals.**
Make the integral, by plugging the intervals value of s(t) and splitting in the two domains of the functions with different values.

Make sure to divide the integral in the various interval where it has some value.
**Note that n is a constant inside cos and sin, we cannot leave it as that to solve it, we must make the integrals by substitution!**

$a_0=1/n \int_{-\pi}^\pi s(t) dt= 1/\pi(\int_{-\pi}^{0}2dt +\int_{0}^{\pi}1dt = [2t]_{-\pi}^0 + [t]_{0}^{\pi}$

= $(2\pi+\pi)/\pi = 3$


$a_n=1/\pi \int_{-\pi}^\pi s(t) cos(nt) dt$

$= 1/\pi(\int_{-\pi}^{0}2cos\cdot t(nt)dt +\int_{0}^{\pi}cos(nt)dt)$

we will use the substitution $u = nt$, so $du/dt = n$ and $dt = du/n$.
We redefine the integral in the form of having the derivative of the element substituted in the integral:

$1/\pi(1/n\int_{-\pi}^{0}2cos(nt)*n*dt +1/n\int_{0}^{\pi}cos(nt)*n*dt$

$=1/\pi(1/n\int_{-\pi}^{0}2cos(u)du +1/n\int_{0}^{\pi}cos(u)du$

$=1/\pi[1/n * 2 * sin(u)]_{u(-\pi)}^{u(0)} +[1/n * sin(u)]_{u(0)}^{u(\pi)}) = 0$ 

where $\forall n, sin(n\pi)=0$. So the final result, substituting $u(\pi)= n\pi$ will result in a $=0$.


$a_n=1/n \int_{-\pi}^\pi s(t) sin(nt) dt= 1/\pi(\int_{-\pi}^{0}sin(nt)dt +\int_{0}^{\pi}sin(nt)dt$

We will use the substitution $u = nt$, so $du/dt = n$ and $dt = du/n$.
We redefine the integral in the form of having the derivative of the element substituted in the integral:
$1/\pi(1/n\int_{-\pi}^{0}2(sin(nt)*n)dt +1/n\int_{0}^{\pi}(sin(nt)*n)dt$

$=1/\pi(1/n\int_{-\pi}^{0}2(sin(u))du +1/n\int_{0}^{\pi}(sin(u))du$

$=1/\pi[1/n * 2 * -cos(u)]_{u(-\pi)}^{u(0)} +[1/n  -cos(u)]_{u(0)}^{u(\pi)})$ = 0

the formula will become, extended, bearing in mind that $cos(-x)=cos(x)$

$1/(n*\pi)*(-2+2cos(n\pi)-cos(n\pi)+1)$
$=1/(n*\pi)*(-1+cos(n\pi))$ 

We make the cases:
* $n$ is odd, then we have $cos(\pi)$, $cos(3\pi)$ and so on, always equal to $-1$, meaning that $b_n=0$ when n is odd.
* $n$ is even, we have $cos(2\pi)$,.. and so on, where its always equal to $+1$, meaning that $b_n=-2/(\pi*n)$ when n is even
The absolute value decreases to $0$.

The coefficient can be seen here:
![[Pasted image 20230611123807.png]]


We may make an example by letting $n = 2k - 1$, and plugging the coefficients in the Fourier Series. For all k>0, in such way we get just n odd numbers!
$$s(t)=\frac{3}{2}-\sum^{\infty}_{k=1}(\frac{2}{(2k-1)\pi}\cdot sin((2k-1)\cdot t)))$$

We can plot a finite sum of harmonics. Plotting an increased number of harmonics, we approximate better the functions.
The discontinuity are hard to handle. It is close to those, you have the oscillation behaviour. With more harmonics, you reconstruct better the signal at those points. As it may be seen here in this comparison:
![[Pasted image 20230611124013.png]]


# Exercise 2

![[Pasted image 20230611124200.png]]
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{0.2cm} -\pi<t<-1 \\ 
	0 \hspace{0.4cm} if \hspace{0.2cm} -1\leq t < \pi \\
	1 \hspace{0.4cm} if \hspace{0.8cm} 1 \leq t \leq \pi
\end{cases}
$$

Instead than substitution, we may also use the well known integrals, to solve directly: 
$$\int sin(t)dt=-cos(t)$$
$$\int cos(t)dt=sin(t)$$
$$\int sin(nt)dt=-\frac{cos(nt)}{n}$$
$$\int cos(nt)dt=\frac{sin(nt)}{n}$$


In this case we will split in 3 parts the integrals but its the same procedure. We may then plot the first n harmonics and see the difference:
![[Pasted image 20230611125041.png]]


# Fourier series with arbitrary period
**We can generalise, to not just the harmonic with period of 2$\pi$**. by applying the theorem which in a more generic form.
Periodic in a period $T$. We can have a signal, continues and periodic in time in the interval $-T/2$, $T/2$.

Formally:
Given a continuous signal s(t): $\mathbb{R} \rightarrow \mathbb{R}$, periodic in the interval $[-\pi,\pi]$, using the substitution $y = 2\pi t/T$ to get

$$f(y) = s(\frac{T}{2\pi}\cdot y)$$ that is periodic in the interval $[-\pi,\pi]$ 

We can define the Fourier Series
$$f(y) = s(\frac{T}{2\pi}\cdot y) = \frac{1}{2}\cdot a_0+ \sum_{n=1}^\infty(a_n \cdot cos(ny)+b_n \cdot sin(ny))$$

Then we may return to the initial variable and obtain the formula:
$$s(t)=\frac{1}{2}\cdot a_0+\sum_{n=1}^\infty(a_n\cdot cos(2\pi nt/T)+b_n \cdot sin(2\pi nt/T))$$

We consider that in $a_n$ and $b_n$ we have $2/T$ instead of $\pi$ in the integral intervals. Therefore, instead of $nt$ inside the cosine and sine harmonics, we have $(2\pi \cdot n \cdot t)/T$

![[Pasted image 20230611144337.png]]


# Energy of a continuous signal

Given a signal s(t) defined in the interval $[-T/2,T/2]$ , its **energy** defined as:
$$E_s(T) ≜ \int_{-T/2}^{T/2}|s(t)|^2dt$$
Which has the meaning in physics that if s(t) represents the voltage, applied to a $1\ohm$ resistor, then $E_s(T)$ is the energy dissipated in the period T.

## Energy Signal
A signal with finite energy is defined as **energy signal**.
We have an energy signal if we have the following limit greater than 0.
$$E_s=lim_{T \rightarrow\infty}E_s(T) = \int_{-\infty}^{+\infty}|s(t)|^2dt > 0 \land E_s<+\infty$$

(I would say that in an infinite period the energy dissipated is more than 0 and less than infinity, meaning finite number for the signal $s(t)$ and then the signal is an energy signal).

That definition includes:
* finite duration signals
* infinite duration signals
	* if the signal has infinite duration, then $E_s \rightarrow 0$ as fast as $1/t$ or even faster

**In the physical world, all signals have finite energy, as no signal will last forever**.

# Power of a signal

We define the **average power of the signal** given $s(t)$ defined in the interval $[-T/2,T/2]$
$$P_f(T)≜ \frac{1}{T} \int_{-T/2}^{T/2}|s(t)|^2dt=\frac{E_s(T)}{T}$$
So we average the energy of the signal over the whole period.

## Power Signal
A signal, with finite power, also defined as *power signal*, is a power signal if the following limit is greater than 0

$$P_s=lim_{T\rightarrow \infty}\frac{1}{T}\cdot E_s(T) = \frac{1}{T} \cdot \int_{-\infty}^{+\infty}|s(t)|^2dt > 0 \land P_s<+\infty$$
(Basically, if the average of the energy of the signal, with the limit of the period to infinity is greater than 0 and less than infinity meaning that its finite then its a power signal)

### Periodic signal
Periodic signal are a class of signals important because, **given that** they have *finite power* so they are power signal, they also have:
* infinite energy
* *their average power is equal to the average power computed in a period (the same from a period to the whole duration)*



# Energy and Power

**If a signal has finite energy, then it has an average power of $0$**.
So we have the classification of:
* finite energy signal (energy signal), with their power being $0$
* finite average power signal (power signal) $>0$, with their energy being infinite
**Those are two disjointed sets**
![[Pasted image 20230611155155.png]]
Power signals contain periodic signals. While energy signal contain Pulse signals, where they contain limited duration signals.


# Example
Having an exponential signal:
$$
s(t)=\begin{cases} 
	0 \hspace{0.9cm} \forall \hspace{0.1cm} t < 0 \\
	ae^{bt} \hspace{0.4cm} \forall \hspace{0.1cm} t\geq 0
\end{cases}
$$
It has finite energy, so its an energy signal, as we may see up to infinity

$$E_s = \int_0^\infty|s(t)|^2dt= \int_0^\infty|ae|^{-bt2}dt$$
we can remove the absolute value, as we have defined the signal as 0 in the case $t<0$.

$\begin{align*} & \int_0^\infty (a \cdot e^{-b \cdot t})^2 dt \\ & = \int_0^\infty a^2 \cdot e^{-2b \cdot t} dt \\ & = a^2 \int_0^\infty e^{-2b \cdot t} dt \\ & = a^2 \left[ -\frac{1}{2b} \cdot e^{-2b \cdot t} \right]_0^\infty \\ & = a^2 \left[ -\frac{1}{2b} \cdot (e^{-2b \cdot \infty} - e^{-2b \cdot 0}) \right] \\ & = a^2 \left[ -\frac{1}{2b} \cdot (0 - e^{-2b \cdot 0}) \right] \\ & = a^2 \left[ -\frac{1}{2b} \cdot (-1) \right] \\ & = \frac{a^2}{2b} \end{align*}`$

where at step 3 we computed the integral of e, in the format:
$$\int e^{cx}dx=\frac{1}{c}e^{cx}$$
Furthermore, we proceeded with the substitution, knowing that $e^{-\infty}=0$ and that $e^0=1$, obtaining $+1/2b$ which is then multiplied with $a^2$

We may see that it has null power since, taking the average over a period T going to infinity, the power is 0.

$$P_s=\lim_{T\rightarrow\infty}\frac{1}{T}\int^{T/2}_{0}|s(t)|^2dt=lim_{T\rightarrow \infty}\frac{a^2}{2bT}=0$$

### Power signal example
A periodic signal, such as cos or sin, are power signal.
Given $s(t)=cos(t)$ $\forall t$ considering its period $2\pi$ from 0 to $2/\pi$ 
We may see that for sure since the function is bounded between $0$ to $2\pi$, in the values 0 and 1, the average power will be limited in those and so finite.
**You may notice that the integral of the energy is undefined, but consider that we know that the set of power signal and energy signal are disjointed, we can say that the energy is infinite!**

![[Pasted image 20230611170731.png]]

To do the integral, the half angle identity was used as
$\int cos^2(x)dx=\int 1/2(1+cos(2x))dx$.

Then this was split into two intervals, note that in the right interval, there is a bit of an error in the slide. What happens is that we need to make the substitution $u=2t$. So we multiply the integral outside by $1/2$ and inside by $2$.
Thus at the end we will obtain for the right side, $[1/(4\pi) sin(2t)]_0^{2\pi}$

### Question 2

$$
s(t)=\begin{cases} 
	3 \hspace{0.4cm} -2<t < 0 \\
	0 \hspace{0.4cm} otherwise
\end{cases}
$$
We try to understand if this is a power signal or an energy signal

$E_s$=$lim_{T\rightarrow\infty}E_s(T)$ = $\int_{-\infty}^{+\infty}|s(t)|^2dt > 0$ && $E_s<+\infty$ 
so we write
$\int_{-2}^{-1}|3|^2dt= [9*t]_{-2}^{-1} = -9+18 = 9$ 

Since the energy is $>0$ and $<\infty$ we can say that this is an energy signal, not a power signal since the two sets are disjointed, so the power will be zero.

### Question 3
$$
s(t)=\begin{cases} 
	3/t \hspace{0.4cm} 1<t < 10 \\
	0 \hspace{0.8cm} otherwise
\end{cases}
$$

$E_s$=$lim_{T\rightarrow\infty}E_s(T)$ = $\int_{-\infty}^{+\infty}|s(t)|^2dt < 0 \land E_s<+\infty$ 
so we write
$\int_{1}^{10}|3/t|^2dt = 9*\int_1^{10} 1/t^2 = -9*1/t|_1^{10} = -9/10 +9= 81/10$

here too the energy is finite. So its an energy signal.