num = int(input())
for i in range(1, num + 1):   
    counter = 0               
    for _ in range(i):        
        counter += 1          
        print(counter, end="")
    for _ in range(i, 1, -1): 
        counter -= 1          
        print(counter, end="")
    print()     