def nth_fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return nth_fibonacci(n-1)+nth_fibonacci(n-2)
def main():
	print(nth_fibonacci(3))
	print(nth_fibonacci(8))
if __name__ == '__main__':
	main()