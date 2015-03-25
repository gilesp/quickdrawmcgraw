from math import acos, atan, degrees, sqrt

class Kinematics(object) :

    def __init__(self, arm1Length, arm2Length):
        self.a = float(arm1Length)
        self.b = float(arm2Length)

    def computeAngles(self, x, y):
        x = float(x)
        y = float(y)
        c = x**2 + y**2
        angle1 = self._computeAngle1(x, y, c)
        angle2 = self._computeAngle2(x, y, c)
        return (angle1, angle2)

    def _computeAngle2(self, x, y, c):
        top = ((self.a**2) + (self.b**2) - c)
        bottom = (2 * self.a * self.b)
        return degrees(acos(top / bottom))

    def _computeAngle1(self, x, y, c):
        rads = atan(y/x) + acos(abs(((self.a**2) - (self.b**2)) + c) / ((2 * self.a) * c))
        return degrees(rads)


if __name__ == "__main__":
    print "X = 200"
    print "Y = 100"
    k = Kinematics(247, 285)
    (angle1, angle2) = k.computeAngles(200, 100)
    print "angle1 = " + str(angle1)
    print "angle2 = " + str(angle2)
