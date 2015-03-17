from math import acos, cos, sin

class Kinematics(object) :

    def __init__(self, arm1Length, arm2Length):
        self.length1 = arm1Length
        self.length2 = arm2Length

    def computeAngles(self, x, y):
        angle2 = self._computeAngle2(x, y)
        angle1 = self._computeAngle1(x, y, angle2)
        return (angle1, angle2)

    def _computeAngle2(self, x, y):
        print (x**2 + y**2 - self.length1**2 - self.length2**2)
        print (2 * self.length1 * self.length2)
        return acos((x**2 + y**2 - self.length1**2 - self.length2**2) / (2 * self.length1 * self.length2))

    def _computeAngle1(self, x, y, theta):
        cosTheta = cos(theta)
        sinTheta = sin(theta)
        totalLength = self.length1 + self.length2
        top = -((self.length2 * sinTheta) * x) + ((totalLength * cosTheta) * y)
        bottom = ((self.length2 * sinTheta) * y) + ((totalLength * cosTheta) * x)
        return top / bottom

if __name__ == "__main__":
    print "X = 10"
    print "Y = 10"
    k = Kinematics(5, 5)
    (angle1, angle2) = k.computeAngles(10, 10)
    print "angle1 = " + angle1
    print "angle2 = " + angle2
