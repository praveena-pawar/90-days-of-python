# Task 1: 

# Find Maximum Element

nums = [3, 7, 2, 9, 4]

def find_max(nums):
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    
    return max_num

print(find_max(nums))

