PCM
===
PCM method is used to transfer an analog signal to a digital signal. This method includes three stages that show in the following figure:

<img src="/PCM Sampling/pcmdiag.png" width="653">

In the sampling stage, the analog signal is sampled every Ts second, where we call Ts sampling period and fs = 1 / Ts sampling frequency. For not losing data in the sampling stage, the sampling frequency should 2 times more than the largest frequency of the analog signal.

In the quantization stage the lower band and upper band of the signal are checked, then this interval divide into L states. Then every sample from the previous stage is mapped to the nearest state. In other words, each sample approximates to the previously specified states.

Finally, a specified code is assigned to each state. Every sample at the end presented with a bit string. Considering we have L state for quantization, for presenting each state we should use at least log2 L bits.

## Output
<img src="/PCM Sampling/pcm.png" width="640">