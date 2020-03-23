
def add_dots(string):
    new_str = list(string)
    return ".".join(new_str)


with_dots = add_dots("Remi")

def remove_dots(string):
    return string.replace(".", "")


without_dots = remove_dots(with_dots)

print(f'THis is the string with the dots: {with_dots}')
print(f'This is the string without the dots: {without_dots}')
