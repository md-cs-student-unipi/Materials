
## Complex Numbers

$\overline{x} = a + jb$ is a complex number, composed of the real part a and the imaginary part $jb$, j is the imaginary number, $j=\sqrt{-1}$ .

We may also define the conjugate of $\overline{x} = a + jb$  being  $\overline{x}^* = a - jb$ 
We may **represent the number in the imaginary plane, using the vector with $|x|$ as modulo and phase $\phi$**

![[Pasted image 20230611184040.png]] ![[Pasted image 20230611184057.png]]
On the right we can see it with its conjugate.
Consider that we can also obtain the single components:
* $|x|=\sqrt{a^2+b^2}$
* $\phi=tan^{-1} b/a$
* $a= |x|cos(\phi)$
* $y= |x|sin(\phi)$
then we can also **write into an alternate form the complex number**
$\overline{x} = a + jb = |x|*cos(\phi)+j|x|*sin(\phi)$


## Euler exponential
We can define the Euler exponential, which is a complex number, defined as:
* $e^{\pm j\phi}=cos(\phi)\pm j*sin(\phi)$

We can derive then the Euler formulas
* $cos(\phi)=(e^{j\phi}+e^{-j\phi})/2$
* $sin(\phi) = (e^{j\phi}-e^{-j\phi})/2j$

$\overline{x}=a+jb$ can be rewritten then as  $\overline{x}=|x|\cdot e^{j\phi}$ 
which fits into the definition of $\overline{x} = a + jb = |x| \cdot cos(\phi)+j|x|\cdot sin(\phi) = |x|\cdot e^{j\phi}$

We then may represent the conjugate $\overline{x}^*=|x|\cdot e^{-j\phi}$


# Fourier series with exponential base
As seen in the introduction of signals([[An Introduction to the Theory of Signals]]), the formula of the Fourier series may be rewritten according to the Euler exponential

Formally, the Fourier series is **expressed in the complex numbers domain, allowing to represent signals s(t):$\mathbb{R}$->$\mathbb{C}$**
Since  $\mathbb{R}\subseteq \mathbb{C}$, that definition includes also signals  $s(t):\mathbb{R}$->$\mathbb{R}$

The following form, is a generalization of the Fourier series for real functions, this form is the one generally used and allows to generalize Fourier series for real functions using the complex exponential.

Given a continuous signal $s(t):R \rightarrow R$ periodic in the interval $[-\pi,\pi]$ (so $T=2\pi$ period).
$s(t)=1/2*a_0+\sum_{n=1}^\infty(a_n*cost(nt)+b_n*sin(nt))$

We may redefine using as base of Fourier, the set of functions:
* $e^{j\cdot 2\cdot \pi\cdot n\cdot F\cdot t}\forall{n}\in\mathbb{Z}$, where there is defined $\phi=2\cdot\pi\cdot n\cdot F\cdot t$. 
* $n$ is also called the weight
* The complex exponential $e^{x+jy}$ can be decomposed into $e^{x+jy}$ = $e^x\cdot e^{jy}=e^{x}\cdot(cos(y)+jsin(y))$ as we substituted the $e^{\pm j\phi}=cos(\phi)\pm j\cdot sin(\phi)$ and add the x component with $e^x$, here $y=\phi$

**This results in the base of Fourier set of functions to be**:
* $e^{j\cdot 2\cdot \pi\cdot n\cdot F\cdot t}=cos(2\cdot\pi\cdot n\cdot F\cdot t)+j\cdot sin(2\cdot\pi\cdot n\cdot F\cdot t)$
(note that $e^x= 1$ here and $x=0$)

## Formally Fourier with exponential base
Given a **periodic** signal:
* $s(t)=s(t+T)\forall t$
* $s(t)$ is defined as a power signal (infinite energy and finite power)
The frequency $F = 1/T$ is the *fundamental (first) harmonic, expressed in Hertz*

The signal can be represented with the linear combination

$$s(t) = \sum_{n=-\infty}^\infty S_n\cdot e^{j\cdot 2\cdot\pi\cdot n\cdot F\cdot t}$$

which then can be expanded with the previous result for the base of Fourier set of functions:
$$\sum_{n=-\infty}^\infty S_n\cdot(cos(2\cdot\pi\cdot n\cdot F\cdot t)+j\cdot sin(2\cdot\pi\cdot n\cdot F\cdot t))$$

In those cases the harmonics are:
* $e^{j2\pi nFt}$
* $(cos(2\pi nFt)+j\cdot sin(2\pi nFt))$

While the amplitude of the harmonic is:
$$S_n = \frac{1}{T}\int^{T}_{0}s(t)e^{-j2\pi nFt}$$

**Dirichlet theorem states that the Fourier series give the same values of $s(t)$ where $s(t)$ is continuous but not in discontinuities**. That expresses the fact that $s(t)$ is fully represented by ${S_n}$, meaning that the knowledge of the series $S_n$ is equivalent to the knowledge of $s(t)$
*The periodic signal $s(t)$ can be tough as being composed by an infinite number of periodic signal.*

The idea is that the Fourier base, have frequency $nF$, which is a multiple of the fundamental harmonic $F = 1/T$.

* For $n>1$:
	* The terms $S_n\cdot e^{j2\pi nFt}$ are called **the harmonic components of $s(t)$** each of those with frequency $nF$
* For $n=0$
	* The coefficient $S_0=1/T\int_0^Ts(t)dt$ is the "constant" component, as it is the average value of $s(t)$
* For $|n| = 1$:
	* there is the fundamental frequency $f_0=F$ with period $T=1/F$
	* $S_1$ and also $S_{-1}$ are the amplitudes of the fundamental frequency (consider that we start from $-\infty$ so of course we will have also $S_{-1}$)
* For $|n|>1$ (same as first):
	* the harmonics of frequency $f_n=nF$ with period $T/n$
	* $S_n$ are the amplitude of the harmonics, whenever the value is different than -1 and 1, the harmonics after the fundamental are the one represented

# Fourier series of aperiodic signals using limited support
Consider limited support, where the signal is not defined out of the bounds $[a,b]$.
Furthermore, we can obtain the Fourier series **for an aperiodic signal with limited support**, as the series assumes that the signal is periodic,**taking as period the entire duration of the signal**.

As a consequence, you may revert from $S_n$ to s(t) and obtain **the periodic extension of the signal**
As can be seen in the image:

![[Pasted image 20230612102804.png]]

## Example
Consider the signal with period T and frequency $F= 1/T$
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{1.75cm} |t|\leq T/4 \\ 
	0 \hspace{0.4cm} if \hspace{0.3cm} T/4 < |t| \leq T/2 \\
\end{cases}
$$

![[Pasted image 20230612114552.png]]
The coefficient of the Fourier series are

$$S_n=1/T\int_0^T s(t)\cdot e^{-j2\pi nFt}dt = 1/T\int_{-T/4}^{T/4} 1\cdot e^{-j2\pi nFt}dt$$
expressing to the period where the signal is defined and using the value of $s(t)$ for the interval.
This integral has two values, $1/2$ if $n=0$, while $\frac{sin(n\pi/2)}{n\pi}$ if $n\neq0$. 

The resolution is done by doing the integral with substitution, then it solves the integral by plugging the intervals, at the end it equalizes the result to this one:
![[Pasted image 20230612112549.png]]
Since there is a sine, it can have two possible values. As we saw in [[An Introduction to the Theory of Signals]] the function can be decomposed in odd ($2k-1$) and even values.

We may see the formula in its full form, by using said n:
$$s(t)=\frac12+\sum_{k=-\infty \ \& \ k\neq 0}^{k=\infty}(-\frac{(-1)^k}{(2k-1)\pi}(cos(2\pi(2k-1)Ft)+j\ sin(2\pi(2k-1)Ft)))$$

**Using the fact that sin is an odd function and $sin(x)=-sin(-x)$**:

The formula becomes for the **complex part** becomes, *also by taking out t*
$\sum_{k=1}^{k=\infty}j*sin(2\pi(2k-1)Ft)=$
$-\sum_{k=1}^{k=\infty}j*sin(-2\pi(2k-1)Ft)=$
$-\sum_{k=1}^{k=\infty}j*sin(2\pi(-2k+1)Ft)=$
$-\sum_{k=-1}^{k=-\infty}j*sin(2\pi(2k-1)Ft)$ 

What we basically stated is that the part from $-\infty$ to $-1$ will be the negative of the part from 1 to $\infty$ so they will null each other.
*The complex terms are null in this example.

Furthermore the formula becomes:
$$s(t)=\frac{1}{2}+ \sum^{k=\infty}_{k=-\infty}-\frac{(-1)^k}{(2k-1)\pi}cos(2\pi(2k-1)Ft)$$

So only the real part of the cosine remains.
We can see an approximation, with period $T = 4$. Which means that at $F=1/4$ Hertz, we have that representation of the signal.
![[Pasted image 20230612120249.png]]
**We can see how there are different approximation depending on the range from which k is iterated!**

Consider that the original signal is:
![[Pasted image 20230612120338.png]]
Taking 200 of k values, yields the blue that is exactly the same signal with some noise


# Spectrum of a signal
Given a signal $s(t)$ and using Fourier it can find the coefficient $S_n$ of the series, given it we can reconstruct the signal $s(t)$.
The sequence of order coefficient, $S_n$ with $n=-\infty$ to $+\infty$ is called **spectrum of $s(t)$**.
*The spectrum itself can be seen as a discrete signal* (a digital signal).

The spectrum of:

$$
S_n=\begin{cases} 
	1/2 \hspace{1.5cm} if \hspace{0.3cm} n=0 \\ 
	0 \hspace{2cm} if \hspace{0.3cm} n \hspace{0.3cm} even \\
	-\frac{(-1)^k}{(2k-1)\pi} \hspace{0.4cm} if \hspace{0.3cm} n=2k-1
\end{cases}
$$
is
![[Pasted image 20230612124245.png]]
In $n=0$ we have the constant signal.
In $n=1$ and $n=-1$ we have the fundamental harmonic.

So without knowing $s(t)$, but just by knowing $S_n$ we can reconstruct the signal. The spectrum $S_n$ as may be seen in the image, is a set of values, which are discrete values

## Fourier Transform
*Having s(t)* which is a continuous signal, we can transition to its spectrum, which is its discrete signal $S_n$.
**The transition is called Fourier Transform (FT)**.

That is denoted in such way:
$$s(t) \underset{FT}{\iff}S_n$$
We may even represent it with:
$$S_n=\mathcal{F}(s(t)) \hspace{1cm} (transform)$$
$$s(t)=\mathcal{F}^{-1}(S_n) \hspace{1 cm} (inverse\hspace{0.2 cm} transform)$$


With the transform the domain changes from **the time domain of $s(t)$** to the *frequency domain* of $S_n$

$S_n$ is a function of n, that identifies an harmonic and that harmonic identifies a frequency.
That is because $S_n$ is the amplitude of the harmonic of frequency $nF$ and period $T=1/nF$.

*The frequency domain in this case is the discrete frequency domain.* This is because we have a discrete set of frequencies.
In conclusion the Fourier Transform is a transform to the **discrete frequency domain**.

## Spectrum of a signal in complex dimension

In general $S_n$ is a complex number, while there may be some lucky cases where both $S_n$ and s(t) are real.
It is not always possible to represent the spectrum with a 2D diagram as before.
*We can use the Euler exponential, to represent $S_n$*.
$$S_n=|S_n|\cdot e^{j\theta_n}$$
Where:
* Phase of the harmonics = $e^{j\theta_n}$
* Amplitude of the harmonics $|S_n|$

*So the representation of $s(t)$ has two diagrams*:
* phase spectrum diagram
* amplitude spectrum diagram

### Example
Given this signal:
$$
s(t)=\begin{cases} 
	-1 \hspace{0.4cm} if \hspace{0.91cm} 0< t\leq T/2 \\ 
	1 \hspace{0.75cm} if \hspace{0.4cm} T/2 < t \leq T \\
\end{cases}
$$

We have those coefficients for the Fourier series
(again the resolution is done by doing the integral with substitution, then it solves the integral by plugging the intervals, at the end it equalizes the result to this one):
![[Pasted image 20230612153735.png]]

So as result the coefficients are
$$
S_n=\begin{cases} 
	0 \hspace{1.cm} if \hspace{0.55cm} n \hspace{0.2cm} even\\ 
	j\frac{2}{n\pi} \hspace{0.4cm} if \hspace{0.55cm} n \hspace{0.2cm} odd \\
\end{cases}
$$

#### Using the complex numbers representation
Recalling the following statements from the start of this note
* $|x|=\sqrt{a^2+b^2}$
* $\phi=tan^{-1} b/a$
* $a= |x|cos(\phi)$
* $y= |x|sin(\phi)$
then we can also **write into an alternate form the complex number**
$\overline{x} = a + jb = |x|*cos(\phi)+j|x|*sin(\phi)$

Such that:
* if n is odd:
	$S_n=j*(2/n\pi)$ where $a=0$ (as there is no real part), $b=2/n\pi$, $\theta_n=tan^{-1}b/a$ can be written as: $$S_n=|S_n|\cdot e^{j\theta_n}$$
Furthermore we have two cases.
* when a>0, then $\theta_n=tan^{-1}b/a=\pi/2$
* when b<0, then $\theta_n=tan^{-1}b/a=-\pi/2$

As such the representation of the coefficient $S_n$ is:
$$
S_n=\begin{cases} 
	0 \hspace{2.3cm} if \hspace{0.3cm} n \hspace{0.2cm} even\\
	\frac{2}{n\pi}e^{j\pi/2} \hspace{1cm} if \hspace{0.3cm} n>0 \land n \hspace{0.2cm} odd \\
	-\frac{2}{n\pi}e^{-j\pi/2} \hspace{0.35cm} if \hspace{0.3cm} n<0 \land n \hspace{0.2cm} odd
\end{cases}
$$
Here, we isolate the amplitude as:
$$
S_n=\begin{cases} 
	0 \hspace{1.05cm} if \hspace{0.3cm} n \hspace{0.2cm} even\\
	\frac{2}{n\pi} \hspace{0.7cm} if \hspace{0.3cm} n>0 \land n \hspace{0.2cm} odd \\
	-\frac{2}{n\pi}\hspace{0.35cm} if \hspace{0.3cm} n<0 \land n \hspace{0.2cm} odd
\end{cases}
$$
**We represent the amplitude in the spectrum**
![[Pasted image 20230612155937.png]]
Furthermore the phase is:
$$
S_n=\begin{cases} 
	0 \hspace{1.2cm} if \hspace{0.3cm} n \hspace{0.2cm} even\\
	\pi/2 \hspace{0.7cm} if \hspace{0.3cm} n>0 \land n \hspace{0.2cm} odd \\
	-\pi/2 \hspace{0.35cm} if \hspace{0.3cm} n<0 \land n \hspace{0.2cm} odd
\end{cases}
$$
which is represented by 
![[Pasted image 20230612160013.png]]
With the previous found coefficient, we can represent the signal:
![[Pasted image 20230612160100.png]]

# Fourier Transform for non-periodic signals
It is possible to apply the transform to *finite signals* not just to periodic signals. The signals are finite in a time frame of length $T$. Hence, the counter-transform will instead return a periodic signal with period $T$.

When $T \rightarrow \infty$ then the Fourier Transform interprets the signal with a fundamental frequency $F=1/T$ that tends to 0 ($F\rightarrow 0$). What happens is that the harmonic tend to become infinitely close to each other. The periodicity will disappear progressively.

So, a non periodic signal s(t) can be expressed as:
$$s(t)=\int_{-\infty}^{\infty}S(f)e^{j2\pi ft}df$$
*where f is the continuous frequency*, which ranges in $[-\infty,+\infty]$
$S(f)$ is **the amplitude** of the frequency $f$. In this case, we have that $S(f)$ is given:
$$S(f)= \int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}dt$$
and $S(f)$ is the spectrum. 

Unlike the continuous signals that produce a discrete spectrum, these finite signals produce a spectrum as a continuous function. This can be seen in the next example, compared to the previous the difference is well visible. 
A continuous and aperiodic signal can have energy concentrated in a continuous range of frequencies rather than only in specific frequencies. This can make the frequency spectrum of a non-periodic signal more difficult to interpret.

The passage from the non-periodic signal to its spectrum is called **Continuous Fourier Transform* (CFT).
We denote it in two ways:
$$s(t)\underset{CFT}{\iff}S(t)$$
Or also with:
$$S(f)=\mathcal{F}_c(s(t)) \hspace{1cm} (transform)$$
$$s(t)=\mathcal{F}_c^{-1}(S(f)) \hspace{1cm} (inverse \hspace{0.2cm} transform)$$

## Example

Given the pulse signal, which has finite energy and power equal to zero, but being a pulse is not continuous.
$$
s(t)=\begin{cases} 
	-1 \hspace{0.4cm} if \hspace{0.2cm} |t|\leq T/2 \\ 
	0 \hspace{0.75cm} otherwise \\
\end{cases}
$$
Which is represented as:
![[Pasted image 20230612165543.png]]

The coefficients of the Fourier series are:
$S(f) = \int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}dt=$
by dividing in the intervals with different values of $s(t)$ 
$\int_{-T/2}^{T/2}e^{-j2\pi ft}dt$ = 
performing the integral by substitution of $u = -j2\pi ft$, we get the final result
$[e^{-j2\pi ft}/(-j2\pi f)]^{T/2}_{-T/2}$ we then plug the values:

To obtain:
$$S(f)=\frac{e^{\frac{j2\pi fT}{2}}}{j2\pi f}-\frac{e^{-\frac{j2\pi fT}{2}}}{j2\pi f}=\frac{sin(\pi fT)}{\pi f}$$

Furthermore, by considering different values of T, we can obtain different approximation,
*It has to be noted that in this particular case $S(f)$ is real, with no imaginary part*.
The phase of the spectrum is constant and is not represented.

Original signal:
![[Pasted image 20230612171659.png]]

Spectrum with T=5
![[Pasted image 20230612171717.png]]
The backward transformation of it
![[Pasted image 20230612171745.png]]
Spectrum with T=10
![[Pasted image 20230612171818.png]]
Its backward transformation:
![[Pasted image 20230612171846.png]]

**We may see that by increasing the period, we increase the length of the pulse in the signal, giving it a length of T**.

With $T=20$
![[Pasted image 20230612171948.png]]

![[Pasted image 20230612172003.png]]


# Band of a signal

Whenever the signal is periodic, the spectrum contains only the harmonics of the main frequency (it being the fundamental frequency,  F = 1/T) with different amplitudes (its multiple frequencies). In general the spectrum of a signal spans across all frequencies in $(-\infty, +\infty)$.

*We may filter some of the frequencies of the spectrum*.
In such way we may obtain a *signal limited in bandwidth*.

The signal can:
* exclude high frequencies, those are called **low-pass filter**
* exclude low frequencies, those are called high-pass filter
* exclude low and high frequencies, keeping the intermediate frequencies, those filters are called **band-pass filter**.

## Example
Considering the pulse signal , which was then transformed into the spectrum, and then obtain in the new form by the reverse transform.
With T=20.
It became:
![[Pasted image 20230612173835.png]]
The new signal became:
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{0.2cm} |t|\leq 10 \\ 
	0 \hspace{0.4cm} otherwise \\
\end{cases}
$$
Its spectrum is then:$$S(f)=\frac{e^{\frac{j2\pi fT}{2}}}{j2\pi f}-\frac{e^{-\frac{j2\pi fT}{2}}}{j2\pi f}=\frac{sin(\pi fT)}{\pi f}$$
By plugging $T=20$
$$S(f)=\frac{sin(20\pi f)}{\pi f}$$
The spectrum is:
![[Pasted image 20230612174036.png]]

### Apply a low-pass filter
By applying a low pass filter for frequency below $0.5$. We can obtain a different spectrum, where the little points which are not very near to 0 will be erased:
![[Pasted image 20230612174250.png]]
This will then get us this new digital signal:
![[Pasted image 20230612174305.png]]


### Apply an high-pass filter
By applying an high pass filter for frequency above $0.5$.
We increase the values in the range distant from the very near of 0.
![[Pasted image 20230612174448.png]]

### Apply a band-pass filter
By applying an band pass filter for frequency in range $[0.1,0.5]$.
We increase the values in the range distant from the very near of 0.
This will erase the very very near values in 0. But it will keep the values up to $0.5$.
![[Pasted image 20230612174622.png]]


## But what is a band for a signal
A band represents the range of frequencies within a signal.
Where Bandwidth represents the range of frequencies over which the signal can operate effectively.
A signal is said band-limited if the **frequency content** is **limited to a certain range**.
For humans the audible frequency range is limited between 20 Hz and 20 kHz. Here **the band is the range of frequencies within that range**.

# Question
![[Pasted image 20230612182834.png]]
Consider that f is a continuous frequency ranging from $-\infty$ to $\infty$. Consider that the period here is $T=5$.
This signal is ***not limited*** in band, this is because it has infinite support in the frequency domain. That means that it contains contribution from all frequencies, which are both the positive and negatives.

By applying a low pass filter with threshold frequency set to 1. We need to remove all the frequency going above this line:

![[Pasted image 20230704120451.png]]As such the frequencies remaining are:
![[Pasted image 20230704120802.png]]

### An example of a signal with limited band

The signal
$$
s(t)=\begin{cases} 
	A \cdot sin(2πf_0t) \hspace{0.4cm} if \hspace{0.2cm} \leq T/2 \\ 
	0 \hspace{3.1cm} otherwise \\
\end{cases}
$$
where $A$ is the amplitude of the signal, $f_0$ is the center frequency, and $T$ is the duration of the signal.
The signal is non zero only in the interval $[-T/2,T/2]$.
Since it contains a single component, only the frequency component at $f_0$, the bandwidth of the signal is equal to the frequency range which is significant for it, that is of size $2f_0$.
The signal is band-limited to frequency range $[-f_0,f_0]$


# From FT do DTF
We may define for discrete signal a Fourier Transform, which represents signals only at *N* instants, which are *separated by sample times T*. Basically the sample are a finite sequence of data.

*Continuous signals are reduced to discrete time signal, by applying a domain restriction, from $\mathbb{R}$ into $\mathbb{Z(T)}$.

Sampling is the operation that performs this restriction, it is stated by the relationship:
* $sc(n\cdot T)=s(n\cdot T), n\cdot T\in \mathbb{Z(T)}$
**Where**:
* $s(t), t\in \mathbb{R}$ is the reference to the continuous signal, and  $sc(nT),nT\in \mathbb{Z(T)}$ is the discrete signal **obtained by the sampling operation**.

## Discrete Time Signal
A discrete-time signal is a ***complex function***, **of a discrete variable**.
It is defined as:
* $f(t):\mathbb{Z}(T)\rightarrow$ℭ
	* the domain is $\mathbb{Z}(T)$, which represent the of multiples of $T$, being $\mathbb{Z}(T)=${$...,-T,0,T,2T,..$} for $T>0$.
The signal can be denoted in two forms:
* $s(nT)$, $nT\in\mathbb{Z}(T)$
* $s(t$), $t\in\mathbb{Z}(T)$

## Onwards to discrete Fourier transform
Having defined $s(t)$, $t\in\mathbb{R}$ to be the continuous signal that is the **source of the data**. Letting the $N$ samples to be denoted by $s(0),s(1),....s(N-1)$

The Discrete Fourier Transform will consider each sample as **an impulse having area $s(t)$**.
The integral exists only at the sample points. What the amplitude of frequency $f$ will become is:
$$\displaylines{
S(f)= \int_{-\infty}^{\infty}s(t)e^{-j*2\pi ft}dt=\\
s(0)\cdot e^{-j2\pi f0}+s(1)\cdot e^{-j2\pi f1}+s(2)\cdot e^{-j2\pi f2}+...+s(N-1)\cdot e^{-j2\pi f(N-1)}
}$$

In short, the formula becomes:
$$S(f)=\sum_{k=0}^{N-1}s(k)\cdot e^{-j2\pi fk}$$
*The DFT treats the data as if they were periodic, this is because there is a finite number of input data points*. So what happens is that:
* $s(N)$ to $s(2N-1)$ is equal to $s(0)$ to $s(N-1)$.
**Given this, we can evaluate the DFT equation for the fundamental frequency which is $(1/NT)$** and its harmonics, *since the operation treats the data as periodic.*
So $f = 0,\frac1{NT},\frac2{NT},...,\frac{N-1}{NT}$
What happens is that the DFT computes a finite number of DFT coefficient, just $N$.

# Discrete Fourier Transform
We can further improve the formulation and state:
* given a finite length sequence composed of $N$ values, $s_n$ with $n=0,1,...,N-1$. We can calculate the Discrete Fourier Transform
	$$S_f = \sum_{n=0}^{N-1}s_ne^{j\frac{2\pi f}Nn}$$
with $f=0,1,...,N-1$
* we divide by $N$ to normalize the scale. As said before we take into account the fundamental frequency and its harmonic. Without the normalization factor their magnitude would be scaled by $N$,
	* fundamental frequency would have a magnitude $N$
	* the second harmonic would have magnitude $2N$
	* so on..
* those do not represent the actual amount of each frequency in the signal, instead they are artificially boosted by a component $N$
Furthermore, the anti-transform, capable of returning the temporal series of samples $s_n$, is defined as:
$$s_n=\frac1N\sum_{f=0}^{N-1}S_fe^{j2\pi f\frac nN}$$
The computational complexity of the Discrete Fourier Transform is $O(N^2$) with $N$ being the data set of samples. We can have a faster version called the [[Fast Fourier Transform]] reducing the complexity to $O(Nlog_2N)$


## Computing the DFT
Given 
$$
s(t)=\begin{cases} 
	1 \hspace{0.4cm} if \hspace{0.2cm} n=0,1,2,3 \\ 
	0 \hspace{0.4cm} if \hspace{0.2cm} n=4,5,6,7 \\
\end{cases}
$$
Having $N=8$ samples the computation of DFT is:
1) Calculate the formula of the summation for a generic $f$.
2) For all the $f\in[0,N-1]$ plug the value and calculate their amplitude

The result is as follow:
![[Pasted image 20230613112950.png]]
**Note that the calculation of $S_2$ and the other even frequencies are not reported, equaling to 0.** 
Further more the amplitude of the DFT can be seen here as follows:

![[Pasted image 20230613113140.png]]