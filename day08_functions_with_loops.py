# 1. Read & think

nums = [5, 14, 8, 19, 20]
def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

result = count_even(nums)
print("The count of even numbers :", result)

#output:
#The count of even numbers : 3


# Think:

# Why is count inside the function?

# What does the function return?

# What happens when we call the function?