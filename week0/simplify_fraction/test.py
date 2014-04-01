import solution
import unittest
from fractions import *


class FractionTest(unittest.TestCase):
    """docstring for FractionTest"""

 #    def test_fractions(self):
 #        self.assertEqual(Fraction(1, 3)
 # ,solution.simplify_fraction((3,9)))
    def test_fractions(self):
        self.assertEqual((1,3), solution.simplify_fraction((3,9)))
        self.assertEqual((1,7), solution.simplify_fraction((1,7)))
        self.assertEqual((2,5), solution.simplify_fraction((4,10)))
        self.assertEqual((3,22), solution.simplify_fraction((63,462)))
        self.assertEqual((1,5), solution.simplify_fraction((3,15)))
        self.assertEqual((1071,11), solution.simplify_fraction((3213,33)))

if __name__ == '__main__':
    unittest.main()