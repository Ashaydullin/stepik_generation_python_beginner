num = int(input())   
fix_num = num
total = 0    
product = 1  
counter = 0    
while num != 0:                
    total += num % 10          
    product *= num % 10        
    counter += 1               
    num //= 10                 
print(
      total, 
      counter, 
      product, 
      total / counter, 
      fix_num // 10 ** (counter - 1), 
      fix_num // 10 ** (counter - 1) + fix_num % 10, 
      sep="\n"
      )      


