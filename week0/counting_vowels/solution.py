def count_vowels(str):
    vowels = "aeiouy"
    count = 0
    for v in vowels:
        count += str.lower().count(v) 
    return count
