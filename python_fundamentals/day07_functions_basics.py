# 1. Read & understand
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)


# Think:

# Why do we use def?
# def is used to define (create) a function.

# What does return do?
# return sends the result back to the place where the function was called.

# What happens after return?
# The function stops immediately
# Control goes back to the caller Any code after return inside the function does not run
# Example : 
# def test():
#     return 10
#     print("Hello")  # ❌ never runs




# Task 1️

# Write a function to:
# Take one number
# Return square of that number

def square(x):
    return x ** 2

x = float(input("Enter a number :"))
result = square(x)
print("the square of", x ,"is", result)




# Task 2️

# Write a function to:
# Take a list
# Return the sum of all numbers
# (Use loop, don’t use sum())

nums = [10, 30, 60, 80, 50]

def sum_of_list(nums):
    total = 0

    for n in nums:
        total += n
    return total

result = sum_of_list(nums)
print("The sum of all numbers :", result)

#output:
#The sum of all numbers : 230




# Task 3️

# Write a function to:
# Take a list
# Return the largest number

nums = [10, 54, 67, 94, 83, 92]

def largest_num(nums):
    large_num = nums[0]

    for n in nums:
        if n > large_num:
            large_num = n
    return large_num

result = largest_num(nums)
print("The largest number is :", result)

#output:
#THe largest number is: 94
        
