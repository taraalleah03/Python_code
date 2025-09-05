nlist = []

a = int(input("How many students are in class? "))

def ask():
    n = (input("Which nationality are you? "))
    nlist.append(n)
    return

for i in range(a) :
    ask()

print("The nationalities in your class are" , *nlist, sep="\n") #sep stands for separator

