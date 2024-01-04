# # odd or even using def
# def check_even_odd(number):
#     if number % 2 == 0:
#         print("It is an even number")
#     else:
#         print("It is odd")
# user_input = int(input("Enter an integer: "))
# check_even_odd(user_input)


# dictionary with number and its square
# def generate_square_dict():
#     square_dict = {}
#     for num in range(1, 21):
#         square_dict[num] = num ** 2
#     return square_dict
# result_dict = generate_square_dict()
# print(result_dict)


#list comprehension is used to create list using the syntax
#new_list = [expression for item in iterable if condition]
# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     result_string = ''.join([char for char in input_string if char not in vowels])
#     return result_string
# user_input = input("Enter a string: ")
# result = remove_vowels(user_input)
# print("String with vowels removed:", result)


#a program to display Powers of 2 using Anonymous functions lambda and map
#map(function, iterable)
#lambda arguments: expression
# Define the anonymous function (lambda) to calculate powers of 2
# power_of_2 = lambda x: 2 ** x
# # Define the range of powers you want to display
# n = 5  # Adjust the value of n as needed
# # Use map() to generate powers of 2 for the given range
# powers = map(power_of_2, range(n + 1))
# # Display the powers of 2 using a loop
# for i, power in enumerate(powers):#built-in function that allows iteration over a sequence (such as a list, tuple, or string) while keeping track of the index (position) and the corresponding value of each element
#     print(f"2^{i} = {power}")


#two list of same length as input and return a dictionary with one as keys and other as values
# def create_dictionary(keys, values):
#     # Check if the lists have the same length
#     if len(keys) != len(values):
#         raise ValueError("Lists must be of the same length")#ValueError is a built-in exception that is raised when a function receives an argument of the correct data type but with an invalid value
#     # Use a dictionary comprehension to create the dictionary
#     result_dict = {keys[i]: values[i] for i in range(len(keys))}
#     return result_dict
# # Example usage:
# keys_list = ['a', 'b', 'c']
# values_list = [1, 2, 3]
# result_dictionary = create_dictionary(keys_list, values_list)
# print("Resulting Dictionary:", result_dictionary)

#program to print fibonocci series using recursion
#fibonacci is a seequence where each number is the sum of preceeding two numbers;f(n)=f(n-1)+f(n-2)
#recursion is a function calling itself
#0 1 1 2 3 5
#n=1  then 0,n=2 then 01 and so on
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_series = fibonacci(n - 1)
#         fib_series.append(fib_series[-1] + fib_series[-2])
#         return fib_series
# result=fibonacci(10)
# print(result)

# #factorial using recursion
# def factorial(n):
#     # Base case: factorial of 0 is 1
#     if n == 0:
#         return 1
#     # Recursive case: factorial of n is n times factorial of (n-1)
#     else:
#         return n * factorial(n - 1)#recusion call
# # Example: Find the factorial of 5
# number = 5
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

#def find_second_smallest(numbers):
    # if len(numbers) < 2:
    #     return None  # Not enough elements in the list
    # smallest = second_smallest = float('inf')  # Initialize with positive infinity
    # for num in numbers:
    #     if num < smallest:
    #         second_smallest = smallest
    #         smallest = num
    #     elif num < second_smallest and num != smallest:
    #         second_smallest = num
    # return second_smallest

#generators in python
#Generators in Python are a way to create iterators using a special kind of function
#iterate over a potentially large sequence of data without loading the entire sequence into memory at once
# Generators are defined using functions with the yield statement, which allows the function to yield values one at a time, suspending its state until the next value is requested
# def generate_numbers(n):
#     for number in range(n + 1):
#         if number % 5 == 0 and number % 7 == 0:
#             yield number
# # Example usage:
# n = int(input("Enter the value of n: "))

# result_generator = generate_numbers(n)

# print(f"Numbers divisible by 5 and 7 between 0 and {n}: {', '.join(map(str, result_generator))}")#.join() method is a string method in Python that concatenates elements of an iterable (e.g., a list, tuple, or generator) into a single string

# def even_numbers_generator(n):
#     return (str(num) for num in range(n + 1) if num % 2 == 0)
# def main():
#     try:#try block is executed
#         n = int(input("Enter a number (n): "))
#         if n < 0:
#             raise ValueError("Please enter a non-negative integer.")

#         result = ', '.join(even_numbers_generator(n))

#         print(f"Even numbers between 0 and {n}: {result}")

#     except ValueError as ve:#if an exception occurs then this block is executed;value error if the entered value cannot be converted to integer
#         print(f"Error: {ve}")

# if __name__ == "__main__":# This checks whether the script is being run as the main program. If it is, the code inside this block will be executed
#     main()

# Decorators in python
#decorators help you to modify the program without actually changing the code.
#Decorators are implemented using functions and the @decorator syntax in Python
#A decorator is essentially a function that takes another function as an argument, adds or modifies some functionality, and then returns the modified function. This can be achieved using nested functions

