# Task 1 :

# Given a list of numbers, find the largest even number.

def largest_even(nums):
    even_nums = None
    for n in nums:
        if n % 2 == 0:
            if even_nums is None or n > even_nums:
                even_nums = n
            

    return even_nums

print(largest_even([3, 7, 2, 9, 10, 4, 5]))

#output:
#10