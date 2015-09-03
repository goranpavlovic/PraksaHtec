__author__ = 'vladimir'

import math
import numpy as np
import scipy as sc
import matplotlib.pyplot as pl

# First function - SINUSOID
left = -0
right = 50

xs = np.arange(left, right, 0.1)
ys = np.cos(2*xs + math.pi/15)

# Second function - EXPONENTIAL

xe = np.arange(left, right, 0.1)
ye = np.exp(-xe/10)

# Third Function - ENVELOPE

ya = ys*ye

# Plot

font = {'size': 22}

pl.title('Envelope function', **font)
pl.grid()
pl.plot(xs, ya)
pl.hold(True)
pl.plot(xe, ye, '-', color='red')
pl.plot(xe, -ye, '-', color='red')

pl.savefig('envelope.png')
pl.hold(False)
pl.show()












