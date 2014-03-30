import unittest
import solution
# from random import randint

class SumOfMaxAndMinTest(unittest.TestCase):
	"""docstring for SumOfMaxAndMinTest"""
	def test_of_max_min(self):
		self.assertEqual(39,solution.sum_of_min_and_max(range(10,30)))
		self.assertEqual(22,solution.sum_of_min_and_max([3,4,5,7,9,19]))
	def test_for_negative_numbers(self):
		self.assertEqual(9,solution.sum_of_min_and_max(range(-10,20)))
		self.assertEqual(-31,solution.sum_of_min_and_max(range(-20,-10)))
		self.assertEqual(4989,solution.sum_of_min_and_max(range(-10,5000)))

if __name__ == '__main__':
	unittest.main()
# def sum_of_min_and_max(arr):
	
	
# 	maximum = arr[0]
# 	smallest = arr[0]
# 	for element in arr:
# 		if element > maximum:
# 			maximum = element
# 	for item in arr:
# 		if item < smallest:
# 			smallest = item

# 	return maximum + smallest
# def main():
# 	print(sum_of_min_and_max([4,2,3,4,43,6,8,23]))
# 	print(sum_of_min_and_max([-10,5,10,100]))
# 	print(sum_of_min_and_max([1]))
# 	print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
