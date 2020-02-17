import numpy as np
import matplotlib.pyplot as plt

# time resulotion
r = 0.001

# Time span
t = np.arange(0, 2, r)
# Data signal
m_t = np.hstack((np.sin(np.pi * np.arange(0, 1, r)), -np.arange(1, 1.5, r) + 1, np.arange(1.5, 2, r) - 2))

# Carrier frequency
fc = 20
# AM modulated signal
x_t = m_t * np.cos(2 * np.pi * fc * t)

# SNR
snr_db = 10
# Calculate signal power and convert to dB 
x_t_watts = np.mean(x_t**2)
x_t_db = 10 * np.log10(x_t_watts)

# Calculate noise according to [2] then convert to watts
noise_db = x_t_db - snr_db
noise_watts = 10 ** (noise_db / 10)

# Generate AWGN noise
noise = np.random.normal(0.0, np.sqrt(noise_watts), len(x_t))
y_t = x_t + noise


fig, axs = plt.subplots(3)
fig.suptitle('AM Modulation')
axs[0].plot(t , m_t)
axs[1].plot(t , x_t)
axs[2].plot(t , y_t)

axs[0].set(ylabel='m(t)')    
axs[1].set(ylabel='x(t)')    
axs[2].set(xlabel='time (sec)', ylabel='x(t) + noise')    

# Hide x labels and tick labels for all but bottom plot.
for ax in axs:
    ax.label_outer()
    ax.grid()

plt.show()