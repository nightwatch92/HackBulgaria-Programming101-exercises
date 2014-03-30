import solution
import unittest

class TestFibonacci(unittest.TestCase):
    """docstring for TestFibonacci"""

    def test_fibonacci(self):
        
        self.assertEqual(28657, solution.nth_fibonacci(23))
        self.assertEqual(55, solution.nth_fibonacci(10))

    def test_fibonacci_negative_number(self):
        
        self.assertEqual(None, solution.nth_fibonacci(-10))



if __name__ == '__main__':
    unittest.main()