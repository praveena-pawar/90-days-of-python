# Problem :

# Write a function that:
# Takes a list of numbers
# Returns how many numbers are greater than 10

nums = [5, 12, 3, 18, 7, 25]

def count_greater_than_10(nums):
    count = 0
    for num in nums:
        if num > 10:
            count += 1
    return count

print(count_greater_than_10(nums))