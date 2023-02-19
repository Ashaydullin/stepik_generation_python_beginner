counter = 0
maximum = -1
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        counter += 1
        if x > maximum:
            maximum = x
if counter > 0:
    print(counter)
    print(maximum)
else:
    print("NO")