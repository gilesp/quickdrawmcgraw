import unittest
from math import degrees
from pythagoras import cosineRule, angleA

class TestPythagoras(unittest.TestCase):

    def setUp(self):
        pass

    def test_cosineRule_2_3_4(self):
        angle = cosineRule(2, 3, 4)
        angle_as_string = "{0:.2f}".format(angle)
        self.assertEqual(angle_as_string, "1.82")

    def test_cosineRule_5_6_8(self):
        angle = cosineRule(5, 6, 8)
        angle_as_string = "{0:.2f}".format(angle)
        self.assertEqual(angle_as_string, "1.62")

    def test_cosineRule_111_110_180(self):
        angle = cosineRule(111, 110, 180)
        angle_as_string = "{0:.2f}".format(angle)
        self.assertEqual(angle_as_string, "1.90")

    def test_cosineRule_equals_angleA(self):
        self.assertEquals(angleA(4, 2, 3), cosineRule(2, 3, 4))

    def test_interior_angles_equal_180(self):
        a = 2
        b = 3
        c = 4
        A = angleA(2, 3, 4)
        B = angleA(3, 4, 2)
        C = angleA(4, 2, 3)
        totalInRads = A + B + C
        self.assertEquals(degrees(totalInRads), 180)

if __name__ == '__main__':
    unittest.main()
