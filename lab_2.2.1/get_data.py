import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import *
def get_data(name):
    with open (name + '.csv', 'r') as file:
        reader = csv.reader(file)
        xy = [i for i in reader]

    return xy


filenames = ['data_40', 'data_80', 'data_120', 'data_160']
linenames = [f'p = {i} торр' for i in [40, 80, 120, 160]]
xy = [0] * 4
name_x = [0] * 4
name_y = [0] * 4
for i in range(4):
    xy[i] = get_data(filenames[i])
    
name_x = xy[0][0]
name_y = xy[0][1]
print(name_x)

xy = [i[1:] for i in xy]

x  = [0] * 4
y  = [0] * 4
coeffs = [0] * 4
y_fit = [0] * 4

f = open("graph_inf.txt", "w")

col = ['green', 'blue', 'red', 'orange']
for i in range(4):
    x = [float(j[0]) for j in xy[i]]
    y = [float(j[1]) for j in xy[i]]

    u0 = y[0]
    y = [-log(j / u0) for j in y]
    
    x_mid = sum(x)/len(x)
    y_mid = sum(y)/len(y)
    x_2_mid = sum(j*j for j in x)/len(x)
    y_2_mid = sum(j*j for j in y)/len(y)

    # Perform curve fitting
    #params, covariance = curve_fit(linear_func, x, y)
    #slope, intercept = params
    #slope_error = np.sqrt(np.diag(covariance))[0]  # Standard deviation of the slope

    coeffs = np.polyfit(x, y, 1)
    slope_err = sqrt(1/len(x)) * sqrt((y_2_mid - y_mid**2)/(x_2_mid - x_mid**2) - int(coeffs[0]))
    
    print(f'coeffs{i} = ', coeffs)
    
    y_fit = np.polyval(coeffs, x)
    plt.plot(x, y_fit, color=col[i], label=linenames[i])
  
    #str_slope = ' slope = ' + str(slope)
    #str_intercept = ' intercept = '+ str(intercept)
    #str_slope_error = ' slope_error = ' + str(slope_error)
    str_coeffs = ' coeffs = ' + str(coeffs)
    slope_err = ' slope_err = ' + str(slope_err)
    s = str(i) + str_coeffs + slope_err + '\n'
    f.write(s)
    
f.close()

    
plt.ylabel('ln(U0/U)')
plt.xlabel('t, c')
plt.title('График ln(U0/U(t))')

plt.xlim(0, 600)
plt.ylim(0, 1)

plt.legend()
plt.savefig('graph')

plt.grid()
plt.show()
        
