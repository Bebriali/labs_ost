def GetValues (b):
    with open(b) as f:
        a = [float(i) for i in f.readline().split()]
    return a


delta_size = 0.005
delta_values = GetValues("delta.txt")
exp_quantity = len(delta_values)
delta_values = [i * delta_size for i in delta_values]

periods = exp_quantity * [0]

with open("periods.txt") as file:
    periods = [[float(j) for j in l.split()] for l in file]

print(delta_values)
print(periods)


m = 1.5268
d_m = 1e-4

I0 = 0.00807
k = 0.0004023
d_k = 1.9e-9
m0 = 1.0264
d_m0 = 1e-4

I = [0] * exp_quantity
h2 = [0] * exp_quantity
for i in range(exp_quantity):
    I[i] = k * (m + m0) * (sum(periods[i]) / len(periods[i]))**2 - I0
    h2[i] = delta_values[i]**2

print(h2)
print(I)

import matplotlib
import math
import numpy as np
from statistics import mean
from matplotlib import pyplot as plt

def mnk(x, y):
    xy = []
    xx = []
    yy = []
    for i in range(0, len(x)):
        xy.append(x[i]*y[i])
        xx.append(x[i]**2)
        yy.append(y[i]**2)

    b = (mean(xy)-mean(x)*mean(y))/(mean(xx)-mean(x)**2)
    a = mean(y) - b * mean(x)

    sb = 1/math.sqrt(len(x))*math.sqrt((mean(yy)-mean(y)**2)/(mean(xx)-mean(x)**2)-b**2)
    sa = sb * math.sqrt(mean(xx)-mean(x)**2)

    return a,b,sa,sb

a,b,sa,sb = mnk(h2, I)
plt.plot([0, 0.05**2], [a, a + b * 0.05**2], color = "r")
print("I1: ", I)

print("a =", a)
print("b =", b)
print("sa =", sa)
print("sb =", sb)

#a,b,sa,sb = mnk(h2, I2)
#plt.plot([0, 0.05**2], [a, a + b * 0.05**2])
#print("I2: ", I1)

#print("a =", a)
#print("b =", b)
#print("sa =", sa)
#print("sb =", sb)

plt.xlabel("h²")
plt.ylabel("I")


plt.scatter(h2, I)
#$plt.scatter(h2, I2)
plt.grid()
plt.show()
