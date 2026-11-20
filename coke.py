def money_change():
    amount_due = 50

    while amount_due > 0:
        userinput = int(input("Insert Coin: "))
        if userinput == 25 or userinput == 10 or userinput == 5:
            amount_due -= userinput
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")

    print(f"Change owed: {amount_due*-1}")

money_change()
