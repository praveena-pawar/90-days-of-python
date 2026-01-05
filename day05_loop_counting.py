# 1. Read & think
nums = [2, 5, 8, 11, 14]
even_count = 0
odd_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, odd_count)

#output:
#even_count : 3 and odd_count : 2

# Think:

# Why do we need two counters?
# We use two counters because we are tracking two different results.

# What happens in each loop iteration?
# A for loop goes one element at a time.



# 2. You write code

# Task 1️

# Write a program to:
# Count how many numbers are greater than 10
# And how many are 10 or less

nums = [9, 11, 10, 18, 25, 5, 4, 12]
small_count = 0
big_count = 0

for n in nums:
    if n <= 10:
        small_count += 1
    else:
        big_count += 1

print("Small numbers count :", small_count)
print("Big numbers count :", big_count)

