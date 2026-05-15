import matplotlib.pyplot as plt
import numpy as np
# #
# #
# # # Sample data
# # x = [1, 2, 3, 4, 5]
# # y = [2, 3, 5, 7, 11]
# #
# # # Create a line plot
# # plt.plot(x, y, marker='x')
# # plt.title("Line Plot")
# # plt.xlabel("X-axis")
# # plt.ylabel("Y-axis")
# #
# # plt.show()
# #
# #
# #
# # Sample data
# categories = ['A', 'B', 'C', 'D']
# values = [10, 150, 7, 10]
#
# # Create a bar plot
# plt.bar(categories, values, color='violet')
# plt.title("Bar Plot")
# plt.xlabel("Categories")
# plt.ylabel("Sales")
# plt.show()

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a plot with customizations
# plt.plot(x, y1, marker='o', label='Series 1', color='blue')
# plt.plot(x, y2, marker='x', label='Series 2', color='green')
#
# # Customizing the plot
# plt.title("Customized Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid(True)
# plt.show()


#
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# # Sample data
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# # Create a figure with two subplots
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
#
# # First subplot
# ax1.plot(x, y1, color='blue', label='Sine')
# ax1.set_title('Sine Function')
# ax1.set_xlabel('X-axis')
# ax1.set_ylabel('Y-axis')
# ax1.legend()
#
# Second subplot
# ax2.plot(x, y2, color='red', label='Cosine')
# ax2.set_title('Cosine Function')
# ax2.set_xlabel('X-axis')
# ax2.set_ylabel('Y-axis')
# ax2.legend()
#
# # Show the plots
# plt.tight_layout()
# plt.show()




# Sample data
# data = np.random.randn(100)
#
# # Create a figure with a histogram and a density plot
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
#
# # Histogram
# ax1.hist(data, bins=10, color='skyblue', edgecolor='black')
# ax1.set_title('Histogram')
# ax1.set_xlabel('Value')
# ax1.set_ylabel('Frequency')
#
# # Density plot
# ax2.hist(data, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.6)
# data_density = np.linspace(min(data), max(data), 100)
# ax2.plot(data_density, (1/(np.sqrt(2 * np.pi))) * np.exp(-0.5 * (data_density)**2), color='red')
# ax2.set_title('Density Plot')
# ax2.set_xlabel('Value')
# ax2.set_ylabel('Density')
#
# # Show the plots
# plt.tight_layout()
# plt.show()

#
#
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
#
# # Create a sample DataFrame
# data = pd.DataFrame({
#     'x': np.random.rand(100),
#     'y': np.random.rand(100)
# })
#
# # Create a scatterplot
# sns.scatterplot(x='x', y='y', data=data)
# plt.title('Scatterplot of x vs y')
# plt.show()
#
#
# # Create a sample DataFrame with a time series
# data = pd.DataFrame({
#     'time': pd.date_range(start='1/1/2020', periods=10),
#     'value': np.random.rand(10) #.cumsum()
# })
#
# # Create a lineplot
# sns.lineplot(x='time', y='value', data=data)
# plt.title('Lineplot of Value over Time')
# plt.show()
#
#
# # Create a sample DataFrame
# data = pd.DataFrame({
#     'category': ['A', 'B', 'C', 'D'],
#     'value': [10, 20, 15, 25]
# })
#
# # Create a barplot
# sns.barplot(x='category', y='value', data=data)
# plt.title('Barplot of Categories')
# plt.show()
#
#
# # Create a sample DataFrame
# data = pd.DataFrame({
#     'category': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'C','A', 'D',
#                 'C', 'C','A', 'D', 'C', 'C']
# })
#
# # Create a countplot
# sns.countplot(x='category', data=data, legend='auto',color='red')
# plt.title('Countplot of Categories')
# plt.show()
#
# # Create a sample DataFrame
# data = pd.DataFrame({
#     'value': np.random.randn(100)
# })
#
# # Create a histogram
# sns.histplot(data['value'], bins=10)
# plt.title('Histogram of Values')
# plt.show()
#
# # Create a KDE plot
# sns.kdeplot(data['value'])
# plt.title('KDE Plot of Values')
# plt.show()
# #

import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')
'''
# Create a pair plot
sns.pairplot(iris, hue='species')
plt.title('Pair Plot of Iris Dataset')
plt.show()

# Create a joint plot
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter', hue='species')
plt.suptitle('Joint Plot of Sepal Length vs Sepal Width')
plt.show()

# Exclude non-numeric columns
numeric_iris = iris.drop(columns=['species'])

# Create a sample correlation matrix
data = numeric_iris.corr()

# Create a heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Heatmap of Iris Correlation Matrix')
plt.show()

# Create a facet grid
g = sns.FacetGrid(iris, col='species')
g.map(sns.histplot, 'sepal_length')
plt.suptitle('Facet Grid of Sepal Length by Species')
plt.show()
'''
#Customising Plots

# Set a theme
# sns.set_theme(style='whitegrid')
#
# # Create a scatter plot with the theme
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
# plt.title('Scatter Plot with Whitegrid Theme')
# plt.show()
#
# # Set a color palette
# sns.set_palette('pastel')
#
# # Create a bar plot with the color palette
# sns.barplot(x='species', y='sepal_length', data=iris)
# plt.title('Bar Plot with Pastel Color Palette')
# plt.show()
#
#
# # Create a bar plot with annotations
# sns.barplot(x='species', y='sepal_length', data=iris, errorbar='sd')
#
# # Add annotations
# for p in plt.gca().patches:
#     plt.gca().annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')
#
# plt.title('Bar Plot with Statistical Annotations')
# plt.show()
#
#
# # Create a scatter plot with Seaborn
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
#
# # Customize with Matplotlib
# plt.title('Scatter Plot with Matplotlib Customization')
# plt.xlabel('Sepal Length')
# plt.ylabel('Sepal Width')
# plt.legend(title='Species')
# plt.grid(True)
# plt.show()
#







import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')
'''
# Create a pair plot
sns.pairplot(iris, hue='species')
plt.title('Pair Plot of Iris Dataset')
plt.show()

# Create a joint plot
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter', hue='species')
plt.suptitle('Joint Plot of Sepal Length vs Sepal Width')
plt.show()

# Exclude non-numeric columns
numeric_iris = iris.drop(columns=['species'])

# Create a sample correlation matrix
data = numeric_iris.corr()

# Create a heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Heatmap of Iris Correlation Matrix')
plt.show()

# Create a facet grid
g = sns.FacetGrid(iris, col='species')
g.map(sns.histplot, 'sepal_length')
plt.suptitle('Facet Grid of Sepal Length by Species')
plt.show()
'''
#Customising Plots

# Set a theme
# sns.set_theme(style='whitegrid')
#
# # Create a scatter plot with the theme
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
# plt.title('Scatter Plot with Whitegrid Theme')
# plt.show()
#
# # Set a color palette
# sns.set_palette('pastel')
#
# # Create a bar plot with the color palette
# sns.barplot(x='species', y='sepal_length', data=iris)
# plt.title('Bar Plot with Pastel Color Palette')
# plt.show()
#
#
# # Create a bar plot with annotations
# sns.barplot(x='species', y='sepal_length', data=iris, errorbar='sd')
#
# # Add annotations
# for p in plt.gca().patches:
#     plt.gca().annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')
#
# plt.title('Bar Plot with Statistical Annotations')
# plt.show()
#
#
# # Create a scatter plot with Seaborn
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
#
# # Customize with Matplotlib
# plt.title('Scatter Plot with Matplotlib Customization')
# plt.xlabel('Sepal Length')
# plt.ylabel('Sepal Width')
# plt.legend(title='Species')
# plt.grid(True)
# plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')
'''
# Create a pair plot
sns.pairplot(iris, hue='species')
plt.title('Pair Plot of Iris Dataset')
plt.show()

# Create a joint plot
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter', hue='species')
plt.suptitle('Joint Plot of Sepal Length vs Sepal Width')
plt.show()

# Exclude non-numeric columns
numeric_iris = iris.drop(columns=['species'])

# Create a sample correlation matrix
data = numeric_iris.corr()

# Create a heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Heatmap of Iris Correlation Matrix')
plt.show()

# Create a facet grid
g = sns.FacetGrid(iris, col='species')
g.map(sns.histplot, 'sepal_length')
plt.suptitle('Facet Grid of Sepal Length by Species')
plt.show()
'''
#Customising Plots

# Set a theme
sns.set_theme(style='whitegrid')

# Create a scatter plot with the theme
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
plt.title('Scatter Plot with Whitegrid Theme')
plt.show()

# Set a color palette
sns.set_palette('pastel')

# Create a bar plot with the color palette
sns.barplot(x='species', y='sepal_length', data=iris)
plt.title('Bar Plot with Pastel Color Palette')
plt.show()


# Create a bar plot with annotations
sns.barplot(x='species', y='sepal_length', data=iris, errorbar='sd')

# Add annotations
for p in plt.gca().patches:
    plt.gca().annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.title('Bar Plot with Statistical Annotations')
plt.show()


# Create a scatter plot with Seaborn
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')

# Customize with Matplotlib
plt.title('Scatter Plot with Matplotlib Customization')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(title='Species')
plt.grid(True)
plt.show()









