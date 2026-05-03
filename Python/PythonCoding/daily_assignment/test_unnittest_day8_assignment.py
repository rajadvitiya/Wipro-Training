# Basic Test Case
# Write a unittest class TestMath with one test method that checks if 2 + 3 equals 5.

import unittest
from unittest import loader


# class TestMath(unittest.TestCase):
#
#     def test_sum(self):
#         self.assertEqual(2 + 3, 5)


#output

# ============================= test session starts =============================
# collecting ... collected 1 item
#
# daily_assignment/test_unnittest_day8_assignment.py::TestMath::test_sum
#
# ============================== 1 passed in 0.06s ==============================
# PASSED [100%]
# Process finished with exit code 0




# Setup and Teardown
# Create a test class that uses setUp() to initialize a list [1, 2, 3] and tearDown() to print
# "Test completed".
# Verify that the list length is 3 inside your test method.




# class TestListOperations(unittest.TestCase):
#     def setUp(self):
#         print('Initialize the list in set up')
#         self.list = [1,32,3]
#
#     def tearDown(self):
#         print('Test completed')
#
#     def test_list_len(self):
#         self.assertEqual(len(self.list), 3)
#
#
#     #output
#
#     == == == == == == == == == == == == == == = test
#     session
#     starts == == == == == == == == == == == == == == =
#     collecting...collected
#     1
#     item
#
#     daily_assignment / test_unnittest_day8_assignment.py::TestListOperations::test_list_len
#
#     == == == == == == == == == == == == == == == 1
#     passed in 0.06
#     s == == == == == == == == == == == == == == ==
#     PASSED[100 %]
#     Initialize
#     the
#     list in set
#     up
#     Test
#     completed
#
#     Process
#     finished
#     with exit code 0



# Multiple Assertions
# Write a test class TestStringMethods with methods to test:
# "hello".upper() equals "HELLO"
# "hello".isupper() returns False


# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual("hello".upper(),'HELLO')
#
#     def test_isupper(self):
#         self.assertFalse("hello".isupper(), "Hello")
#
#
#     #output
#     == == == == == == == == == == == == == == = test
#     session
#     starts == == == == == == == == == == == == == == =
#     collecting...collected
#     2
#     items
#
#     daily_assignment / test_unnittest_day8_assignment.py::TestStringMethods::test_isupper
#     daily_assignment / test_unnittest_day8_assignment.py::TestStringMethods::test_upper
#
#     == == == == == == == == == == == == == == == 2
#     passed in 0.06
#     s == == == == == == == == == == == == == == ==
#     PASSED[50 %]
#     PASSED[100 %]
#     Process
#     finished
#     with exit code 0



# Exception Testing
# Use assertRaises to verify that dividing by zero (10 / 0) raises a ZeroDivisionError.

# class TestException(unittest.TestCase):
#     def test_zero_division_error(self):
#         with self.assertRaises(ZeroDivisionError):
#             var = 10 / 0
#
#
# #output
# "C:\Wipro Training\Python\PythonCoding\.venv\Scripts\python.exe" "C:/Program Files/JetBrains/PyCharm Community Edition 2025.2.6/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --target daily_assignment/test_unnittest_day8_assignment.py::TestException
# Testing started at 7:57 PM ...
# Launching pytest with arguments daily_assignment/test_unnittest_day8_assignment.py::TestException --no-header --no-summary -q in C:\Wipro Training\Python\PythonCoding
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# daily_assignment/test_unnittest_day8_assignment.py::TestException::test_zero_division_error
#
# ============================== 1 passed in 0.06s ==============================
# PASSED [100%]
# Process finished with exit code 0



# Test Suite Execution
# Create two test classes (TestAdd and TestSubtract) and combine them into a single test
# suite using unittest.TestSuite.
# Run the suite using unittest.TextTestRunner().

# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(2+4,6)
#         self.assertEqual(2+6,8)
#
#
# class TestSub(unittest.TestCase):
#     def test_sub(self):
#         self.assertEqual(12 - 4, 8)
#         self.assertEqual(22 - 6, 16)
#
#
# def suite():
#     suite = unittest.TestSuite()
#     loader = unittest.TestLoader()
#     suite.addTests(loader.loadTestsFromTestCase(TestAdd))
#     suite.addTests(loader.loadTestsFromTestCase(TestSub))
#     return suite
#
# # runner = unittest.TextTestRunner()
# # runner.run(suite())
#
#
# #output
#
# ============================= test session starts =============================
# collecting ... collected 2 items
#
# daily_assignment/test_unnittest_day8_assignment.py::TestAdd::test_add
# daily_assignment/test_unnittest_day8_assignment.py::TestSub::test_sub
#
# ============================== 2 passed in 0.03s ==============================
# PASSED [ 50%]PASSED [100%]
# Process finished with exit code 0
#







