class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.elevator = bottom #this is where the elevator is currently

    def floor_up(self):
        if self.elevator < self.top:
            self.elevator += 1

    def floor_down(self):
        if self.bottom < self.elevator:
            self.elevator -= 1

    def go_to_floor(self, floor_togo):
        while self.elevator < floor_togo:
            self.floor_up()
        while self.elevator > floor_togo:
            self.floor_down()
        print ("You have made it to your destination!")

class Building:
    def __init__(self, bottom, top, num_floors):
        self.floors = []

        for i in range(num_floors):
            new_floor = Elevator(bottom, top)
            self.floors.append(new_floor)




