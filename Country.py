def display_menu():
    print("Country Application")
    print("Command Menu")
    print("View - View country name")
    print("Add - Add a counrty")
    print("Del - Delete a country")
    print("Exit - Exit application")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes:"
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
    display_codes(countries)
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country Name : {name}. \n")
    else:
        print("There is no country with that code. \n")

def add(countries):
    code = input("Enter a country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code. \n")
    else:
        name = input("Enter Country Name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added. \n")

def delete(countries):
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted. \n")
    else:
        print("There is no country with that code. \n")

def main():
    countries = {"US": "United States", "EN": "England", "IT": "Italy"}

    display_menu()

    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command, please try again. \n")

if  __name__ == "__main__":
    main()
