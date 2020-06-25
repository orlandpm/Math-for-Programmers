from collections import namedtuple

List = namedtuple('List', ['head', 'tail'])

empty = None

def count(lst):
    if lst is empty:
        return 0
    else:
        return 1 + count(lst.tail)

def sum(lst):
    if lst:
        return lst.head + sum(lst.tail)
    else:
        return 0

def verbose_sum(lst):
    if lst:
        print("looking at list element: %s" % lst.head)
        return lst.head + verbose_sum(lst.tail)
    else:
        return 0

def to_python_list(lst):
    if lst is empty:
        return []
    else:
        return [lst.head] + to_python_list(lst.tail)

def from_python_list(lst):
    if lst:
        return List(lst[0], from_python_list(lst[1:]))
    else:
        return empty

def append(lst1, lst2):
    if lst1:
        return List(lst1.head, append(lst1.tail, lst2))
    else:
        return lst2

def print_list(lst):
    if lst:
        print(lst.head)
        print_list(lst.tail)

def contains(lst, element):
    if lst is empty:
        return False
    else:
        return (lst.head == element or contains(lst.tail, element))

def flatten(lst):
    if lst is empty:
        return lst
    elif isinstance(lst.head, List):
        return append(lst.head, lst.tail)
    else:
        return List(lst.head, lst.tail)

## Accumulators

def last(lst):
    if lst is empty:
        raise ValueError("no last element of empty list")
    elif lst.tail is empty:
        return lst.head
    else:
        return last(lst.tail)

def all_but_last(lst):
    if lst is empty:
        raise ValueError("expected non-empty list")
    elif lst.tail is empty:
        return empty
    else:
        return List(lst.head, all_but_last(lst.tail))

def reverse(lst):
    if lst is empty:
        return lst
    else:
        return List(last(lst), reverse(all_but_last(lst)))

def reverse(lst, acc=empty):
    if lst is empty:
        return acc
    else:
        return reverse(lst.tail, List(lst.head, acc))

def sum(lst, acc=0):
    if lst is empty:
        return acc
    else:
        return sum(lst.tail, acc + lst.head)

# def max(lst, default=None):
#     if lst is empty:
#         if default is None:
#             raise ValueError("Cannot find 'max' of an emtpy list.")
#         else:
#             return default
#     else:
#         if lst.head >

# max/min
# chunkbysize
# equals
# def reverse(lst):
#     def reverse_internal(acc,rest):
#countup
# distinct

def distinct(lst, previous=empty):
    if lst is empty:
        return lst
    elif contains(previous, lst.head):
        return distinct(lst.tail, previous)
    else:
        new_previous = List(lst.head, previous)
        return List(lst.head, distinct(lst.tail, new_previous))

def range(start, end):
    if start == end:
        return empty
    else:
        return List(start, range(start+1, end))


# countby
# findif

def map(f, lst):
    if lst is empty:
        return lst
    else:
        return List(f(lst.head), map(f,lst.tail))

def copy(lst):
    if lst is empty:
        return lst
    else:
        return List(lst.head, copy(lst.tail)) #<1>

def filter(p, lst):
    if lst is empty:
        return lst
    elif p(lst.head):
        return List(lst.head, filter(p, lst.tail)) #<1>
    else:
        return filter(p, lst.tail) #<2>

def count_if(p, lst):
    if lst is empty:
        return 0
    elif p(lst.head):
        return 1 + count_if(p, lst.tail)
    else:
        return count_if(p, lst.tail)

# countif
#map
#iterable
#filter
def reduce(f, lst, initial=None):
    if lst and lst.tail:
        return f(lst.head, reduce(f, lst.tail, initial))
    elif lst:
        return f(lst.head, initial) if initial else lst.head
    elif initial:
        return initial
    else:
        raise TypeError("reduce() of empty List with no initial value")

# def count_down(n):
#     if n <= 0:
#         return empty
#     else:
#         return cons(n, count_down(n-1))
#
# cons(1,cons(2,cons(3,empty)))



import unittest

class Test(unittest.TestCase):
    def test_len(self):
        self.assertEqual(count(cons(1,cons(2,cons(3,empty)))), 3)

    def test_count_down(self):
        self.assertEqual(count_down(2), (2,(1,empty)))
        self.assertEqual(count(count_down(10)), 10)

if __name__ == '__main__':
    unittest.main()
