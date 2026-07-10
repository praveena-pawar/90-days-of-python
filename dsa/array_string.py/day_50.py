# 1: Two Sum
def two_sum(nums, target):
    seen = {}
    num = 0
    needed = 0

    for i in range(len(nums)):
        num = nums[i]
        needed = target - num

        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))



# 2: Best Time to Buy and Sell Stock