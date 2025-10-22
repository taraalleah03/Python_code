class Car:

    def __init__(self,brand,color,mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def drive(self,distance):
        self.mileage = self.mileage + distance
        print(f"The {self.brand} that is {self.color} has drove a total of {self.mileage} miles.")
        return

    def repaint(self,color):
        print(f"The {self.brand} that was {self.color} is now {color}")
        self.color = color

car1 = Car('Toyota','red',0)
car2 = Car('Audi','blue',0)

car1.drive(10)
car2.drive(20)
car1.drive(10)
car2.repaint('yellow')
car2.repaint('pink')


