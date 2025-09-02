glist= ["eggs", "ham", "bacon"]

items = input("What item have you bought from your grocery list: ").lower()
if items in glist:

    while glist != "":

        glist.remove(items)
        print("You still have to buy", glist)
        items = input("What else have you bought: ").lower()

        if items != "eggs" and items != "ham" and items != "bacon":
            print("Sorry, you don't have that item")
            break

else:
    print("Sorry, you don't have that item")

print("You still have to buy", glist)
