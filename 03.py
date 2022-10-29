from math import *


def z1(a):
    return round((sin(2 * a) + sin(5 * a) - sin(3 * a)) / (cos(a) + 1 - 2 * (sin(2 * a) ** 2)), 5)


def z2(a):
    return round(2 * sin(a), 5)