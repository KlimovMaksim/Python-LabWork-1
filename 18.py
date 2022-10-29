from math import *


def z1(a):
    return round(((a + 2) / sqrt(2*a) - a / (sqrt(2 * a) + 2) + 2 / (a - sqrt(2*a))) * ((sqrt(a) - sqrt(2)) / (a + 2)), 5)


def z2(a):
    return round(1 / (sqrt(a) + sqrt(2)), 5)