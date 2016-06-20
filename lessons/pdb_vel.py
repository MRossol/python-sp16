import numpy as np
import pdb

def y_fall(t, x0, v0):
    a = -9.8
    y = a*t**2 + v0*t + x0
    return y

v  = 2520 # m/s
x0 = 0    # m
t = np.arange(0,300,0.1) # s

pdb.set_trace()

print(y_fall(t, x0, v))