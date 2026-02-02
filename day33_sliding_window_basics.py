# Think:

# [1 2 3] 4 5 6
#   [2 3 4]
#     [3 4 5]
#       [4 5 6]

# We remove left element
# We add right element




# Task 1 :

# Find maximum sum of any subarray of size k.
# nums = [2, 1, 5, 1, 3, 2]
# k = 3

def max_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]        # add new element
        window_sum -= nums[i - k]    # remove old element
        max_sum = max(max_sum, window_sum)

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
print(max_sum(nums, 3))

#output:
#9
#(window = [5,1,3])





# Task 2 :

# Find the average of every subarray of size k
# nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5

def average(nums, k):
    result = []
    window_sum = sum(nums[:k])
    result.append(window_sum / k)
    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        result.append(window_sum / k)

    return result


print(average([1, 3, 2, 6, -1, 4, 1, 8, 2],5))
















# nums = [2, 1, 5, 1, 3]
# k = 3

# def sum_of_three(nums, k):
#     best_answer = sum(nums[:k])
#     for i in range(k, len(nums)):
#         return best_answer

#     return None

# print(sum_of_three(nums, 3))


# best_answer = sum(nums[:k])
# for i in range(k, len(nums)):
#     best_answer += nums[i]       
#     best_answer -= nums[i - k] 
#     print(best_answer%3) 