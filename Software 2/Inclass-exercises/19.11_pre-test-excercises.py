
class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def printinfo(self):
        print("Food:", self.name)
        print("Calories:", self.calories)

class Fruit(Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet

    def printinfo(self):
        super().printinfo()
        print(f"Sweet: {'Yes' if self.is_sweet else 'No'}")

class Vegetable(Food):
    def __init__(self, name, calories, is_leafy):
        super().__init__(name, calories)
        self.is_leafy = is_leafy

    def printinfo(self):
        super().printinfo()
        print(f"Leafy: {'Yes' if self.is_leafy else 'No'}")

class Store:
    def __init__(self):
        self.inventory = {}

    def add_product(self,food):
        self.inventory[food.name.lower()] = food

    def show_product(self):
        print("Inventory:")
        for food in self.inventory.values():
            food.printinfo()

    def buy_product(self, product_name):
        name = product_name.lower()
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None

class Smoothie:
    def __init__(self, name: object, ingredients):
        self.name = name
        self.ingredients = ingredients

        total = 0
        for item in ingredients:
            total += item.calories

        self.total_calories = total

    def smoothie_info(self):
        print("Total calories:", self.name)
        print("Ingredients:")

        for item in self.ingredients:
            print(item.name)

        print("Total calories:", self.total_calories)


prisma = Store()

banan = Fruit("Banana", 15, True)
brocolli = Vegetable("Brocolli", 20, False)
apple = Fruit("Apple", 10, True)
berry = Fruit("Blueberry", 10, True)
cucumber = Vegetable("Cucumber", 20, False)

prisma.add_product(banan)
prisma.add_product(brocolli)
prisma.add_product(apple)
prisma.add_product(berry)

prisma.show_product()

ingredients = []
print("Welcome to Prisma! We have the following, choose what you want for your smoothie:")

while True:
    i = input("Add an ingredient to your smoothie (empty to finish): ")
    if i.lower() == "":
        break

    product = prisma.buy_product(i)
    if product :
        ingredients.append(product)
        print(f"Added {product.name}")
    else:
        print("This ingredient is not available.")

    if len(ingredients) == 0:
        print("No ingredients added.")

if ingredients:
    name = input("what is the smoothie called?: ")
    smoothie = Smoothie(name, ingredients)
    smoothie.smoothie_info()
else:
    print("cancelled")


"""
food1 = Food("Celery", 10)
food1.printinfo()
food2 = Food("Apple", 20)
food2.printinfo()

food3 = Fruit("Banana", 15, True)
food3.printinfo()
food4 = Vegetable("Brocolli", 20, False)
food4.printinfo()
"""




