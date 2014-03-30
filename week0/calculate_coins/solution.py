#calculate_coins.py
def calculate_coins(sum1):

    coins = [100, 50, 20, 10, 5, 2, 1]
    change = {100: 0, 50: 0, 20:0, 10:0, 5:0, 2:0,1:0}
    remove_dot = str(sum1).replace(".","")
    remove_dot = int(remove_dot)
    for value in coins:
        if remove_dot // value > 0:
            change[value] = remove_dot // value
            remove_dot -= remove_dot // value * value
    return change
def main():

   print(calculate_coins(3.45))
   print(calculate_coins(2.46))

if __name__ == '__main__':
    main()