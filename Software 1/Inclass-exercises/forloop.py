names = []

name =input("Enter name to the list: ")

while name != "":
    names.append(name)
    name = input("Enter another name to the list: ")

for name in names:
    print("Hi", name)