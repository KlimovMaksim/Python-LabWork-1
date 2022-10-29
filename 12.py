from math import *


def z1(a):
    return round((sin(4*a) * cos(2*a)) / ((1 + cos(4*a))*(1 + cos(2*a))), 5)


def z2(a):
    return round(1 / (tan(3/2*pi - a)), 5)