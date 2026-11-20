def emcsqr():
    c = 300000000
    userinput = int(input("Give a mass in Kg as an integer for me to calculate E=mc²: "))
    E = (userinput)*(c**2)
    return(E)

print(emcsqr())

