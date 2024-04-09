def convert(path):
    photo = ""
    with open(path, 'rb') as file:
        photo = file.read()
    return photo


print(convert("img.png"))