num = int(input())
counter = 0
counter_last = 0
counter_even = 0
sum_more_five = 0
multy_more_seven = 1
zero_and_five_counter = 0
last = num % 10
while num > 0:
    x = num % 10
    if x == 3:
        counter += 1
    if x == last:
        counter_last += 1
    if x % 2 == 0:
        counter_even += 1
    if x > 5:
        sum_more_five += x
    if x > 7:
        multy_more_seven *= x
    if x == 0 or x == 5:
        zero_and_five_counter += 1
    num //= 10
print(
     counter, counter_last,
     counter_even, sum_more_five,
     multy_more_seven, zero_and_five_counter,
     sep="\n"
      )