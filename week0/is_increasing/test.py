import unittest
import solution

class IsIncreasingTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_increasing(self):
        self.assertEqual(True,solution.is_increasing(range(100)))
        self.assertEqual(False,solution.is_increasing(range(-1, -20, -1 )))
        self.assertEqual(True,solution.is_increasing(range(-1, 100, -1 )))
        self.assertEqual(False,solution.is_increasing(range(-1,-20,-1 )))
        self.assertEqual(True,solution.is_increasing([1]))
        self.assertEqual(False,solution.is_increasing([3,3,3,3]))
        self.assertEqual(False,solution.is_increasing([0,0,0,0,0]))
        self.assertEqual(False,solution.is_increasing([5,6,-10]))
        
if __name__ == '__main__':
    unittest.main()