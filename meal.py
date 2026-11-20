def main():
    userinput = str(input("What time is it? ")).strip(" ").lower()
    eatingTime = convert(userinput)

    if eatingTime >= 7.0 and eatingTime <= 8.0:
         print("breakfast time")
    elif eatingTime >= 12.0 and eatingTime <= 13.0:
         print("lunch time")
    elif eatingTime >= 18.0 and eatingTime <= 19.0:
         print("dinner time")
    else:
         pass



def convert(time):
    if time.find("a.m.") != -1:
        timeClean = time.replace("a.m.", "")
        time_list = timeClean.split(":")
        return(float(time_list[0])+float(time_list[1])/60)

    elif time.find("p.m.") != -1:
        timeClean = time.replace("p.m.", "")
        time_list = timeClean.split(":")
        return(12+float(time_list[0])+float(time_list[1])/60)
    else:
        time_list = time.split(":")
        return(float(time_list[0])+float(time_list[1])/60)



if __name__ == "__main__":
    main()
