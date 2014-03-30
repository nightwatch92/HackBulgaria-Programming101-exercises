#prepare_meal.py

def prepare_meal(n):
    index = 3
    index1 = 5
    niz = ''
    while n % index == 0:
        index = index*3
        niz += "spam "

    while n % index1 == 0:
        niz += "and eggs"
        index1 = index1*5
    return niz
