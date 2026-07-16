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