def convert(userString):
    Ruserstring = userString.replace(":)","🙂").replace(":(","🙁")
    return(Ruserstring)

def main():
    userinput = str(input("Give me You sentence: "))
    print(convert(userinput))

main()
