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



# problem 3 :

# Move all zeros to the end of the array, while keeping the order of non-zero elements.

def move_all_zero_to_end_of_array(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    while slow < len(nums):
        nums[slow] = 0
        slow += 1

    return nums

nums = [0, 1, 0, 3, 12]
print(move_all_zero_to_end_of_array(nums))

#output:
#[1, 3, 12, 0, 0]