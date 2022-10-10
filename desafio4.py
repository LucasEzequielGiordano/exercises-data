import numpy as np
import matplotlib.pyplot as plt

n = 101

X = np.linspace(-1, 1, n)
Y = np.absolute(X)
plt.plot(X,Y)
plt.show()