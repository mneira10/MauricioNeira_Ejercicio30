import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('serial.dat')
plt.hist(data,label='serial',alpha = 0.7,bins=30)
data = np.loadtxt('parallel.dat')
plt.hist(data,label='parallel',alpha=0.7,bins=30)
plt.legend()
plt.savefig('compare.pdf')