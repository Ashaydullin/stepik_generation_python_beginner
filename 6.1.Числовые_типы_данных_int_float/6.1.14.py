num = int(input())
dig1 = (num // 100) % 10
dig2 = (num // 10) % 10
dig3 = num % 10
nummax = max(dig1, dig2, dig3)
sum = dig1 + dig2 + dig3
midval = 2 * nummax
if sum == midval:
    print("Число интересное")
else:
    print("Число неинтересное")