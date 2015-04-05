from math import acos, atan2, degrees, sqrt

class Kinematics(object) :

    def __init__(self, m1x, m1y, m2x, m2y, l1, l2, r1, r2):
        self.m1x = float(m1x)
        self.m1y = float(m1y)
        self.m2x = float(m2x)
        self.m2y = float(m2y)
        self.l1 = float(l1)
        self.l2 = float(l2)
        self.r1 = float(r1)
        self.r2 = float(r2)

    def computeAngles(self, x, y):
        m1angle = self._motorAngle(x - self.m1x, y - self.m1y, self.l1, self.l2)
        m2angle = self._motorAngle(x - self.m2x, y - self.m2y, self.r1, self.r2)
        return (m1angle, m2angle)

    def _motorAngle(self, dx, dy, l1, l2):
        c = sqrt(dx**2 + dy**2)
        a1 = atan2(dy, dx)
        a2 = self._cosinerule(l1, l2, c)
        angle = degrees(a1 + a2) - 90
        return angle

    def _cosinerule(self, a, b, c):
        return acos(((b**2 + c**2) - a**2) / (2 * b * c))


if __name__ == "__main__":
    k = Kinematics(66, -25,  159, -26, 111, 110, 114, 111)
    (angle1, angle2) = k.computeAngles(200, 100)
    print "angle1 = " + str(angle1)
    print "angle2 = " + str(angle2)
