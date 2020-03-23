def capitalIndexes(string):
    copy_str = string.lower()
    lst = []
    for i in range(len(string)):
        if (copy_str[i].upper() == string[i]) & (copy_str[i] != " "):
            lst.append(i)
    return lst


print(capitalIndexes("HeLlO"))
