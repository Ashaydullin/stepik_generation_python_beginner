list1 = [int(i) for i in input().split()]
minn = list1.index(min(l))
maxx = list1.index(max(l))
list1[minn] = max(list1)
list1[maxx] = min(list1)
print(*list1)