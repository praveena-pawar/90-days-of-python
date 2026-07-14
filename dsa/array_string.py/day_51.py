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
def move_all_zeros_to_end(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
           nums[write], nums[read] = nums[read], nums[write]
           write += 1
            
    return nums

nums = [0, 1, 0, 3, 12]
print(move_all_zeros_to_end(nums))



# 6: Remove Duplicates from a Sorted Array
def remove_duplicate_array(nums):
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k = remove_duplicate_array(nums)

print("k =", k)
print("Modified array:", nums)
print("Unique elements:", nums[:k])



# 7: Rotate Array by One Position (Right Rotation)

