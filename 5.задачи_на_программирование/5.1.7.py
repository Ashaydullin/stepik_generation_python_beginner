num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
sum = num1 + num2 + num3 + num4
if sum % 2 == 1 and num1 != num3 and num2 != num4:
    print("YES")
else:
    print("NO")
#Если сумма всех значений нечетная и первое значение не равно третьей 
#и второе значение не равно четвертой то напечатать 'ДА' иначе 'НЕТ'