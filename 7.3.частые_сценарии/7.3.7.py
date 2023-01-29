from math import log     

diff = 0                 
num = int(input())         
for i in range(1, num + 1):
    diff += (1 / i)      
print(diff - log(num))  