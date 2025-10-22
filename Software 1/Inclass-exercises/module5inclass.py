names = ["Princess", "Maria", "Tara", "Clary"]
surnames = ["John", "Smith"]
x = 0
while x <= 3:
    print(names[x])
    x += 1

print(names[1:3]) #does not print the last value
print(names[0:]) #prints until the end
print(len(names))

names.append("Ana")
print(names)

names.insert(0, "Joshua")
print(names)
names.remove("Joshua")
print(names)

names.extend(surnames)
print(names)

maria = names.index("Maria")
print(maria)

if "Joshua" in names:
    print("Joshua was found")
else:
    print("Joshua was not found")

names.sort(reverse=True)
print(names)

