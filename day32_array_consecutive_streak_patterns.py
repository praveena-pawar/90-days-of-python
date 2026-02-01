# Task 1 :

# Find the length of the longest consecutive increasing streak.

def longest_increasing_streak(nums):
    current = 1
    max_streak = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current += 1
        else:
            current = 1

        if current > max_streak:
            max_streak = current

    return max_streak


print(longest_increasing_streak([1, 3, 2, 4, 6, 5, 7]))

#output:
#3





# Task 2 :

# Find the longest streak where numbers do not go down