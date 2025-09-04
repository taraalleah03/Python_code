import random

sumofdice = 0
r = int(input("How many dices do you want to roll? "))

for i in range(r):
    dice = random.randint(1, 6) #Have to have it inside the loop because if it's outside it will all be the same number
    sumofdice = sumofdice + dice
    print("You rolled a",dice,"!")

print("In total your dice rolls equal to",sumofdice)