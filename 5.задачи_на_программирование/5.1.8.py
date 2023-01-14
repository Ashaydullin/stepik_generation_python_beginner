num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if (num1 - num2 == num3 - num4) or (num1 + num2 == num3 + num4) or (num1 == num3) or (num2 == num4):
        print("YES")
else:
        print("NO")

#Объединил ход слона и ход ладьи, более красивого решения придумать не смог

#UPD смог:
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# diff1 = num1 - num2
# diff2 = num3 - num4
# sum1 = num1 + num2
# sum2 = num3 + num4
# if (diff1 == diff2) or (sum1 == sum2):
#         print("YES")
# else: 
#     if (num1 == num3) or (num2 == num4):
#         print("YES")
#     else:
#         print("NO")