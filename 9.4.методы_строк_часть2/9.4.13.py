word = input()
numcounter = 0
wordcounter = ""
for i in word:
    if word.count(i) >= numcounter:
        numcounter = word.count(i)
        wordcounter = i
print(wordcounter)