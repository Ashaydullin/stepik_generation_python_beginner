a = int(input())
first = a // 1000
second = a // 100 - (a // 1000 * 10)
third = (a % 100 - a % 10) / 10
last = a % 10
if first + last == second - third:
    print('ДА')
else:
    print('НЕТ')