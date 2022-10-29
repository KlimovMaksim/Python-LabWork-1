from math import *


def z1(x):
    return round((x**2 + 2*x - 3 + (x + 1)*sqrt(x**2 - 9)) / (x**2 - 2*x - 3 + (x - 1)*sqrt(x**2 - 9)), 5)


def z2(x):
    return round(sqrt((x + 3) / (x - 3)), 5)


if z1(10) == z2(10):
    print('Ok')