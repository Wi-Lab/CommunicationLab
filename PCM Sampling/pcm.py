import numpy as np
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx

def analogueSignal(t):
    f = 1
    return np.sin(2 * np.pi * f * t)

# Sampling frequency
fs = 32
# Code length
nb = 3

# time resulotion for analogue signal
r = 0.001

# Time span
t = np.arange(0, 2, r)
# Data signal
x_t = analogueSignal(t)
# Sampling Time span
Ts = np.arange(0, 2, 1.0/fs)
# Quantized Signal
x_tq = []

# Analogue signal min amplitude
Vmin = np.min(x_t)
# Analogue signal max amplitude
Vmax = np.max(x_t)
# Quantization level count
L = 2 ** nb
# Quantized levels
QLevels = np.arange(Vmin, Vmax, (Vmax-Vmin)/L)
# Binary code list
QBcodelist = []
QBcode = ''
for l in range (L):
    QBcodelist.append(bin(l)[2:].zfill(3))

# Sampling and Quantization
for ts in Ts:  
    Qvalue, Qindex = find_nearest(QLevels, analogueSignal(ts))
    x_tq.append(Qvalue)
    QBcode +=  QBcodelist[Qindex]

print(QBcode)
# Draw x_t and x_ts plots
plt.plot(t, x_t)
plt.step(Ts, x_tq)
plt.xlabel('time(sec)')
ax = plt.gca()
ax.yaxis.grid(linestyle='-.')
plt.show()