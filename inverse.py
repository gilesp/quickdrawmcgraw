from math import acos, atan, degrees, sqrt

a = float(5)
b = float(5)

x = float(1)
y = float(5)

c = sqrt(x**2 + y**2)

print "c: " + str(c)

angle2 = degrees(acos((a**2 + b**2 - c) / (2 * a * b)))

print "atan(y/x) "+ str(atan(y/x))
print "acos... " + str(acos(((a**2) - (b**2)) + c / ((2 * a) * c)))

angle1 = degrees(atan(y/x) + acos(((a**2) - (b**2)) + c / ((2 * a) * c)))

print "angle1 = " + str(angle1)
print "angle2 = " + str(angle2)

angle2inv = 180 - angle2

print "angle2inv = " + str(angle2inv)
