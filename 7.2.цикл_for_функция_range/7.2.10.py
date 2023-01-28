num = int(input())
num1 = int(input())
for i in range(num, num1 + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 15 == 0:
        print(i)