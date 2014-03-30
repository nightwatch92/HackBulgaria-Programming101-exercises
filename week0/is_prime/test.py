import unittest
import solution
from random import randint

class IsPrimeTest(unittest.TestCase):
	"""docstring for IsPrimeTest"""
	def test_is_prime(self):
		self.assertEqual(True, solution.is_prime(7))
 
	def test_is_one_not_prime(self):
		self.assertEqual(False, solution.is_prime(1))
	def test_zero(self):
		self.assertEqual(None, solution.is_prime(0))
	def test_negative_number(self):
		self.assertEqual(False, solution.is_prime(-10))
	# def test_is_random_number(self):
	# 	self.assertEqual(False,solution.is_prime(randint(0,100)))

if __name__ == '__main__':
	unittest.main()

