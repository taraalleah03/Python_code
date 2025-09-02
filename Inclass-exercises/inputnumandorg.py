numbers = []

num = int(input("New item: "))

while numbers != 0:
    numbers.append(num)
    print("The list is now: ", numbers)
    print("The list in order: ", sorted(numbers))
    num = int(input("New item: "))

    if num == 0:
        print("Exited program")
        break