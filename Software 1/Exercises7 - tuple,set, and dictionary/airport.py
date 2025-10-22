airports = {
    "AGAF": "Afutara Airport",
    "BGAT": "Attu Heliport",
    "CYAL": "Alert Bay Airport",
    "DAAJ": "Tiska Airport"
}

while True:
    user_input = input("Choose what to do (add/fetch/quit) : ").lower()

    if user_input == "add":
        code = input("What is the airport's ICAO code? ")
        name = input("What is the name of the airport? ")
        airports[code] = name
        print(f"The airport {name} had been added with the code: {code}.")

    elif user_input == "fetch":
        code = input("What is the airport's ICAO code? ")
        if code in airports:
            print(f"The airport's name is {airports[code]}.")
        else:
            print("This airport is not in the dictionary.")

    elif user_input == "quit":
        break

    else:
        print("Invalid input.")

print("Session ended")