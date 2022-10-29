from math import *


def z1(a):
    return round(cos(a) + sin(a) + cos(3 * a) + sin(3 * a), 5)


def z2(a):
    return round(2 * sqrt(2) * cos(a) * sin((pi / 4) + 2 * a), 5)