import random

roll = 0

def roll_dice(sides):
    roll = random.randint(1, sides)
    return roll

sides = int(input("How many sides does the dice have? "))

while roll != sides: #sides will act as the max amount you can roll
    roll = roll_dice(sides)
    print("You rolled a",roll,"!")