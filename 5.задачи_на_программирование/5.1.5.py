num = int(input())
if num % 2 == 1:
    print("YES")
elif (num % 2 == 0) and num > 20:
    print("NO")
elif (2 <= num <= 5) and num % 2 == 0:
    print("NO")
elif (6 <= num <= 20) and num % 2 == 0:
    print("YES")