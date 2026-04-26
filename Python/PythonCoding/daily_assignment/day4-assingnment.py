# Use class, objects, constructors while coding
# Bank Account Management System
# You are tasked with creating a simple bank account management system in Python.
# Implement a class called BankAccount with the following specifications:
# The class should have private instance variables for account number, account holder
# name, and balance.
# Include a constructor to initialize these variables.
# Implement getter and setter methods for each instance variable to ensure
# encapsulation.
# Implement methods to deposit and withdraw money from the account.
# Ensure that the withdraw method checks if the account has sufficient balance before
# allowing withdrawal.
# Write a Python program to demonstrate the functionality of the BankAccount class by
# creating instances, depositing and withdrawing money, and displaying account
# information.


# class BankAccount:
#     def __init__(self, account_no, holder_name, balance=0):
#         self.__account_no = account_no
#         self.__holder_name = holder_name
#         self.__balance = balance
#
#     def get_account_no(self):
#         return self.__account_no
#
#     def set_account_no(self, accno):
#         self.__account_no = accno
#
#     def get_holder_name(self):
#         return self.__holder_name
#
#     def set_holder_name(self, hol_name):
#         self.__holder_name = hol_name
#
#     def deposit_money(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive.")
#         return self.__balance
#
#     def withdraw_money(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return self.__balance
#         else:
#             print("Low Balance !!!")
#             return None
#
#     def show_balance(self):
#         return f"Your balance is {self.__balance}"
#
#     def show_account_details(self):
#         return (
#             f"Account No: {self.__account_no}\n"
#             f"Holder Name: {self.__holder_name}\n"
#             f"Available Balance: {self.__balance}"
#         )
#
#
# # Demonstration
# hol1 = BankAccount("45955604", "Advitiya", 50000)
# hol1.deposit_money(120000)
# hol1.withdraw_money(200000)
# print(hol1.show_account_details())
#
#
# #output
# Low Balance !!!
# Account No: 45955604
# Holder Name: Advitiya
# Available Balance: 170000





# Employee Management System
# You are developing an employee management system for a company. Implement a
# class called Employee with the following specifications:
# The class should have private instance variables for employee ID, name, and salary.
# Include a constructor to initialize these variables.
# Implement getter and setter methods for each instance variable.
# Implement a method to display employee information.
# Implement a method to give a salary hike to an employee. The method should accept a
# percentage value by which the salary will be increased.
# Write a Python program to demonstrate the functionality of the Employee class by
# creating instances, displaying employee information, giving salary hikes, and displaying
# updated employee information.



# class Employee:
#     def __init__(self,eid, nam, sal):
#         self.__empid = eid
#         self.__name = nam
#         self.__salary = sal
#
#
# 
#     # Getter methods
#     def get_empid(self):
#         return self.__empid
#
#     def get_name(self):
#         return self.__name
#
#     def get_salary(self):
#         return self.__salary
#
#     # Setter methods
#     def set_empid(self, eid):
#         self.__empid = eid
#
#     def set_name(self, nam):
#         self.__name = nam
#
#     def set_salary(self, sal):
#         if sal >= 0:  # validation to avoid negative salary
#             self.__salary = sal
#         else:
#             print("Salary must be non-negative.")
#
#     # Display method
#     def show_details(self):
#         return f"Employee ID: {self.__empid}\nName: {self.__name}\nSalary: {self.__salary}"
#
#
#     def hike_salary(self,hike_percent):
#
#         self.__salary +=  self.__salary* (hike_percent / 100)
#         print(f'Updated salary {self.__salary}')
#
#
# emp1 = Employee(12,'Rahul',500000)
#
# emp1.hike_salary(20)
# print(emp1.show_details())


#output
# Updated salary 600000.0
# Employee ID: 12
# Name: Rahul
# Salary: 600000.0
