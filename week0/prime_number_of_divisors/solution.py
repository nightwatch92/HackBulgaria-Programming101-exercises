

def prime_number_of_divisors(n):
    n = abs(n)
    index = 1
    totalOfDivisiors = 0
    isPrime = True
    while index<=n:
        if n % index == 0:
            totalOfDivisiors += 1
        index +=1

    # print(totalOfDivisiors)
    counter = 2
    result = 0
    while counter < totalOfDivisiors:
        if totalOfDivisiors % counter == 0:
            result = result + counter
        counter = counter +1

    if totalOfDivisiors == 2 or totalOfDivisiors == 3:
        return isPrime
    
    elif result == 0:
        
        return isPrime
    else:
        isPrime = False
        return isPrime