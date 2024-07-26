def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

def main():
    print("Enter the number of toppings:")
    num_items = int(input())
    
    sandwich_items = []
    for _ in range(num_items):
        item = input("Enter an item: ")
        sandwich_items.append(item)
    
    # Unpack the list into the make_sandwich function
    make_sandwich(*sandwich_items)

if __name__ == "__main__":
    main()
