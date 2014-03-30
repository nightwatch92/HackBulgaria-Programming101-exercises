import unittest
import solution

class WhatIsTheSign(unittest.TestCase):
    """docstring for TheSign"""

    def test_the_sign(self):
        self.assertEqual("Aquarius", solution.what_is_my_sign(10, 2))
        self.assertEqual("Leo", solution.what_is_my_sign(15, 8))
        self.assertEqual("Pisces", solution.what_is_my_sign(21, 2))

if __name__ == '__main__':
    unittest.main()
