# 1: Remove Element (LeetCode 27)
def remove_element(nums, val):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow


nums = [3, 2, 2, 3]
val = 3

k = remove_element(nums, val)

print(k)          
print(nums[:k])  