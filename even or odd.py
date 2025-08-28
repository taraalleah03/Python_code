num = int(input("Enter a number: "))

if num >0:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative or zero")