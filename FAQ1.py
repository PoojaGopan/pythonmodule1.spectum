#Write a program to check whether the entered number is postive or negative
# x=int(input("enter a number"))
# if x>0:
#     print("positive")
# elif x<0:
#     print("negative")
# else:
#     print("neither positive nor negative")


# #odd or even
# x=int(input("enter a number"))
# if x % 2==0:
#     print("even")
# else:
#     print("odd")

#pattern printing

# n=5
# for i in range(n):#range is from 0 to n-1
#     for j in range(i,n):#inner loop coloumn and outer loop row,range is from i t0 n-1
#         print("*",end=" ")
#     print()

#swap two numbers
# x=10
# y=50
# temp=x
# x=y
# y=temp
# print("print value of x",x)
# print("print value of y",y)

#to remove puncuation from a string

# punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
# my_str = input("Enter a string: ")  
# no_punct = ""  
# for char in my_str:  # char identifies the data type
#    if char not in punctuation:  
#        no_punct = no_punct + char  
# print(no_punct)  

# check whether leap year or not
# If the year is divisible by 4, it's a leap year.
# If the year is divisible by 100, it must also be divisible by 400 to be a leap year.

# year = int(input("Enter any year to check if it's a leap year: "))
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("The given year is a leap year.")
#         else:
#             print("The given year is not a leap year.")
#     else:
#         print("The given year is a leap year.")
# else:
#     print("The given year is not a leap year.")

#check if a number is fibonacci or not
# n = 10
# m1, m2 = 0, 1#since the first two are initalized as 0 and 1

# print("Fibonacci series:", m1, m2, end=" ")

# for i in range(2, n):#starts from 2 and moves till n-1
#     m3 = m1 + m2#fn=fn-1+fn-2
#     m1, m2 = m2, m3#updates the value of m1 and m2
#     print(m3, end=" ")
# print() 

#check if prime or not
# lower = 10
# upper = 30

# print("Prime numbers between", lower, "and", upper)

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#checks if there's any factor other than 1 and num itself. If true, the number is not prime (break is used to exit the loop).

#pattern printing
# rows = int(input("Enter the number of rows: "))

# # Upper part of the pyramid
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")

# # Lower part of the pyramid
# for i in range(rows + 1, 0, -1):#takes value from 6 to 0 decrementing by 1 and not including zero
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

#to find odd numbers from 1 to 50 and to find their sum
# sum=0
# for num in range(1,50):
 
#     # checking condition
#     if num % 2 != 0:
#         print(num)
#         sum+=num#sum=sum+num
# print(sum)
#to find factorial of a number
# Input: Get the number from the user
# number = int(input("Enter a number to find its factorial: "))

# # Initialize the factorial to 1
# factorial = 1

# # Calculate the factorial using a for loop
# for i in range(1, number + 1):
#     factorial *= i

# # Output: Print the factorial
# print(f"The factorial of {number} is: {factorial}")#f for formatting
##to check if your no is a palindrome or not
# number = int(input("Enter a number to check if it's a palindrome: "))
# number_str = str(number)#string manipulation is more convenient
# reversed_str = number_str[::-1] #Output: !dlroW ,olleH

# if number_str == reversed_str:
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")

#numders within a range that is divisible with 7
# for num in range(100, 200):
#     if num % 7 == 0:
#         print(num, "is divisible by 7.")

#to display the multipication table
# number = int(input("Enter the number to generate its multiplication table: "))
# count = 1

# print("The Multiplication Table of:", number)
# while count <= 10:
#     result = number * count
#     print(f"{number} x {count} = {result}")
#     count += 1

#program to calculate the area and perimeter of a rectangle.
# l = int(input("Enter Length of Rectangle: "))
# b = int(input("Enter Breadth of Rectangle: "))
# p = 2*(l+b)
# print("\nPerimeter = ", p)

#program to find the sum of n' Natural Numbers
# num = int(input("Enter a number: "))  
# if num < 0:  
#    print("Enter a positive number")  
# else:  
#    sum = 0  
#    while(num > 0):  
#        sum += num  
#        num -= 1  
#    print("The sum is",sum)  
#to check if a number is an amstrong number or not
# num = int(input("Enter a number: "))
# x = 0
# t = num

# # Loop to calculate the sum of cubes of individual digits
# while t > 0:
#     d = t % 10  # Extract the last digit
#     x += d ** 3  # Cube the digit and add to the sum
#     t //= 10     # Remove the last digit #floor division to remove last number

# # Check if the original number is equal to the sum of cubes
# if num == x:
#     print(num, "IS AN ARMSTRONG NUMBER")
# else:
#     print(num, "IS NOT AN ARMSTRONG NUMBER")
 
#to find largest amoung three numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)
#pattern pattern
# for i in range(5):    
#     for j in range(i):    
#         print(i, end=" ")     
#     print(" ") 

#a program to count the no:of each vowel in a given string
# string_input = input('Enter the string: ')
# count = sum(1 for char in string_input.lower() if char in 'aeiou')

# if count == 0:
#     print('No vowels found')
# else:
#     print('Total vowels: ' + str(count))

#to perform Addition,Subtraction,Multiplication and division on Complex-No's.
# print("Addition of two complex numbers : ",(4+3j)+(3-7j))
# print("Subtraction of two complex numbers : ",(4+3j)-(3-7j))
# print("Multiplication of two complex numbers : ",(4+3j)*(3-7j))
# print("Division of two complex numbers : ",(4+3j)/(3-7j))

#Write a python function to add ‘python’ at the end of a given stringand return the new string. If the given string already ends with ‘python’then add ‘java’. If the length of the given string is less than 5, then add‘php’
#def is the keyword used to call a funnction in python followed by the function name and the parameters
# def add_string(str1):
#     if str1.endswith('python'):# str.endswith method in Python is a string method that returns True if the string str1 ends with the specified suffix
#         return str1+'java'
#     elif len(str1)<5:
#         return str1+'php'
#     else:
#         return str1+'python'
# result=add_string('python') #function call
# print(result)

