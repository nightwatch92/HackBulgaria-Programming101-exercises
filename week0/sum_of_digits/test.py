import unittest
import solution

class SumOfDigitsTest(unittest.TestCase):
    """docstring for SumOfDigitsTest"""

    def test_negative_number(self):
        self.assertEqual(4,solution.f_sum(--4000))
        
    def test_for_sum(self):
        self.assertEqual(14,solution.f_sum(1241231))


if __name__ == '__main__':
    unittest.main()