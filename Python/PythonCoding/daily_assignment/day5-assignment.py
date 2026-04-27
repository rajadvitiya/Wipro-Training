# Write a program that asks the user to enter some text and saves it to a file called
# output.txt. Then, open the file and read its contents, printing them to the console.


# txt = input("Enter text her want to put in file ")
# with open("example.txt", "a")  as file:
#     file.write(f'{txt}\n')
#
#
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
#
# #output
# Enter text her want to put in file you are going to get your new life
#
# hello how are you
# doing well
# what is your next plan
# you are going to get your new life
#
#
# Process finished with exit code 0



# Write a program that reads a text file called sample.txt and counts the number of lines,
# words, and characters in the file. Print the counts.


# with open("example.txt", "r") as file:
#     contents  = file.read()
#     num_char = len(contents)
#     num_words = len(contents.split())
#     num_line = len(contents.splitlines())
#
#
# print(f"Number of char : {num_char}\nNumber of words : {num_words}\nNumber of line : {num_line}")
#
# #output
# Number of char : 88
# Number of words : 19
# Number of line : 5

# Process finished with exit code 0



# Write a program that reads the contents of a file called source.txt and writes the
# contents to another file called destination.txt. Ensure that destination.txt is created if it
# doesn't exist.


# with open("example.txt", "r") as src , open("destination.txt", "w") as des:
#     for line in src:
#         des.write(line)
#
#     print("file transfer successful...")
#
# with open("destination.txt", "r") as file:
#     content = file.read()
# print(content)
#
#
# #output
# file transfer successful...
#
# hello how are you
# doing well
# what is your next plan
# you are going to get your new life
#
#
# Process finished with exit code 0

# Write a program that appends a line of text to a file called log.txt. After appending the
# text, open the file and print its contents to verify that the text was added.

# with open("log.txt", "r") as file:
#     content = file.read()
# print(content)
#
# with open("log.txt", "a") as file:
#     file.write("I'm doing good.. new line is here ")
#
# with open("log.txt", "r") as file:
#     content = file.read()
# print(content)
#
# #output
# hello how are you
# hello how are youI'm doing good.. new line is here
#
# Process finished with exit code 0




# Write a program that asks the user to input a number in the form of a string. Use a try
# except block to convert the string to an integer. If a ValueError occurs (e.g., if the user
# inputs a non-numeric string), print an error message. Otherwise, print the integer.



# num = input("Enter a number : ")
#
# try:
#     num1 = int(num)
#
# except:
#     print("Non-numeric-string")
#
# else:
#     print('Number is',int(num))
#
# #OUTPUT
#
# # Enter a number : 345
# # Number is 345
# #
# # Process finished with exit code 0
#
#
# Enter a number : jhdsvdsdf
# Non-numeric-string
#
# Process finished with exit code 0



# Write a program that tries to open a file specified by the user for reading. Use a try
# except block to handle FileNotFoundError if the file does not exist. If the file is
# successfully opened, print its contents; otherwise, print an error message.

# file_name = input("Enter file name as example.txt..")
#
# try:
#     file = open(file_name, "r")
#
# except:
#     print("File not found..")
#
# else:
#     print(file.read())


#output
# Enter file name as example.txt..log.txt
# hello how are youI'm doing good.. new line is here
#
# Process finished with exit code 0


# Enter file name as example.txt..hgfj.txt
# File not found..
#
# Process finished with exit code 0



# try:
#     num1 = int(input("Enter dividend: "))
#     num2 = int(input("Enter divisor: "))
#     res = num1 / num2
#
# except ValueError:
#     # Raised if user enters something that's not an integer
#     print("ValueError: Please enter valid numbers!")
#
# except ZeroDivisionError:
#     # Raised if divisor is zero
#     print("ZeroDivisionError: Division by zero is not allowed!")
#
# else:
#     # Runs only if no exception occurs
#     print("Result:", res)


#output
# Enter dividend: erge
# ValueError: Please enter valid numbers!

# Process finished with exit code 0

#output
# Enter dividend: 45
# Enter divisor: 0
# ZeroDivisionError: Division by zero is not allowed!



# Write a program that takes a list of numbers and asks the user to input an index to
# access an element from the list. Use a try-except block to handle IndexError if the user
# enters an invalid index. Print the corresponding element if the index is valid; otherwise,
# print an error message.


# A sample list of numbers
# numbers = [10, 20, 30, 40, 50]
#
# try:
#     index = int(input("Enter an index to access an element: "))
#     print("Element at index", index, "is:", numbers[index])
#
# except ValueError:
#     # Raised if the user enters something that's not an integer
#     print("ValueError: Please enter a valid integer index!")
#
# except IndexError:
#     # Raised if the index is out of range for the list
#     print("IndexError: The index you entered is out of range!")

#output
# Enter an index to access an element: jhgfg
# ValueError: Please enter a valid integer index!
#
# Process finished with exit code 0


# Enter an index to access an element: 5
# IndexError: The index you entered is out of range!
#
# Process finished with exit code 0


# Write a program that defines a custom exception class NegativeNumberError. The
# program should ask the user to input a positive number. If the user enters a negative
# number, raise the NegativeNumberError and handle it using a try-except block, printing
# an appropriate error message.


# class Negative_Num__Error(Exception):
#     #raised for negative nuber is enter
#     pass
#
# try:
#     num = int(input("Enter a number : "))
#     if num < 0:
#         raise Negative_Num__Error("Negative number is not allowed ...")
#     else:
#         print("Entered number ")
#
# except Negative_Num__Error as ne:
#     print(ne)
# except ValueError:
#     print("Enter valid  number...")
#
# finally:
#     print("Program is completed")

#output
# Enter a number : -89
# Negative number is not allowed ...
# Program is completed
#
# Process finished with exit code 0

# Enter a number : jhgh
# Enter valid  number...
# Program is completed



# Write a program that repeatedly asks the user to input two numbers and performs
# division. Use a try-except block inside a loop to handle ZeroDivisionError and
# ValueError. The program should continue until the user provides valid input and a valid
# division result is printed.


# while True:
#     try:
#         num1 = int(input("Enter first number "))
#         num2 = int(input("Enter second number "))
#         res = num1/num2
#
#     except ZeroDivisionError as ze:
#         print("zero in denominator is not allowed ..")
#         break
#
#     except ValueError as ve:
#         print("Invalid input..")
#         break
#
#     else:
#         print("result ",res)

#output
# Enter first number ghk
# Invalid input..

# Enter first number 90
# Enter second number 0
# zero in denominator is not allowed ..

# Enter first number 78
# Enter second number 9
# result  8.666666666666666
# Enter first number 76
# Enter second number 9
# result  8.444444444444445
# Enter first number jh
# Invalid input..



# Write a program that tries to open and read a file. Use a try-except-finally block to
# handle potential exceptions like FileNotFoundError. Ensure that the finally block prints a
# message indicating that the program has completed, whether an exception occurred or
# not.



# try:
#     # Try to open and read the file
#     with open("ejk.txt", "r") as file:
#         content = file.read()
#         print("File content:\n", content)
#
# except FileNotFoundError:
#     # Raised if the file does not exist
#     print("Error: The file was not found!")
#
# except PermissionError:
#     # Raised if you don’t have permission to read the file
#     print("Error: You don’t have permission to read this file!")
#
# else:
#     # Runs only if no exception occurs
#     print("File read successfully.")
#
# finally:
#     # Always runs, whether an exception occurred or not
#     print("Program has completed.")

#output

# hello how are you
# doing well
# what is your next plan
# you are going to get your new life
#
# File read successfully.
# Program has completed.
#
# Process finished with exit code 0

# Error: The file was not found!
# Program has completed.



# def add_numbers(a, b):
#     try:
#
#         result = float(a) + float(b)
#         print("Result:", result)
#     except ValueError:
#         # Raised if conversion fails (e.g., "abc" → float)
#         print("ValueError: Both arguments must be numeric!")


# Example usage
# add_numbers(10, 5)       # Works fine → Result: 15
# add_numbers("10", 5)     # Raises TypeError → handled by except block
# add_numbers("abc", "xyz") # Raises TypeError → handled by except block


# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print("You entered:", num)
#         break   # Exit the loop once a valid integer is given
#     except ValueError:
#         print("ValueError: Please enter a valid integer!")
#
#
# #output
# Enter an integer: hgv
# ValueError: Please enter a valid integer!
# Enter an integer: hbhb
# ValueError: Please enter a valid integer!
# Enter an integer: 567
# You entered: 567
#
# Process finished with exit code 0




