numline = int(input())
counter = 0
for _ in range(numline):
    messages = input().count("11")
    if messages >= 3:
        counter += 1
print(counter)