# Task 1 :

# You are given a list of numbers.
# Write a function that:
# Creates a new list
# Stores squares of only positive numbers
# Ignores zero and negative numbers
# Returns the new list

nums = [2, -3, 4, 0, -1, 5, 6]

def squares_of_positive_num(nums):
    positive_num = []
    for n in nums:
        if n < 0:
            continue
        elif n == 0:
            continue
        else:
            positive_num.append(n * n) 
            

    return positive_num

result = squares_of_positive_num(nums)
print(result)

#output:
# [4, 16, 25, 36]





# Task 2 : 

# You are given a list of numbers.
# Write a function that:
# Creates a new list
# Stores only numbers that are divisible by both 3 and 5
# Returns the new list
