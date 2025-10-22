numlist = []

while numlist != "":
    num = (input("Enter a number: "))

    if num == "":
        break

    numlist.append(int(num))

numlist.sort()
dnumlist = sorted(numlist, reverse= True)
print(dnumlist)
