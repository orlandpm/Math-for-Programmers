def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 0

def power(n,p):
    if p > 1:
        return n * power(n,p-1)
    else:
        return n

def product(n, m):
    if m > 1:
        return n + product(n, m-1)
    else:
        return n
