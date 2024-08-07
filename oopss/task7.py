class ShoppingCard:
    items = {
        "pizza": 1000,
        "sandwich": 300,
        "fruits": 130,
        "foods": 130,
        "perfume": 1400,
        "icecream": 1050,
        "watermelon": 150,   
    }

    def __init__(self):
        self.user_items = {}

    def display(self):
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: {price}")

    def user_display(self):
        print("Items in your cart:")
        for item, price in self.user_items.items():
            print(f"{item}: {price}")

    def add_item(self, item):
        if item in self.items:
            self.user_items[item] = self.items[item]
            print(f"Added {item} to the cart.")
        else:
            print(f"{item} is not available.")

    def remove_item(self, item):
        if item in self.user_items:
            del self.user_items[item]
            print(f"Removed {item} from the cart.")
        else:
            print(f"{item} is not in your cart.")

    def total_items(self):
        total_items_count = len(self.user_items)
        print(f"Total Items: {total_items_count}")
        return total_items_count

    def total_price(self):
        total = sum(self.user_items.values())
        print(f"Total Price: {total}")
        return total

# Example usage
shopping_cart = ShoppingCard()

# Display available items
shopping_cart.display()

# Add items to the cart
shopping_cart.add_item('pizza')
shopping_cart.add_item('sandwich')
shopping_cart.add_item('perfume')

# Display items in the cart
shopping_cart.user_display()

# Display total items and price
shopping_cart.total_items()
shopping_cart.total_price()

# Remove an item from the cart
shopping_cart.remove_item('sandwich')

# Display items in the cart again
shopping_cart.user_display()

# Display total items and price again
shopping_cart.total_items()
shopping_cart.total_price()
