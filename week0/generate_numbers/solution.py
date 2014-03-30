# generate_numbers.py
import sys
from random import randint

	

def main():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		n = int(sys.argv[2])
		fx = []
		file = open(filename, "w")
		index = 0
		while index <= n:
			argument = randint(1, 1000)
			b = str(argument)
			
			fx.append(b)
			# file.write(" ".join(b))	
			index =index +1
		# print(fx)
		file.write(" ".join(fx))
    	
    
if __name__ == '__main__':
    main()