def contains_digits(number, digits):
	b = str(number)
	c = []
	for digit in b:
		c.append(int(digit))
	count = 0
	for element in digits:
		if element in c:
			count +=1
	if count == len(digits):
		return True
	else:
		return False
	# print(contains_digits(123,[1,1,1,2]))
	# print(contains_digits(64305, [6,4,3,3,3,5]))
	# print(contains_digits(402123, [0, 3, 4]))
	# print(contains_digits(666, [6,4]))
	# print(contains_digits(123456789, [1,2,3,0]))
	# print(contains_digits(456, []))
