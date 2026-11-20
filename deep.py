def response_to_universe():
    userinput = str(input("What is the Answer to the Great Question of life ? ")).strip(" ").lower()
    if userinput == "42" or userinput == "forty-two" or userinput == "forty two":
        print("Yes")
    else:
        print("No")

response_to_universe()
