class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.elevator = bottom #this is where the elevator is currently

    def floor_up(self):
        if self.elevator < self.top:
            self.elevator += 1
            print(f"The elevator has moved one floor up. Now on floor {self.elevator}")

    def floor_down(self):
        if self.bottom < self.elevator:
            self.elevator -= 1
            print(f"The elevator has moved one floor down. Now on floor {self.elevator}")

    def go_to_floor(self, floor_togo):
        while self.elevator < floor_togo:
            self.floor_up()
        while self.elevator > floor_togo:
            self.floor_down()

class Building:

    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            new_elevator = Elevator(bottom, top)
            self.elevators.append(new_elevator)

    def run_elevator(self, num, destination):
        print(f"\nElevator{num} is moving to {destination}.")
        self.elevators[num].go_to_floor(destination)

    def fire_alarm(self):
        print("\nFire alarm warning! All elevators must move to the bottom floor!\n")
        for floor in self.elevators:
            floor.go_to_floor(floor.bottom)

h = Elevator(0, 7)
h.go_to_floor(6)
h.go_to_floor(2)
building = Building(0, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2,7)
building.fire_alarm()

