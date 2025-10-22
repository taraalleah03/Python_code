x = 0

while x == 0:
    x = int(input("Enter inches: "))

    if x > 0:
        print(x, "inches converts to", x*2.54, "cm")
        x = 0

    elif x < 0:
        print("Invalid number")