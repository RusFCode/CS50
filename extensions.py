def extensions_check():
    userinput = str(input("File name: ")).strip(" ").lower()

    if userinput.find(".gif") != -1:
        print("image/gif")
    elif userinput.find(".jpg") != -1 or userinput.find(".jpeg") != -1:
        print("image/jpeg")
    elif userinput.find(".png") != -1:
        print("image/png")
    elif userinput.find(".pdf") != -1:
        print("application/pdf")
    elif userinput.find(".txt") != -1:
        print("text/plain")
    elif userinput.find(".zip") != -1:
        print("application/zip")
    else:
        print("application/octet-stream")

extensions_check()
