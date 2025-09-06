num = int(input("Enter a number: "))

for i in range(2,num+1):

    if num%1 == 0:
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
