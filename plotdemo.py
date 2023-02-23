import matplotlib.pyplot as plt
import numpy as np

f = np.sin
x = np.arange(0, 2*np.pi, .1)
x_0 = 5
f0 = np.sin(x_0)
f1 = (x - x_0)*np.cos(x_0)
f2 = 1/2*(x - x_0)**2 * (-np.sin(x_0))

plt.plot(x, f(x), label='sin(x)')
plt.plot(x, f0 + f1, label='linear approx')
plt.plot(x, f0 + f1 + f2, label='quadratic approx')
plt.legend()
plt.show()