AM Modulation
=============
In AM modulation data signal is placed in the envelope of a high-frequency sin signal. The high-frequency sin signal called carrier. After modulation, the envelope of sin signal will be in shape of the data signal. The output of AM modulation for a normalized data signal between (-1, +1) could be derived from the following formula:

<img src="https://render.githubusercontent.com/render/math?math=x(t)=m(t).cos(2\pi f_ct)"> 

In this relation, fc should be so larger than the bandwidth of the data signal.

To make our AM modulation more realistic we could add some noise to the final result with a specific SNR. We can use the following formula to calculate corresponding noise power for specific SNR.

<img src="https://render.githubusercontent.com/render/math?math=SNR=\dfrac{P_{signal}}{P_{noise}}"> 

or its equivalent in dB could be calculated as follows:

<img src="https://render.githubusercontent.com/render/math?math=SNR_{db}=P_{signal,dB}%20-%20P_{noise,dB}"> 

## Output
<img src="/AM Modulation/AM_modulation.png" width="640">
