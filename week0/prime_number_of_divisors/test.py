import unittest
import solution

class SumOfPrimeDivisiorTest(unittest.TestCase):
    """docstring for SumOfDigitsTest"""

    def test_truth(self):
        self.assertEqual(True,solution.prime_number_of_divisors(7))
        self.assertEqual(True,solution.prime_number_of_divisors(29))
        self.assertEqual(True,solution.prime_number_of_divisors(31))
        self.assertEqual(False,solution.prime_number_of_divisors(8))
        self.assertEqual(True,solution.prime_number_of_divisors(0))
    def test_for_sum(self):
        self.assertEqual(False,solution.prime_number_of_divisors(1241))
    def test_negative_number(self):
        self.assertEqual(False,solution.prime_number_of_divisors(-1241))



# 	index = 1
# 	totalOfDivisiors = 0
# 	isPrime = True
# 	while index<=n:
# 		if n % index == 0:
# 			totalOfDivisiors += 1
# 		index +=1

# 	print(totalOfDivisiors)
# 	counter = 2
# 	result = 0
# 	while counter < totalOfDivisiors:
# 		if totalOfDivisiors % counter == 0:
# 			result = result + counter
# 		counter = counter +1

# 	if totalOfDivisiors == 2 or totalOfDivisiors == 3:
# 		print(isPrime)

# 	elif result == 0:

# 		print(isPrime)
# 	else:
# 		isPrime = False
# 		print(isPrime)



# def main():
# 	print(prime_number_of_divisors(25))
# 	print(prime_number_of_divisors(7))
# 	print(prime_number_of_divisors(8))
# 	print(prime_number_of_divisors(9))
# 	print(prime_number_of_divisors(56))
# 	print(prime_number_of_divisors(64))
# 	print(prime_number_of_divisors(255))
# 	print(prime_number_of_divisors(196))

if __name__ == '__main__':
	unittest.main()
