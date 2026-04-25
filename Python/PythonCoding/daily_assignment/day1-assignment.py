# Write a program that asks the user for their age and checks if they are eligible to
# vote (18 years and older). Print a message based on their eligibility.

# age = int(input('Enter your age : '))
# if age >= 18:
#     print('You can vote..')
# else:
#     print("You can't vote..")
#
# #output
# Enter your age : 22
# You can vote..




# Write a program that takes a year as input and checks if it is a leap year or not.
# Print the result.

# year = int(input('Enter the year : '))
#
# if year % 400 == 0:
#     print('Leap year..')
#
# elif year % 100 == 0 and year % 400 != 0 :
#     print('Not a leap year..')
#
# elif year % 4 ==0 and year % 100 != 0:
#     print('Leap year..')
#
# #output
# Enter the year : 2024
# Leap year..



# Write a program that takes a number as input and checks if it is divisible by 5.
# Print a message if it is divisible or not.


# num = int(input('Enter the number : '))
#
# if num % 5 == 0:
#     print('Divisible by 5..')
# else:
#     print('Not divisible by 5..')
#
#
# #output
# Enter the number : 65
# Divisible by 5..



# Write a program that takes a character as input and checks if it is a vowel or
# consonant. Print the result.

# char = input('Enter a character: ')
# if char.lower() in ('a','e','i','o','u'):
#     print('Vowel..')
# else:
#     print('Consonent..')
#
# #output
# Enter a character: A
# Vowel..



# Write a program that takes a password as input and checks if it is strong (at least
# 8 characters). Print a message based on the result.


# password = input('Enter you password: ')
# if len(password) >= 8:
#     print('Strong password..')
#
# else:
#     print('Create a strong password !!!')
#
#
# #output
#
# Enter you password: lkknfnfsdv
# Strong password..

# Write a program that takes a grade (A, B, C, D, F) as input and uses match-case
# to print a message corresponding to the grade (e.g., "Excellent" for A, "Good" for
# B, etc.).

# grade = input('Enter grade : ')
#
# match grade.upper():
#     case 'A':
#         print('Excellent')
#
#     case 'B':
#         print('Good')
#
#     case 'C':
#         print('Bad')
#
#     case 'D':
#         print('Very Bad')
#
#     case _:
#         print('Invalid grade..')
#
#
# #output
# Enter grade : a
# Excellent


# Write a program that takes a traffic light color (Red, Yellow, Green) as input and
# uses match-case to print the corresponding action (e.g., "Stop" for Red, "Wait"
# for Yellow, etc.).


# Program to check traffic light action using match-case

# Take input from user
# color = input("Enter traffic light color (Red, Yellow, Green): ").strip().capitalize()
#
# # Use match-case to decide action
# match color:
#     case "Red":
#         print("Stop")
#     case "Yellow":
#         print("Wait")
#     case "Green":
#         print("Go")
#     case _:
#         print("Invalid color entered")
#
# #output
# Enter traffic light color (Red, Yellow, Green): yellow
# Wait


# Write a program that takes a number as input and uses a for loop to calculate its
# factorial. Print the result.



# Program to calculate factorial using a for loop

# Take input from user
# num = int(input("Enter a number: "))
#
# # Initialize factorial result
# factorial = 1
#
# # Use for loop to calculate factorial
# for i in range(1, num + 1):
#     factorial *= i
#
# # Print the result
# print(f"The factorial of {num} is {factorial}")
#
#
# #output
# Enter a number: 5
# The factorial of 5 is 120


# Write a program that uses a for loop to print all even numbers between 1 and 20.


# for num in range(1, 21):
#     if num % 2 == 0:
#         print(num)
#
# #output
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# . Write a program that uses a while loop to create a countdown timer from 10 to 0.
# Print each number.



# count = 10
#
# # Use while loop to countdown
# while count >= 0:
#     print(count)
#     count -= 1
#
#
#     #output
#
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0



# Write a program that uses a for loop to count the number of vowels in a given
# string. Print the count.


# text = input("Enter a string: ")
#
# # Define vowels
# vowels = "aeiouAEIOU"
#
# # Initialize counter
# count = 0
#
# # Loop through each character in the string
# for char in text:
#     if char in vowels:
#         count += 1
#
# # Print the result
# print(f"The number of vowels in the string is: {count}")
#

#output

# Enter a string: aedei
# The number of vowels in the string is: 4



#  Write a program that uses a for loop to print numbers from 1 to 10, but skips
# printing the number 5 (use continue) and stops the loop if the number 8 is
# reached (use break).

# Program to print numbers from 1 to 10
# Skips 5 and stops at 8
#
# for num in range(1, 11):
#     if num == 5:
#         continue   # Skip printing 5
#     if num == 8:
#         break      # Stop the loop when 8 is reached
#     print(num)
#
#
#
# #output
#
# 1
# 2
# 3
# 4
# 6
# 7










