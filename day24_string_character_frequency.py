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

#output:
#{'d': 1, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}




# Task 2 :

# Count how many vowels and consonants are in a string.

def count_vowels_consonants(word):
    freq_count = {"vowels": 0, "consonants": 0}

    for ch in word.lower():
        if ch.isalpha():
            if ch in "aeiou":
                freq_count["vowels"] += 1
            else:
                freq_count["consonants"] += 1

    return freq_count

print(count_vowels_consonants("datascience"))

#output:
#{'vowels': 5, 'consonants': 6}