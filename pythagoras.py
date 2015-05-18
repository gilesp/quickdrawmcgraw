from math import acos

def cosineRule(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    top = a**2 + b**2 - c**2
    bottom = 2*a*b
    return acos(top/bottom)

def angleA(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    top = b**2 + c**2 - a**2
    bottom = 2*b*c
    return acos(top/bottom)
