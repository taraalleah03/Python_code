import random
class Car:

    def __init__(self, rnum, maxspeed, speed, distance):
        self.rnum = rnum #rnum is short for registration number
        self.maxspeed = maxspeed
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed):

        self.speed += speed
        if self.speed < 0:
            self.speed = 0
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed

        """
        if speed < 0:
            minusspeed = speed
            self.speed = self.speed - minusspeed
            if self.speed > 0:
                self.speed = 0
                #print(f"The speed of the car cannot be negative, the car has {self.speed} km/h")
        else:
            addspeed = speed + self.speed
            self.speed = addspeed
            if addspeed > self.maxspeed:
                self.speed = self.maxspeed
                #print(f"The car has reached its maximum speed of {self.speed} km/h")
            else:
                self.speed = self.maxspeed
                #print(f"The car has a speed of {self.speed} km/h")
        """
    def drive(self, hour):
        self.distance = self.distance + (self.speed * hour)
        return self.distance

class ElectricCar(Car):

    def __init__(self, rnum, maxspeed, speed, distance,battery):
        self.battery = battery
        super().__init__(rnum, maxspeed,speed,distance)

class GasolineCar(Car):

    def __init__(self, rnum, maxspeed, speed, distance,tank):
        self.tank = tank
        super().__init__(rnum, maxspeed,speed,distance)

class Race:
    def __init__(self,name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self, hour = 1):
        for car in self.cars:
            randomspeed = random.randint(-10, 15)  # this is for the car to accelerate
            car.accelerate(randomspeed)
            car.drive(hour)

    def print_status(self):
        print("\nRace Status:\n")
        for car in self.cars:
            print(f"{car.rnum}: speed-{car.speed} distance-{car.distance} maxspeed-{car.maxspeed}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False # if no car finished the race it returns false

electric_car = ElectricCar("ABC-15", 180, 0, 0, 52.5)
gas_car = GasolineCar("ACD-123", 165, 0, 0,32.3)

electric_car.accelerate(110)
gas_car.accelerate(120)

electric_car.drive(3)
gas_car.drive(3)

print("The electric car drove a total of",electric_car.distance,"km.")
print("The gas car drove a total of",gas_car.distance,"km.")

'''
cars =[]

for x in range(10):
    randommaxspeed = random.randint(100, 200)
    car = Car(f"ABC-{x+1}",randommaxspeed,0,0)
    cars.append(car)

derby = Race("Grand Demolition Derby", 8000, cars)

print("WELCOME TO THE RACE! READY SET GO!")

hours = 0
while not derby.race_finished():
    derby.hour_passes()
    hours += 1
    if hours % 10 == 0:
        derby.print_status()

derby.print_status() #print once more at the end of the race

winner = derby.cars[0]

for car in derby.cars:
    if car.distance > winner.distance:
        winner = car
print("\nThe winner is", winner.rnum, "with", winner.distance, "km traveled!")
'''