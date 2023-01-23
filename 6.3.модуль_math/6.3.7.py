from math import *

num1 = float(input())
num2 = float(input())
num3 = float(input())
d = num2 ** 2 - 4 * num1 * num3       
if d < 0:
    print("Нет корней")
elif d == 0:         
    print(-num2 / ( 2 * num1))
elif d > 0:          
    root1 = (-num2 - d ** 0.5) / (2 * num1)
    root2 = (-num2 + d ** 0.5) / (2 * num1)
    print(min(root1, root2), max(root1, root2), sep="\n")