# 1: Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""

    for i in range(len(strs[0])):

        for word in strs[1:]:

            if i >= len(word) or word[i] != strs[0][i]:
                return prefix

        prefix += strs[0][i]

    return prefix


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))



# 2: Valid Palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))



# 3: Find the Length of the Last Word
def length_of_last_word(s):
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == " ":
        i -= 1

    length = 0

    # Count the last word
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


s = "   fly me   to   the moon  "
print(length_of_last_word(s))