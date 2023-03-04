key = int(input())
word = input()
letters = 26
for i in range(len(word)):
    gcode = ord(word[i]) - key
    if gcode < 97:
        gcode += letters
    print(chr(gcode), end="") 