num = int(input())             
counter = 0                      
for y in range(1, num + 1):    
    for x in range(y):         
        counter += 1             
        print(counter, end=" ")  
    print()                    
