import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load data from CSV file
data = pd.read_excel('p(t).xlsx')
print("len data = ", len(data))
print(data[1])
for i in range(1, len(data)):
    print("data[", i, "] = ", data[i])
# Convert columns to numeric, forcing errors to NaN
p = pd.to_numeric(data.iloc[:, 0], errors='coerce')  # First column for p
t = pd.to_numeric(data.iloc[:, 1], errors='coerce')  # Second column for t

# Drop any rows with NaN values
valid_data = pd.DataFrame({'t': t, 'p': p}).dropna()
t = valid_data['t']
p = valid_data['p']

if p[0] == 'P':
    p = p[1:]
    t = t[1:]
elif p[0] == 't':
    u = p
    p = t[1:]
    t = u[1:]
    
with open ("data2_p.txt") as f:
    for i in range(len(p)):
        f.write(p[i], " ", endl = '')
with open ("data2_t.txt") as f:
    for i in range(len(t)):
        f.write(p[i], " ", endl = '')
