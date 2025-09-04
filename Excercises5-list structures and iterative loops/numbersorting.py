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

l = len(dnumlist) #this is to check how many elements are in the list using the built in len() function
i = 0

if l > 5: #it makes more sense to me to use while in this situation
    while i < 5 :
        print(dnumlist[i])
else:
    print(dnumlist)

#I tested this out with multiple numbers with carrying digits ,and it doesn't seem to work that well, it works best with 1 digit numbers, is it cuz they're string?