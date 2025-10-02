import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, IndexLocator, MaxNLocator

multiply = 0.75 / 150 * 1e3
print(multiply)

lengths_num = 3

u_del = [0] * lengths_num
u_del[0] = [0, 27, 32, 37, 43, 56, 79, 94]
u_del[1] = [0, 39, 48, 61, 82, 125, 140, 139]
u_del[2] = [0, 62, 69, 78, 84, 99, 115, 145]

u_v = [0] * lengths_num
for i in range(lengths_num):
    u_v[i] = [j * multiply for j in u_del[i]]

for i in range(lengths_num):
    print(u_del[i])
    print(u_v[i])

i_ma = [0] * lengths_num
i_ma[0] = [0, 67.27, 78.39, 91.54, 106.74, 138.44, 197.12, 233.24]
i_ma[1] = [0, 65.0, 80.75, 101.87, 136.88, 209.20, 233.20, 232.85]
i_ma[2] = [0, 62.71, 69.65, 78.08, 84.7, 99.40, 115.3, 145.59]


col = ['r', 'c', 'm']

mn = 1

fig = plt.figure(figsize = (16 * mn, 9 * mn))
ax = fig.add_subplot()

for i in range(lengths_num):
    y = np.array(u_v[i])
    x = np.array(i_ma[i])
    ax.plot(x, y, col[i] + '-', marker = '.', linewidth = 1)
    

ax.set_xlim(xmin = 0, xmax = 250)
ax.set_ylim(ymin = 0, ymax = 800)

ax.minorticks_on()
ax.grid(which = 'major', lw = 2)
ax.grid(which = 'minor')
lc = NullLocator()
ax.xaxis.set_major_locator(MaxNLocator(10))
ax.xaxis.set_minor_locator(MaxNLocator(50))
ax.yaxis.set_minor_locator(MaxNLocator(50))

plt.xlabel('I, mA')
plt.ylabel('U, mV')
plt.legend(loc = 'best', fontsize = 12)

#plt.set(xlim = (0, 350), ylim = (0, 850))


plt.show()
