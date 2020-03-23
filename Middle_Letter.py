def midLet(string):
    if len(string) % 2 == 0:
        return ""
    else:
        return string[len(string) // 2] 


print(midLet("Hello"))