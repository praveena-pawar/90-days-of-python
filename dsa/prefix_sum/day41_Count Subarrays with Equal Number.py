# problem 1 :

# Count Subarrays with Equal Number of 0s and 1s

def count_subarray_with_equal_number(nums):
    prefix_sum_count = {0: 1}  
    current_sum = 0
    count = 0

    for num in nums:
        if num == 0:
            num -= 1 

        current_sum += num


        if current_sum  in prefix_sum_count:
            count += prefix_sum_count[current_sum]

        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1

    return count

print(count_subarray_with_equal_number([0,1,0,1]))