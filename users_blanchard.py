# Instructions:

# Make a class called User.

# Create two attributes called first_name and last_name, and then create several other 
# attributes (at least 2 more) that are typically stored in a user profile.

# Make a method called describe_user() that prints a summary of the user’s information.

# Make another method called greet_user() that prints a personalized greeting to the user.

# Create 3 instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"His first name is {self.first_name}, his last name is {self.last_name}, his age is {self.age}, and the city he lives in is {self.city}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Hope you are having a great day today!")

user_information1 = User("Chase", "Blanchard", 16, "St. Louis")
user_information1.describe_user()
user_information1.greet_user()
print("")
user_information2 = User("Bill", "Nye", 68, "Washington D.C.")
user_information2.describe_user()
user_information2.greet_user()
print("")
user_information3 = User("Wayne", "Gretzky", 63, "Brantford, Canada")
user_information3.describe_user()
user_information3.greet_user()
