# 1: Find the Missing Number
def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


nums = [3, 0, 1]
print(missing_number(nums))



# 2: Find the Majority Element