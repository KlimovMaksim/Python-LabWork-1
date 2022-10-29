from math import *


def z1(b):
    return round((sqrt(2*b + 2*sqrt(b**2 - 4))) / (sqrt(b**2 - 4) + b + 2), 5)


def z2(b):
    return round(1 / sqrt(b + 2), 5)