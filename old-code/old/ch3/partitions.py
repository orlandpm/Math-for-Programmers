def partitions_below(n, max_part):
    if n == 0:
        yield []
    else:
        for next_part in range(1,max_part+1):
            leftover = n - next_part
            if leftover >= 0:
                for p in partitions_below(leftover, next_part):
                    yield [next_part] + p[:]

def partitions(n):
    return partitions_below(n,n)
    # if n == 0:
    #     yield []
    # else:
    #     for max_part in range(1,n):
    #         yield partitions_below(n, max_part)

partitions(8)
