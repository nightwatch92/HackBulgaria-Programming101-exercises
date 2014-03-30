import unittest
import solution

class ContainDigitsTest(unittest.TestCase):
    """docstring for ContainDigitsTest"""
    def test_contains_digit(self):
        self.assertEqual(2, solution.count_substrings("This is a test string","is"))
        self.assertEqual(2, solution.count_substrings("babababa", "baba"))
        self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))
        self.assertEqual(1, solution.count_substrings("Python is an awesome language to program in!", "prog"))
        self.assertEqual(23, solution.count_substrings("Pyth,,,,,,,,,,,,,,,,,,,,,,,rogram in!", ","))

# 	print(count_substrings("This is a test string", "is"))
# 	print(count_substrings("babababa", "baba"))
# 	print(count_substrings("Python is an awesome language to program in!", "o"))

if __name__ == '__main__':
	unittest.main()