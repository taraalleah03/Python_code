import random

roll = 0

def roll_dice():
    roll = random.randint(1, 6)
    return roll


while roll != 6:
    roll = roll_dice()
    print("You rolled a",roll,"!")








