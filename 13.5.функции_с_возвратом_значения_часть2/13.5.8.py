def isPrime(n):
    if n % 2 == 0: return(n == 2)
    d = 3
    while d * d <= n and n % d != 0: d += 2
    return(d * d > n)

def isPalindrom(n):
    n = str(n)
    return(n == n[::-1])

def isEven(n): return(not n % 2)

def is_valid_password(password):
    try:
        a, b, c = map(int, password.split(':'))
        return(isPalindrom(a) and isPrime(b) and isEven(c))
    except: return(False)

psw = input()

print(is_valid_password(psw))