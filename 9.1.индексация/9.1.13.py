word = input()
neighbours = 0                 
for i in range(len(word) -1): 
    if word[i] == word[i + 1]: 
        neighbours += 1        
        
print(neighbours)