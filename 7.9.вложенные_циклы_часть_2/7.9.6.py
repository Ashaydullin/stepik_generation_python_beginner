num = int(input())     
total = 0               
factorial = 1            
for i in range(1, num + 1):
    for j in range(1, i + 1):
        factorial *= j       
    total += factorial       
    factorial = 1            
print(total)