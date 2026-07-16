# 1: Find the Missing Number
def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


nums = [3, 0, 1]
print(missing_number(nums))



# 2: Find the Majority Element
def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))



# 3: Find All Leaders in an Array
def find_leaders(nums):
    leaders = []
    max_right = float("-inf")

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > max_right:
            leaders.append(nums[i])
            max_right = nums[i]

    leaders.reverse()
    return leaders


nums = [7, 4, 5, 7, 3]
print(find_leaders(nums))



# 4: Find the Frequency of Each Element
def frequency(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1

        else:
            freq[num] = 1

    return freq

nums = [1, 2, 2, 3, 1, 1]
print(frequency(nums))



# 5: Check if Two Strings are Anagrams