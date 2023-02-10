num = int (input())
while num > 9: 
    summ = 0    
    while (num > 0):
        last_digit = num % 10  
        summ += last_digit    
        num = num // 10       
    num = summ
print(num)