import re

# beg and end pattern matching

# text = input('Enter a text ') # India is my countary
# bpat = input('Enter begining pattern ')  # India
# epat = input('Enter ending pattern ')  #country
# # bpat = '^' + bpat
# # epat = epat + '$'
#
#
# if re.search(pattern=bpat,string=text):
#     print('Begining pattern present ')
# else:
#     print('Beginning pattern is not present ')
#
#
#
# if re.search(pattern=epat,string=text):
#     print('Ending pattern present ')
# else:
#     print('Ending pattern is not present ')

    
#digit
# mbno = input('Enter a text ')
# pat = r"\d"
#
#
# if re.fullmatch(pattern =pat, string=mbno):
#     print('Only digit')
# else:
#     print('Other char avail')


#username

# un = input('Enter UN ')
# pat = r"^[a-z_]{8,}$"
#
# if re.match(pattern=pat,string=un):
#     print('valid user name')
#
# else:
#     print('Invalid user name')


#email

"""email = input('Enter your email ')
pat = r"^[a-zA-Z0-9]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat,string=email):
    print('valid user name')

else:
    print('Invalid user name')
"""

#pwd
"""pwd = input('pwd : ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=]).{8,}$"
if re.match(pattern=pat,string=pwd):
    print('valid ')

else:
    print('Invalid ')
    
"""
#
# text = input('Text ')
# pat = r"\s+"

# print(re.sub(pattern=pat,string=text,repl=' '))

# print(re.split(pattern=pat,string=text))

