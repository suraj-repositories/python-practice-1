# module = a file containing code you want to include in your protram
#         use 'import' to include a module (built-in or your own)
#         useful to break up a large program reuseable separate files

# FOR HELP ABOUT MODULE FUNTIONS
# print(help("modules"))

import math
import math as m
from math import e 

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)
print("----------------------")

# --------------------- Using my own module --------------------------

import myModule

print(myModule.pi)

print(myModule.square(5))

print(myModule.cube(3))