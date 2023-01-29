num = int(input())
while num:           
    last_digit = num % 10
    num = num // 10    
    print(last_digit)

