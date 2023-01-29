num = int(input())
for i in range(1, num + 1):
    if i in range(5, 10):
        continue
    elif i in range(17, 38):
        continue
    elif i in range(78, 88):
        continue   
    print(i)
