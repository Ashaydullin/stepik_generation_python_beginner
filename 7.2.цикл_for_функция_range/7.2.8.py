num = int(input())
num1 = int(input())
if num < num1:
    for i in range(num, num1 + 1):
        print(i)
else:
    for i in range(num, num1 - 1, - 1):
        print(i)
