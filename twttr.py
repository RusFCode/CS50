def DeleteVowels():
    userinput = str(input("Input: "))
    vowels_list = ["a","e","i","o","u","A","E","I","O","U"]

    for char in userinput:
        if char in vowels_list:
            userinput = userinput.replace(char, "")
    print(userinput)

DeleteVowels()
