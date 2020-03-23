def ints_only(lst):
    for item in lst:
        if type(item) != type(int()):
            return False
    return True

print(ints_only([1, 2]))
