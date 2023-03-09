word = input()
star = 0                 
plus = 0                
for i in word:
    if i == "*":         
        star += 1        
    elif i == "+":       
        plus += 1        

print(
      f"Символ + встречается {plus} раз", 
      f"Символ * встречается {star} раз", 
      sep="\n"
      )
