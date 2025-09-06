num = int(input("Enter a number: "))

for i in range(2, num+1):
    if i % num == 0:
        print(num,"is a prime number")
    elif num > 1:
        print(num,"is not a prime number")