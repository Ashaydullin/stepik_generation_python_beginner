word = input()
result = word[:word.find("h")] + word[word.rfind("h") + 1:] 
print(result)