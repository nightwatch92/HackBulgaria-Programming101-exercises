import unittest
import solution

class IsDecreasingTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_decreasing(self):
        self.assertEqual(False,solution.is_decreasing(range(100)))
        self.assertEqual(True,solution.is_decreasing(range(-1, -20, -1 )))
        self.assertEqual(True,solution.is_decreasing(range(-1, 100, -1 )))
        self.assertEqual(True,solution.is_decreasing(range(-1,-20,-1 )))
        self.assertEqual(True,solution.is_decreasing([1]))
        self.assertEqual(False,solution.is_decreasing([3,3,3,3]))
        self.assertEqual(False,solution.is_decreasing([0,0,0,0,0]))
        self.assertEqual(False,solution.is_decreasing([5,6,-10]))
        
if __name__ == '__main__':
    unittest.main()