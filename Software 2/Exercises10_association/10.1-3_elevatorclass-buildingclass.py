class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.elevator = bottom #this is where the elevator is currently

    def floor_up(self):
        self.top = elevator + 1

    def floor_down(self):
        self.bottom = elevator - 1

    def go_to_floor(self, elevator):
        if elevator < self.top:
            self.floor_up(elevator)
        elif elevator > self.bottom:
            self.floor_down(elevator)
        else:
            print ("You have made it to your destination!")

