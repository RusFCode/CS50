def Fruits_Calories():

    fruits_dict = {
        "apple":130,
        "avocado":50,
        "banana":110,
        "cantaloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew Melon":50,
        "kiwifruit":90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80,
    }

    userinput = input("Item: ").strip(" ").lower()

    # Just to avoid O(n) and stay in O(1)
    
    try:
        print(f"Calories: {fruits_dict[userinput]}")
    except:
        pass

Fruits_Calories()
