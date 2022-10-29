from math import *


def z1(a, b):
    return round((cos(a) - cos(b))**2 - (sin(a) - sin(b))**2, 5)


def z2(a, b):
    return round(-4*(sin((a-b)/2)**2)*cos(a+b), 5)