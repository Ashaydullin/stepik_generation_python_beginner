a = input().split()
s = 0
for i in range(len(a) - 1):
    s += a[i + 1:].count(a[i])
print(s)