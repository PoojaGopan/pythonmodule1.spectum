# #Define a class which has at least two methods one, to get a
# #string from console input and other is to print the string in
# #uppercase

# class StringManipulator:
#     def __init__(self):
#         self.input_string = ""

#     def get_string_from_console(self):
#         self.input_string = input("Enter a string: ")

#     def print_uppercase(self):
#         print("Uppercase: ", self.input_string.upper())

# # Example usage:
# if __name__ == "__main__":
#     manipulator = StringManipulator()
#     manipulator.get_string_from_console()
#     manipulator.print_uppercase()

# #Define a class, which have a class parameter and have a
# #same instance parameter.

# class ExampleClass:
#     class_parameter = "Class Parameter"

#     def __init__(self, instance_parameter):
#         self.instance_parameter = instance_parameter

# # Example usage:
# if __name__ == "__main__":
#     # Creating instances with different instance parameters
#     instance1 = ExampleClass("Instance 1")
#     instance2 = ExampleClass("Instance 2")

#     # Accessing class parameter and instance parameters
#     print("Class Parameter:", ExampleClass.class_parameter)
#     print("Instance 1 Parameter:", instance1.instance_parameter)
#     print("Instance 2 Parameter:", instance2.instance_parameter)


# #Define a class named Circle which can be constructed by
# #radius. The Circle class has a method which can compute the
# #area
    
#     import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def compute_area(self):
#         area = math.pi * self.radius ** 2
#         return area

# # Example usage:
# if __name__ == "__main__":
#     # Creating a Circle instance with a radius of 5
#     my_circle = Circle(5)

#     # Computing and printing the area
#     area = my_circle.compute_area()
#     print(f"The area of the circle with radius {my_circle.radius} is: {area}")

# #Define a class named BankAccount. This class should contain
# #methods withdraw() and deposit to calculate the balance
# #amount remained in your account
    
#     class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. Current Balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount. Please enter a positive value.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. Current Balance: ${self.balance}")
#         elif amount <= 0:
#             print("Invalid withdrawal amount. Please enter a positive value.")
#         else:
#             print("Insufficient funds. Withdrawal not allowed.")

# # Example usage:
# if __name__ == "__main__":
#     account = BankAccount(1000)

#     account.deposit(500)
#     account.withdraw(200)
#     account.withdraw(1500)


# #Define a class named Shape and its subclass Square. The
# #Square class has an init function which takes a length as
# #argument. Both classes have a area function which can print
# #the area of the shape where Shape's area is 0 by default. 
    
#     class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2

# # Example usage:
# if __name__ == "__main__":
#     shape = Shape()
#     square = Square(4)

#     print("Area of the Shape:", shape.area())    # Outputs: 0
#     print("Area of the Square:", square.area())  # Outputs: 16
