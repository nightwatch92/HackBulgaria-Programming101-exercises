def is_prime(n):
	if n == 0:
		return print("0 is nothing")
	index = 2
	result = 0
	isPrime = False
	while index < abs(n):
		if n % index == 0:
			result += index
		
		index +=1
	if n == 1:
		isPrime = False
		return isPrime
	
	elif result == 0:
		isPrime = True
		return isPrime
	else:
		return isPrime
	 
# def main():
# 	print(is_prime(1))
# 	print(is_prime(2))
# 	print(is_prime(8))
# 	print(is_prime(11))
# 	print(is_prime(-10))

# if __name__ == '__main__':
# 	main()

