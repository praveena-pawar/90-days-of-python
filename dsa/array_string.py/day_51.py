# 1: Find the Largest Element
def largest_element(nums):
    large_num = float('-inf')

    for num in nums:
        if num > large_num:
            large_num = num

    return large_num

nums = [5, 2, 9, 1, 7]
print(largest_element(nums))



# 2: Find the Second Largest Distinct Element