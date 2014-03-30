import unittest
import solution

class ListToNumerTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_diferent_lists(self):
        self.assertEqual(2333,solution.list_to_number([2,3,3,3]))
        self.assertEqual(1111,solution.list_to_number([1,1,1,1]))
        self.assertEqual(3333,solution.list_to_number([3,3,3,3]))
        self.assertEqual(300000,solution.list_to_number([3,0,0,0,0,0]))

    def test_with_zero(self):
        self.assertEqual(0,solution.list_to_number([0]))
        
    def test_consonants_upper_case(self):
        self.assertEqual(3311,solution.list_to_number([3,3,1,1]))

if __name__ == '__main__':
    unittest.main()