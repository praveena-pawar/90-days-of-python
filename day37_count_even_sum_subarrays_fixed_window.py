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


