# What is a Palindrome?
# ---> A string that reads the same forward and backward.

# Examples:
# "madam" 
# "racecar" 



# Task 1 :

# Check whether a given string is a palindrome.

s = "madam"

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalpha():
            left += 1
            continue

        if not s[right].isalpha():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome(s))
