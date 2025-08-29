c = input("Enter you cabin class: ").lower()

if c == "lux":
    print("LUX: upper-deck cabin with a balcony.")
elif c == "a":
    print("A: above the car deck, equipped with a window.")
elif c == "b":
    print("B: windowless cabin above the car deck.")
elif c == "c":
    print("C: windowless cabin below the car deck.")

else:
    print("Invalid cabin class")

