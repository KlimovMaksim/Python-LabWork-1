from math import *


def z1(x, y):
    return round(cos(x)**4 + sin(y)**2 + 1/4*sin(2*x)**2 - 1, 5)


def z2(x, y):
    return round(sin(x + y)*sin(y - x), 5)