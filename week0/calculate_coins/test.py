#calculate_coins.py
import unittest
import solution

class CoinsTest(unittest.TestCase):
    """docstring for CoinsTest"""

    def test_coins(self):
        self.assertEqual({1: 0, 50: 0, 20: 2, 5: 1, 100: 3, 10: 0, 2: 0}
,solution.calculate_coins(3.45))
        self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}
,solution.calculate_coins((0.53)))
        self.assertEqual({1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}
,solution.calculate_coins(8.94))

if __name__ == '__main__':
    unittest.main()
