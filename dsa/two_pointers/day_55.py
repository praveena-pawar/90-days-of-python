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