import unittest
import solution

class PrimeFactorizationTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_factorization(self):
        self.assertEqual([(2, 1), (5, 1)],solution.prime_factorization(10))
        self.assertEqual([(2, 1), (7, 1)],solution.prime_factorization(14))
        self.assertEqual([(2, 2), (89, 1)],solution.prime_factorization(356))
        self.assertEqual([(2, 3), (5, 3)],solution.prime_factorization(1000))
        self.assertEqual([(89,1)],solution.prime_factorization(89))
        self.assertEqual([(2, 2), (2731, 1)],solution.prime_factorization(10432420))
if __name__ == '__main__':
    unittest.main()