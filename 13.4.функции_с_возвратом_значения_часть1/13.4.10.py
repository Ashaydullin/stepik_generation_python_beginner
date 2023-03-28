def find_all(target, symbol):
    return [x for x in range(len(target)) if target[x] == symbol]

s = input()
char = input()

print(find_all(s, char))