search = [input() for _ in range(int(input()))]
coincidences = [input() for _ in range(int(input()))]
for i in search:
    for j in coincidences:
        if j.lower() not in i.lower():
            break
    else:
        print(i)