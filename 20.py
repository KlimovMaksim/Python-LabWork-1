from math import *


def z1(m, n):
    return round(((m - 1)*sqrt(m) - (n - 1)*sqrt(n)) / (sqrt((m**3)*n) + n*m + m**2 - m), 5)


def z2(m, n):
    return round((sqrt(m) - sqrt(n)) / m, 5)