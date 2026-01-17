# Task 1 :

# Write a function that:
# Takes a list of numbers
# Groups them into a dictionary:

nums = [1, 2, 3, 4, 5]

def group_even_odd(nums):
    result = {"even": [], "odd": []}

    for num in nums:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)

    return result

print(group_even_odd(nums))

#output:
#{'even': [2, 4], 'odd': [1, 3, 5]}
    