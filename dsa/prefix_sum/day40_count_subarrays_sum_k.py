# problem 1 :

# Count subarrays with sum = k

def count_subarrays_with_sum_k(nums, k):
    prefix_sum_count = {0: 1}  # How many times a prefix sum has appeared
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num  # running sum up to current index

        # If (current_sum - k) exists, it means a subarray sums to k
        if (current_sum - k) in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]

        # Update the frequency of current_sum in the map
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1

    return count


# Example usage:
nums = [1, -1, 2, 3, -2, 2]
k = 3
print(count_subarrays_with_sum_k(nums, k))





# problem 2 : 

# Find length of longest subarray with sum = 3.

arr = [1, -1, 5, -2, 3]
k = 3


def longest_subarray(nums, k):
    current_sum = 0
    max_length = 0
    prefix_map = {}

    for i in range(len(nums)):
        current_sum += nums[i]

        # Case 1: if current_sum itself equals k
        if current_sum == k:
            max_length = i + 1

        # Case 2: check if (current_sum - k) was seen before
        needed = current_sum - k
        if needed in prefix_map:
            length = i - prefix_map[needed]
            max_length = max(max_length, length)

        # Store prefix sum (only first occurrence)
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_length

print(longest_subarray( [1, -1, 5, -2, 3], 3))

#output:
#4





# problem 3 : 

# Longest subarray with sum = 0

def find_max_length(nums):
    current_sum = 0
    max_length = 0
    prefix_map = {}

    for i in range(len(nums)):
        
        # Convert 0 to -1
        if nums[i] == 0:
            current_sum += -1
        else:
            current_sum += 1

        # If sum becomes 0
        if current_sum == 0:
            max_length = i + 1

        # If sum seen before
        if current_sum in prefix_map:
            length = i - prefix_map[current_sum]
            max_length = max(max_length, length)
        else:
            # Store first occurrence
            prefix_map[current_sum] = i

    return max_length

print(find_max_length([0,1,0,1,1,0]))