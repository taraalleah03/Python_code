import random

#The Monte Carlo simulation is a mathematical technique that predicts possible outcomes of an uncertain event.

N = int(input("How many random points would you like to generate? "))
n = 0

for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if ((x*x)+(y*y) < 1):
        n += 1

approx = (n*4)/N
print("The approximation of pi is", approx)


