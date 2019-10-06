import math
from numpy import isclose
a=3
if math.sqrt(a)**2 !=a:
    print("WTH??")
to1=1e-10
if abs(math.sqrt(a)**2-a) > to1:
    print("WTH again!?")
if isclose(math.sqrt(a)**2,a):
    print("Close enough!")