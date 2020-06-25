def product(*sets):
    if len(sets) == 0:
        return {()}
    else:
        return {(x,) + rest for x in sets[0] for rest in product(*sets[1:])}


def split(*args):
    print (args[0])
    print(args[1:])
