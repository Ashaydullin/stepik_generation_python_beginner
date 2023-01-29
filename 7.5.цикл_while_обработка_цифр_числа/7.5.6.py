num = int(input())         
min_num = 9  
max_num = 0  
while num != 0: 
    if num % 10 > max_num:   
        max_num = num % 10 
    if num % 10 < min_num: 
        min_num = num % 10 
    num = num // 10        
print(f"Максимальная цифра равна {max_num}", 
      f"Минимальная цифра равна {min_num}", 
      sep="\n")