g = input("What is your gender(m/f)? ").lower()
h = float(input("What is your hemoglobin value (g/l)? "))

if g == "m":
    if h  < 134:
        print("Your hemoglobin is too low")
    elif 134 <= h <= 167:
        print("Your hemoglobin is normal")
    elif h > 167:
        print("Your hemoglobin is too high")

if g == "f":
    if h  < 117:
        print("Your hemoglobin is too low")
    elif 117 <= h <= 155:
        print("Your hemoglobin is normal")
    elif h > 155:
        print("Your hemoglobin is too high")
