# problem 1 :

# Remove Duplicates

def remove_duplicates(nums):
    write = 0

    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1

            nums[write] = nums[read]

    return write + 1


nums = [1, 1, 2, 2, 3]
length = remove_duplicates(nums)
print(nums[:length])

#output:
#[1, 2, 3]





# problem 2 :

# Move all zeros to the end



