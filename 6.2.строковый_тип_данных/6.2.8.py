city1 = input()
city2 = input()
city3 = input()
linecity1 = len(city1)
linecity2 = len(city2)
linecity3 = len(city3)
maxcity = max(len(city1), len(city2), len(city3))
mincity = min(len(city1), len(city2), len(city3))
if linecity1 == mincity:
    print(city1)
elif linecity2 == mincity:
    print(city2)
elif linecity3 == mincity:
    print(city3)
if linecity1 == maxcity:
    print(city1)
elif linecity2 == maxcity:
    print(city2)
elif linecity3 == maxcity:
    print(city3)