#o implement the concept of calendar module
#calender module to handle operations of calender

# import calendar#importing calender module
# # cal = calendar.TextCalendar()#The TextCalendar class is used to create text calendars that can be printed
# # print(cal.formatmonth(2024, 1))#formats and prints for 2024 jan

# # weekday = calendar.weekday(2024, 2, 27)#weekday function from the calendar module to find the day of the week for a specific date(year,month day);This function returns the day of the week as an integer, where Monday is 0 and Sunday is 6
# # print(f"feb 27, 2024 is a {calendar.day_name[weekday]}.")# to print the day of the week corresponding to the result

# months = calendar.month_name[1:]#slicing to create the subset of the list
# days = calendar.day_name
# print("Months:", months)
# x=list(("Days of the week:", days))
# print(x)

# import calendar
# # Get the names of the days of the week
# days_of_week = calendar.day_name
# # Print the names of the days of the week
# print("Days of the week:")
# for day in days_of_week:
#     print(day)

# import calendar
# # Get the names of the days of the week
# days_of_week = calendar.day_name
# # Print the names of the days of the week
# print("Days of the week:", list(days_of_week))

# import calendar
# leap_year = 2023
# if calendar.isleap(leap_year):#to check if leap year or not
#     print(f"{leap_year} is a leap year.")
# else:
#     print(f"{leap_year} is not a leap year.")

#date and time module
# from datetime import datetime

# # Get the current date and time
# current_datetime = datetime.now()
# print("Current Date and Time:", current_datetime)

# # Create a specific date and time
# specific_datetime = datetime(2024, 1, 5, 12, 30, 45)  # Year, Month, Day, Hour, Minute, Second
# print("Specific Date and Time:", specific_datetime)#to print the specific value inputed

# # Format a datetime object as a string
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")#ormat the current_datetime object as a string using the strftime method, specifying the desired format ("%Y-%m-%d %H:%M:%S")
# print("Formatted Date and Time:", formatted_datetime)

# # Parse a string to a datetime object
# date_string = "2024-01-10 08:15:30"
# parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")#.strptimeclass to parse a string representing a date and time according to a specified format;.%Y-%m-%d %H:%M:%SThis string is the format specifier that indicates the expected format of the input string
# print("Parsed Date and Time:", parsed_datetime)

# # Perform operations with timedelta
# from datetime import timedelta#datetime module to perform operations on datetime objects by adding a specific duration to a given datetime

# delta = timedelta(days=5, hours=3, minutes=30)
# result_datetime = current_datetime + delta
# print("Result Date and Time:", result_datetime)


#The time module in Python primarily deals with time-related functions
# import time

# # Get the current time in seconds since the epoch
# current_time_seconds = time.time()
# print("Current Time in Seconds:", current_time_seconds)

# # Get the current local time struct
# current_local_time_struct = time.localtime()
# print("Current Local Time Struct:", current_local_time_struct)

# # Format the current local time as a string
# formatted_time_string = time.strftime("%Y-%m-%d %H:%M:%S", current_local_time_struct)
# print("Formatted Time String:", formatted_time_string)

# # Delay the program for 2 seconds
# print("Waiting for 2 seconds...")
# time.sleep(2)
# print("Done waiting!")

# # Measure the elapsed time for a code block
# start_time = time.time()
# # Your code block here
# end_time = time.time()
# elapsed_time = end_time - start_time
# print("Elapsed Time:", elapsed_time, "seconds")


#various operators
# import operator
# a, b = 10, 3
# add_result = operator.add(a, b)
# sub_result = operator.sub(a, b)
# mul_result = operator.mul(a, b)
# div_result = operator.truediv(a, b)#floating point results even if integers
# print("Addition:", add_result)
# print("Subtraction:", sub_result)
# print("Multiplication:", mul_result)
# print("Division:", div_result)

# import operator
# # Sample data
# numbers = [5, 2, 8, 1, 7]
# # Using operator functions
# print("Original List:", numbers)
# sorted_numbers = sorted(numbers,)
# print("Sorted List ", sorted_numbers)
# max_value = max(numbers)
# min_value = min(numbers)
# print("Max Value:", max_value)
# print("Min Value:", min_value)
# sum_of_numbers = sum(numbers)
# print("Sum of List:", sum_of_numbers)
# tuple_list = [(1, 5), (3, 2), (2, 8), (4, 1)]
# sorted_tuples = sorted(tuple_list, key=operator.itemgetter(1))#sorting will be based on the second element of the list
# print("Sorted Tuples (by second element):", sorted_tuples)


#The math module in Python provides a set of mathematical functions for performing operations like square roots, trigonometry, logarithms, and more
# import math
# # Square root
# number = 16
# sqrt_result = math.sqrt(number)
# print(f"Square root of {number}: {sqrt_result}")
# # Trigonometric functions
# angle_rad = math.radians(45)  # Convert degrees to radians
# sin_result = math.sin(angle_rad)
# cos_result = math.cos(angle_rad)
# print(f"Sine of 45 degrees: {sin_result}")
# print(f"Cosine of 45 degrees: {cos_result}")
# # Logarithmic functions
# log_result = math.log(100, 10)  # Log base 10 of 100
# print(f"Log base 10 of 100: {log_result}")
# # Power function
# power_result = math.pow(2, 3)  # 2^3
# print(f"2 to the power of 3: {power_result}")
# # Constants in math module
# print(f"Value of pi: {math.pi}")
# print(f"Value of e (Euler's number): {math.e}")
