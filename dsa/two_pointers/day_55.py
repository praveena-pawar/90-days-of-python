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
