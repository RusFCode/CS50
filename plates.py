def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) <= 6 and len(s) >=2:

        if s[0].isalpha() and s[1].isalpha():

            number_count = 0

            for char in s:
                if not char.isnumeric() and not char.isalpha():
                    return False
                if char.isnumeric() and number_count == 0 :
                    number_count += 1
                    if int(char) == 0:
                        return False
                if number_count > 0 and char.isalpha():
                    return False
            return True

        else:
            return False

main()
