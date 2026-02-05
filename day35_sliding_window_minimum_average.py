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
