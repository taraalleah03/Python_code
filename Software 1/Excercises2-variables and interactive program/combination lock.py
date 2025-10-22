import random
randomlist1 = random.sample(range(0, 9), 3)
randomlist2 = random.sample(range(1, 6), 4)

#first method, kind of silly
#print("Your 3-digit random code is:", random.randrange(1, 10),random.randrange(1, 10), random.randrange(1, 10))

#second method ( chosen method )

print("Your 3-digit random code is: " , randomlist1)
print("Your 4-digit random code is: " , randomlist2)
