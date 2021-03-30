from numpy import linspace, cos, pi, ceil, floor, arange, sin, sinc
from pylab import plot, show, axis, subplot, errorbar
import matplotlib.pyplot as plt
import random
import numpy as np
import array

f = 1
fs = 10
'''
t = linspace(-1,1,100)
ts = arange(-1,1+1/fs,1/fs)
'''
t = linspace(-1,1,100)
ts = np.array([random.uniform(-1, 1 + 1 / fs)])

for i in range(1,fs):
    a = np.array([random.uniform(-1, 1 + 1 / fs)])
    ts = np.concatenate((ts,a))

wsp = len(ts)
s_rec = 0


for k in range(-wsp, wsp):
  s_rec = s_rec + sin(2 * pi * (k/fs)) * sinc(k - fs*t)


plot(t, s_rec, '--', t, sin(2 * pi * t), ts, sin(2 * pi * ts), 'o',t, (s_rec - sin(2 * pi * t)))
plt.show()