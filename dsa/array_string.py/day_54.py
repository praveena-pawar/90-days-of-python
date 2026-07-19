# 1: Is Subsequence
def is_subsequence(s, t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)


s = "abc"
t = "ahbgdc"

print(is_subsequence(s, t))



# 2: Find the First Unique Character in a String
def first_unique_char(s):
    freq = {}

    # Count frequency
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Find first unique character
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


s = "loveleetcode"
print(first_unique_char(s))