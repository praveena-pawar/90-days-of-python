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

