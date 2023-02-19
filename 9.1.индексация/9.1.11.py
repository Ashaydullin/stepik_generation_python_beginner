word = input()                  
message = "Цифр нет"                
for i in range(len(str(word))):  
    if word[i] in "0123456789":   
        message = "Цифра"           
        break                  
print(message)