num1 = int(input())
num2 = int(input())
total_maximum = 0                    
digit = 0                            
for i in range(num1, num2 + 1):      
    maximum = 0                      
    for j in range(1, i + 1):        
        if i % j == 0:               
            maximum += j             
        if maximum >= total_maximum: 
            total_maximum = maximum
            digit = j
print(digit, total_maximum)        


