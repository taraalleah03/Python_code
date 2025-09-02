user = input("Create a username: ")
password = input("Create a password: ")

loginuser = input("Enter your username: ")
loginpassword = input("Enter your password: ")

while loginuser != user or loginpassword != password:

    print("Wrong username or password, try again")
    loginuser = input("Enter your username: ")
    loginpassword = input("Enter your password: ")


print("Welcome ")
