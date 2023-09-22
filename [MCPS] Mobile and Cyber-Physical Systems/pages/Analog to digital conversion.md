Sensors must take values from physical quantities, which are physical quantities and we want to take values in a specific time interval. 
Then we want to represent the values in a digital form to process them with a computer device. That has many useful properties, including the processing of a value without needed special purpose numbers. Why? Because you have numbers, with whom you may work. Also the data may be managed and transmitted without altering the signal.
If condition changes, you do not have to alter the signal, the signal is robust over some specific conditions.

What we can do when sampling from a sensor is to sample an analog signal. We have for sample a value and then transmit it after passing into a analog to digital conversion on a channel that sends a signal. 
But also we may need to reconstruct a signal from digital to digital. It is important that the A/D process does not lose much information from the initial signal.

![[Pasted image 20230613123856.png]]
The process can be seen in the image above.
A/D will transform the analog signal $s(t)$ into a sequence of integer, then the sequence can be ***stored, processed and transmitted by a digital device***. 
To apply those operations, the numeric sequence is transformed into a binary stream.

The main elements of analog to digital are:
* sampling: pick values of a continuous signal
* quantization: represent a value using the representation specification of our system.

### Sampling
Input: a continuous signal $s(t)$
Output: a stream of real numbers

The sampling of a Signal $s(t)$ means to extract a sequence of numeric values that the signal **assumes at discrete time intervals**.
When we sample a signal we consider the value is a instance of time, we consider the sampling period and take the value of the signal at multiples of the signal.
*Sampling is performed at uniformly spaced time intervals*. Those intervals are spaced of **$T_c$** that is the sampling period.

### Quantization
Input: a stream of real numbers produced by sampling
Output: a stream of numbers (integers)

We may have in quantization:
* float representation: just a finite number of bits, to represent a continues domain you can only do a subset of values of the real domain, according to the bits we have you have different quantization solution. The value you can represent from a smaller value of a subset that you can represent.
* integer representation

### Losses for sampling and quantization
In theory, sampling may allows to preserve the *original signal*, under some hypothesis, so without loss. We need to sample correctly to represent well the signal and to reconstruct well the original continuous signal from the samples obtained.

Quantization instead implies to have a loss of information, there will be an error in the representation of the sampled signal. We do not represent exactly the sample value but the goal must be to make the reconstruction of the original signal feasible rather than perfectly. 
There is a trade-off on how well will be the sampled quantized with how much time this process requires.


# Sampling Continuous signal
Sampling allows to obtain from an analog signal, being a continuous signal s(t) a discrete signal $g(n\cdot T$), $n\in\mathbb{Z}$.
Where we can see that there is an equality for the signal in points n of the samples.
$$g(n\cdot T)=s(nT)$$
We have a period and a frequency here for **sampling** too.
* $T_c$ is the sampling period
* $1/T_c$ is the sampling frequency

Given this continuous signal
![[Pasted image 20230613151556.png]]

With sampling we get a discrete signal with points in time. We see on x the *samples at points that are* multiples of our sampling period.
![[Pasted image 20230613151732.png]]

## Example for sin(t)
Given $s(t) = sin(t)$ and **having frequency** $f=1/(2\pi)\approx0.159$, a sample will be the value of a signal at precise time.

**A sample is a value of signal itself, which is defined as $s(nT_c)$**, taking a value for every multiple of the sampling period $T_c$.

So we approximate $s(t)$ with another signal.
We can decide the sampling period $T_c$ and then see what is the value of the sampling frequency:
	if $T_c=3.09$
	then it implies that $f_c=1/ {T_c} \approx0.324>2f$
We have a simple signal and it is enough here to sample with double the signal frequency; but in general, we will see that it is  enough to sample double the frequency for sampling frequency to *approximate well the signal*. The continuous signal can be seen here:
![[Pasted image 20230613152853.png]]
We get then the approximation points as we can see in the bottom graph:

![[Pasted image 20230613152913.png]]

We get only information related to the dots, but we lose some information.


# Reconstruct a Signal - Interpolation

**We apply interpolation to reconstruct the continuous signal.**

There are several ways to do this, such as using the sample value to reconstruct a continuous signal.

There are several methods:
- **Piecewise-constant signal**: This can be done, for instance, by building a zero-order hold, nearest neighbor.
    - **Zero-order hold/Nearest neighbor**: Using a sample, this method decides the value of the curve of a signal from 0 to T. Basically zero-order hold means to assume that the signal assumes a constant value, which is the value of a sample, until the next sample is reached, then it will be the value of that other sample.  
    - **Nearest neighbor** refers to the fact that the reconstructed signal value at any point in time is the one of the nearest sample value.
- **Piecewise linear**: For example, by using first-order hold reconstruction. 
	- First-order hold reconstruction: it approximates a continuous signal, by connecting adjacent samples with straight line segments. it can be seen mathematically as having piecewise linear interpolation between adjacent samples (get the value of a point which is unknown by using other points). The continuous signal will have less discontinuity using piecewise interpolation than other methods for piecewise linear reconstruction. Basically this method involves drawing a line between two consecutive samples. Here, you do not reconstruct the original signal, but something close to it.

Zero Order Hold Interpolation can be seen here:
![[Pasted image 20230613155941.png]]
It can be seen how the values of the reconstructed signal will have the value of the last sample at each point.

# Sampling Theorem
The basic assumption is that if you have a signal that changes rapidly you need to have an high number of samples.
If it changes slowly, you need a low number of samples to represent its variations.
A fast changing signal must be sampled faster than one changing slowly.

**The sampling theorem suggests the minimal sampling frequency required to reconstruct the original signal but that  is only valid in *ideal* conditions** (infinite samples).

Given a sinusoid. We may get a lot for samples for a period, there we sample at high frequency.
Intuitively we will have enough info to reconstruct the signal, whenever $f_c>>1/T$ so if the sample frequency is much greater than the signal frequency (defined as $1/T$ Hertz).
$$x(t)=sin(\frac{2\pi}T)t$$

![[Pasted image 20230613163155.png]]

## Sampling at low rate
In the following image we may see in blue the **original signal**.
![[Pasted image 20230613163344.png]]
If we sample at a frequency that is too low, we may see that the dots do not represent well the original signal. As such we end up reconstruction **a lower frequency signal, which is the one in red**.
The problem there is that the sample does not represent our signal. If we over impose a graph over the points, the red sinusoid matches the samples, which is at a lower frequency.

### Aliasing
The effect where we reconstruct a low frequency signal is called **aliasing**. 
Aliasing is has the effect of making **different signals become indistinguishable when they are sampled**.
Aliasing depends on:
* sampling rate
* frequency content of the signal


## Theorem
The sampling theorem is a fundamental theorem that gives us the sampling frequency required to get enough sample to reconstruct signals and avoid the effect of aliasing.

Given a signal $s(t)$, which is limited in band, which is an important assumption. The spectrum is defined for a range of frequencies up to $f_M$ maximum frequency, after which **the spectrum is null**.

When the signal respect the condition that the spectrum is null above the frequency $f_M$  then we can say *formally*:
$s(t)$ **is completely represented** by its sampled taken:
* at regular intervals $t_n=n\cdot T_c$  where $(n\in \mathbb{Z})$
* with a sampling period $T_C<=1/(2f_M)$. Meaning that we are sampling two times at minimum the double of the maximum frequency.

**With those samples it is possible to reconstruct** $s(t)$ for any $t$.

## Nyquist frequency
So we define the Nyquist frequency.
$$f_{c_{min}}=1/T_{c_{max}}=2\cdot f_M$$
This is obtained by maximizing the sampling period, which allows to obtain the minimum sampling frequency.
**The Nyquist frequency is the minimum frequency at which a signal $s(t)$ limited in band must be sampled*** to be able to reconstruct well the original signal.

**$f_{c_{min}}$ ultimately corresponds to the double of the maximum frequency in $s(t)$.**


### Reconstructing the signal.
We have to do interpolation to reconstruct the signal, there are several ways from sample. One interpolation starting from the samples is the one using the cardinal sin.
This can be seen here in formula:
$$s(t)=\sum_{n=-\infty}^\infty s(n\cdot T_c)\cdot \frac{sin(\pi f_c(t-nT_c)}{\pi f_c(t-nT_c)}$$

We reconstruct signal by using multiples of the period of sample.
By shifting the argument of the cardinal sine function, we can estimate the signal value at any time, not just at the times where we have samples. The shift is a multiple of the sampling period and is determined by the frequency of the signal.
We shift by multiple of the sampling period the argument of the sin, which is ultimately produced by  $\pi$ * frequency of sampling * shift of the multiple of the sampling theorem!

When evaluating the reconstructed signal at a time that is a multiple of the sampling period, such as $2T_c$, the value of the cardinal sine function becomes centered at 0, e.g. $2T_c$
you will get the multiplication of $s(nT_c)\ sin(\pi  fc$) which not shifted but centered at 0.

The ripples around infinity can cause some distortion in the reconstructed signal, which is why other interpolation methods may be preferred in some cases.
So it will be 1 at the center and 0 everywhere else.
You sum the cardinal sin at different point to reconstruct the signal..
To get the value of the signal between two samples, we need to take into account the contribution of the sampling period. This is because the cardinal sine function assumes that the signal is periodic with a period equal to the sampling period. By including the contribution of the sampling period, we can estimate the value of the signal at any point in time.

# FT of a band limited signal
Given a signal $x(t)$ **which is a band limited signal as defined before**, **the Fourier transform of the signal will consist of shifted and scaled copies of $X(f)$**. Where $X(f)$ correspond to the coefficients of the harmonics composing the signal $x(t)$ (the amplitudes). 

The Fourier Transform of a band limited signal can be seen here:
![[Pasted image 20230524163958.png]]

The Fourier transform for a continuous signal is different than the discrete one as we have seen in [[Fourier Transform]].
We make the Fourier of the samples and we obtain the spectrum regards to the transformation. The result is basically a spectrum made of a set of distinct frequencies composing the sampled signal.
The spectrum itself is repeated multiple times in the plane, as it is centered around multiples of the sampling frequency.
So we have spectral replicates also called aliases that are centered around $f_s$.  You can imagine an infinite number of replicas.

### Spacing between the replicas
The replicas of $X(f)$ are spaced depending *around the sampling rate* $f_s$. They are centered around 0 with spacing $f_s$ from their central point.

There is the problem that *if sampling at a too low frequency, we may have overlapping between replicas as it may be seen below*

![[Pasted image 20230524164154.png]]
If you sample at frequency $f_s$ greater than the maximum of the signal. You increase the distance of the replicas, so not overlapping!

![[Pasted image 20230524164238.png]]

*If we sample every T second, the spacing between the replicas in the frequency domain is equal to the sampling frequency $f_s=1/T$*.

**Ignoring what there is between samples, there is the fact that the sampling process throws away lots of information, but since the signal is perfectly band limited, there is no information lost**. *You must account for this in system design!*
*Then take the spectrum and taking the blue part being the original spectrum and having the replicas without overlapping, you have all the information to reconstruct this continuous in time signal*.

With the Fourier transform the signal can be both be represented in the time domain and in the frequency domain, allowing us to convert between them. Using the spectrum you may approximate the signal which is continuous in time, but with discrete samples.
What happens when you sample at a lower frequency, the resulting samples will not contain enough information to reconstruct the signal accurately. This can result in aliasing, distortion, and loss of information.

### Aliasing in depth
Appreciate the aliasing effect you may see that for instance: if you have a signal and know its frequency, you may sample the signal and be able to reconstruct it. But without knowing the frequency *you may reconstruct the wrong signal*.

* Given a sinusoidal signal of frequency $f= 1/2\pi$ which is band limited
	![[Pasted image 20230613183103.png]] 
	**if you know its frequency you can predict precisely the sampled signal.**

There is the problem that **from the sampled signal you cannot find necessarily the frequency of the original signal.**
As it may be seen here:
![[Pasted image 20230613183216.png]]
If you do not **have enough sample** you may construct over the same samples the green signal besides the blue signal.
In this example the sinusoid was taken at a frequency $f'=f/6$, so $1/6$  of the original signal frequency $1/2\pi$.
**This means that the samples will represent more than one signal, which is totally wrong and does not allow to reconstruct the blue signal**.
We may see also how a red signal as below, with an higher frequency may fit in the samples:
![[Pasted image 20230613184056.png]]

This problems holds for all signals.

#### Overlapping example
It can be seen in the images how the spectrum of the sampled signal $s_c(t)$ consist of infinite replicates of the spectrum $s(t)$, those are centered at frequencies multiple of in this examples $f_c=3$

Given the spectrum of $s(t)$:
![[Pasted image 20230613184355.png]]

Then spectrum of $s_c(t)$:
![[Pasted image 20230613184431.png]]

The requirement of Nyquist to have the signal $s(t)$ *be limited in band* is for this reason. As if the signal in the example can be limited at frequency $f_M=1.5$, we can disregard all replicas that have higher frequencies than it!
It can be seen here:
![[Pasted image 20230524164645.png]]

We want most energy of the signal to be limited in the end.
The ideal spectrum of the sampled signal is as follow:
![[Pasted image 20230524164719.png]]
Basically they are not overlapping and when one replica ends, the other starts.

The sampling theorem gives us an hint on the minimum frequency of sampling, providing a proof to reconstruct as most as possible exactly the signal.
Using the Nyquist frequency, we can choose $f_c$ to ensure the above case, so that the replicas of the spectrum of $s(t)$ do not overlap.

## Some sampling frequencies examples
Given a sinusoid, it is supposed to sample it at a frequency $f_c>2f$, saw there
![[Pasted image 20230524164831.png]]
**As we may see here, we sampled at a frequency that is higher than double the signal frequency**

***But the result of the interpolation of the samples, to reconstruct the signal is as follow***
![[Pasted image 20230524164934.png]]
This one is not accurate and does not *reconstruct well the signal*.

By Increasing the sampling frequency and getting it higher than signal frequency, we still may have a problem in the reconstructed signal
![[Pasted image 20230524165005.png]]



![[Pasted image 20230524164903.png]]
As it can be seen here **while the situation improves, and the reconstruction is good for a short interval, the whole result is not a sinusoid!**

## WHY
The problem is that we need:
* limited in band
* sampling at a frequency double the frequency of the signal ($2*f$)
* you need a number of samples that are **infinite in number**
What happens is that even if we satisfy the first two points, by sampling only a finite number of points, the result will include error in reconstructing the original analog signal. *The continuous signal contains an infinite amount of information that a finite set of sample cannot contain*.
**The more sample we acquire, the less is the error in signal reconstruction, but it will never reach 0 with a finite number of samples**.

## What Nyquist did say
Nyquist requires a signal that is limited in band, but not all signals are limited in band.
A finite duration signal will have a spectrum that extends over a range of frequencies. The spectrum is the distribution of the signal's energy over different frequencies.
To have a signal limited in bandwidth then it is necessary that *the signal does not have energy going beyond a frequency band*. For this is necessary that the signal extend infinitely in time.
We can have signal whose higher frequency have low energy or high energy.

What Nyquist stated:
* The boundary is on the frequency of sampling

What Nyquist did not say was:
* the boundary on the number of samples, the **theory works on an infinite number of samples**.

**But we can in any case sample the signal, in finite time and reconstruct it reasonably well.**
No signal is strictly limited, in bandwidth meaning that is unlimited in time this has no physical meaningfulness. Because in practise *they are* ***almost*** limited in band, so their spectrum beyond their band is small, meaning that their energy beyond the band is small.

*There will be little distortion due to this limitlessness* but with good sampling it will be negligible.

### Cutoff Filter
We can apply a cutoff filter to signals that are unlimited in band and focus our attention on a spectrum part. This spectrum part corresponds to the part where most of the energy is concentrated. The cut off signal cuts out components of the signal by **cutting frequencies above a threshold** and then sample the signal. Thus, allows to meet the Nyquist requirement.
You can also use cutoff filter with limited band signal, because these signals are not really limited in band, but they have little energy behind the band limitation. To cancel this little part of signal use cutoff, and this result also having a better signal.

Low pass filter with a cutoff at half the sampling frequency $f_s/2$, but an ideal filter cannot be realised, as you would then attenuate high frequency content. To solve this, you use oversampling and then a cutoff filter, to reduce the loss of attenuated frequencies.

## What Nyquist did not say

«I am going to sample at 8 KHz, so I need to use a filter with a 4 KHz cutoff»
* Sampling at rate $N$ samples per second **Nyquist did not say that you can use an anti-aliasing filter with a cutoff at frequency $f=N/2$.**
* The filter applied to the signal, does not put to $0$ the frequency higher than the limit that we give, it just attenuates its component frequency. Basically *there is no analog filter that is perfect*, there is a **significant amount of frequencies above 4 KHz** that pass, although they are attenuated.
* The aliased signal is not negligible and seriously disturbs sampling.

Meaning that just sampling with a signal with a cutoff half of the frequency cutoff is not enough.
If you want to apply the theorem the solutions are:
* use a more complex anti-aliasing filter, which anti alias filter, without resampling but getting a filter that has a steep slope, so a filter that has a fast transition from passing frequencies to attenuating frequencies. In this way one can cutoff the signal to satisfy the limited band to apply the Nyquist theorem.
	![[Pasted image 20230524165433.png]] 
* You oversample, we may also increase the sampling frequency, as by increasing it, we consider different in replica of the spectrum for example. In this way the replicas do not alter the signal, we move the replica further from each other.

#### Telephone companies solution's
The method is to used as filter to resolve this situation was to use a stronger cutoff  with a low pass filter which filters anything in the band between 0 and 3 KHz.
The frequency that pass are over 3 KHz, than sample at a frequency of 8 KHz, **more importantly they oversampled at 8 KHz**.

So limit the band of the signal, than oversampling at a higher frequency. **It is impossible to give general rules for all cases, but it gives example to study your specific signal.**

#### Another case
«I need to monitor the 60 Hz power line, so I need to sample at 120 Hz»
«We have a signal at 1 kHz we need to detect, so I need to sample at 2 kHz»

**Nyquist did not say that a signal that repeats $N$ times a second, has a bandwidth of $N$ Hertz**. Basically a power line of 60 Hz would mean that the signal repeats every $T=1/60$ Hz. But this does not correspond to the bandwidth. That is because the powerline is nominally at 60 Hz, but there is a lot of distortion, as it may be seen in the figure below, so there are many frequencies involved!

![[Pasted image 20230524165706.png]]
The main signal is of 60 Hz but it is not true that it is limited in bandwidth at 60 Hz.
It does not work just sampling 120 Hz, as you see the ripples, a component is at higher frequency, up to 300 Hz, the 2°, 3°, 4°, 5° harmonic must be considered with their variation (the latter is to 300 Hz).
You need to sample at least at 600 Hz, as this is the maximum frequency that you want to consider. **But in reality even more, because you do not know the phase of the signal, if you want to have accurate sampling in a short time, you need to oversample accurately**.

#### Rephrasing the question
«I need to monitor the 60 Hz power line, so I guess need to sample at well over 120 Hz».

**Not even that, in some case it may be even better to downsample, which means to at first oversample, then waiting long enough with patience to connect enough sample at an high rate before decimating (removing) some of the sample to archive a lower effective sampling rate.***
Or just to sample at a lower rate at the start but wait long enough to get enough information to reconstruct the original signal.

You may discard the effects of the other Harmonics and only care about the main frequency of the power line signal, so discarding the harmonic which are greater than the fundamental harmonic, **if you have as in this case** a steady signal, which has a known and steady frequency, you may need to sample the signal only on some part, and you may discard the transient phase.
You can reconstruct the signal, by reconstructing it at a lower frequency, for example a frequency slightly over 20 Hz.

The sinusoid at different period, given there, if our device cannot sample at a certain frequency.
You have a sampling period = signal period + a small interval.

So we may get a sample in different part of the signal period. **What we see is that the signal phase, within a cycle will advance a little bit for each new sample**.
This allows us to reconstruct the signal, once we wait enough sample, in the required time.
**We need the signal to be stead, repetitive and with a steady frequency to do that**.
![[Pasted image 20230524170148.png]]

This works only for AC/DC signal.
What you do is to make an analysis of the signal and its nominal frequency, which is different from what we did before, as we need to consider (want) also the 5° harmonic.
This shows how the theorem can be applied in different way.

Now we cant get infinity, but when you see the sampling of 20, you know that you approximate well the curve for a bit, after that, you will lose in the middle and after that.
You cant do better than going to infinity, at least us as much samples as possible to approximate better the signal.


# Quantization
In general the values obtained with sampling are Real numbers, but in some applications, even a representation in floating point (32/64 bits) is considered prohibitive (e.g. in IoT).

For example in Arduino Uno ([[Embedded Systems and Case study of Arduino]]), there are only 10 bits per integer, which can be used to represent a sample.

We may see below how the quantized value and the sampled value may be different, because the quantized value may be rounded to the nearest value in the quantized representation, rather than the continuous value.
![[Pasted image 20230614120952.png]]

Given k bits, we can represent integers in the range: \[0, $2^{k-1}$\]
We can represent the integer closer to a sample in that range.

# Doing quantization from a signal
Given a signal sampled at a frequency $f_c$.  This means that the samples are taken at intervals $T_c=1/f_c$

Letting $x_k\in\mathbb{R}$ be the sample read at the time interval $I_k$. This is uniform quantization where the input range is divided into uniformly spaced quantization levels, this means the intervals between quantized values are all the same size.

The quantization will encode $x_k$ in an integer value $y_k\in[0,2^R-1]$. Then we use a R-bit scalar quantized. It is said scalar because the samples are quantized individually.
There is the requirement of R bits per sample, those R bits per sample are defined as the **quantization rate**.
The bit rate for a signal sampled at frequency $f_c$ is $R_b=R\cdot f_c$ bit/sec.

Keep in mind:
	$R_b=R\cdot f_c$ bit/sec bit rate for a signal sampled at frequency $f_c$

When we represent the signal as the quantized signal, you introduce an error, as in the different than sampled in time t instance, you represent the quantized value

For example this is the signal sampled
![[Pasted image 20230614122405.png]]
This is the quantized signal:
![[Pasted image 20230709153652.png]]
$s(t)-y_k$ error, with y being the k-th quantized value.
You do not represent exactly the signal value.
You represent a value on the subset of number that can be represented with your system of representation of bits.
There are errors in the difference between signals and quantized values.
As it may be seen here:
![[Pasted image 20230614122434.png]]


# Quantization noise

## Overload 
**You may have an overload with uniform quantization, which happens whenever** have some points at the same distance, and you are not be able to represent a signal, because it is above the maximum value you can represented correctly, as it will have a lower resolution. This happens formally when:
* $s(t)>2^R-1$
This can be faced with non uniform quantization.
Non-uniform quantization can provide higher resolution for certain input ranges dividing bits for higher ranges, meaning that it allocated more bits for certain higher input ranges.
![[Pasted image 20230709154002.png]]

## Granular noise
If all the values in an interval $I_k$ are represented with a unique $y_k$, meaning that if the signal changes, you are not capturing changes. This is called granular noise and you lose the spacing between points.
Basically you have a piece-wise constant signal, meaning that a signal takes a constant value at different intervals of time, there it can happen that phenomenon.
This process of approximating a continuous signal by a piece-wise constant signal can introduce errors and distortions, which can be seen as a type of granular noise.
![[Pasted image 20230614125302.png]]

### Example
As Humans we can hear in the frequency of 20 to 20.000 Hz (20 kHz).
This is too much, what is really needed and acceptable as degradation in quality can be around 4 kHz usually, or even 3 kHz sometimes. That is the level accepted at phone.

### Solution
We apply a sampling rate, twice the 4 kHz frequency that we want to send.
The sampling rate taken is $f_c=8$ kHz. Each sample is quantized on 8 bits (R=8).
So we sample at 8 kHz and not for example 40 kHz (double of maximum).
We get a bit rate of $R_b=64Kb$ ($R*f_C$)


# Exercise on sampling
Consider that the period, is the point where a trig function returns to its starting initial position. Which may be shifted right by adding $-1$ or shifted left by adding $+1$

Given 4 signals, find the Nyquist sampling frequency, by applying the sampling theorem.

Always check if the band is limited, **if the band is not limited then you cant apply the theorem, you would need to apply a cut-off filter**.
- $s(t)=sin(3t)$
- $s(t)= \begin{cases} 1 \hspace{0.5cm} -2<t<2 \\ 0 \hspace{0.5cm} otherwise \end{cases}$
- $s(t)=sin(2t+5)+sin(8t-1)$
- $s(t)=7+sin(2t-1)$ 

#### $s(t)= sin(3t)$
It is limited in bandwidth as its a sin limited in $-1$ to $+1$ and its a periodic function so its a energy signal.
1) Period is 2$\pi/3$,
2) given the period, we find the signal frequency $f=$ $3/(2\pi)$ 
3) We find the maximum frequency, which is  $f_m$ = $f$ $3/(2\pi)$:
5) Then we calculate the Nyquist sampling frequency $f_c$ = $2 \cdot 3/2\pi$ = $3/\pi$ 

#### $s(t)= \begin{cases} 1 \hspace{0.5cm} -2<t<2 \\ 0 \hspace{0.5cm} otherwise \end{cases}$
This signal is not limited in band, as its maximum value is 1.

That is because the signal is limited in time **but its not limited in band**. If we make the Fourier transform of this, we get contribution in frequencies that go up to the infinite frequencies contributing. So we cant have a Nyquist sampling frequency.

#### $s(t) =sin(2t+5)+sin(8t-1)$

The signal is limited in band.
The period of this one is $T=2\pi/8$
(as $sin(8*(2\pi)/8-1)=sin(-1)$))

The maximum frequency is $f_m= 8/2\pi$.
You have two sinusoid, but you consider just the second to calculate 7 the maximum sampling frequency, because it has higher frequencies

As such we cant calculate the Nyquist frequency:
$f_c= 2* 8/2\pi$.

#### $s(t) =7 + sin(2t-1)$
This signal is limited in band, as we just sum a constant term to a sinusoid function.
In reality the period is $2\pi/2$ as for the argument of the $sin$ function $2t$.
7 will influence the frequency but the influence of sin gets higher values.
The maximum and unique frequency of the signal is then $f_m=2/2\pi$. 
The sampling frequency is then $f_c=4\pi$ being its double.


# Exercise on Quantization
Consider an analog to digital converted ADC, which performs Q-bits quantization of signals. Using Q bits for signals in the range \[0,M\],
Compute the resolution of quantization and the maximum absolute quantization error.

Represent a range and divide in by using q bits.
What is the resolution of the quantization, meaning the distance between two points, and then the absolute quantization error!

We represent a range and divide in by using Q bits.
The quantization resolution is the distance between two points. We represent a range using Q bits, so the quantization resolution is M/$2^Q$, 
Given that we may calculate the absolute quantization error.

![[Pasted image 20230614183156.png]]

* If Q = 10. the quantization resolution is 5/$2^{10}$ = 0.0049.
	* The resolution is the distance between two values.
* The maximum quantization error is **at most half the resolution, because by rounding a value, we may at most most miss half of the interval in precision**. So it is at most 0,0049/2.
		* **The error is the distance of two adjacent values**


So on for all other cases
![[Pasted image 20230614190943.png]]

How a controller can build up a topology and communicate with switches to construct a topology.
At the exam even the scheme and interaction may be to do.
The generations changes must be studied!
The architectural schema are not required!

## Summary 
Sensors produce analog signals that need to be converted to digital form for processing by computers. Sampling involves taking discrete samples of the analog signal at a certain rate. While sampling allows us to represent the analog signal in digital form, it does not necessarily provide all the information required for perfect reconstruction.

The Nyquist sampling theorem states that to perfectly reconstruct a continuous-time signal from its samples, the sampling frequency must be at least twice the highest frequency in the signal, known as the Nyquist frequency. This ensures each cycle of the highest frequency is sampled at least twice.

Aliasing occurs when a signal is sampled below the Nyquist rate, causing different signals with frequencies above the Nyquist frequency to become indistinguishable in the sampled signal. Anti-aliasing filters can be used to remove frequency components above the Nyquist frequency before sampling to prevent aliasing.

In practice, the sampling theorem is applied to signals that are effectively band limited, meaning most of the signal energy is contained below a cutoff frequency. The theorem also strictly requires an infinite number of samples; in practice we use a finite but sufficiently large number of samples to approximate it.

Higher sampling rates and more bits of quantization provide higher resolution and accuracy but at the cost of larger data volumes and higher computational requirements. Non-uniform quantization assigns more bits to higher value ranges for higher resolution.