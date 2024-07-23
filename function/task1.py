# # Initial veg_starter list
# veg_starter = ['paneer 65', 'chilly paneer', 'veg crispy']

# # Function to display the menu card
# def display_menu():
#     global veg_starter
#     print("Menu Card:")
#     for item in veg_starter:
#         print(item.capitalize())

# # Function to add a starter to the menu card
# def add_starter():
#     global veg_starter
#     new_starter = input("Which starter do you want to add to the menu? ").lower()
#     if new_starter not in veg_starter:
#         veg_starter.append(new_starter)
#         print(f"Added Successfully: {new_starter.capitalize()}")
#     else:
#         print(f"{new_starter.capitalize()} is already in the menu!")

# # Function to update a starter in the menu card
# def update_starter():
#     global veg_starter
#     old_starter = input("Which starter do you want to update in the menu? ").lower()
#     if old_starter in veg_starter:
#         new_starter = input(f"What is the new name for {old_starter.capitalize()}? ").lower()
#         index = veg_starter.index(old_starter)
#         veg_starter[index] = new_starter
#         print(f"Updated Successfully: {old_starter.capitalize()} to {new_starter.capitalize()}")
#     else:
#         print(f"{old_starter.capitalize()} is not in the menu!")

# # Function to remove a starter from the menu card
# def remove_starter():
#     global veg_starter
#     starter_to_remove = input("Which starter do you want to remove from the menu? ").lower()
#     if starter_to_remove in veg_starter:
#         veg_starter.remove(starter_to_remove)
#         print(f"Removed Successfully: {starter_to_remove.capitalize()}")
#     else:
#         print(f"{starter_to_remove.capitalize()} is not in the menu!")

# # Main function to demonstrate the operations
# def main():
#     while True:
#         print("\n1) Display menu card")
#         print("2) Add Starter in the menu card")
#         print("3) Update Starter in the menu card")
#         print("4) Remove Starter in the menu card")
#         print("5) Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             display_menu()
#         elif choice == 2:
#             add_starter()
#         elif choice == 3:
#             update_starter()
#         elif choice == 4:
#             remove_starter()
#         elif choice == 5:
#             break
#         else:
#             print("Invalid choice! Please choose a valid option.")

# if __name__ == "__main__":
#     main()
# Initial veg_starter list
veg_starter = ['paneer 65', 'chilly paneer', 'veg crispy']

# Function to display the menu card
def display_menu(menu):

    print("Menu Card:")
    for item in menu:
        print(item)

# Function to add a starter to the menu card
def add_starter(menu, new_starter):
   
    if new_starter not in menu:
        menu.append(new_starter)
        print(f"Added Successfully: {new}")
    else:
        print(f"{new_starter} is already in the menu!")

# Function to update a starter in the menu card
def update_starter(menu, old_starter, new_starter):
    
    if old_starter in menu:
        index = menu.index(old_starter)
        menu[index] = new_starter
        print(f"Updated Successfully: {old_starter} to {new_starter}")
    else:
        print(f"{old_starter} is not in the menu!")

# Function to remove a starter from the menu card
def remove_starter(menu, starter_to_remove):

    if starter_to_remove in menu:
        menu.remove(starter_to_remove)
        print(f"Removed Successfully: {starter_to_remove}")
    else:
        print(f"{starter_to_remove} is not in the menu!")

# Main function to demonstrate the operations
def main():
   
    while True:
        print("\n1) Display menu card")
        print("2) Add Starter in the menu card")
        print("3) Update Starter in the menu card")
        print("4) Remove Starter in the menu card")
        print("5) Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_menu(veg_starter)
        elif choice == 2:
            new_starter = input("Which starter do you want to add to the menu? ")
            add_starter(veg_starter, new_starter)
        elif choice == 3:
            old_starter = input("Which starter do you want to update in the menu? ")
            new_starter = input(f"What is the new name for {old_starter}? ")
            update_starter(veg_starter, old_starter, new_starter)
        elif choice == 4:
            starter_to_remove = input("Which starter do you want to remove from the menu? ")
            remove_starter(veg_starter, starter_to_remove)
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
