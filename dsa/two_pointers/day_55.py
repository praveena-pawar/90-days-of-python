# 1: Reverse String (LeetCode 344)
def revesre_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s

s = ["h", "e", "l", "l", "o"]

print(revesre_string(s))



# 2: Valid Palindrome (LeetCode 125)
def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1


    return True

s = "madam"
print(valid_palindrome(s))




# 3: Two Sum II – Input Array Is Sorted (LeetCode 167)
def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return left, right 
        
        elif current_sum > target:
            right -= 1

        else:
            left += 1  
        
    return None


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))