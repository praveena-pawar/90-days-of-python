# We will practice:

# Functions + Loops + Conditions (deeper)

# Returning multiple values

# Using index while looping

# String + List logic together



#  Task : 1

# Given a list of numbers, write a function that:
# Counts how many are positive
# Counts how many are negative
# Counts how many are zero
# Return all three values.

nums = [5, 8, -2, 0, -4, 3, 0]

def count_nums(nums):
    total_positive = 0
    total_negative = 0
    total_zero = 0
    for n in nums:
        if n > 0:
            total_positive += 1
        elif n < 0:
            total_negative += 1
        else:
            total_zero += 1
        
    return total_positive, total_negative, total_zero

positive, negative, zero = count_nums(nums)
print("Total positive number are :", positive)
print("Total negative number are :", negative)
print("Total zero number are :", zero)

#output:
# Total positive number are : 3
# Total negative number are : 2
# Total zero number are : 2




# Task 2 :

# You are given a list of numbers.
# Write a function that:
# Counts how many numbers are even
# Counts how many numbers are odd

nums = [10, 3, 7, 4, 8, 9]

def count_even_odd(nums):
    total_even = 0
    total_odd = 0
    for n in nums:
        if n % 2 == 0:
            total_even += 1
        else:
            total_odd += 1

    return total_even, total_odd

even, odd = count_even_odd(nums)
print("The total even number are :", even)
print("The total odd number are:", odd)

#output:
#The total even number are : 3
#The total odd number are : 3




# Task 3 :

# You are given a list of words.
# Write a function that:
# Finds which word has the maximum number of consonants
# Ignores vowels
# Ignores case
# Returns only the word