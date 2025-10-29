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
                print(f"The speed of the car cannot be negative, the car has {self.speed} km/h")
        else:
            addspeed = speed + self.speed
            self.speed = addspeed
            if addspeed > self.maxspeed:
                self.speed = self.maxspeed
                print(f"The car has reached its maximum speed of {self.speed} km/h")
            else:
                print(f"The car has a speed of {self.speed} km/h")


car1 = Car('ABC-123', 142,0,0)

#print(car1.rnum)
#print(car1.maxspeed)
#print(car1.curspeed)
#print(car1.distance)
print(f"The car with the registration number of {car1.rnum} has a max speed of {car1.maxspeed} km/h."
      f"\nIt's current speed is {car1.speed} km/h and distance is {car1.distance} km.")
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)



