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
    print("M = ", M, "midT = ", sum(T) / len(T))
    print("periods = ", T)
    print("weights = ", M)
    return k * (m + M) * (sum(T) / len(T))**2 - I


weights = GetValues("weight.txt")
weights[len(weights) - 2] = sum(weights[len(weights) - 2: len(weights)])
del weights[len(weights) - 1]
weights = [i / 1000 for i in weights]
print("weights = ", weights, end = '\n')

sizes = GetValues("size.txt")
sizes = [i / 100 for i in sizes]
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
I1[0] = weights[0] * 0.026**2 / 6
I1[1] = weights[1] * sizes[1] ** 2 / 8
I1[2] = weights[2] * sizes[2] ** 2 / 4
I1[3] = I1[1] + I1[2]
print("I from theory = ", I1, "\n")


# for horizontal rod

t = GetValues("periods\horizontal_rod.txt")
i = weights[0] * (0.026**2 + 0.208**2) / 12
print("th = ", i, "exp = ", k * weights[0] * (sum(t) / len(t)))






