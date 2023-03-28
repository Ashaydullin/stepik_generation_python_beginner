num = int(input())
list_num = []

for _ in range(num):
    numbers = int(input())
    list_num.append(numbers)

for i in list_num:
    if i != min(list_num) and i != max(list_num):
        print(i)