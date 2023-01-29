num = int(input())     
flag = True            
while num > 9:         
    last_digit = num % 10    
    num = num // 10    
    sec_num = num % 10     
    if last_digit != sec_num:    
        flag = False   
if flag:               
    print("YES")       
else:                
    print("NO") 