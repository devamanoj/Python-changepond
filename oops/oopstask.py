class Product:
    prodcount = 0
    
    def __init__(self, prodname, prodprice, proddescription):
        self.prodname = prodname
        self.prodprice = prodprice
        self.proddescription = proddescription
        Product.prodcount += 1
        self.id = Product.prodcount
    
    def getProdDetails(self):
        print("Product ID:", self.id)
        print("Product Name:", self.prodname)
        print("Product Price:", self.prodprice)
        print("Product Description:", self.proddescription)
    
    @staticmethod
    def addProduct(prodname, prodprice, proddescription):
        return Product(prodname, prodprice, proddescription)
    
    def addToCart(self, cart):
        cart.append(self)
        print(f"Product '{self.prodname}' is succesfully added.")

# Example usage
p1 = Product.addProduct("Laptop", 75000, "A high-performance laptop")
p2 = Product.addProduct("Smartphone", 30000, "A latest model smartphone")

# Display product details
p1.getProdDetails()
print("-" * 70)
p2.getProdDetails()

print("=" * 70)

# Simulating a shopping cart
cart = []
p1.addToCart(cart)
p2.addToCart(cart)

# Display cart contents
print("Cart Contents:")
for product in cart:
    product.getProdDetails()
