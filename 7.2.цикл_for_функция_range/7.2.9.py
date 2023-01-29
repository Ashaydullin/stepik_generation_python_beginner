num = int(input())
num1 = int(input())
check = num + num % 2 - 1
for i in range(check, num1 - 1, -2):
    print(i)