# problem 1 :

# Given two strings s and t, return True if t is an anagram of s.

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


print(is_anagram("listen", "silent"))  #True
print(is_anagram("rat", "car"))         #False     
 
#output:
#True
#False




#problem 2 :

# Return a dictionary containing frequency of each element.


def frequency_count(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    return count


print(frequency_count([1,2,2,3,3,3]))

#output:
#{1: 1, 2: 2, 3: 3}




# problem 3 :

# First Non-Repeating Character

def first_non_repeating(s):
    count = {}

    # Step 1: Count frequency
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Step 2: Find first character with frequency 1
    for char in s:
        if count[char] == 1:
            return char

    return None


print(first_non_repeating("leetcode"))  # l
print(first_non_repeating("aabb"))      # None

#output:
#1
#None