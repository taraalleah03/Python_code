cities = []

for r in range(5):
    city = input(f"Enter a city({r+1}/5): ")
    cities.append(city)

for city in cities:
    print(f"{city}")