# problem 1 :

# Two Sum (Sorted Array)

def two_sum_sorted_array(nums, target):
    left = 0
    right = len(nums) - 1
    current_sum = 0

    while left < right:     
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return left, right
        
        elif current_sum < target:
            left += 1

        else:
            right -= 1


    return current_sum

print(two_sum_sorted_array( [1, 2, 3, 4, 6],6))

#output:
#(1, 3)




# problem 2 :

# Remove Duplicates from Sorted Array

def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

nums = [1,2,2,2,3]
length = remove_duplicates(nums)
print(length)       # Output: 3
print(nums[:length]) # Output: first 3 unique elements

#output:
#3