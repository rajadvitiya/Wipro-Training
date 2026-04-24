# string_validations.py

def is_palindrome(s):
    # Normalize case and remove spaces for palindrome check
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_alpha(s):
    return s.isalpha()
