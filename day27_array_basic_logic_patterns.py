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

#output:
#9



# Task 2 :

# Given a list, find the minimum value.

nums = [3, 7, 2, 9, 4]

def find_min(nums):
    min_num = nums[0]
    for n in nums:
        if n < min_num:
            min_num = n
    
    return min_num

print(find_min(nums))

#output:
#2




# Task 3 :

#Count Even  Numbers 

nums = [3, 7, 2, 9, 4, 6]

def count_even_nums(nums):
    even_nums = 0
    for n in nums:
        if n % 2 == 0:
            even_nums += 1

    return even_nums

print(count_even_nums(nums))

#output:
#3