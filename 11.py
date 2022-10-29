from math import *


def z1(a):
    return round((1 - 2 * sin(a)**2) / (1 + sin(2 * a)), 5)


def z2(a):
    return round((1 - tan(a)) / (1 + tan(a)), 5)