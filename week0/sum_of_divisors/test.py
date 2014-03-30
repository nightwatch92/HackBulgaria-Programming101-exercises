import unittest
import solution

class SumOfDivisorsTest(unittest.TestCase):
	"""docstring for SumOfDivisorsTest"""

	def test_negative_number(self):
		self.assertEqual(15, solution.sum_of_divisors(-8))
	def test_big_numbers(self):
		self.assertEqual(42, solution.sum_of_divisors(20))
		self.assertEqual(2340, solution.sum_of_divisors(1000))
	def test_zero(self):
		self.assertEqual(0, solution.sum_of_divisors(0))


# def sum_of_divisors(n):
# 	index = 1
# 	result = 0
# 	while index <= abs(n):
# 		if n % index == 0 :
# 			result = result + index
# 		index = index + 1
		
# 	return result


		
	
# def main():
# 	print(sum_of_divisors(8))
# 	print(sum_of_divisors(3))
# 	print(sum_of_divisors(1))
# 	print(sum_of_divisors(1000))
# 	print(sum_of_divisors(7))

if __name__ == '__main__':
	unittest.main()