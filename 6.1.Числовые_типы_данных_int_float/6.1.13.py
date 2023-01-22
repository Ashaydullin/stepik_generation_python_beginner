num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1 + num2 + num3
nummax = max(num1, num2, num3)
nummin = min(num1, num2, num3)
numtop = sum - nummax - nummin
print(nummax, numtop, nummin, sep="\n")