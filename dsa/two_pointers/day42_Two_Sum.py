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

    write = 1 

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]: 
            nums[write] = nums[i]
            write += 1

    return write

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

#output:
#5
