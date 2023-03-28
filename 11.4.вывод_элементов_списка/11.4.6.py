num = [input() for x in range(int(input()))]
search = input().lower()
for i in num:
    if search in i.lower():
        print(i)