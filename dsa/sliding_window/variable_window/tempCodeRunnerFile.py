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