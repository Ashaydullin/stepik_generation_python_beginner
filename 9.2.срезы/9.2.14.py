word = input()
string_length = len(word)
index = string_length // 2 + string_length % 2
print(word[index:] + word[:index])