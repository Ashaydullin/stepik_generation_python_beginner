a = int(input())
if a == 0:
    print("зеленый")
elif a < 0 or a > 36:
    print("ошибка ввода")
elif (1 <= a <= 10 or 19 <= a <= 28) + (not a % 2) == 1:
    print("красный")
else:
    print("черный")