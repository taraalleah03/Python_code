import random
class Car:

    def __init__(self, rnum, maxspeed, speed, distance):
        self.rnum = rnum #rnum is short for registration number
        self.maxspeed = maxspeed
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed):
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

    def drive(self, hour):
        self.distance = self.distance + (self.speed * hour)
        return self.distance

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
        print("Race Status:")
        for car in self.cars:
            print(f"{car.rnum}: {car.speed} {car.distance} {car.maxspeed}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
            return False # if no car finished the race it returns false

cars =[]

for x in range(10):
    randommaxspeed = random.randint(100, 200)
    car = Car(f"ABC-{x+1}",randommaxspeed,0,0)
    cars.append(car)

derby = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not derby.race_finished():
    derby.hour_passes()
    hours += 1

derby.print_status()

winner = derby.cars[0]

for car in derby.cars:
    if car.distance > winner.distance:
        winner = car
print("The winner is", winner.rnum, "with", winner.distance, "km traveled!")
