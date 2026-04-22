"""
Date: 22-4-2026
Desc: learning various if else statement
"""

#big2
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))
# num3 = int(input('Enter third number : '))

# if num1 == num2:
#     print('Both are equal')
# elif num1 > num2:
#     print(num1 , 'is big.')
# else:
#     print(num2 , 'is big.')


#big3

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))
# num3 = int(input('Enter third number : '))

"""if num1 == num2 and num2 == num3:
    print('all values are equal')

elif num1 > num2  and num1 > num3:
    print(num1 , 'num1 is biggest')

elif num2 > num3 and num2 > num1:
    print(num2 , 'num2 is biggest')

else:
    print(num3 , 'num3 is biggest')"""


#weekday

ch = int(input('Enter a number bet 1-7 '))

match ch:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Invalid choice')