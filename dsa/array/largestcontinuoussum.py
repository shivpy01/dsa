def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_num = sum = arr[0]

    for n in arr[1:]:
        sum = max(sum + n, n)
        max_num = max(sum, max_num)
    return max_num
    pass


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))