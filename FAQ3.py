#transpose of matrix
#matrix is a list of list
#in a transform row becomes column and column becomes row
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Find the transpose of the matrix
# transposed_matrix = []#empty list

# # Iterate through columns
# for i in range(len(matrix[0])):#matrix[0] to access the first row that is the first element of the outer list len counts the number of elements,gives the column length
#     transposed_row = []#empty list
#     # Iterate through rows
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed_matrix.append(transposed_row)

# # Print the original and transposed matrices
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# print("\nTransposed Matrix:")
# for row in transposed_matrix:
#     print(row)


#to captalize the  line
# lines = []
# print("Enter lines (type 'exit' to end input):")
# while True:
#     line = input()#Reads a line of input from the user using the input() function and assigns it to the variable line.
#     if line.lower() == 'exit':#Checks if the lowercase version of the input line is equal to the string 'exit'. The .lower() method is used to ensure case-insensitive comparison
#         break
#     lines.append(line)

# # Capitalize each line
# capitalized_lines = [line.upper() for line in lines]

# # Print the capitalized lines
# print("\nCapitalized Lines:")
# for line in capitalized_lines:
#     print(line)

#to test all the built in functions of list
# Sample list


# my_list = [1, 2, 3, 4, 5]

# Append an element to the list
# my_list.append(6)
# print("After append(6):", my_list)#append adds a single element

# # Extend the list with another list
# my_list.extend([7, 8, 9])#adds multiple elements
# print("After extend([7, 8, 9]):", my_list)

# # Insert an element at a specific index
# my_list.insert(2, 10)
# print("After insert(2, 10):", my_list)#insert has the syntax (index,element),index starts from zero

# # Remove the first occurrence of a value
# my_list.remove(3)
# print("After remove(3):", my_list)#remove element

# # Pop an element by index
# popped_element = my_list.pop(4)
# print(f"Popped element at index 4: {popped_element}")#index of popped element
# print("After pop(4):", my_list)

# # Index of the first occurrence of a value
# index_of_4 = my_list.index(4)
# print(f"Index of the first occurrence of 4: {index_of_4}")

# # Count occurrences of a value
# count_of_5 = my_list.count(5)
# print(f"Count of occurrences of 5: {count_of_5}")#count of occurence of first element

# # Reverse the list in-place
# my_list.reverse()
# print("After reverse():", my_list)

# # Sort the list in ascending order in-place
# my_list.sort()
# print("After sort():", my_list)#.sort to sort in ascending order

# # Clear all elements from the list
# my_list.clear()
# print("After clear():", my_list)


#Write a program to read dictionary values through keyboard and merge
#two dictionaries

# print("Enter values for the first dictionary:")
# dict1 = {}
# while True:
#     key = input("Enter key (type 'exit' to stop): ")
#     if key.lower() == 'exit':
#         break
#     value = input(f"Enter value for {key}: ")#f for formatting and dictionary as key value pairs in{}
#     dict1[key] = value

# # Read values for the second dictionary
# print("\nEnter values for the second dictionary:")
# dict2 = {}
# while True:
#     key = input("Enter key (type 'exit' to stop): ")
#     if key.lower() == 'exit':
#         break
#     value = input(f"Enter value for {key}: ")
#     dict2[key] = value

# # Merge dictionaries
# merged_dict = {**dict1, **dict2}
# #when there are duplicate keys, the value associated with the last occurrence of the key will overwrite any previous values
# # Print the merged dictionary
# print("\nMerged Dictionary:")
# print(merged_dict)


#Write a program to demonstrate all built-in methods of dictionary
# Initialize a dictionary
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# # Display the original dictionary
# print("Original Dictionary:")
# print(my_dict)

# Demonstrate dictionary methods

# 1. get()
# print("\n1. Using get('name'): ", my_dict.get('name'))#to get the value associated with the key

# # 2. keys()
# print("\n2. Dictionary Keys:", my_dict.keys())

# # 3. values()
# print("\n3. Dictionary Values:", my_dict.values())

# # 4. items()
# print("\n4. Dictionary Items:", my_dict.items())

# # 5. pop()
# removed_value = my_dict.pop('age')
# print("\n5. Dictionary after pop('age'):", my_dict)
# print("   Removed Value:", removed_value)

# # 6. popitem()
# removed_item = my_dict.popitem()
# print("\n6. Dictionary after popitem():", my_dict)
# print("   Removed Item:", removed_item)

# # 7. update()
# my_dict.update({'gender': 'Male'})
# print("\n7. Dictionary after update({'gender': 'Male'}):", my_dict)

# # 8. clear()
# my_dict.clear()
# print("\n8. Dictionary after clear():", my_dict)

 #Write a program to find the sum of all the elements in a list
# Sample list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Calculate the sum of all elements in the list
# sum_of_elements = sum(numbers)# built in sum function

# # Print the result
# print("Sum of elements in the list:", sum_of_elements)

#With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an integral number between 1and n. And then the program should print the dictionary.


# n = int(input("Enter a positive integer value for n: "))    
# if n < 1:
#     raise ValueError("Please enter a positive integer.")
# square_dict = {}#an empty dictionary initalized
# for i in range(1, n + 1):
#     square_dict[i] = i * i
# print(f"Generated dictionary: {square_dict}")

#Write a program that accepts a sentence and calculate the number of letters & digits
#a string is a collection of charecteristics
# sentence = input("Enter a sentence: ")

# letter_count = 0
# digit_count = 0

# for char in sentence:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count += 1

# print(f"Number of letters: {letter_count}")
# print(f"Number of digits: {digit_count}")

#Write a program to implement filter(), map() and reduce()

#filter()function in Python is used to filter elements of an iterable

#filter(function, iterable)
#In Python, lambda is a keyword that is used to define anonymous functions. An anonymous function is a function that is defined without a name. The lambda function is a concise way to create small, one-line functions
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Use filter() to get only the even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# #The map() function applies a specified function to each item in an iterable and returns an iterator that produces the results. It is used when you want to transform each element of an iterable independently
# # Use map() to square each number
# squared_numbers = list(map(lambda x: x**2, numbers))

# # Print the results
# print("Original numbers:", numbers)
# print("Even numbers:", even_numbers)
# print("Squared numbers:", squared_numbers)
# #The reduce() function aggregates the elements of an iterable by applying a specified function cumulatively. It takes the result of the previous operation and the next element as arguments, reducing the iterable to a single accumulated result.
# from functools import reduce# works with out importing also

# # Example list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Define a function to multiply two numbers
# def multiply(x, y):
#     return x * y

# # Use reduce() to calculate the product of all numbers
# product_of_numbers = reduce(multiply, numbers)

# # Print the result
# print("Original numbers:", numbers)
# print("Product of numbers:", product_of_numbers)

#Write a program to implement List Comprehension
#[expression for item in iterable if condition]
#list comprehension is used to create lists other than this there is the list() function
#List comprehensions provide a concise way to create lists. They consist of an expression followed by a for clause and an optional if clause.
# Example: Squares of numbers from 0 to 9
# squares = [x**2 for x in range(10)]
# print(squares)

#Write a program to implement Dictionary Comprehension
#{key_expression: value_expression for item in iterable if condition}
#dictionary comprehension is for creating dictionary{} other than this dict()fn
# Using dictionary comprehension to generate a dictionary of squares
# numbers = [1, 2, 3, 4, 5]

# # Create a dictionary of squares
# squares_dict = {x: x**2 for x in numbers}#key value pair

# # Print the result
# print("Original numbers:", numbers)
# print("Squares Dictionary:", squares_dict)

#to find the max and minimum value of a list
#In Python, you can use the built-in max() and min() functions to find the largest and smallest elements in a list
# Example list
# numbers = [10, 5, 8, 20, 3]

# # Using max() and min() functions
# largest = max(numbers)
# smallest = min(numbers)

# # Print the results
# print("List:", numbers)
# print("Largest Element:", largest)
# print("Smallest Element:", smallest)

#Write a Python program to print the numbers of a specified list after removing even numbers from it
#list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
# list1 = [10, 21, 4, 45, 66, 93]
# for num in list1:
 
#     # checking condition
#     if num % 2 != 0:
#         print(num, end=" ")

#Write a Python program to generate and print a list of first and last 5

#elements where the values are square of numbers between 1 and 30
#List slicing in Python allows you to extract a portion of a list by specifying a range of indices
#list[start:stop:step]#start inclusive #stop exclusive
#Generate a list of squares of numbers from 1 to 30
# squares_list = [x**2 for x in range(1, 31)]

# # Extract the first 5 elements using list slicing [:5]
# first_5 = squares_list[:5]

# # Extract the last 5 elements using list slicing [-5:]
# last_5 = squares_list[-5:]

# # Print the results
# print("List of squares:", squares_list)
# print("First 5 elements:", first_5)
# print("Last 5 elements:", last_5)


# # Example list of slicing
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Slicing to get a sublist
# sublist = numbers[2:7]  # Elements from index 2 to 6
# print(sublist)  # Output: [2, 3, 4, 5, 6]

# # Slicing with step
# every_second = numbers[1:8:2]  # Elements from index 1 to 7 with a step of 2
# print(every_second)  # Output: [1, 3, 5, 7]

# # Slicing from the beginning
# first_three = numbers[:3]  # Elements from the beginning to index 2
# print(first_three)  # Output: [0, 1, 2]

# # Slicing to the end
# last_five = numbers[5:]  # Elements from index 5 to the end
# print(last_five)  # Output: [5, 6, 7, 8, 9]

# # Slicing with negative indices
# last_three = numbers[-3:]  # Last three elements
# print(last_three)  # Output: [7, 8, 9]

# # Reverse the list using slicing
# reversed_list = numbers[::-1]
# print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#program to insert a given string at the beginning of all items in a list

# def insert_string_at_beginning(input_list, prefix_string):
#     modified_list = []
#     for item in input_list:
#         modified_list.append(prefix_string + str(item))
#     return modified_list
# # Example usage:
# original_list = [1, 2, 3, 4, 5]
# prefix = "Item "
# result_list = insert_string_at_beginning(original_list, prefix)
# print(result_list)

#Python program to iterate over two lists simultaneously
#the zip function is used to combine elements from two or more iterable objects (like lists, tuples, or strings) into tuples
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']
# # Iterate over two lists simultaneously using zip
# zipped=zip(list1, list2)
# print(list(zipped))

#program to add a key to a dictionary
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# # Adding a new key-value pair
# my_dict['gender'] = 'Male'#add a key to a dictionary by assigning a value to that key
# # Display the updated dictionary
# print(my_dict)

#dictiomnary concatenate
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# # Method 1: Using {**dict1, **dict2, **dict3}
# concatenated_dict1 = {**dic1, **dic2, **dic3}
# # Method 2: Using update() method
# concatenated_dict2 = dic1.copy()#.copy to copy orginal dictionary without modifying
# concatenated_dict2.update(dic2)
# concatenated_dict2.update(dic3)
# # Display the concatenated dictionaries
# print("Concatenated Dictionary (Method 1):", concatenated_dict1)
# print("Concatenated Dictionary (Method 2):", concatenated_dict2)

#to iterate over dictionaries using for loops
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Iterate over values
# for value in my_dict.values():
#     print(value)
# for keys in my_dict.keys():
#     print(keys)
# for keys,value in my_dict.items():
#   print(f"Key: {keys}, Value: {value}")

#program to sum all the items in a dictionary
# my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# # Sum all the values in the dictionary
# total_sum = sum(my_dict.values())

# # Display the sum
# print("Sum of all items:", total_sum)

#dictionary creation
# Create a dictionary for pet information
# pet_dict = {'Dog': 'Willie', 'Cat': 'Mittens', 'Fish': 'Goldie'}
# # Use a for loop to print statements about each pet
# for kind, name in pet_dict.items():
#     print(f"{name} is a {kind}.")

#dictionary created from orginal dictionary
# def filter_marks(subject_marks):
#     # Create a new dictionary for marks more than 50
#     filtered_marks = {subject: marks for subject, marks in subject_marks.items() if marks > 50}
#     return filtered_marks
# # Given dictionary
# marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}
# # Call the function to get a new dictionary with marks more than 50
# filtered_dict = filter_marks(marks)
# # Print the new dictionary
# print(filtered_dict)
#
# def count_letters_digits(sentence):
#     # Initialize counters
#     letter_count = 0
#     digit_count = 0

#     # Iterate over each character in the sentence
#     for char in sentence:
#         if char.isalpha():#is alpha to check if alphabet or not
#             letter_count += 1
#         elif char.isdigit():#to check if digit or not
#             digit_count += 1

#     return letter_count, digit_count

# # Example usage:
# input_sentence = "eureka 123"

# # Call the function to get counts
# letters, digits = count_letters_digits(input_sentence)

# # Print the results
# print(f"Number of letters: {letters}")
# print(f"Number of digits: {digits}")

# def generate_square_dictionary(n):
#     square_dict = {}
#     for i in range(1, n+1):
#         square_dict[i] = i**2#i is the key and i** is the value,dictionary[key]=value
#     return square_dict
# result_dict = generate_square_dictionary(9)
# # Print the generated dictionary
# print(result_dict)


#syntax of various loops

#for variable in iterable:(loops are followed by full collon)
#while condition:
#if condition:
#else goes with if:
            # elif:
            #else:



