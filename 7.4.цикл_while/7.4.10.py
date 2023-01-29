num = input()
counter = 0
while num not in ("стоп", "хватит", "достаточно"):
    counter += 1   
    num = input()  
print(counter)
