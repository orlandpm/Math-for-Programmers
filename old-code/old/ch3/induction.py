def t(n): return n * (n + 1) / 2

def reference_t(n):
    return sum(range(1,n+1))

def reference_t(n):
    if n > 1:
        return n + reference_t(n - 1)
    else:
        return 1
