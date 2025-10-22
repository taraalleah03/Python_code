class Car:

    def __init__(self,brand,color,mileage,fuel):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def drive(self,distance):
        fueltouse = distance * 0.5
        
        if fueltouse > self.fuel:
            print(f"Sorry, there is not enough fuel for the {self.brand} to drive {distance} kilometers.")
        else:
            self.mileage = self.mileage + distance
            self.fuel = self.fuel - (distance * 0.5)
            print(f"The {self.brand} that is {self.color} has drove a total of {self.mileage} kilometers. The remaining fuel is: {self.fuel}")
        return

    def repaint(self,color):
        print(f"The {self.brand} that was {self.color} is now {color}")
        self.color = color

car1 = Car('Toyota','red',0,100)
car2 = Car('Audi','blue',0,100)

car1.drive(10)
car2.drive(20)
car1.drive(10)
car2.repaint('yellow')
car2.repaint('pink')
car1.drive(300)
car1.drive(20)



