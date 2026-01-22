# Task 1 :

# Write a function that:
# Takes a list of integers
# Counts:
# numbers greater than 0 and even
# numbers less than 0 and odd
# Returns the counts as a dictionary

nums = [2, -3, 4, -5, 0, 7, -8]

def count_numbers(nums):
    result = {"positive_even": 0,"negative_odd": 0}

    for n in nums:
        if n > 0 and n % 2 == 0:
            result["positive_even"] += 1
        elif n < 0 and n % 2 != 0:
            result["negative_odd"] += 1

    return result

print(count_numbers(nums))
