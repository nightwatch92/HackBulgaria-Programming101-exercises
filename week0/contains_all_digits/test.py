import unittest
import solution

class ContainAllDigitsTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_digits_contain(self):

        self.assertEqual(True,solution.contains_digits(64305, [6, 4, 3, 3, 3, 5]))
        self.assertEqual(True,solution.contains_digits(402123, [0, 3, 4]))
        self.assertEqual(False,solution.contains_digits(666, [6, 4]))
        self.assertEqual(False,solution.contains_digits(123456789, [1, 2, 3, 0]))
        self.assertEqual(True,solution.contains_digits(123456789, []))
        self.assertEqual(True,solution.contains_digits(123456789, [1,1,1,2]))

if __name__ == '__main__':
    unittest.main()