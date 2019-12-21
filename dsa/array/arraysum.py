def pair_sum(arr, k):
    counter = 0
    lookup = set()
    for num in arr:
        if k - num in lookup:
            counter += 1
        else:
            lookup.add(num)
    return counter

print(pair_sum([1,3,2,2],4))