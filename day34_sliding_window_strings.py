# Task 1 :

# Find length of the longest substring with no duplicate characters.

def longest_unique(s):
    left = 0
    seen = set()
    max_len = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


print(longest_unique("abcabcbb"))
