y = int(input("Enter year: "))

if y % 400 == 0:
    print( y , "is a leap year!")
elif y % 4 == 0:
    print( y , "is a leap year!")
else:
    print( y , "is not a leap year.")