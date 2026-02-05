# Task 1 :

# Minimum Average Subarray (Fixed Sliding Window)
# nums = [3, 7, 5, 20, -10, 0, 12]
# k = 2

def minimum_average_of_subbarray(nums, k):
    window_sum = sum(nums[:k])
    minimum_average = window_sum / k

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]

        current_avarge = window_sum / k
        if current_avarge < minimum_average:
            minimum_average = current_avarge

    return minimum_average

print(minimum_average_of_subbarray( [3, 7, 5, 20, -10, 0, 12], 2))

#output:
# -5.0





# Task 2 :

# Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is ≤ k.
# nums = [2, 1, 1, 1, 3]
# k = 3

def longest_subarray(nums, k):
    left = 0                 # left end of the window
    window_sum = 0           # sum of current window
    max_length = 0           # best answer so far

    for right in range(len(nums)):     # move right end of window
        window_sum += nums[right]      # add new element

        while window_sum > k:          # if condition breaks
            window_sum -= nums[left]   # remove left element
            left += 1                  

        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_subarray([2, 1, 1, 1, 3], 3))

        



