num = int(input())
sum = 0                  
for i in range(1, num + 1): 
    total = i ** 2               
    if total % 10 == 2 or total % 10 == 5 or total % 10 == 8: 
        sum += i            
print(sum)