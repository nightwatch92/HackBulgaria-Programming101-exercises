def f_sum(n):
	s = 0
	if n < 0:
		n = abs(n)

	while n:
		s += n%10
		n //= 10
		
	return s

def main():
	print(f_sum(-33))
	print(f_sum(-10))
	print(f_sum(123))
	print(f_sum(6))
	print(f_sum(1325132435356))

if __name__ == '__main__':
	main()