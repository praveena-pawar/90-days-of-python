# Task 1 :

# Given a list of numbers, find the second largest number.

def second_largest(nums):
    largest = nums[0]
    second_largest = float('-inf')

    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif n < largest and n > second_largest:
            second_largest = n

    return second_largest


print(second_largest([3, 7, 2, 9, 4]))

#output:
#7
