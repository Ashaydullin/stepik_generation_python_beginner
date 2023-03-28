num = int(input())
cycle = [int(input()) for _ in range(num)]
[print(i) for i in cycle if i < 0]
[print(i) for i in cycle if i == 0]
[print(i) for i in cycle if i > 0]