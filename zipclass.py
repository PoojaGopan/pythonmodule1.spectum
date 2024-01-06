# import zipfile
# with zipfile.ZipFile("helloo.zip","w")as zipfile:# Create a ZIP file named "helloo.zip" in write mode ("w")
#     zipfile.write("text.txt")  # Add "text.txt" to the ZIP file
#     zipfile.write("zippp.txt")# Add "zippp.txt" to the ZIP file

# import zipfile
# with zipfile.ZipFile("helloo.zip","r")as zipfile:# Open the existing ZIP file "hello.zip" in read mode ("r")
#     file_list=zipfile.namelist()#the namelist() method is used to retrieve a list of all the file names present in the ZIP archive
#     print("content of the zipfile",file_list)# Print the list of file names

#code is designed to extract a specific file ("text.txt") from the existing ZIP file "hello.zip" and place it in a specified destination directory ("C:/Users/ASUS/OneDrive/Documents")
# import zipfile
# file='text.txt'#the file to be extracted
# file1="C:/Users/ASUS/OneDrive/Documents"#the destination directory for extraction
# with zipfile.ZipFile("helloo.zip","r") as zipf:#Open the existing ZIP file "hello.zip" in read mode ("r")
#     if file in zipf.namelist():#Check if the specified file exists in the ZIP archive
#         zipf.extract(file,file1)#extract to the specified location
#         print(f"'{file} has been extracted to '{file1}'.")
#     else:
#         print(f"'{file} does not exist in the ZIP archive.")

# #zipping using.zip
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# # Use zip to combine the lists
# result = zip(list1, list2)
# # Convert the result to a list (optional)
# result_list = list(result)
# # Print the result
# print(result_list)

#unziping tuples using zip files
# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# numbers, letters = zip(*pairs)
# print(numbers)  # Output: (1, 2, 3)
# print(letters)  # Output: ('a', 'b', 'c')

#over multiple zipfiles
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for num, letter in zip(list1, list2):
#     print(f"Number: {num}, Letter: {letter}")

# #creation of dictionary
# keys = ['name', 'age', 'city']
# values = ['John', 25, 'New York']
# user_info = dict(zip(keys, values))
# print(user_info)

#transpose of matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transposed = list(zip(*matrix))
# print(transposed)


