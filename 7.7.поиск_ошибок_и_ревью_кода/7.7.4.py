mx = - pow(10, 6)      
s = 0
for _ in range(1, 11): 
    x = int(input())
    if x < 0:
        s += x        
    if 0 > x > mx:         
        mx = x
if s < 0:            
    print(s, mx, sep="\n")
else:                 
    print('NO')