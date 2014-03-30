def is_int_palindrom(n):
    n = abs(n)
    digits = abs(n)
    rev = 0
    
    while n!=0:

        rev = n % 10 + rev*10
        n = n // 10

    check = abs(digits) == abs(rev)
    if check:
        return check
    else:
        return check
# def main():
#   print(is_int_palindrom(101))        
#   print(is_int_palindrom(1221))
#   print(is_int_palindrom(12334))
#   print(is_int_palindrom(1))
#   print(is_int_palindrom(100001))

# if __name__ == '__main__':
#   main()

