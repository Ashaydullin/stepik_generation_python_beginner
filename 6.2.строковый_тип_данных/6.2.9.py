line1 = len(input())
line2 = len(input())
line3 = len(input())
sum = line1 + line2 + line3
progress = (min(line1, line2, line3) + max(line1, line2, line3)) / 2 * 3
if sum == progress:
    print("YES")
else:
    print("NO")