# Task 1 :

# Find the length of the longest subarray with sum ≤ k

def longest_subarray_witgh_sum(nums, k):
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_subarray_witgh_sum([2, 1, 1, 3, 2, 1],4))

#output:
#3




# Task 2 :

# Find the length of the longest subarray with at most k distinct numbers

def longest_subarray_at_most_k_distinct(nums, k):
    left = 0
    freq = {}
    max_length = 0

    for right in range(len(nums)):
        # add right element
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        # shrink window if distinct count > k
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        # update answer
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_subarray_at_most_k_distinct([1, 2, 1, 2, 3], 2))

#output:
#4




