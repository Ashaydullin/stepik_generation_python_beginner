rusword = input()
uncons = 0  
cons = 0
wordcons = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"    
worduncons = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ" 

for cycle in rusword:       
    if cycle in wordcons:    
        uncons += 1   
    if cycle in worduncons:  
        cons += 1  
        
print(
     f"Количество гласных букв равно {uncons}", 
     f"Количество согласных букв равно {cons}",
     sep="\n"
     )