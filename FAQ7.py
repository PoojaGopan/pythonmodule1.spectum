#create a file and write data to it text file
# def create_file(file_name, data):
#     try:
#         # Open the file in write mode
#         with open(file_name, 'w') as file:
          #to write data of file
#             file.write(data)

#     except Exception as e:#exception error handling
#         print(f"Error: {e}")

# # Example usage
# file_name = "textfilesample.txt"#create file with text format
# data = "hello world!"#sample data to be written
# create_file(file_name, data)

# #reading text file
# def read_file_with_read(file_name):
#     try:
#         # Open the file in read mode
#         with open(file_name, 'r') as file:
#             # Read the entire content of the file using read()
#             content = file.read()
#             print("Content read using read():\n", content)

#     except FileNotFoundError:#t is a specific exception raised when a file is not found at the specified location.
#         print(f"Error: File '{file_name}' not found.")
#     except Exception as e:#exception error handling
#         print(f"Error: {e}")
# file_name = "textfilesample.txt"
# read_file_with_read(file_name)

#The readline() method in Python is used to read a single line from a file
# Open a file in read mode
# with open('textfilesample.txt', 'r') as file:
#     # line1 = file.readline()
#     # print(line1)
#     # line2 = file.readline()
#     # print(line2)
#     line3 = file.readline()
#     print(line3)

#A CSV (Comma-Separated Values) file is a plain text file format that is commonly used to store tabular data (numbers and text) in a simple, structured format. In a CSV file, each line of the file represents a row of the table, and the values within each row are separated by commas
#write operation in csv file
# import csv
# def write_csv(file_name, data):
#     try:
#         with open(file_name, 'w', newline='') as file:#open the file write format
#             csv_writer = csv.writer(file)#csv.writer is a class as part of the csv module The csv.writer object takes a file object as a parameter and provides methods for writing individual rows or sequences of rows to the CSV file
            
#             # Write data to the CSV file
#             csv_writer.writerows(data)

#         print(f"Data written to '{file_name}' successfully.")
#     except Exception as e:
#         print(f"Error: {e}")
# # Example usage
# csv_file_name = "example.csv"
# # Data to write to the CSV file
# data= [
#     ["Name", "Age", "City"],
#     ["John", 25, "New York"],
#     ["Alice", 30, "London"],
#     ["Bob", 22, "Tokyo"]
# ]
# # Write data to the CSV file
# write_csv(csv_file_name, data)

#read csv file
# import csv
# def read_csv(file_name):
#     try:
#         with open(file_name, 'r', newline='') as file:#to open the file in read mode
#             csv_reader = csv.reader(file)#class as part of the csv module to read
#             # Iterate over rows and print each row
#             for row in csv_reader:
#                 print(row)
#     except FileNotFoundError:
#         print(f"Error: File '{file_name}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")
# # Example usage
# file_name = "example.csv"#part of the csv module, is used for reading data from a CSV file
# # Read data from the CSV file
# read_csv(file_name)

#append data to text file
# def append_to_text_file(file_name, data):
#     try:
#         with open(file_name, 'a', newline='') as file:#open file in append mode
#             # Append data to the file
#             file.write(data + "\n")#escape sequence charecter
#         print(f"Data appended to '{file_name}' successfully.")
#     except Exception as e:
#         print(f"Error: {e}")
# # Example usage
# text_file_name = "textfilessample"
# # Data to append to the file
# data= "This line will be appended."
# # Append data to the existing text file
# append_to_text_file(text_file_name, data)

# #append data to a csv file
# import csv
# def append_to_csv(file_name, data):
#     try:
#         with open(file_name, 'a', newline='') as file:#to write in write mode
#             csv_writer = csv.writer(file)
#             csv_writer.writerow(data)

#         print(f"Data appended to '{file_name}' successfully.")
#     except Exception as e:
#         print(f"Error: {e}")
# # Example usage
# csv_file_name = "example.csv"
# # Data to append to the CSV file
# data= ["Pooja",22, "India"]
# # Append data to the existing CSV file
# append_to_csv(csv_file_name, data)

# # quadratic equation with cmath module
# import cmath  # Importing cmath for handling complex numbers
# def solve_quadratic_equation(a, b, c):
#     # Calculate the discriminant
#     discriminant = cmath.sqrt(b**2 - 4*a*c)#creates the discriminat and return the complex module
#     # Calculate the two solutions using the quadratic formula
#     root1 = (-b + discriminant) / (2*a)
#     root2 = (-b - discriminant) / (2*a)
#     return root1, root2
# # Get coefficients from the user
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))
# # Call the function to solve the quadratic equation
# roots = solve_quadratic_equation(a, b, c)
# # Display the roots
# print("Root 1:", roots[0])
# print("Root 2:", roots[1])

# #quadratic equation  with equation
# def solve_quadratic_equation(a, b, c):
#     # Calculate the discriminant
#     discriminant = b**2 - 4*a*c
#     # Check the nature of the solutions
#     if discriminant > 0:#Discriminant (b2−4acb2−4ac) > 0: Two real and distinct roots;-b+/-squareroot of discriminat by 2a
#         root1 = (-b + (discriminant)**0.5) / (2*a)
#         root2 = (-b - (discriminant)**0.5) / (2*a)
#         return root1, root2
#     elif discriminant == 0:#discriminant (b2−4acb2−4ac) = 0: One real root (double root);root=-b/2a
#         root = -b / (2*a)
#         return root,
#     else:
#         # Discriminant (b2−4acb2−4ac) < 0: Two complex roots
#         #the real part of the root is -b/2a
#         #imaginary part of the root is +/-squareroot of discriminat by 2a
#         real_part = -b / (2*a)
#         imaginary_part = (abs(discriminant))**0.5 / (2*a)#absolute value of discriminat
#         root1 = complex(real_part, imaginary_part)#express in complex format
#         root2 = complex(real_part, -imaginary_part)
#         return root1, root2
# # Example usage
# a = 1
# b = -3
# c = 2
# roots = solve_quadratic_equation(a, b, c)
# print("Roots:", roots)
