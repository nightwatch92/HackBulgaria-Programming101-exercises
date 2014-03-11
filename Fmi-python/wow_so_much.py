def wow_such_much(start, end): 
    doge_array = range(start, end)
    result = []
    for element in doge_array:
        result.append(element)
        if (element % 3 == 0):
            replace_element = doge_array.index(element)
            result[replace_element] = "such"
        elif (element % 5 == 0):
            replace_element = doge_array.index(element)
            result[replace_element] = "much"
        if element % 3 == 0 and element % 5 == 0:
            replace_element = doge_array.index(element)
            result[replace_element] = "suchmuch"
    return result

def main():
        print(wow_such_much(1, 16))

if __name__ == '__main__':
        main()