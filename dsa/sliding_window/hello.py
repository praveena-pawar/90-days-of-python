# def two_pointer_sum(nums, target):
#     left = 0
#     right = len(nums) - 1
#     current_sum = 0

#     while left < right:
#         current_sum = nums[left] + nums[right]

#         if current_sum == target:
#             return left, right
        
#         elif current_sum < target:
#             left += 1

#         else:
#             right -= 1

#     return None

# print(two_pointer_sum([1, 2, 3, 4, 6],6))











# def two_sum_sorted(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]

#         if current_sum == target:
#             return left, right
        
#         elif current_sum < target:
#             left += 1

#         else:
#             right -= 1

#     return current_sum

# print(two_sum_sorted([1, 3, 4, 7, 10, 14], 11))





# nums = [1, 1, 2, 2, 3]

# def remove_duplicates(nums):
#     write = 0

#     for read in range(1, len(nums)):
#         if nums[read] != nums[write]:
#             write += 1
#             nums[write] = nums[read]

#     return write + 1


# nums = [1, 1, 2, 2, 3]
# length = remove_duplicates(nums)
# print(nums[:length])







# # — Valid Palindrome

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if not s[left].isalnum():
#           left += 1
#           continue
        
#         if not s[right].isalnum():
#           right -= 1
#           continue


#         if s[left].lower() != s[right].lower():
#             return False
#         left += 1
#         right -= 1

#     return True

# print(is_palindrome("A man, a plan, a canal: Panama"))





# nums = [2, 7, 11, 15]
# target = 9

# def two_sum(nums, target):
#     seen = {}

#     for i in range(len(nums)):
#         num = nums[i]
#         needed = target - num

#         if needed in seen:
#             return [seen[needed], i]

#         seen[num] = i
# print(two_sum([2, 7, 11, 15], 9))




# # nums = [1,2,3,1]
# # nums = [1,2,3,4]

# def contains_duplicate(nums):
#     seen = {}

#     for num in nums:
#         if num in seen:
#             return True

#         seen[num] = True

#     return False


# print(contains_duplicate([1,2,3,4]))



# nums = [1,3,1,3,2,1]
# def most_frequent(nums):
#     count = {}

#     for num in nums:
#         count[num] = count.get(num, 0) + 1

#     max_num = None
#     max_count = 0

#     for num in count:
#         if count[num] > max_count:
#             max_count = count[num]
#             max_num = num

#     return max_num


# nums = [1,3,1,3,2,1]
# print(most_frequent(nums))






# nums = [1,2,3,1]

# def conatins_duplicates(nums):
#     seen = {}

#     for i in range(len(nums)):
#         if i in seen:
#             return False
        
#         seen[i] = True
        
#     return False 

# print(conatins_duplicates(nums))

# arr = [10, 20 ,40]
# for i in range(len(arr)):
#     print(arr[i])






# nums = [5, 7, 9]

# for i, num in enumerate(nums):
#     if num == 7:
#         print(i)


# nums = [1,2,1,3,2,1]

# count = {}

# for num in nums:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1

# print(count)



# arr = [1, 2, 3, 4, 5]

# left = 0
# right = len(arr) - 1

# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1

# print(arr)


# arr = [4, 2, 9, 1, 7]
# max_value = arr[0]
# min_value = arr[0]  

# for n in range(1, len(arr)):
#     if arr[n] > max_value:
#         max_value = arr[n]
#     if arr[n] < min_value:
#         min_value = arr[n]

# print(max_value)
# print(min_value)



# def frequency_count(nums):
#     count = {}  

#     for num in nums:
#         count[num] = count.get(num, 0) + 1

#     for num in nums:
#         if count[num] == 1:
#             return num

#     return None

# nums = [1, 2, 3, 2, 1]
# print(frequency_count(nums))



# arr = [0, 1, 0, 3, 12]
# new = []

# for i in range(len(arr)):
#     if arr[i] != 0:
#         new.append(arr[i])

# print(new)


# arr = [0, 1, 0, 3, 12]
# right = 0

# for left in range(len(arr)):
#     if arr[left] == 0:
#         arr[right], arr[left] = arr[left], arr[right]

#         right += 1

# print(arr)



# arr = [2, 7, 11, 15]
# target = 9

# def two_sum(arr, target):
#     left = 0
#     right = len(arr) - 1
#     current_sum = 0

#     while left < right:
#         current_sum = arr[left] + arr[right]

#         if current_sum == target:
#             return left, right
        
#         elif current_sum < target:
#             left += 1

#         else:
#             right -= 1

#     return current_sum

# print(two_sum(arr, target))

    
    

# arr = [2, 7, 11, 15]
# target = 9

# def two_sum(arr, target):
#     seen = {}
#     num = 0
#     needed = 0

#     for i in range(len(arr)):
#         num = arr[i]
#         needed = target - num

#         if needed in seen:
#             return[seen[needed], i]
        
#         seen[num] = i

# print(two_sum(arr, target))



# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# def maximum_sum(arr, k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(k, len(arr)):
#         window_sum += arr[i]
#         window_sum -= arr[i - k]

#         max_sum = max(max_sum, window_sum)

#     return max_sum

# print(maximum_sum(arr, k))



arr = [2, 3, 1, 2, 4, 3]
target = 7

def smallest_subarray(arr, target):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_len

print(smallest_subarray(arr, target))








