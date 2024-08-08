# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self,first_name,last_name,place,company,post):
        self.first_name = first_name
        self.last_name = last_name
        self.place = place
        self.company = company
        self.post = post
    def describe_user(self):
        print(f"Name:{self.first_name} {self.last_name} \nPlace:{self.place} \nCompany:{self.company} \nPost:{self.post}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} Good Morning , Welcome Back!")
obj =User("DEVANATHAN","A","PONDICHERRY","CHANGEPOND TECHNOLOGIES","PROGRAM ANALYST TRAINEE")
obj.describe_user()
obj.greet_user()
obj1 = User("RAGHUL","M","MADURAI","CHANGEPOND TECHNOLOGIES","PROGRAM ANALYST TRAINEE")
obj1.describe_user()
obj1.greet_user()
obj2 =User("AJITHKUMAR","A","CHENNAI","CHANGEPOND TECHNOLOGIES","PROGRAM ANALYST TRAINEE")
obj3 =User("BASHIL","H","NAVALLUR","CHANGEPOND","PAT")
obj4 = User("SURESH","K","THIRUNELVELI","CHANGEPOND","PAT")
obj2.describe_user()
obj2.greet_user()
obj3.describe_user()
obj3.greet_user()
obj4.describe_user()
obj4.greet_user()
