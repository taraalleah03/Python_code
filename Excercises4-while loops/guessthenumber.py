import random

num = random.randint(1, 10)
#print(random.randint(0,11))

guess = int(input("Guess the number: "))

if guess == num:
    print("You got it first try!")

while guess != num :
    #print("Sorry try again") this is just extra
    #print(num) this was to check if the random number is the same for every guess
    if guess < num:
        print("Your number is too low")
    elif guess > num:
        print("Your number is too high")
    else:
        print("Invalid input")

    guess = int(input("Guess the number: "))

else:
    print("Correct!")


