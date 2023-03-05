word = str(input())
for i in range(len(word)):
    if i % 3 != 0:
        print(word[i], end="")