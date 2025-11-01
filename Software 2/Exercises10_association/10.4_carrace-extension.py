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

#Module 9 section 4
cars =[]

for x in range(10):
    randommaxspeed = random.randint(100, 200)
    car = Car(f"ABC-{x+1}",randommaxspeed,0,0)
    cars.append(car)

racedone = False

while not racedone:

    for car in cars:
        randomspeed = random.randint(-10, 15) #this is for the car to accelerate
        car.accelerate(randomspeed)
        car.drive(1)

    if car.distance > 10000:
        racedone = True

winner = cars[0]
for car in cars:
    if car.distance > winner.distance:
        winner = car
print("The winner is", winner.rnum, "with", winner.distance, "km traveled!")

