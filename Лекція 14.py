# Task 1. Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and adds a property author and a method called read that prints information about the book.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

# Creating an instance of the Book class
book = Book(name='Python Programming', price=29.99, quantity=100, author='John Doe')

# Accessing properties from the Product class
print(book.name)      # Output: Python Programming
print(book.price)     # Output: 29.99
print(book.quantity)  # Output: 100

# Accessing the property added by the Book class
print(book.author)    # Output: John Doe

# Calling the read method of the Book class
book.read()
# Output:
# Book Name: Python Programming
# Author: John Doe
# Price: 29.99
# Quantity: 100


# Task 2. Create a class Restaurant with properties name, cuisine, and menu. 
# The menu property should be a dictionary with keys being the dish name and values being the price. 
# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not) 
# and a method called order which takes in the dish name and quantity and returns the total cost of the order. 
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. 
# If the dish is not available or if the requested quantity is greater than the available quantity, 
# the method should return a message indicating that the order cannot be fulfilled. Example of usage:
# class Restaurant:
    # your code here
 #    pass

# class FastFood(Restaurant):
    # your code here
#     pass

# menu =  {
 #    'burger': {'price': 5, 'quantity': 10},
 #    'pizza': {'price': 10, 'quantity': 20},
 #    'drink': {'price': 1, 'quantity': 15}
# }

# mc = FastFood('McDonalds', 'Fast Food', menu, True)

# print(mc.order('burger', 5)) # 25
# print(mc.order('burger', 15)) # Requested quantity not available
# print(mc.order('soup', 5)) # Dish not available

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu and self.menu[dish_name]['quantity'] >= quantity:
            total_cost = self.menu[dish_name]['price'] * quantity
            self.menu[dish_name]['quantity'] -= quantity
            return total_cost
        elif dish_name not in self.menu:
            return "Dish not available"
        else:
            return "Requested quantity not available"

# Example of usage
menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # Output: 25
print(mc.order('burger', 15))  # Output: Requested quantity not available
print(mc.order('soup', 5))  # Output: Dish not available