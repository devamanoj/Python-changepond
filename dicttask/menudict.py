def display_menu(menu):
    print("Menu Card:")
    for key, value in menu.items():
        print(f"{key}: {value}")
    print("\n")

def add_starter(menu, starter_name, starter_details):
    menu[starter_name] = starter_details
    print(f"'{starter_name}' has been added to the menu.\n")

def update_starter(menu, old_starter, new_starter, new_details):
    if old_starter in menu:
        del menu[old_starter]
        menu[new_starter] = new_details
        print(f"'{old_starter}' has been updated to '{new_starter}' with new details.\n")
    else:
        print(f"'{old_starter}' not found in the menu.\n")

def remove_starter(menu, starter):
    if starter in menu:
        del menu[starter]
        print(f"'{starter}' has been removed from the menu.\n")
    else:
        print(f"'{starter}' not found in the menu.\n")

def main():
    menu_card = {
        'paneer 65': 'Spicy fried paneer ',
        'chilly paneer': 'Paneer in spicy chili',
        'veg crispy': 'Crispy fried '
    }

    while True:
        print("Menu Operations:")
        print("1. Display menu card")
        print("2. Add starter to the menu card")
        print("3. Update starter in the menu card")
        print("4. Remove starter from the menu card")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_menu(menu_card)
        elif choice == '2':
            starter_name = input("Enter the starter name to add: ")
            starter_details = input("Enter the details of the starter: ")
            add_starter(menu_card, starter_name, starter_details)
        elif choice == '3':
            old_starter = input("Enter the starter name to update: ")
            new_starter = input("Enter the new starter name: ")
            new_details = input("Enter the new details of the starter: ")
            update_starter(menu_card, old_starter, new_starter, new_details)
        elif choice == '4':
            starter = input("Enter the starter name to remove: ")
            remove_starter(menu_card, starter)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
