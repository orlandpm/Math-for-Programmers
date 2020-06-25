def fits(bin_size, items, bins):
    return [(item, bin_index, bin)
                for item in set(items)
                for bin_index,bin in enumerate(bins)
                if sum(bin) + item <= bin_size]

def add(item, bin_index, bins):
    return [bin if i != bin_index else [item] + bin[:]
                for i,bin in enumerate(bins)]

def rest(item, items):
    if len(items) == 1:
        return []
    elif items[0] == item:
        return items[1:]
    else:
        return [items[0]] + rest(item, items[1:])

def all_packs(bin_size, items, bins=[]):
    if items:
        all_fits = fits(bin_size, items, bins)
        if all_fits:
            for (item, bin_index, bin) in all_fits:
                next = add(item, bin_index, bins)
                for p in all_packs(bin_size, rest(item,items), next):
                    yield p
        else:
            for p in all_packs(bin_size, items, bins[:] + [[]]):
                yield p
    else:
        yield bins

def best_pack(bin_size, items):
    all = all_packs(bin_size, items)
    return min(all, key=len)
