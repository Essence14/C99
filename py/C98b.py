def WordCountFromFile():
    file=open("abc.txt", "r")
    WordCount=1
    for line in file:
        Word=line.split(",")
        print(Word)
        WordCount+=len(Word)
    print(WordCount)

WordCountFromFile()