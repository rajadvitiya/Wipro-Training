# list manipulation
#q1

# fruits = ['Apple','Banana','Orange','Guava','Watermelon']

# fruits.append('papaya')

# fruits.append('Grapes')

# print(fruits)

# fruits.pop()

# print(fruits)

# print('second fruit ',fruits[1])

# print('fourth fruit ',fruits[3])

# print(fruits[0:3])

# print(len(fruits))

#outputs

# ['Apple', 'Banana', 'Orange', 'Guava', 'Watermelon', 'papaya', 'Grapes']
# ['Apple', 'Banana', 'Orange', 'Guava', 'Watermelon', 'papaya']
# second fruit  Banana
# fourth fruit  Guava
# ['Apple', 'Banana', 'Orange']
# 6



#tuple manipulation
#q2

# cities = ("Mumbai",'Lucknow','Kanpur')
#
# print(cities[0])
# print(cities[2])
#
# addon = ('Varanshi','Nagpur')
#
# comb = cities + addon
#
# print(comb)
#
# city1, city2, city3 = cities
#
# print(city1)
# print(city2)
# print(city3)
#
# #output
#
# Mumbai
# Kanpur
# ('Mumbai', 'Lucknow', 'Kanpur', 'Varanshi', 'Nagpur')
# Mumbai
# Lucknow
# Kanpur

#set manipulation
#q3

# colors = {'pink','red','green','yellow','white'}
# print(colors)
#
# colors.add('orange')
# print(colors)
#
# colors.remove('white')
# print(colors)
#
# addon = {'blue','black','brown'}
#
# print('intersections : ',colors.intersection(addon))
# print('union : ',colors.union(addon))
# print('difference : ',colors.difference(addon))
#
# if 'white' in colors:
#     print('white is present : ')
# else:
#     print('not present : ')
#
# fruits = ['Apple','Banana','Orange','Guava','Watermelon','Apple']
#
# set1 = set(fruits)
# print(set1)
#
# #output
#
# {'red', 'pink', 'green', 'yellow', 'white'}
# {'red', 'pink', 'orange', 'green', 'yellow', 'white'}
# {'red', 'pink', 'orange', 'green', 'yellow'}
# intersections :  set()
# union :  {'red', 'black', 'pink', 'orange', 'blue', 'brown', 'green', 'yellow'}
# difference :  {'orange', 'red', 'pink', 'green', 'yellow'}
# not present :
# {'Apple', 'Banana', 'Guava', 'Watermelon', 'Orange'}


# # Dictionary manipulation
# q4
# info = {'name':'Aditya','age':22,'hobby':'coding'}
# print(info)
#
# print('name : ',info['name'])
#
# info['fav_food'] = "paneer"
#
# info['hobby'] = 'writing'
#
# print('updated info ',info)
#
# for k, v in info.items():
#     print('keys: ',k,'values; ',v)
#
# info.pop('age')
#
# print(info)
#
# #output
#
# {'name': 'Aditya', 'age': 22, 'hobby': 'coding'}
# name :  Aditya
# updated info  {'name': 'Aditya', 'age': 22, 'hobby': 'writing', 'fav_food': 'paneer'}
# keys:  name values;  Aditya
# keys:  age values;  22
# keys:  hobby values;  writing
# keys:  fav_food values;  paneer
# {'name': 'Aditya', 'hobby': 'writing', 'fav_food': 'paneer'}
