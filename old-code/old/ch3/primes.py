def primes():
    yield 2
    previous = {2}
    current = 3
    while True:
        factors = {p for p in previous if current % p == 0}
        print(current, previous, factors)
        if not factors:
            yield current
            previous.add(current)
        current += 1
