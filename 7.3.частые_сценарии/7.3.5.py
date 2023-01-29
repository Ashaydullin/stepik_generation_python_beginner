num = int(input())
num1 = int(input())
counter = 0      
for i in range(num, num1 + 1): 
    if i % 10 == 4 or i % 10 == 9:  
        counter += 1              
print(counter)