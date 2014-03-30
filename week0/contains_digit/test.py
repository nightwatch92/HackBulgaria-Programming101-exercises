import unittest
import solution

class ContainDigitsTest(unittest.TestCase):
    """docstring for ContainDigitsTest"""
    def test_contains_digit(self):
        self.assertEqual(False, solution.contains_digit(222,3))
        self.assertEqual(False, solution.contains_digit(2224,1))
        self.assertEqual(False, solution.contains_digit(234,5))
        self.assertEqual(None, solution.contains_digit(0,13))
        self.assertEqual(True, solution.contains_digit(2220,0))
        self.assertEqual(False, solution.contains_digit(222,3))
    def test_zero_number(self):
        self.assertEqual(True, solution.contains_digit(-222,2))
        self.assertEqual(True, solution.contains_digit(-222,-2))




  
    # print(contains_digit(2244,1))
    # print(contains_digit(245,5))

if __name__ == '__main__':
    unittest.main()