def permutations(lst):
    if not lst:
        yield []
    else:
        for index, value in enumerate(lst):
            leftovers = lst[:index] + lst[index+1:]
            for p in permutations(leftovers):
                yield [value] + p[:]

import itertools
list(itertools.islice(permutations([1,2,3,4,5,6,7,8,9,10]), 1000))
