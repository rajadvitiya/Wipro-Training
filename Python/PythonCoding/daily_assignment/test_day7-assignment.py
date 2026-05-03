# Basic Test Function
# Write a pytest test function that checks whether the sum of two numbers (3 and 5)
# equals 8.

import pytest


#  Developer code


# def sum_of_two_num(num1, num2):
#     return num1 + num2


# Test code


# def test_sum_of_two_num():
#     assert sum_of_two_num(10,5) == 15, 'Add Error'


# output

#  pytest -v
# =============================================================================== test session starts ===============================================================================
# platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Wipro Training\Python\PythonCoding\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Wipro Training\Python\PythonCoding\daily_assignment
# collected 1 item
#
# test_day7-assignment.py::test_sum_of_two_num PASSED                                                                                                                          [100%]




# Assertion Failure
# Create a pytest test that intentionally fails by asserting that "hello".upper() equals
# "hello".






# Developer code

# def check_hello():
#     str1 = 'hello'.upper()
#     return str1



# Test code

# def test_hello():
#     assert check_hello() == 'hello', 'Not Equal'


# output

#  pytest -v
# =============================================================================== test session starts ===============================================================================
# platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Wipro Training\Python\PythonCoding\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Wipro Training\Python\PythonCoding\daily_assignment
# collected 1 item

# test_day7-assignment.py::test_hello FAILED                                                                                                                                   [100%]
#
# ==================================================================================== FAILURES =====================================================================================
# ___________________________________________________________________________________ test_hello ____________________________________________________________________________________
#
#     def test_hello():
# >       assert check_hello() == 'hello', 'Not Equal'
# E       AssertionError: Not Equal
# E       assert 'HELLO' == 'hello'
# E
# E         - hello
# E         + HELLO
#
# test_day7-assignment.py:56: AssertionError
# ============================================================================= short test summary info =============================================================================
# FAILED test_day7-assignment.py::test_hello - AssertionError: Not Equal





# Fixture Usage
# Define a pytest fixture that returns a list of numbers [1, 2, 3]. Write a test that uses this
# f
# ixture to verify the list length is 3.


# fixture
# @pytest.fixture(scope='function')
# def fixture():
#     list1 = [1, 2, 3]
#     return list1


# Test code

# def test_list_len(fixture):
#     assert len(fixture) == 3 , 'len not equal to  3'
    

#output

# platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Wipro Training\Python\PythonCoding\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Wipro Training\Python\PythonCoding\daily_assignment
# collected 1 item
#
# test_day7-assignment.py::test_list_len PASSED




# Parameterized Test
# Use @pytest.mark.parametrize to test a function square(x) for inputs 2, 3, 4 and
# expected outputs 4, 9, 16.

#Devloper

# def square(num):
#     return num * num


#Tester code

# @pytest.mark.parametrize('num, res',[(2,4),(3,9),(4,16)])
# def test_square(num, res):
#     assert square(num) == res , 'Error'

#output
# =============================================================================== test session starts ===============================================================================
# platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Wipro Training\Python\PythonCoding\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Wipro Training\Python\PythonCoding
# collected 3 items
#
# daily_assignment/test_day7-assignment.py::test_square[2-4] PASSED                                                                                                            [ 33%]
# daily_assignment/test_day7-assignment.py::test_square[3-9] PASSED                                                                                                            [ 66%]
# daily_assignment/test_day7-assignment.py::test_square[4-16] PASSED
#
# [100%]


# Exception Handling
# Write a pytest test that verifies a ZeroDivisionError is raised when dividing by zero using
# pytest.raises.


#Developer code

# def div(n1, n2):
#
#     return n1 / n2


#Tester code

# def test_div():
#      with pytest.raises(ZeroDivisionError):
#          div(10,0)


#output
# pytest -v
# =============================================================================== test session starts ===============================================================================
# platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Wipro Training\Python\PythonCoding\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Wipro Training\Python\PythonCoding
# collected 1 item
#
# daily_assignment/test_day7-assignment.py::test_div PASSED                                                                                                                    [100%]
#
# ================================================================================ 1 passed in 0.05s ================================================================================



