# How to Think About Strings (IMPORTANT)

# A string is:
# an array of characters
# immutable (cannot change directly)


# Task 1 :

#s = "datascience"
# Count how many times each character appears in a string.

s = "datascience"

def chr_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    return freq

print(chr_frequency(s))