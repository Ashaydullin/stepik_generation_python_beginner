num = int(input())
mid = num // 2 + 1         
counter = 0             
for i in range(1, num + 1):
    if i > mid:           
        counter -= 1         
    else:
        counter += 1          
    
    for _ in range(counter):  
        print("*", end="")
    print()