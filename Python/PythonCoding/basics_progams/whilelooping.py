#natural numbers printing

# num = int(input('Enter a number'))
# value = 1
#
# while value <= num:
#     print(value)
#     value += 1

#armstrong number code

num = input('Enter a number')
count = len(num)

ni = int(num)
comp = ni
sum = 0
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni // 10
if comp == sum:
    print('Armstrong number')
else:
    print('Not Armstrong')


