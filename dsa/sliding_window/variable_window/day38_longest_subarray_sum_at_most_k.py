# problem 1 :

# Longest subarray with sum ≤ k

def longest_subarray(nums, k):
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_subarray([2, 1, 5, 2, 3],7))

#output:
#2




# problem 2 :

# Smallest subarray with sum ≥ k

def smallest_subarray(nums, k):
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= k: 
          min_len = min(min_len, right - left + 1)
          window_sum -= nums[left]
          left += 1

    if min_len == float('inf'):
       return 0
    return min_len

print(smallest_subarray([2, 3, 1, 2, 4, 3], 7))