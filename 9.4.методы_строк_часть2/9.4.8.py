word = str(input())
counter = 1
for i in word:
    if i == " ":
        counter += 1
print(counter)