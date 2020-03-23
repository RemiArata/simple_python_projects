def double_letters(string):
    for i in range(len(string) - 1):
        current = string[i].lower()
        next = string[i].lower()
        if current == next:
            return True
    return False


print(double_letters("HelLo"))