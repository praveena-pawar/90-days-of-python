# problem 1 :

# Longest subarray with at most k zeros

def longest_suabarray_at_most_k_zeros(nums, k):
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_suabarray_at_most_k_zeros( [1, 1, 0, 0, 1, 1, 0, 1], 2))

#ouptut:
#6




# problem 2 :

# Longest substring with at most k distinct characters


def longest_substring_at_most_k_distinct(s, k):
    left = 0
    freq = {}
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


print(longest_substring_at_most_k_distinct("eceba", 2))





# probelm 3 : 

# Find the smallest subarray with sum ≥ target.

arr = [2, 3, 1, 2, 4, 3]
target = 7

def smallest_subarray(arr, target):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_len

print(smallest_subarray(arr, target))

