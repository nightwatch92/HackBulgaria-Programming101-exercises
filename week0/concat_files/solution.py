# concat_files.py

import sys
import os.path

def main():


    fx = []

    for arg in sys.argv[1:]:
        filename = arg
        file = open(filename, "r")
        # print(file.read())
        content = file.read()
        fx.append(content)


        # print(type(content))

    file_megatron = "megatron.txt"
    write_megatron = open(file_megatron, "a")
    write_megatron.write(" ".join(fx))
    write_megatron.close()





    # print(fx)
if __name__ == '__main__':
    main()