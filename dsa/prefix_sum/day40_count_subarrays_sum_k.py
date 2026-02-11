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

