__author__ = 'vladimir'

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(-30, 30)
y = np.sin(2*x + 1)*np.exp(x/100)
f = interpolate.interp1d(x, y)
xnew = np.arange(-9, 9, 0.01)
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()
plt.savefig('plot_image.png')
# plt.interactive(False)

