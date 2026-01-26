# Problem: Count Zeros in a List

nums = [1, 0, 2, 0, 3, 0, 4]

def count_zeros(nums):
    zeros = 0
    for n in nums:
        if n == 0:
            zeros += 1

    return zeros

print(count_zeros(nums))

#output:
#3