from math import *


def z1(m):
    return round(((3*m + 2)**2 - 24*m) / (3*sqrt(m) - 2/sqrt(m)), 5)


def z2(m):
    return round(-sqrt(m), 5)


print(z1(10))
print(z2(10))