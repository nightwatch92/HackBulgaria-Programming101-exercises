def contains_digit(number,digit):
    number = abs(number)
    digit = abs(digit)
    while (number!=0):
        remain = number%10
        number = number//10
        isThere = digit == remain
        # print(remain) 
        if isThere:
            return isThere
        else:
            return isThere
    
    
def main():
    print(contains_digit(2244,1))
    print(contains_digit(245,5))

if __name__ == '__main__':
    main()