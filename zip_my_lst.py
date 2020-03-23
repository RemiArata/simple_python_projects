def zap(lst1, lst2):
    new_lst = []
    for i in range(0, len(lst1)):
         new_lst.append(tuple([lst1[i], lst2[i]]))
    return new_lst

print(zap([1, 2, 3], [4, 5, 6]))
