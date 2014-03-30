import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        file = open(filename, "r")
        content = (file.read())
        file.close()
        return print(content)
    else:
        return print("No arguments given")

if __name__ == '__main__':
    main()