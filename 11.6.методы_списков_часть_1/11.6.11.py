num = input().split()   
for i in range(len(num)):    
    num[i] = int(num[i])        
num.sort()              
print(*num)             
num.sort(reverse=True)  
print(*num)   