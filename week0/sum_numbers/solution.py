import sys

def main():
		
	file_with_numbers = sys.argv[1]

	file = open(file_with_numbers, "r")
	contents = file.read().split(" ")
	numbers = map(int, contents)
	# print(list(numbers))
	print(sum(numbers))
if __name__ == '__main__':
	main()

# [1,2,3]
# map(str,[1,2,3])
# [str(1), str(2), str(3)]





# # sum_number.py
# import sys

# def main():
# 	if len(sys.args) > 1:
# 		filename = sys.args[1]
# 		file = open(filename, "r")
# 		contents = file.read()
# 		# print(contents)
		
# if __name__ == '__main__':
# 	main()