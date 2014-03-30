import unittest
import solution

class SlopeStyleTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_slope_style(self):
        self.assertEqual(94.67,solution.slope_style([94, 95, 95, 95, 90]))
        self.assertEqual(73.5,solution.slope_style([95,100,31,52]))
        self.assertEqual(80.0,solution.slope_style([60, 70, 80, 90, 100]))
        self.assertEqual(93.5,solution.slope_style([96, 95.5, 93, 89, 92]))
        self.assertEqual(93.42,solution.slope_style([33, 95.5, 93.4233]))



    # def test_biggest_diffarance_negative(self):
    #     self.assertEqual(-9,solution.slope_style([-10, -9, -1]))
    #     self.assertEqual(-42,solution.slope_style([-3, -45, -22]))
    #     self.assertEqual(-18,solution.slope_style([-13, -23, -31]))
    #     self.assertEqual(-88,solution.slope_style([-50, -91, -3]))

if __name__ == '__main__':
    unittest.main()