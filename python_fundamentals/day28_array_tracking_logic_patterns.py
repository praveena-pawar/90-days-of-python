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




# Task 2 :

# Given a list of numbers, find the second smallest number.

def second_smallest(nums):
    smallest = nums[0]
    second_smallest = float('inf')

    for n in nums:
        if n < smallest:
            second_smallest = smallest
            smallest = n
        elif n > smallest and n < second_smallest:
            second_smallest = n

    return second_smallest

print(second_smallest([3, 7, 2, 9, 4]))

#output:
#3