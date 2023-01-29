num = int(input())
max1 = max2 = 1       
for i in range(1, num + 1):
    num1 = int(input())    
    if num1 > max1:        
        max2 = max1     
        max1 = num1     
    elif num1 > max2:   
        max2 = num1  
print(max1, max2, sep="\n") 