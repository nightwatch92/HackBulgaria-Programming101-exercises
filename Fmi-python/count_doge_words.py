def count_doge_words(str):
    word_count = 0
    doge_words = ["much", "such", "so", "lol", "wow", "very"]
    for words in str.split(" "):
        if words in doge_words:
            word_count += 1
    return word_count
def main():
    print(count_doge_words("wow much wow wow wow hard such difficult"))
    print(count_doge_words("wow much hard such difficult"))

if __name__ == '__main__':
    main()