# Task 1 :

# Given a list and a value k, find the largest number strictly less than k.

def largest_less_than_k(nums, k):
    best = None

    for n in nums:
        if n < k:
            if best is None or n > best:
                best = n

    return best


print(largest_less_than_k( [3, 7, 2, 9, 4, 10, 5], 8))
