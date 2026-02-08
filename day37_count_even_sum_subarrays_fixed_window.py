# problem 1 :

# Count subarrays of size k whose sum is even

def even_sum(nums, k):
    window_sum = sum(nums[:k])
    even_sum = 0

    if window_sum % 2 == 0:
        even_sum += 1

    for i in range(k, len(nums)):
        window_sum += nums[i]      
        window_sum -= nums[i - k] 

        if window_sum % 2 == 0:
            even_sum += 1
            
    return even_sum

print(even_sum([2, 1, 5, 1, 3, 2], 3))

#output:
#2




# problem 2 :

# Maximum sum of subarray of size k

def max_sum_of_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

print(max_sum_of_subarray( [4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))

#output:
#16




# problem 3 :

# Minimum sum of subarray of size k

def min_sum_of_subarray(nums, k):
    window_sum = sum(nums[:k])
    min_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        min_sum = min(window_sum, min_sum)
    
    return min_sum

print(min_sum_of_subarray([3, 7, 90, 20, 10, 50, 40], 3))

#output: