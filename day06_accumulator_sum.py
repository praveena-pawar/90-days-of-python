# 1. Read & think
nums = [2, 4, 6, 8]
total = 0

for n in nums:
    total += n

print(total)

#output:
#total : 20

# Think:

# Why did we start total = 0?
# We start with total = 0 because 0 is the neutral value for addition.

# What happens in each loop iteration?
# In each iteration the loop adds the current element to the accumulator.




# 2: You write code
# Task 1️

# Write a program to:
# Find the sum of all numbers in a list

nums = [10, 85, 76, 98, 42, 38]
total = 0

for n in nums:
    total += n

print("The sum of all numbers is :", total)

#output :
# The sum of all numbers is : 349




# Task 2️

# Write a program to:
# Find the sum of only even numbers in a list

nums = [80, 69, 78, 7, 18, 52, 99]
total_even = 0

for n in nums:
    if n % 2 == 0:
        total_even += n

print("The sum of only even numbers :", total_even)

#output:
#The sum of only even numbers : 228




# Task 3️

# Write a program to:
# Find the largest number in a list
# (Do NOT use max())

nums = [25, 38, 47, 55, 67, 78, 10]

large_num = nums[0]   # assume first number is largest

for n in nums:
    if n > large_num:
        large_num = n   # replace, not add

print(large_num)





