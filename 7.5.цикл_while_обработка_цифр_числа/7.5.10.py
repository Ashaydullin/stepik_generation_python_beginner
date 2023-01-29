num = int(input())
tag = "YES"           
last_digit = num % 10 

while num:            
    if last_digit > num % 10: 
        tag = "NO"  
    else:           
        last_digit = num % 10 
    num //= 10      
print(tag)