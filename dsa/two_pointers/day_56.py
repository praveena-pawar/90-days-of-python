# 4: Remove Duplicates from Sorted Array (LeetCode 26)
def remove_duplicates(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]


    return slow + 1

nums = [1, 1, 2]
print(remove_duplicates(nums))




# 5: Move Zeroes (LeetCode 283)