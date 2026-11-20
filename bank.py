def greetings_check():
    userinput = str(input("Greting: ")).strip(" ").lower()

    if userinput.find("hello") == 0:
        print("$0")
    elif userinput.find("h") == 0:
        print("$20")
    else:
        print("$100")

greetings_check()
