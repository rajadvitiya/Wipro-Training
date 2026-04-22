# count a char in a sequence using enumarate

str = input('Enter a sequence here : ')

count = 0

for i , char in enumerate(str):
    if char == 'a':
        count +=1

print('a comes ',count,'times')