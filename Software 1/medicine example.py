age = int(input("How old are you? "))
weight = 0

if age <= age < 18:
    weight = float(input("What is your weight in kg? "))

if age>=18 or age>=15 and weight>=55:
    print("You can take the medicine")

else:
    print("You can not take the medicine")
