rom math import sqrt
num1 = float(input())
num2 = float(input())
midarf = (num1 + num2) / 2
midgem = sqrt(num1 * num2)
midgarm = (2 * num1 * num2) / (num1 + num2)
midqad = sqrt((num1 ** 2 + num2 ** 2) / 2)
print(midarf, midgem, midgarm, midqad, sep="\n")