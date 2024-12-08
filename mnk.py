
import matplotlib
import math
import numpy as np
from statistics import mean
from matplotlib import pyplot as plt
from matplotlib.ticker import NullLocator, IndexLocator, MaxNLocator

def GetValues (b):
    with open(b) as f:
        a = [float(i) for i in f.readline().split()]
    return a

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


print("enter the values name : ")
name = input()

print("enter the pathy : ")
pathy = input()
print("enter the filenamey : ")
filenamey = input()

print("enter the pathx : ")
pathx = input()
print("enter the filenamex : ")
filenamex = input()

Oy = GetValues(pathy + '/' + filenamey + '.txt')
Ox = GetValues(pathx + '/' + filenamex + '.txt')
a, b, sa, sb = mnk(Ox, Oy)


mn = 0.5
fig = plt.figure(figsize = (16 * mn, 9 * mn))
ax = fig.add_subplot()

ax.set_xlim(xmin = 0, xmax = max(Ox) + 2 * min(Ox))
ax.set_ylim(ymin = 0, ymax = max(Oy) + 2 * min(Oy))

ax.minorticks_on()
ax.grid(which = 'major', lw = 2)
ax.grid(which = 'minor')
lc = NullLocator()
ax.xaxis.set_major_locator(MaxNLocator(10))
ax.xaxis.set_minor_locator(MaxNLocator(50))
ax.yaxis.set_minor_locator(MaxNLocator(50))

plt.scatter(Ox, Oy)

plt.plot([0, len(Oy)], [a, a + b * len(Oy)], color = "r")
print(name + ": ", Oy)

print("a =", a)
print("b =", b)
print("sa =", sa)
print("sb =", sb)

print('Ox = ', Ox)

mid_f = [Oy[i] / Ox[i] for i in range(len(Oy))]
print('mid_f = ', mid_f)

plt.xlabel("harmonic number")
plt.ylabel(name)

plt.savefig(pathy + '/' + filenamey + '_graph.png')
plt.show()

