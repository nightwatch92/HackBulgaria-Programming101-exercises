# cat2.py
import sys

def main():
    for arg in sys.argv[1:]:
        filename = arg
        file = open(filename, "r")
        print(file.read())

if __name__ == '__main__':
    main()