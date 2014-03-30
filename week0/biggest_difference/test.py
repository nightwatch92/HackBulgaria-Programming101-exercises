import unittest
import solution

class BiggestDifferenceTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_biggest_difference(self):
        self.assertEqual(-99,solution.biggest_diffarance(range(100)))
        self.assertEqual(0,solution.biggest_diffarance([1,1,1,1]))
        self.assertEqual(0,solution.biggest_diffarance([3,3,3,3]))
        self.assertEqual(0,solution.biggest_diffarance([0,0,0,0,0]))

    def test_biggest_diffarance_negative(self):
        self.assertEqual(-9,solution.biggest_diffarance([-10, -9, -1]))
        self.assertEqual(-42,solution.biggest_diffarance([-3, -45, -22]))
        self.assertEqual(-18,solution.biggest_diffarance([-13, -23, -31]))
        self.assertEqual(-88,solution.biggest_diffarance([-50, -91, -3]))

    # def test_consonants_upper_case(self):
        # self.assertEqual(3311,solution.biggest_diffarance([3,3,1,1]))

if __name__ == '__main__':
    unittest.main()