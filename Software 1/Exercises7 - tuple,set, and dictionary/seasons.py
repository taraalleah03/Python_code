seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Enter a number of a month(1-12): "))

if month in (12, 1, 2):
    ms = seasons[3]  #winter
    print(f"The month {month} is {ms} season")
elif 3 <= month <= 5:
    ms = seasons[0]  #spring
    print(f"The month {month} is {ms} season")
elif 6 <= month <= 8:
    ms = seasons[1]  #summer
    print(f"The month {month} is {ms} season")
elif 9 <= month <= 11:
    ms = seasons[2]  #autumn
    print(f"The month {month} is {ms} season")
else:
    print("Invalid month number")