math = int(input("Enter your score for Math: "))
physics = int(input("Enter your score for Physics: "))
programming = int(input("Enter your score for Programming: "))

maximumgrade = 15
total = math + physics + programming
percentage = float((total/ maximumgrade) * 100)

print("Your total score is: ", percentage , "%")


