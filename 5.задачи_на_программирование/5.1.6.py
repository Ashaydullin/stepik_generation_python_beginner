num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if (num1 - num2 == num3 - num4) or (num1 + num2 == num3 + num4):
    print("YES")
else:
    print("NO")
# Условие x1 - y1 == x2 - y2 
# соответствует одной диагонали, а условие x1 + y1 == x2 + y2 -- другой диагонали. 
#Так как слон ходит по обоим диагоналям, то используем логическую операцию or: