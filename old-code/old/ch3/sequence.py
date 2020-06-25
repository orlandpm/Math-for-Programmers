

# from list import *
# def natural_numbers(start_from=0):
#     return List(start_from, natural_numbers(start_from + 1))

from collections import namedtuple



def natural_numbers(start_from=0):
    return Sequence(start_from, lambda: natural_numbers(start_from + 1))

from list import *
import sys

class Sequence(namedtuple('Sequence', ['head', 'tail'])):
    def __repr__(self, count=5):
        if count == 0:
            return "..."
        else:
            return str(self.head) + ", " + self.tail().__repr__(count-1)
    def take_list(self, n):
        if n == 0:
            return empty
        else:
            return List(self.head, self.tail().take_list(n-1))
    def skip(self, n):
        if n == 0:
            return self
        else:
            return self.tail().skip(n-1)
    def map(self, f):
        return Sequence(f(self.head), lambda: self.tail().map(f))

    def partial_sums(self, acc=0):
        new_acc = self.head + acc
        return Sequence(new_acc, lambda:self.tail().partial_sums(new_acc))

    def limit(self, epsilon=sys.float_info.epsilon):
        next = self.tail().head
        if abs(next - self.head) < abs(epsilon):
            return next
        else:
            return self.tail().limit(epsilon)

    def filter(self, predicate):
        if predicate(self.head):
            return Sequence(self.head, lambda: self.tail().filter(predicate))
        else:
            return self.tail().filter(predicate)

    def windowed(self, n):
        this_window = to_python_list(self.take_list(n))
        return Sequence(this_window, lambda: self.tail().windowed(n))

def take(n, seq):
    if n == 0 or not seq:
        return empty
    else:
        return List(seq.head, take(n-1, seq.tail()))

def fibonacci(current=1, next=1):
    return Sequence(current, lambda: fibonacci(next, current + next))

def exists(lst,predicate):
    if lst is empty:
        return False
    else:
        return predicate(lst.head) or exists(lst.tail, predicate)

def primes(current=2, previous_primes=empty):
    if exists(previous_primes, lambda p: current % p == 0):
        return primes(current+1, previous_primes)
    else:
        new_prime_list = List(current, previous_primes)
        return Sequence(current, lambda: primes(current+1, new_prime_list))

#
# class Seq():
#     def __init__(self, state, next, value=lambda x: x):
#         self._state = state
#         self._next = next
#         self._value = value
#     def next(self):
#         return Seq(self._next(self._state), self._next, self._value)
#     def current(self):
#         return self._value(self._state)
#
#     def take(self, n):
#         if n > 0:
#             return List(self.current(), self.next().take(n-1))
#         else:
#             return empty
#
# evens = Seq(0, lambda x: x+2)
#
# def next_fibonacci_pair(pair): return (pair[1], pair[0] + pair[1])
# fibonacci = Seq((1,1), next_fibonacci_pair, lambda x: x[0])
