# problem 1 :

# Two Sum (Unsorted Array)

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i
        
print(two_sum([2, 7, 11, 15], 9))

#output:
#[0, 1]   #these are index values 




# problem 2 :

# Return True if the array contains duplicates.
# Return False if all numbers are unique.

def contains_duplicate(nums):
    seen = {}

    for num in nums:
        if num in seen:
            return True

        seen[num] = True

    return False

print(contains_duplicate([1,2,3,4]))