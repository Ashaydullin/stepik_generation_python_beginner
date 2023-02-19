num = int(input())
while num > 999:
    num //= 10
print(num % 10)