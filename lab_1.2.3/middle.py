from math import *

def GetValues (b):
    with open(b) as f:
        a = [float(i) for i in f.readline().split()]
    return a


print("'middle value and middle sigma calculator'")
print("enter the path to the file with the values")
path = input()
values = GetValues(path)
mid_value = sum(values) / len(values)
delta = [0] * len(values)

for i in range(len(delta)):
    delta[i] = mid_value - values[i]
    delta[i] **= 2

sigma = sqrt(sum(delta) / len(delta) / (len(delta) - 1))

print("middle value = ", mid_value)
print("sigma middle = ", sigma)
print("epsilon = ", sigma / mid_value * 100, "%")