def prime_factorization(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    
    if n > 1:
        primfac.append(n)
    
    f = [primfac.count(el) for el in primfac]
    if len(primfac) == 1:
        first_value1 = primfac.pop(0)
        first_value_stepen1 = f.pop(0)
        f = ([(first_value1,first_value_stepen1)])
        return f
    else:
        first_value = primfac.pop(0)
        first_value_stepen = f.pop(0)
        second_value = primfac.pop()
        second_value_stepen = f.pop()
    b = ([(first_value,first_value_stepen),(second_value, second_value_stepen)])
    return b
    
    # print(prime_factorization(24))
    # print(prime_factorization(10))
    # print(prime_factorization(14))
    # print(prime_factorization(10432420))
    # print(prime_factorization(89))