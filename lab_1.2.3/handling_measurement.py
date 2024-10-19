from math import *


def GetValues (b):
    with open(b) as f:
        a = [float(i) for i in f.readline().split()]
    return a

def CountK():
    R = 0.115
    r = 0.0302
    l = 2.16
    z0 = sqrt(l * l - R * R)
    g = 9.81
    pi = 3.14

    return g * R * r / 4 / z0 / (pi * pi)

def CountIMeasury(T, M, m, k, I):
    return k * (m + M) * (sum(T) / len(T))**2 - I
def CountITeoretically(m, s, i):
    if i == 0:
        return m * 0.026**2 / 6
    elif i == 1:
        return m * s[1]**2 / 8
    elif i == 2:
        return m * s[2]**2 / 4
    else:
        return m * s[1]**2 / 8 + m * s[2]**2 / 4

weights = GetValues("weight.txt")
weights[len(weights) - 2] = sum(weights[len(weights) - 2: len(weights)])
del weights[len(weights) - 1]
weights = [i / 1000 for i in weights]
print("weights = ", weights, end = '\n')

sizes = GetValues("size.txt")
print("sizes = ", sizes, end = '\n')

periods = [0] * 4

periods[0] = GetValues('periods/vertical_rod.txt')
periods[1] = GetValues('periods/plate.txt')
periods[2] = GetValues('periods/hollow_cylinlder.txt')
periods[3] = GetValues('periods/pot.txt')

for i in range(len(periods)):
    print(periods[i], end = '\n')

k = CountK()
print("k = ", k, "\n")


T = 4.42
m = 1.0264
I0 = k * m * T * T
print("I(space} = ", I0, "\n")

I = [0] * 4
for i in range(len(I)):
    I[i] = CountIMeasury(periods[i], weights[i], m, k, I0)
print("I from measures = ", I, "\n")

I1 = [0] * 4
for i in range(len(I1)):
    I1[i] = CountITeoretically(weights[i], sizes, i)
print("I from teory = ", I1, "\n")






