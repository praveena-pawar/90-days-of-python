# Think:

# [1 2 3] 4 5 6
#   [2 3 4]
#     [3 4 5]
#       [4 5 6]

# We remove left element
# We add right element




# Task 1 :

# Find maximum sum of any subarray of size k.
# nums = [2, 1, 5, 1, 3, 2]
# k = 3

def max_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]        # add new element
        window_sum -= nums[i - k]    # remove old element
        max_sum = max(max_sum, window_sum)

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
print(max_sum(nums, 3))

#output:
#9
#(window = [5,1,3])





# Task 2 :

# Find the average of every subarray of size k
# nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5

def average(nums, k):
    result = []
    window_sum = sum(nums[:k])
    result.append(window_sum / k)
    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        result.append(window_sum / k)

    return result


print(average([1, 3, 2, 6, -1, 4, 1, 8, 2],5))

#output:
#[2.2, 2.8, 2.4, 3.6, 2.8]





# Task 3 :

# Find the length of the longest subarray

def longest_subarray(nums, target):
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > target:
            window_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_subarray([4, 2, 1, 7, 3, 2], 8))

#output:
#3


















