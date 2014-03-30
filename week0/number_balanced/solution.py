def is_number_balanced(n):
    to_str = str(n)
    lenght = len(to_str)
    first_part = to_str[:len(to_str)//2]
    second_part = to_str[len(to_str)//2:]
    
    # print(first_part, second_part, third_part)
    left_part = 0
    for x in first_part:
        left_part += int(x)
    # print(left_part)
    right_part = 0
    for y in second_part:
        right_part += int(y)

    if lenght % 2 == 1:
        third_part = to_str[len(to_str)//2]
        final = right_part - int(third_part)
        if final == left_part:
            return True
        else:
            return False
    else:
        if left_part == right_part:
            return True
        else:
            return False