num = int(input())
def quick_merge(num):
    return sorted([int(i) for i in range(num) for i in input().split()])
print(*quick_merge(num))