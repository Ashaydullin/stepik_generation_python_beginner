word = input()
coup = word[:word.find("h")] + word[word.rfind("h"):word.find("h"):-1] + word[word.rfind("h"):]
print(coup)