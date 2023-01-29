numcycle = int(input())        
num1 = 0                       
num2 = 1                       
for _  in range(numcycle):            
    num2 = num1 + num2         
    num1 = num2 - num1         
    print(num1, end=' ')
