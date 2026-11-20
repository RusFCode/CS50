def SnakeCase():
    userinput = str(input("camelCase: ")).strip(" ")
    snake_string = ""
    for char in userinput:
        if char.isupper():
            snake_string += "_"
            snake_string += char.lower()
        else:
            snake_string += char
    print(snake_string)

SnakeCase()
