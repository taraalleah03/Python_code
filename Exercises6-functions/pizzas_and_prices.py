def unit_price(cm,euro):

    unitprice = euro / ((3.14 * (cm / 2) ** 2) / 10000)

    return unitprice

pizzas = []
prices = []

i = 1

while i <= 2:
    pizza = int(input(f"What is the diameter of the {i}.pizza(cm)? "))
    pizzas.append(float(pizza))
    price = int(input(f"What is the price of the {i}.pizza(€)? "))
    prices.append(float(price))
    i = i + 1

unit1 = (unit_price(pizzas[0],prices[0]))
unit2 = (unit_price(pizzas[1],prices[1]))

print(unit1) #this is just to check
print(unit2)

if unit1 < unit2:
    print(f"The first pizza has better value with a unit price of {round(unit1,2)}€/m²")
elif unit1 > unit2:
    print(f"The second pizza has better value with a unit price of {round(unit2,2)}€/m²")
else:
    print("Both pizzas have the same value")