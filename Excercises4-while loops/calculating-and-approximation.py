import random

#The Monte Carlo simulation is a mathematical technique that predicts possible outcomes of an uncertain event.

p = int(input("How many random points would you like to generate? "))
r = 0
while r != p:
    x = random.randint(1,100)
    y = random.randint(1,100)

    check = (x*x)+(y*y)

    if check < 1:
        print("(",x,",",y,") points are in the circle")
    else:
        print("(",x,",",y,") points are not in the circle")

r += 1
