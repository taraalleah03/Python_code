name = input("What is your name? ").lower()
soupprice = 5.90

if name == "matti" :
    print("You had soup already!")
else:
    portions = float(input("Hi "+ name + "!,how many portions of soup would you like? "))
    print("Your total cost will be ",round(soupprice*portions,2))

#can also be in this format
#if name != "Matti":
    #p = int(input("How many portions of soup?"
    #print(f"Total cost is {p * 5.9}")
#else:
    #print("Next please!")

print("Next please!")