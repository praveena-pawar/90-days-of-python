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

#output : 
#4





# problem 2 :

# Count Subarrays Divisible by K

def count_subarrays_divisible_by_k(nums, k):
    remainder_count = {0: 1}   
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num

        remainder = prefix_sum % k

        remainder = (remainder + k) % k

        if remainder in remainder_count:
            count += remainder_count[remainder]
            
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count


nums = [4,5,0,-2,-3,1]
k = 5
print(count_subarrays_divisible_by_k(nums, k))
