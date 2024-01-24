num = int(input())
list_num = []

for _ in range(num):
    numbers_int = int(input())
    list_num.append(numbers_int)
    print(numbers_int)

print()

for i in list_num:
    value_funс = i ** 2 + 2 * i + 1
    print(value_funс)