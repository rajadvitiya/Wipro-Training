# #functions
#
# def add(n1, n2):
#     print(n1,n2)
#     return n1+n2
#
# def sub(n1, n2):
#     return n1-n2
#
# def mul(n1, n2):
#     return n1*n2
#
# def div(n1, n2):
#     return n1/n2
#
#
#
#
#
#
#
# #driver
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter second number : "))
#
# res = add(n2 = num2, n1 = num1)  # keyword argument
#
# res1 = sub(num1, num2)# posisional arguments
#
# res2 = mul(num1, num2)
#
# res3 = div(num1, num2)
#
#
#
# print('Addition :',res)
#
# print('Addition :',res1)
#
# print('Addition :',res2)
#
# print('Addition :',res3)
#



#Arbitary arguments
# def add(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     return sum


# numbers = list()
# count = int(input('How many ? '))
#
#
# for _ in range(1,count+1):
#     numbers.append(int(input('enter no: ')))
# print(numbers)

# print(add(5,6,9,5))


#optional arguments


# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter second number : "))


def add(n1, n2,n3=10):
    return n1+n2+n3

# print(add(num1,num2))
# print(add(num1,num2,100))


#lamda fun

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter second number : "))
#
# add = lambda n1 ,n2 : n1+n2
#
# print(add(num1,num2))

numbers = [1,2,3,4,5]

sq = lambda num : [num * num for num in numbers if num % 2 == 0]

print(sq(numbers))



