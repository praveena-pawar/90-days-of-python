# 1: Container With Most Water (LeetCode 11)
def max_area(height):
    left = 0
    right = len(height) - 1

    max_water = 0

    while left < right:

        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height

        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water 


height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))



# 2: 3Sum (LeetCode 15)
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

            
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))