from math import acos, cos, sin, degrees

x = 4.0
y = 3.0
la = 5.0
lb = 5.0

x2 = x**2
y2 = y**2
la2 = la**2
lb2 = lb**2



print "x = " + str(x)
print "y = " + str(y)
print "la = " + str(la)
print "lb = " + str(lb)
print "x^2 = " + str(x2)
print "y^2 = " + str(y2)
print "la^2 = " + str(la2)
print "lb^2 = " + str(lb2)

top = x2 + y2 -la2 -lb2
bottom = 2 * la * lb

print "top = " + str(top)
print "bottom = " + str(bottom)

inner = top/bottom

print "inner = " + str(inner)

angle2 = acos(inner)

print "angle2 = " + str(degrees(angle2))

sinAngle2 = sin(angle2)
cosAngle2 = cos(angle2)
topLeft = (lb * sinAngle2) * x
topRight = (la + lb * cosAngle2) * y
top = -topLeft + topRight

print "top = " + str(top)

bottomLeft = (lb * sinAngle2) * y
bottomRight = (la + lb * cosAngle2) * x
bottom = bottomLeft + bottomRight

print "bottom = " + str(bottom)

angle1 = top / bottom

print "angle1 = " + str(degrees(angle1))
