name = input("What is your name? ")
soupprice = 5.90

if name == "Matti":
    print("You had soup already!")
else:
    portions = float(input("Hi "+ name + "!,how many portions of soup would you like? "))
    print("Your total cost will be ",round(soupprice*portions,2))

print("Next please!")