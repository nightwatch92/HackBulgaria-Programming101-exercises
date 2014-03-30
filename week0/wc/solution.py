# wc.py
import sys

def main():
	file_name = sys.argv[2]
	open_file = open(file_name, "r")
	data = open_file.read()
	each_line = data.split("\n")
	each_word = data.split(' ')
	# lines(file)

	if sys.argv[1] == "chars":
		print(chars(data))
	elif sys.argv[1] == "words":
		print(words(each_word))
	elif sys.argv[1] == "lines":
		print(lines(each_line))



def chars(data):
	chars = 0
	for char in data:
		chars +=len(char)
	return chars

def words(each_word):
	words = 0

	for wordcount in each_word:
		words += 1
	return words



def lines(each_line):
	lines = 0
	for line_ in each_line:
		lines += 1
	return lines

if __name__ == '__main__':
	main()