def sum_of_divisors(n):
	index = 1
	result = 0
	while index <= abs(n):
		if n % index == 0 :
			result = result + index
		index = index + 1
		
	return result


		
	
def main():
	print(sum_of_divisors(8))
	print(sum_of_divisors(3))
	print(sum_of_divisors(1))
	print(sum_of_divisors(1000))
	print(sum_of_divisors(7))

if __name__ == '__main__':
	main()