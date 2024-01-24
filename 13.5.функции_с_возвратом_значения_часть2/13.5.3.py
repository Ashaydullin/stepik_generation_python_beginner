def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

n = int(input())

print(is_prime(n))