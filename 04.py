from math import *


def z1(a):
    return round((sin(2 * a) + sin(5 * a) - sin(3 * a)) / (cos(a) - cos(3 * a) + cos(5 * a)), 5)


def z2(a):
    return round(tan(3 * a), 5)


print(z1(10))
print(z2(10))
