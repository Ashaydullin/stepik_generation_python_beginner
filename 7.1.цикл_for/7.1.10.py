startpop = int(input())
midrange = int(input())
days = int(input())
for item in range(days):
    print(item + 1, startpop)
    startpop = startpop + midrange / 100 * startpop