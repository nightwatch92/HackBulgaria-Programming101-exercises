def number_to_list(n):
    n = abs(n)
    n = str(n)
    list = []
    for digit in n:
        list.append(int(digit))
    return list