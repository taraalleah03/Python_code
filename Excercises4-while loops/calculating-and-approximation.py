import random

#The Monte Carlo simulation is a mathematical technique that predicts possible outcomes of an uncertain event.

N = int(input("How many random points would you like to generate? "))
n = 0
i = 0 #number of points generated
while i < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if ((x*x)+(y*y) < 1):
        n += 1
i += 1

approx = (n*4)/N
print("The approximation of pi is", approx)


