word = input()
counter = 0
for i in range(len(word)):
     if word[i] != word[i].upper():    
        counter += 1
print(counter)