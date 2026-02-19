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

#output:
#False




# Problem 3 :

# Return the number that appears most times in the array.

def most_frequent(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    max_num = None
    max_count = 0

    for num in count:
        if count[num] > max_count:
            max_count = count[num]
            max_num = num

    return max_num


nums = [1,3,1,3,2,1]
print(most_frequent(nums))

#output:
#1     #because 2 appears 1 time
