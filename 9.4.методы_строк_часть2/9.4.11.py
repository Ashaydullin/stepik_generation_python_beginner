word = str(input())
counter = 0
for char in word:
    if char in "0123456789":
        counter += 1
print(counter)