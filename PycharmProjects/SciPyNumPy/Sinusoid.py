__author__ = 'vladimir'

import math
import numpy as np
import matplotlib.pyplot as pl
from PIL import Image, ImageFilter

xe = np.arange(0, 100, 0.1)


def func_draw(x):
    colors = ['#eeefff', '#ee45ff', '#00ef4f', '#eaaa45', '#785274', '#ab14df', '#7896ff',
              '#000045', '#7844aa', '#221100', '#cc78bb', '#eeefff', '#eeefff', '#eeefff',
              '#951200', '#aaafff', '#eeaabb', '#12021f', '#ee4512', '#ccddcc', '#001236']
    pl.hold(True)
    pl.grid()
    for i in range(1, 20):
        y = 0.1*np.cos(x/10 + math.pi/i)
        pl.plot(x, y, colors[i])
    pl.savefig('Sinusoid')


func_draw(xe)

original = Image.open("RUYST_1.jpg")  # load an image from the hard drive
# blurred = original.filter(ImageFilter.BLUR)  # blur the image

original.show()  # display both images
# blurred.show()

