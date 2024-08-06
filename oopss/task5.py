#menu dictionary using oops
class MenuCard:
    def __init__(self):
        self.menu = {
            'paneer 65': 'Spicy fried paneer',
            'chilly paneer': 'Paneer in spicy chili',
            'veg crispy': 'Crispy fried'
        }

    def display_menu(self):
        print("Menu Card:")
        for key, value in self.menu.items():
            print(f"{key}: {value}")
        print("\n")

    def add_starter(self, starter_name, starter_details):
        self.menu[starter_name] = starter_details
        print(f"'{starter_name}' has been added to the menu.\n")

    def update_starter(self, old_starter, new_starter, new_details):
        if old_starter in self.menu:
            del self.menu[old_starter]
            self.menu[new_starter] = new_details
            print(f"'{old_starter}' has been updated to '{new_starter}' with new details.\n")
        else:
            print(f"'{old_starter}' not found in the menu.\n")

    def remove_starter(self, starter):
        if starter in self.menu:
            del self.menu[starter]
            print(f"'{starter}' has been removed from the menu.\n")
        else:
            print(f"'{starter}' not found in the menu.\n")

class MenuOperations:
    def __init__(self):
        self.menu_card = MenuCard()

    def start(self):
        while True:
            print("Menu Operations:")
            print("1. Display menu card")
            print("2. Add starter to the menu card")
            print("3. Update starter in the menu card")
            print("4. Remove starter from the menu card")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.menu_card.display_menu()
            elif choice == '2':
                starter_name = input("Enter the starter name to add: ")
                starter_details = input("Enter the details of the starter: ")
                self.menu_card.add_starter(starter_name, starter_details)
            elif choice == '3':
                old_starter = input("Enter the starter name to update: ")
                new_starter = input("Enter the new starter name: ")
                new_details = input("Enter the new details of the starter: ")
                self.menu_card.update_starter(old_starter, new_starter, new_details)
            elif choice == '4':
                starter = input("Enter the starter name to remove: ")
                self.menu_card.remove_starter(starter)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    operations = MenuOperations()
    operations.start()
