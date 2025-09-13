names = set()

name = (input("Enter a name? "))

while name != "":

    if name in names:
        print("Existing name")
    elif name == "":
        break
    else:
        print("New name")

    names.add(name)
    name = input("Enter a name? ")


print("Your set of names are:")
for i in names:
    print(i)

