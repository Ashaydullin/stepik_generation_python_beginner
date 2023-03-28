string_list = []

for _ in range(int(input())):
    num = input()
    if num in string_list:
        continue
    else:
        string_list.append(num)

print(*string_list, sep="\n")