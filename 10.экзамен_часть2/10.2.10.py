word = input()
if word.count("f") == 1:
    print("-1")
elif word.count("f") == 0:
    print("-2")
else:
    word = word.replace("f", " ", 1)
    print(word.find("f"))