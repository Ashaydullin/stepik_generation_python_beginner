word = str(input())
counter = 0
for i in range(len(word)):
    if word[i] in "0123456789":
        counter += 1
print(counter)