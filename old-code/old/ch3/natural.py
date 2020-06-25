zero = None



class Successor():
    def __init__(self, prev):
        self.prev = prev
    def __repr__(self):
        if self.prev is zero:
            return "s(0)"
        else:
            return "s(%s)" % self.prev.__repr__()
    def __eq__(self, other):
        try:
            return self.prev == other.prev
        except AttributeError:
            return False
    def __add__(self, other):
        if other is zero:
            return self
        else:
            return Successor(self + other.prev)

def s(n): return Successor(n)

def int_to_peano(n):
    if n == 0:
        return zero
    else:
        return s(int_to_peano(n-1))

def peano_to_int(n):
    if n is zero:
        return 0
    else:
        return 1 + peano_to_int(n.prev)

def sum(n,m):
    if m is zero:
        return n
    else:
        return s(sum(n, m.prev))

def product(n, m):
    if m is zero:
        return zero
    else:
        return add(n, product(n, m.prev))

def power(n, p):
    if p is zero:
        return s(zero)
    else:
        return product(n, power(n, p.prev))

def factorial(n):
    if n is zero:
        return s(zero)
    else:
        return product(n, factorial(n.prev))

def absolute_difference(n,m):
    if n is zero:
        return m
    elif m is zero:
        return n
    else:
        return absolute_difference(n.prev, m.prev)
