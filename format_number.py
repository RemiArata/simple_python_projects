def format_num(num):
    num = str(num)[::-1]
    new = ""
    j = 0
    for char in num:
        print(j)
        if j == 3:
            j = 1
            new += ","
            new += char
        else:
            j += 1
            new += char
    return new[::-1]
print(format_num(1000000000))
