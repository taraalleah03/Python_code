
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

day_n = int(input("Enter the day number(1-7): "))

day = days_of_the_week[day_n -1]

print("The day is: ", day )

#die roll

import random

def cast():
    first, second = random.randint(1,7), random.randint(1,7) #you can set two variables at once
    return first, second

die1, die2 = cast()
print(f"You rolled a {die1} and a {die2}")

fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits
print(f"The fruits are: {first}, {second} and {third}.")

