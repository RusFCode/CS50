def math_interpreter():
    userinput = str(input("Expression: ")).strip(" ").replace(" ", "")
    operators = ["+", "-", "*", "/"]
    r = 0

    for operator in operators:
        if operator in userinput:
            numbersList = userinput.split(operator)
            x = int(numbersList[0])
            z = int(numbersList[1])

            if operator == "+":
                r = float(x+z)
            elif operator == "-":
                r = float(x-z)
            elif operator == "*":
                r = float(x*z)
            else :
                r = float(x/z)
            break

    print(round(r,1))

math_interpreter()
