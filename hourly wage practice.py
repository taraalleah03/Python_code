wage = float(input("What is your hourly wage: "))
hours = float(input("How many hours have you worked? "))
day = input("Which day of the week? ").lower()

#okay so made this way longer than it should be lol , could have just used if else

if day == "monday":
    print("You made a total of", wage*hours, " euros")
elif day == "tuesday":
    print("You made a total of", wage*hours, " euros")
elif day == "wednesday":
    print("You made a total of", wage * hours, " euros")
elif day == "thursday":
    print("You made a total of", wage*hours, " euros")
elif day == "friday":
    print("You made a total of", wage*hours, " euros")
elif day == "saturday":
    print("You made a total of", 2*wage*hours , " euros")
elif day == "sunday":
    print("You made a total of", 2*wage*hours, " euros")

else:
    print("Enter a valid day")