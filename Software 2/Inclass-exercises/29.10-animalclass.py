class Animal:

    def __init__(self, name, species, sound="womp womp"):
        self.name = name
        self.species = species
        self.sound = sound

    def speak(self):
        print(f'{self.name} says "{self.sound}"')

    def print_info(self):
        print(f'The name of the animal is {self.name}, it is a {self.species}')

class Lion(Animal):

    def __init__(self, name, species = "Mammal", sound = "Rawr"):
#        self.species = species
#        self.sound = sound
        super().__init__(name, species, sound)

class Elephant(Animal):

    def __init__(self, name, species = "Mammal", sound = "Honk"):
#        self.species = species
#        self.sound = sound
        super().__init__(name, species, sound)

class Snake(Animal):

    def __init__(self, name, species = "Reptile", sound = "Hiss"):
#        self.species = species
#        self.sound = sound
        super().__init__(name, species, sound)

class Zoo:
    def __init__(self):
        self.animals = []

    def animal_add(self, animal):
        self.animals.append(animal)
        return

    def print_all(self):
        total = len(self.animals)
        print(f"There are a total of {total}, all the animals are:")
        for a in self.animals:
            a.print_info()
        return

    def all_speak(self):
        for a in self.animals:
            a.speak()

anim1 = Animal("Mary", "Mammal")
anim2 = Lion("Leonard")
anim4 = Elephant("Eleanor")
anim3 = Snake("Sally")

zoo = Zoo()

zoo.animal_add(anim1)
zoo.animal_add(anim2)
zoo.animal_add(anim3)
zoo.animal_add(anim4)

zoo.print_all()
zoo.all_speak()