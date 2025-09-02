colors = ["red", "green", "yellow", "blue", "pink"]

x = input("What is your favorite color? ").lower()

if x in colors:
    print("Your favourite color is in the list!", colors)
    print("Your color's index is", colors.index(x))
else:
    y = input("Your color is not in the list, would you like to add it?(yes/no) ").lower()

    if y == "yes":
        colors.append(x)
        print(colors)
    elif y == "no":
        print("Ok!")
    else:
        print("Invalid input")

