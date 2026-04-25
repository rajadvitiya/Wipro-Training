# Do the following in a single program using built-in functions
# Take a list of numbers as input and print the largest and smallest numbers in the list.
# Take a string as input and print the length of the string.
# Take a list of names as input and print the list in alphabetical order.
# Take a list of numbers as input and print the total sum of the elements in the list.
# Takes a string as input and print the string in uppercase.
import math

# numbers = [11,22,33,44,55]
# print('max number : ',max(numbers), 'smallest number ; ', min(numbers))

#output
# max number :  55 smallest number ;  11


# str = input('Enter a string..')
# print(len(str))

#output
# Enter a string..jhbvkjvf
# 8


# names = input('Enter names separated by space')
# name_list = names.split()
# name_list.sort()
# print(name_list)

#output
# Enter names separated by spaceswati rohit choti roji
# ['choti', 'rohit', 'roji', 'swati']

# numbers = [11,22,33,44,55]
# print('Sum of numbers : ', sum(numbers))

#output
# Sum of numbers :  165


# str = input('Enter a string : ')
# print(str.upper())

#output
# Enter a string : kjhghdg
# KJHGHDG



# Write a user-defined function factorial(n) that takes a positive integer n as an argument
# and returns its factorial. Use the function in a program and print the factorial of a given
# number.


# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return fact
#
# num = int(input('Enter number : '))
# print(num ,'factorial is : ', factorial(num))

#output
# Enter number : 4
# 4 factorial is :  24



# Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
# arguments and returns the largest of the three. Use the function in a program to find and
# print the largest of three given numbers.



# def find_largest(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
#
#
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))
#
# largest = find_largest(x, y, z)
# print("The largest number is:", largest)

#output
# Enter first number: 45
# Enter second number: 52
# Enter third number: 33
# The largest number is: 52



# Write a user-defined function greet(name) that takes a name as an argument and prints
# a greeting message like "Hello, [name]!" Use the function to greet the user with their
# name.


# def greet(name):
#     print("Hello, " + name + "!")
#
#
# user_name = input("Enter your name: ")
# greet(user_name)

# #output
# Enter your name: Swati
# Hello, Swati!



# Combining Built-in and User-Defined Functions:
# Find the Average of a List:
# Write a user-defined function average(numbers) that takes a list of numbers as an
# argument and returns the average of the numbers. Call the function with a list of
# numbers and print the average.


# def average(numbers):
#     if len(numbers) == 0:   # avoid division by zero
#         return 0
#     return sum(numbers) / len(numbers)
#
# num_list = [10, 20, 30, 40, 50]
# avg = average(num_list)
#
# print("The average is:", avg)

#output
# The average is: 30.0



# Check Palindrome:
# Write a user-defined function is_palindrome(s) that takes a string as an argument and
# returns True if the string is a palindrome (reads the same forward and backward), and
# False otherwise. Test the function with different strings and print the results.


# str = input('Enter a string : ')
#
# reversed = str[::-1]
# print(str==reversed)

#output
# Enter a string : bbcbb
# True



# Use the Math Module:
# Write a program that imports the math module and uses it to:
# Find the square root of a number.
# Calculate the sine of an angle .
# Find the greatest common divisor (GCD) of two numbers .

# import math
#
# num = int(input('Enter a number : '))
# num = int(input('Enter a Angle in degree : '))
# num1 = int(input('Enter first number for gcd : '))
# num2 = int(input('Enter second number for gcd : '))
# # sq = math.sqrt(num)
# sin = math.sin(num)
# gcd = math.gcd(num1,num2)
# #
# # print('sq of : ',num,'is ',sq)
# print('sin of ',num,'is ',sin)
# print('Gcd of ','of ',num1,'and ',num2,'is ',gcd)

#output
# Enter a number : 156
# sq of :  156 is  12.489995996796797
# Enter a Angle in degree : 0
# Enter first number for gcd : 10
# Enter second number for gcd : 20
# sin of  0 is  0.0
# Gcd of  of  10 and  20 is  10



# Use the Random Module:
# Write a program that imports the random module and uses it to:
# Generate and print a random integer between 1 and 100.
# Create a list of random numbers  and print the list.
# Shuffle a list of numbers and print the shuffled list.


# import random
#
#
# rand_int = random.randint(1, 100)
# print("Random integer between 1 and 100:", rand_int)
#
#
# random_list = [random.randint(1, 100) for _ in range(10)]  # 10 random numbers
# print("List of random numbers:", random_list)
#
#
# numbers = list(range(1, 11))  # list from 1 to 10
# random.shuffle(numbers)
# print("Shuffled list:", numbers)
#
#
# #output
# Random integer between 1 and 100: 22
# List of random numbers: [74, 11, 75, 27, 72, 55, 72, 4, 96, 38]



# Use the OS Module:
# Write a program that imports the os module and uses it to:
# Print the current working directory
# Create a new directory and verify its existence.
# List all files and directories in the current directory

# import os
#
# # 1. Print the current working directory
# print("Current working directory:", os.getcwd())
#
# # 2. Create a new directory
# new_dir = "my_new_folder"
# os.mkdir(new_dir)
#
# # Verify its existence
# if os.path.exists(new_dir):
#     print(f"Directory '{new_dir}' created successfully!")
#
# # 3. List all files and directories in the current directory
# print("Files and directories in current directory:")
# for item in os.listdir():
#     print(item)
#
# #output
# Current working directory: C:\Wipro Training\Python\PythonCoding\daily_assignment
# Directory 'my_new_folder' created successfully!
# Files and directories in current directory:
# countchar.py
# day2-assignment.py
# day3-assignment.py
# my_new_folder
# sumofnum.py



# Create and Use a Custom Package:
# Create a package called my_math with two modules: arithmetic.py and geometry.py.
# In arithmetic.py, define functions for addition, subtraction, multiplication, and division.
# In geometry.py, define functions to calculate the area of a circle and the area of a
# rectangle.
# Write a program that imports these functions from the my_math package and uses
# them to perform various calculations.

# from my_math import arithmetic,geometric
#
#
#
# print("Addition:", arithmetic.add(10, 5))
# print("Subtraction:", arithmetic.subtract(10, 5))
# print("Multiplication:", arithmetic.multiply(10, 5))
# print("Division:", arithmetic.divide(10, 5))
#
# # Geometry examples
# print("Area of circle (r=7):", geometric.area_circle(7))
# print("Area of rectangle (l=10, w=5):", geometric.area_rectangle(10, 5))
#
# #output
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
# Area of circle (r=7): 153.93804002589985
# Area of rectangle (l=10, w=5): 50



# Create a Package for String Utilities:
# Create a package called string_utils with two modules: string_operations.py and
# string_validations.py.
# In string_operations.py, define functions for reversing a string, converting a string to
# uppercase, and finding the length of a string.
# In string_validations.py, define functions to check if a string is a palindrome and if it
# contains only alphabetic characters.
# Write a program that imports and uses these functions from the string_utils package.


# from string_utils import string_operations as so, string_validations as sv
#
# text = "Radar"
#
# # Using string_operations
# print("Reversed:", so.reverse_string(text))
# print("Uppercase:", so.to_uppercase(text))
# print("Length:", so.string_length(text))
#
# # Using string_validations
# print("Is palindrome?", sv.is_palindrome(text))
# print("Contains only alphabets?", sv.is_alpha(text))
# #output
# Reversed: radaR
# Uppercase: RADAR
# Length: 5
# Is palindrome? True
# Contains only alphabets? True





















