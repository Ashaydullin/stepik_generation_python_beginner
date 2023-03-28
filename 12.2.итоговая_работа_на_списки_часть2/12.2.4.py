n = input().split("-")
c = [len(i) for i in n] 
if c == [3, 3, 4] and ''.join(n).isdigit(): 
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == "7": 
    print("YES")
else:
    print("NO")