def primes(n):
    if n < 2:
        return {}
    elif n == 2:
        return {}
    else:
        lower_primes = primes(n-1)
        return {}


words = {"doctor", "loving", "tail", "weight", "rule", "lonely", "bike", 
            "circle", "tricky", "push", "whirly", "belief"}
