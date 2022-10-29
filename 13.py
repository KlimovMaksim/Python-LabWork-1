from math import *


def z1(a, b):
    return round((sin(a) + cos(2*b -a)) / (cos(a) - sin(2*b - a)), 5)


def z2(a, b):
    return round((1 + sin(2*b)) / (cos(2*b)), 5)