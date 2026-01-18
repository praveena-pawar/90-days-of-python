# Simple Example :

nums = [1, 2, 3, 4, 5]

result = []

for n in nums:
    if n % 2 == 0:
        result.append(n * n)

print(result)



# Task 1 :

# Write a function that:
# Takes a list of numbers
# Keeps only positive numbers
# Stores their squares in a list
# Returns the list

nums = [-2, 3, 0, 4, -1, 5]

def square_of_positive_number(nums):
    result = []
    for n in nums:
        if n > 0:
            result.append(n * n)
        
    return result

positive_nums = square_of_positive_number(nums)
print("The square of positive numbers are :", positive_nums)

#output:
#The square of positive numbers are : [9, 16, 25]




# Task 2 :

# Write a function that:
# Takes a string
# Removes all vowels
# Converts remaining characters to uppercase
# Returns the final string