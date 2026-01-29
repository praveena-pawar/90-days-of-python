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




# Task 2 :

# Given a list of numbers, find the smallest positive number.

def smallest_positive_number(nums):
    positive_number = None
    for n in nums:
        if n > 0:
            if positive_number is None or n < positive_number:
                positive_number = n
    
    return positive_number

print(smallest_positive_number( [3, -1, 7, 0, 2, -5, 4]))

#output:
#2



# Task 3 :

# Given a list of numbers, count how many elements are strictly greater than the average of the list.