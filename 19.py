from math import *


def z1(a):
    return round((((1 + a + a**2) / (2*a + a**2) + 2 - (1 - a + a**2) / (2*a - a**2))**-1) *
                 (5 - 2*(a**2)), 5)


def z2(a):
    return round((4 - a**2) / 2, 5)