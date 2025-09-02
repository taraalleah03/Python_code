user = input("Create a username: ")
password = input("Create a password: ")

loginuser = input("Enter your username: ")
loginpassword = input("Enter your password: ")

tries = 1

while loginuser != user or loginpassword != password:

    while tries < 5:
        print("Wrong username or password, try again")

        loginuser = input("Enter your username: ")
        loginpassword = input("Enter your password: ")

        tries += 1

        if tries == 5:
            print("Access Denied")
            break

        elif loginuser == user and loginpassword == password:
            print("Welcome")
            break


