def unique_words_count(arr):
    b = [arr.count(el) for el in arr]
    d = list(set(arr))
    counting = 0
    for index in d:
        counting += 1
    return counting
