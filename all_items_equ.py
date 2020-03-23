def all_equal(lst):
    for i in range(1, len(lst)):
        j = i - 1
        if lst[j] != lst[i]:
            return False
    return True

print(all_equal([1, 1, 1, 3]))
