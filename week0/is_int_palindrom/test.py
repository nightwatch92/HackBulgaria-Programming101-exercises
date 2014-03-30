import unittest
import solution

class IsIntPalindrom(unittest.TestCase):
    """docstring for SumOfDivisorsTest"""

    def test_is_palindrom(self):
        self.assertEqual(False, solution.is_int_palindrom(889))
        self.assertEqual(True, solution.is_int_palindrom(101))
    def test_zero_palindrom(self):
        self.assertEqual(True, solution.is_int_palindrom(0))
    def test_negative_number(self):
        self.assertEqual(True, solution.is_int_palindrom(-101))
        self.assertEqual(True, solution.is_int_palindrom(-123321))
        self.assertEqual(False,solution.is_int_palindrom(-3134))
    #     # self.assertEqual(2340, solution.is_int_palindrom(1000))
    # def test_zero(self):
    #     self.assertEqual(0, solution.is_int_palindrom(0))

if __name__ == '__main__':
    unittest.main()

# def is_int_palindrom(n):
#   digits = n
#   rev = 0
    
#   while n!=0:
#       rev = n%10+rev*10
        
#       n = n//10
#   # print(rev)
#   # print(n)
#   # print(digits)
#   if digits == rev:
#       print True
#   else:
#       print False
    
# def main():
#   print(is_int_palindrom(101))        
#   print(is_int_palindrom(1221))
#   print(is_int_palindrom(12334))
#   print(is_int_palindrom(1))
#   print(is_int_palindrom(100001))



