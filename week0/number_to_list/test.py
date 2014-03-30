import unittest
import solution

class NumerToListTest(unittest.TestCase):
    """docstring for VowelsTest"""
    def test_different_numbers(self):
        self.assertEqual([2,3,3,3],solution.number_to_list(2333))
        self.assertEqual([1,1,1,1],solution.number_to_list(1111))
        self.assertEqual([3,3,3,3],solution.number_to_list(3333))
        self.assertEqual([3,0,0,0,0,0],solution.number_to_list(300000))

    def test_zero_number(self):
        self.assertEqual([0],solution.number_to_list(0))

    def test_negative_number(self):
        self.assertEqual([3,3,1,1],solution.number_to_list(-3311))
        self.assertEqual([3,1,2,3,1,3],solution.number_to_list(312313))
        self.assertEqual([7,6,8,6,7],solution.number_to_list(76867))

if __name__ == '__main__':
    unittest.main()