# Working with external libraries
import math # standard library
print('This is Math {}'.format(type(math)))
print(dir(math))
print('This is pi to 5 digits = {:.5}'.format(math.pi))
print(math.log(32,2))
help(math.log)
# Shorter naming of imorts
import math as mt
print(mt.pi)

# Refering from modules by themselves
from math import *
print(pi, log(32,5))

import numpy 
print("this ia a {}".format(type(numpy)))
print("it contains...",
      dir(numpy.random)[-15:]
      )

