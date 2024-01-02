# #pattern printing

# rows = 5
# for i in range(1, rows + 1):#for rows
#     for j in range(1, i + 1):#for columns
#         print("*", end=" ")
#     print()

#for loop :is used to iterate over a sequence (such as a list, tuple, string, or range),list mutable[],tuple immutable(),string immutable""or'',rangle immutable starts from zero unless specified to n-1 also incerment and decrement can be specified
#for variable in sequence

# num = 1 #initalize
# for i in range(1, 5):#for rows
#     for j in range(i):#for columns
#         print(num, end=" ")
#         num += 1#increment
#     print()#print() is used to move the cursor to a new line after each row of numbers is printed

# for i in range(1, 5):#for the rows
#     # Inner loop to print letters from 'A' to 'A + i'
#     for j in range(i):#for thee columns
#         print(chr(ord('A') + j), end=" ")#ord()to find the integer value of char and char to find the char of the int value
#     print()

# char = 'A'

# for i in range(1, 5):
#     # Inner loop to print letters from 'A' to 'A + i'
#     for j in range(i):
#         print(char, end=" ")
#         char = chr(ord(char) + 1)  # Move to the next character
#     print()


# num = 2
# for i in range(1, 5):
#     # Inner loop to print numbers from 'num' to 'num + i * 2'
#     for j in range(i):
#         print(num, end=" ")
#         num += 2
#     print()

# rows = 4

# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("# ", end="")
#     print()
