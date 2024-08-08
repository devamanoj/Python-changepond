# 9-1. Restaurant: Make a class called Restaurant. The _init_() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant Name : {self.restaurant_name} \n cuisine_type : {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open.")
obj = Restaurant("Copper Kitchen","South Indian Authentic")
print(obj.restaurant_name)
print(obj.cuisine_type)
obj.describe_restaurant()
obj.open_restaurant()
obj1 = Restaurant("Mani's dum briyani","seeraga samba briyani")
obj2 = Restaurant("Hotel Salem","South Indian Cuisine.")
obj3 = Restaurant("Sukku Bai Briyani","multicusine")
obj1.describe_restaurant()
obj1.open_restaurant()
obj2.describe_restaurant()
obj2.open_restaurant()
obj3.describe_restaurant()
obj3.open_restaurant()
