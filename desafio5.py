import matplotlib.pyplot as plt
import numpy as np
import math

n = 100
x = np.linspace(-5,5,n)
gaussiana = np.exp(-x**2/2) 

plt.plot(x, gaussiana)
plt.show()