numlist = []

num= (input("Enter a number: "))
numlist.append(num)

while numlist != "":
    num = (input("Enter a number: "))
    numlist.append(num)

    if num == "":
        break

numlist.sort()
numlist.remove(numlist[0]) #this is to remove the blank space that ends the while loop
intlist = list(map(int, numlist))

dnumlist = sorted(numlist, reverse= True)
print(dnumlist)

#I tested this out with multiple numbers with varying digits ,and it doesn't seem to work that well, it works best with 1 digit numbers, is it cuz they're string?