x = []

while x != "":
    y = (input("Enter a number: "))

    if y == "":
        break

    x.append(y)

print("exited program")
#map() function applies a given function to all elements in an iterable. Here, we use map(int, x) to convert each string in the list to an integer.
xnum = list(map(int, x))

print ("All the numbers you have are", xnum)

print("Your largest number is", max(xnum)) #using max() function with a list of numbers, it will return the largest number in the list
print("Your smallest number is", min(xnum)) #using min() function with a list of numbers, it will return the smallest number in the list