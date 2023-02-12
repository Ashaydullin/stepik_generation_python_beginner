num = 8 
counter = 0
maximum = -10 ** 6 - 1 
for i in range(1, num + 1):
    x = int(input())
    if x % 4 == 0: 
        counter += 1
        if x > maximum:
            maximum = x
if counter > 0:
    print(counter)
    print(maximum)
else:
    print("NO")