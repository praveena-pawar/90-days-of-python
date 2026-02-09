# marsk = [10, 20, 10, 5, 25]

# def smallest_number(nums):
#     smallest = marsk[0]
#     for m in marsk:
#         if m < smallest:
#             smallest = m

    
#     return smallest

# print(smallest_number(marsk))




# smallest = min(marsk)
# print("the smallest marsk is :", smallest)


# for m in marsk:
#     print(m)


# for i in range(100):
#     print(i)


# marks = [10, 20, 10, 5, 25]
# print(marks[-1])
# print(marks.index(min(marks)))


# smallest = marks[0]
# for m in range(len(marks)):
#     if marks[m] < smallest:
#         smallest = marks[m]

# print(smallest)



# def Average_of_Subarrays(nums, k):
#     result = []
#     window_sum = sum(nums[:k])
#     average = window_sum / k
#     result.append(average)

#     for i in range(k, len(nums)):
#         window_sum += nums[i]
#         window_sum -= nums[i - k]
#         result.append(window_sum / k)

#     return result

# print(Average_of_Subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2],5))



def longest_subarray(nums, k):
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(nums)):
       window_sum += nums[right]

       while window_sum > k:
           window_sum -= nums[left]
           left += 1

       max_len = max(max_len, right - left + 1)

    return max_len

print(longest_subarray( [2, 1, 5, 2, 3],7))

    
