num = int(input())
last_digit = 0 
while num > 9:         
    last_digit = num % 10
    num = num // 10
print(last_digit)     