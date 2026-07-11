# 1: Find the Largest Element
def largest_element(nums):
    large_num = float('-inf')

    for num in nums:
        if num > large_num:
            large_num = num

    return large_num

nums = [5, 2, 9, 1, 7]
print(largest_element(nums))



# 2: Find the Second Largest Distinct Element
def second_largest_element(nums):
    large_num = float('-inf')
    second_large_element = float('-inf')

    for num in nums:
        if num > large_num:
            second_large_element = large_num
            large_num = num

        elif num > second_large_element and num != large_num:
            second_large_element = num

    if second_large_element == float('-inf'):
        return -1

    return second_large_element

nums = [12, 35, 1, 10, 34, 1]
print(second_largest_element(nums))



# 3: Check if an Array is Sorted
def array_sorted_or_not(nums):
    for i in range(len(nums) -1):
        if nums[i] > nums[i + 1]:
            return False
        
    return True

nums = [1, 2, 2, 4, 5]
print(array_sorted_or_not(nums))



# 4: Reverse an Array (In-Place)
def reverse_an_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

    return nums

nums = [1, 2, 3, 4, 5]
print(reverse_an_array(nums))



# 5: Move All Zeros to the End