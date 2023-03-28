def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

n = int(input())

print_digit_sum(n)