t = float(input("Enter talents: "))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))

g = ((((t * 20) + p) * 32) + l) * 13.3

print("The weight in modern units:\n",int(g * 0.001) ,"kilograms and" , round((g % 1000), 2),"grams." )