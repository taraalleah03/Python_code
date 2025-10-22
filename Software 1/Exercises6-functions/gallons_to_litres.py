def gallons_to_litres(g):
    conversion = g * 3.78541
    return conversion

g = int(input("Input amount of gallons: "))

while g > 0:
    print(g,"gallons is equal to",round(gallons_to_litres(g),2))
    g = int(input("Input amount of gallons: "))

print("Negative number given, conversion exited")