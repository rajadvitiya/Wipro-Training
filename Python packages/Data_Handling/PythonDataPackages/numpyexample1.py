'''
NumPy Arrays
Creating Arrays from Lists
'''

import numpy as np

# # Creating a 1D array from a list
# list_1d = [1, 2, 3, 4, 5]
# array_1d = np.array(list_1d)
# print("1D Array from list:", array_1d)
#
# # Creating a 2D array from a list of lists
# list_2d = [[1, 2, 3], [4, 5, 6]]
# array_2d = np.array(list_2d)
# print("2D Array from list of lists:\n", array_2d)


'''
Array Attributes
Shape and Size: Get the shape and size of a NumPy array using the shape
 and size attributes.
Data Types: NumPy arrays have a single data type for all elements.
You can check the data type with the dtype attribute.
Specify the data type when creating an array.

'''

# array = np.array([[1, 2, 3], [4, 5, 6]])
#
# # Shape of the array
# print("Shape of array:", array.shape)
#
# # Size of the array
# print("Size of array:", array.size)
#
# # Data type of the array
# print("Data type of array:", array.dtype)
#
# array_float = np.array([1, 2, 3], dtype=np.float16)
# print("Array with specified data type:", array_float)
# print("Data type of the array:", array_float.dtype)



'''
Built-in Functions
arange: Similar to Python's range() but returns a NumPy array.
linspace: Creates an array of evenly spaced values over a specified range.
ones: Creates an array filled with ones.
zeros: Creates an array filled with zeros.
'''

# array_arange = np.arange(0.5, 10.75, 0.75)
# print("Array with arange:", array_arange)
#
# array_linspace = np.linspace(21, 51, 5)
# print("Array with linspace:", array_linspace)
#
# array_ones = np.ones((2, 3))
# print("Array of ones:\n", array_ones)
#
# array_zeros = np.zeros((2, 3))
# print("Array of zeros:\n", array_zeros)


# '''
# Random Arrays
# rand: Creates an array of given shape with random values between 0 and 1.
# randn: Creates an array of given shape with random values from a
#                 standard normal distribution.
# randint: Creates an array with random integers within a specified range.
#
# '''

# array_rand = np.random.rand(2, 3)
# print("Random array with rand:\n", array_rand)
#
# array_randn = np.random.randn(2, 3)
# print("Random array with randn:\n", array_randn)
#
# array_randint = np.random.randint(0, 10, (2, 3))
# print("Random array with randint:\n", array_randint)



'''
Indexing and Slicing
Reshaping Arrays
Change the shape of an array without changing its data using the
 reshape() method.

'''

array = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing
print("Element at [0, 1]:", array[0, 1])

# Slicing
print("First row:", array[0, :])
print("First column:", array[:, 0])
print("Sub-array:", array[0:2, 1:3])

array = np.arange(6)
print("Original array:", array)
print("Shape of array:", array.shape)

reshaped_array = array.reshape((2, 3))
print("Reshaped array:\n", reshaped_array)




'''
Array Operations
Element-wise Operations :  NumPy supports element-wise operations,
which apply operations to each element in the array individually.

'''

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
print("Element-wise addition:", array1 + array2)

# Element-wise subtraction
print("Element-wise subtraction:", array1 - array2)

# Element-wise multiplication
print("Element-wise multiplication:", array1 * array2)

# Element-wise division
print("Element-wise division:", array1 / array2)

'''
Basic Arithmetic Operations
NumPy provides functions for basic arithmetic operations which also operate element-wise.

Aggregate Functions
NumPy provides aggregate functions that operate over the entire array 
or along a specific axis.

'''

# Adding a scalar to an array
print("Adding 10 to each element:", array1 + 10)

# Multiplying each element by a scalar
print("Multiplying each element by 2:", array1 * 2)

# Using numpy functions
print("Square of each element:", np.square(array1))
print("Square root of each element:", np.sqrt(array1))


array = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of all elements
print("Sum of all elements:", np.sum(array))

# Mean of all elements
print("Mean of all elements:", np.mean(array))

# Minimum element
print("Minimum element:", np.min(array))

# Maximum element
print("Maximum element:", np.max(array))

# Sum along each column
print("Sum along each column:", np.sum(array, axis=0))

# Sum along each row
print("Sum along each row:", np.sum(array, axis=1))



'''
Basic Mathematical Functions
Trigonometric Functions
NumPy provides various trigonometric functions such as sine, cosine,
tangent, etc.
'''

import numpy as np

angles = np.array([0, np.pi/2, np.pi])
print(angles)
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Tangent of angles:", np.tan(angles))

# Inverse trigonometric functions
print("Arcsine of 1:", np.arcsin(1))
print("Arccosine of 0:", np.arccos(0))
print("Arctangent of 1:", np.arctan(1))

'''
Exponential and Logarithmic Functions
Rounding and Modulus Functions
'''

values = np.array([1, 2, 3])

print("Exponential of values:", np.exp(values))
print("Natural log of values:", np.log(values))
print("Base-10 log of values:", np.log10(values))

values = np.array([1.7, 2.3, 3.9])

print("Floor of values:", np.floor(values))
print("Ceil of values:", np.ceil(values))
print("Rounded values:", np.round(values))

print("Modulus of 5 and 2:", np.mod(5.5, -2.0))
print("Remainder of 5 divided by 2:", np.remainder(5.5, -2.0))

'''
Linear Algebra Functions
Dot Product and Matrix Multiplication
Determinants and Inverses
Eigenvalues and Eigenvectors

'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot product of A and B:", np.dot(A, B))
print("Matrix multiplication of A and B:", np.matmul(A, B))

print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)



'''
Basic Mathematical Functions
Trigonometric Functions
NumPy provides various trigonometric functions such as sine, cosine,
tangent, etc.
'''

import numpy as np

angles = np.array([0, np.pi/2, np.pi])
print(angles)
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Tangent of angles:", np.tan(angles))

# Inverse trigonometric functions
print("Arcsine of 1:", np.arcsin(1))
print("Arccosine of 0:", np.arccos(0))
print("Arctangent of 1:", np.arctan(1))

'''
Exponential and Logarithmic Functions
Rounding and Modulus Functions
'''

values = np.array([1, 2, 3])

print("Exponential of values:", np.exp(values))
print("Natural log of values:", np.log(values))
print("Base-10 log of values:", np.log10(values))

values = np.array([1.7, 2.3, 3.9])

print("Floor of values:", np.floor(values))
print("Ceil of values:", np.ceil(values))
print("Rounded values:", np.round(values))

print("Modulus of 5 and 2:", np.mod(5.5, -2.0))
print("Remainder of 5 divided by 2:", np.remainder(5.5, -2.0))

'''
Linear Algebra Functions
Dot Product and Matrix Multiplication
Determinants and Inverses
Eigenvalues and Eigenvectors

'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot product of A and B:", np.dot(A, B))
print("Matrix multiplication of A and B:", np.matmul(A, B))

print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)




import pandas as pd

'''
Basic Usage and Conventions
Pandas provides two main data structures: DataFrame and Series. 
A DataFrame is a 2-dimensional labeled data structure with columns of potentially 
different types. 
A Series is a 1-dimensional labeled array.
'''

#Creating a Series:
data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(data)
print(type(data))
series = pd.Series(data)
print(series)
print(type(series))

#Creating a DataFrame
# data = [[1,2,3],[4,5,6]]
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print(df)

'''
Basic DataFrame Operations:
Head and Tail: View the first or last few rows of the DataFrame.
'''

print('head \n ',df.head(4))  # First 5 rows by default
print('tail - 2  \n ',df.tail(2)) # Last 2 rows

print( '=============================================')
print('info',df.info())
print('desc   \n',df.describe())

#Selecting Columns
print(df['Name'])
print(df[['Name', 'City']])

#Filtering Rows
print(df[df['Age'] >= 30])







'''
Data Structures in Pandas
Series
A Series is a one-dimensional labeled array capable of holding data of
any type (integer, string, float, python objects, etc.).
The axis labels are collectively referred to as the index.

Creating Series from Lists, Dictionaries, and Arrays
'''

import pandas as pd

data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print(series_from_list)

data_dict = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)

import numpy as np

data_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(data_array)
print(series_from_array)

'''
Series Attributes and Methods
Attributes, Methods
'''

print(series_from_list.index)  # RangeIndex(start=0, stop=5, step=1)
print(series_from_list.values) # array([1, 2, 3, 4, 5])
print(series_from_list.dtype)  # dtype('int64')

print(series_from_list.head(3))  # First 3 elements
print(series_from_list.tail(2))  # Last 2 elements
print(series_from_list.mean())   # Mean value
print(series_from_list.sum())    # Sum of all values
print(series_from_list.describe()) # Statistical summary


#Indexing and Slicing Series

print(series_from_list[2])
print(series_from_dict['b'])

print(series_from_list[1:4])
print(series_from_list[:3])
print(series_from_list[3:])

#Operations on Series
print(series_from_list + 2)  # Adding 2 to each element
print(series_from_list * 2)  # Multiplying each element by 2

other_series = pd.Series([10, 20, 30, 40, 50])
print(series_from_list + other_series)

'''
DataFrames
A DataFrame is a 2-dimensional labeled data structure with columns of 
potentially different types. You can think of it as a table or a spreadsheet in Excel.

Creating DataFrames from Dictionaries, Lists, and NumPy Arrays

'''

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict)

data_list_dicts = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df_from_list_dicts = pd.DataFrame(data_list_dicts)
print(df_from_list_dicts)

data_array = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
])

df_from_array = pd.DataFrame(data_array, columns=['Name', 'Age', 'City'])
print(df_from_array)

'''
DataFrame Attributes and Methods
Attributes, Methods

'''

print(df_from_dict.index)   # RangeIndex(start=0, stop=3, step=1)
print(df_from_dict.columns) # Index(['Name', 'Age', 'City'], dtype='object')
print(df_from_dict.values)  # 2D array of the DataFrame values


print(df_from_dict.head(2))     # First 2 rows
print(df_from_dict.tail(1))     # Last row
print(df_from_dict.info())      # Information about the DataFrame
print(df_from_dict.describe())  # Statistical summary of numeric columns


#Indexing and Slicing DataFrames
print(df_from_dict['Name'])
print(df_from_dict[['Name', 'City']])

print(df_from_dict.iloc[0])  # By integer index
print(df_from_dict.loc[0])   # By label index (same as iloc in this case)

print(df_from_dict.iloc[0:2])  # First 2 rows
print(df_from_dict.loc[0:1])   # Rows with labels 0 and 1

#Single column selection:
print(df_from_dict['Age'])

#Multiple columns selection:
print(df_from_dict[['Name', 'City']])

#Row selection using labels (loc):
print(df_from_dict.loc[0])
print(df_from_dict.loc[0:2])

#Row selection using integer positions (iloc):
print(df_from_dict.iloc[0])
print(df_from_dict.iloc[0:2])


'''
Panel Data
Panel data, also known as longitudinal data or cross-sectional time series data, 
involves observations of multiple phenomena obtained over multiple time periods 
for the same firms or individuals. In pandas, Panel data used to be handled using 
the Panel class, but it has since been deprecated in favor of using multi-index DataFrames.

Panel Data Structure
Panel data structure allows for the storage and manipulation of three-dimensional data,
 typically with dimensions (items, major_axis, minor_axis):

Items: Axis 0, each item corresponds to a DataFrame (like different variables).
Major_axis: Axis 1, usually represents time.
Minor_axis: Axis 2, represents individual entities (like different firms or individuals).
Due to the deprecation of Panel, we now use multi-index DataFrames to handle panel data.

Creating and Manipulating Panels
Creating Panel-like Data with Multi-index DataFrames
'''

import pandas as pd
import numpy as np

# Create a multi-index DataFrame
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]

index = pd.MultiIndex.from_arrays(arrays, names=('person', 'time'))
data = pd.DataFrame(np.random.randn(4, 3), index=index, columns=['entity1',
                                                                 'entity2', 'entity3'])

print("Multi-index DataFrame:")
print(data)

#Manipulating Multi-index DataFrames
# Access data for variable 'A'
print("\nData for variable 'A':")
print(data.loc['A'])

# Access data for time period 1
print("\nData for time period 1:")
print(data.xs(1, level='time'))

# Adding a new row for a new time period
new_data = pd.DataFrame({
    'entity1': [0.5, 0.3],
    'entity2': [1.5, 1.3],
    'entity3': [2.5, 2.3]
}, index=pd.MultiIndex.from_product([['A', 'B'], [3]], names=['variable', 'time']))
print(new_data)

data = pd.concat([data, new_data])
print("\nData after adding new time period:")
print(data)

'''
Applications and Use Cases

Economics and Finance: Analyzing the financial performance of different firms over time.
Healthcare: Monitoring patient health metrics across different time periods.
Social Sciences: Studying the behavior of individuals across various time points.
Marketing: Observing the impact of marketing campaigns over time.

'''






[{"A":1,"B":5,"C":9},{"A":2,"B":6,"C":10},{"A":3,"B":7,"C":11},{"A":4,"B":8,"C":12}]