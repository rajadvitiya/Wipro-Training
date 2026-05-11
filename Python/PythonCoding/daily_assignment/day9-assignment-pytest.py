# 1. The Basic Assertion
# Goal:  Understand the simplicity of pytest syntax.
# Write a file named `test_logic.py`. Create a test function `test_math_operations` that
# uses simple `assert` statements to verify:
# That $15 \times 3$ equals $45$.
# That the string `"pytest"` is present within the phrase `"Learning pytest is fun"`.



# File: test_logic.py

import pytest
# def test_math_operations():
#     #  Check that 15 * 3 equals 45
#     assert 15 * 3 == 45
#
#     #  Check that "pytest" is present in the phrase
#     assert "pytest" in "Learning pytest is fun"


#output

# ============================= test session starts =============================
# collecting ... collected 1 item
#
# day9-assignment-pytest.py::test_math_operations PASSED                   [100%]
#
# ============================== 1 passed in 0.08s ==============================
#
# Process finished with exit code 0


# 2. Using Fixtures for Setup
# Goal:  Replace `setUp` and `tearDown` with the modern `@pytest.fixture` approach.
# Create a pytest fixture named `sample_dict` that returns a dictionary: `{"name":
# "Alice", "role": "Dev"}`.
# Write a test function `test_dict_keys` that:
# Accepts the fixture as an argument.
# Asserts that the key `"role"` exists in the dictionary.
# Asserts that the value of `"name"` is `"Alice"`.



# File: test_logic.py
# import pytest
#
# @pytest.fixture
# def sample_dict():
#     # Fixture returns a dictionary for tests
#     return {"name": "Alice", "role": "Dev"}
#
# def test_dict_keys(sample_dict):
#     # Check that the key "role" exists
#     assert "role" in sample_dict
#
#     # Check that the value of "name" is "Alice"
#     assert sample_dict["name"] == "Alice"
#


#output
# Launching pytest with arguments day9-assignment-pytest.py::test_dict_keys --no-header --no-summary -q in C:\Wipro Training\Python\PythonCoding\daily_assignment
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# day9-assignment-pytest.py::test_dict_keys PASSED                         [100%]
#
# ============================== 1 passed in 0.04s ==============================
#
# Process finished with exit code 0



# 3. Handling Exceptions
# Goal:  Use the `pytest.raises` context manager.
# Write a function `get_element(my_list, index)` that returns an item from a list. Write a
# test function `test_index_error` that uses `with pytest.raises(IndexError):` to verify that
# attempting to access index `10` of the list `[1, 2, 3]` correctly triggers an error.



# File: test_logic.py
# import pytest
#
# def get_element(my_list, index):
#     # Return the element at the given index
#     return my_list[index]
#
# def test_index_error():
#     # Verify that accessing index 10 of a 3-element list raises IndexError
#     with pytest.raises(IndexError):
#         get_element([1, 2, 3], 10)


#output
# Launching pytest with arguments day9-assignment-pytest.py::test_index_error --no-header --no-summary -q in C:\Wipro Training\Python\PythonCoding\daily_assignment
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# day9-assignment-pytest.py::test_index_error PASSED                       [100%]
#
# ============================== 1 passed in 0.03s ==============================
#
# Process finished with exit code 0


# 4. Parameterized Testing
# Goal:  Run the same test logic with multiple sets of data.
# Use the `@pytest.mark.parametrize` decorator to create a single test function
# `test_is_even`.
# Pass three different inputs to the test: `2`, `10`, and `22`.
# The test should assert that each input `% 2 == 0`.
# Observe how pytest treats these as three separate test cases in the output.


# File: test_logic.py
# import pytest
#
# @pytest.mark.parametrize("num", [2, 10, 22])
# def test_is_even(num):
#     # Assert that the number is even
#     assert num % 2 == 0



#output

# Launching pytest with arguments day9-assignment-pytest.py::test_is_even --no-header --no-summary -q in C:\Wipro Training\Python\PythonCoding\daily_assignment
#
# ============================= test session starts =============================
# collecting ... collected 3 items
#
# day9-assignment-pytest.py::test_is_even[2]
# day9-assignment-pytest.py::test_is_even[10]
# day9-assignment-pytest.py::test_is_even[22]
#
# ============================== 3 passed in 0.04s ==============================
# PASSED                        [ 33%]PASSED                       [ 66%]PASSED                       [100%]
# Process finished with exit code 0



# 5. Cleaning Up with Fixture Yields
# Goal:  Manage resources (like files or database connections) properly.
# Create a fixture named `temp_file`.
# In the  Setup phase : Create a new text file named `test.txt` and write `"Hello World"`
# into it.
# Yield  the filename to the test.
# In the  Teardown phase  (after the yield): Use the `os` module to delete the file.
# Write a test `test_file_content` that reads the file and verifies the text matches.


# File: test_logic.py
# import pytest
# import os
#
# @pytest.fixture
# def temp_file():
#     # Setup phase: create a file and write text
#     filename = "test.txt"
#     with open(filename, "w") as f:
#         f.write("Hello World")
#
#     # Yield the filename to the test
#     yield filename
#
#     # Teardown phase: delete the file after test completes
#     if os.path.exists(filename):
#         os.remove(filename)
#
# def test_file_content(temp_file):
#     # Read the file and verify its content
#     with open(temp_file, "r") as f:
#         content = f.read()
#     assert content == "Hello World"

#output
# Launching pytest with arguments day9-assignment-pytest.py::test_file_content --no-header --no-summary -q in C:\Wipro Training\Python\PythonCoding\daily_assignment
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# day9-assignment-pytest.py::test_file_content PASSED                      [100%]
#
# ============================== 1 passed in 0.35s ==============================
#
# Process finished with exit code 0

