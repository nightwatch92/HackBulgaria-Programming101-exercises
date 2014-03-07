def sum_of_min_and_max(arr):
	
	
	maximum = arr[0]
	smallest = arr[0]
	for element in arr:
		if element > maximum:
			maximum = element
	for item in arr:
		if item < smallest:
			smallest = item

	return maximum + smallest
def main():
	print(sum_of_min_and_max([4,2,3,4,43,6,8,23]))
	print(sum_of_min_and_max([-10,5,10,100]))
	print(sum_of_min_and_max([1]))
	print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
if __name__ == '__main__':
	main()