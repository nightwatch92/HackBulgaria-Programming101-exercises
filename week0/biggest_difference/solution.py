def biggest_diffarance(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    maximum = arr[0]
    for y in arr:
    
        if y > maximum:
            maximum = y
    return smallest - maximum
            
    
    # print(biggest_diffarance([23,41,23,13]))
    # print(biggest_diffarance([1,2,3,4,5]))
    # print(biggest_diffarance(range(100)))
    # print(biggest_diffarance([-10, -9, -1]))
