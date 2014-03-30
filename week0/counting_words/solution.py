from collections import Counter #10x to python docs
def count_words(arr):
    cnt = Counter()
    for word in arr:
        cnt[word]+=1
    return(cnt)
    
def main():
    print(count_words(['apple', 'banana', 'apple', 'pie']))
if __name__ == '__main__':
    main()