import solution
import unittest

class BalancedNumberTest(unittest.TestCase):
    """docstring for BalancedNumberTest"""

    def test_is_balanced(self):
        
        self.assertEqual(True, solution.is_number_balanced(1238033))
        self.assertEqual(True, solution.is_number_balanced(333))
        self.assertEqual(False, solution.is_number_balanced(4344))
        self.assertEqual(False, solution.is_number_balanced(1234))
        self.assertEqual(True, solution.is_number_balanced(1))
        self.assertEqual(True, solution.is_number_balanced(0))

if __name__ == '__main__':
    unittest.main()

# def is_number_balanced(n):
#   to_str = str(n)
#   lenght = len(to_str)
#   first_part = to_str[:len(to_str)//2]
#   second_part = to_str[len(to_str)//2:]
    
#   # print(first_part, second_part, third_part)
#   left_part = 0
#   for x in first_part:
#       left_part += int(x)
#   # print(left_part)
#   right_part = 0
#   for y in second_part:
#       right_part += int(y)

#   if lenght % 2 == 1:
#       third_part = to_str[len(to_str)//2]
#       final = right_part - int(third_part)
#       if final == left_part:
#           return True
#       else:
#           return False
#   else:
#       if left_part == right_part:
#           return True
#       else:
#           return False

    


# def main():
#   # print(is_number_balanced(1233334))
#   print(is_number_balanced(1238033))
#   print(is_number_balanced(99))
#   print(is_number_balanced(28471))
#   print(is_number_balanced(11))
#   print(is_number_balanced(13))
#   print(is_number_balanced(121))
#   print(is_number_balanced(4518))
#   print(is_number_balanced(28471))
# if __name__ == '__main__':
#   main()