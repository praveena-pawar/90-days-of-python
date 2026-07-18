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