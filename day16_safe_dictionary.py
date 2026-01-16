# Task 1 :

# Write a function that:
# Takes a string
# Counts character frequency
# Uses dict.get()
# Ignores spaces
# Returns the dictionary

word = "apple"

def character_frequency(word):
    freq = {}

    for ch in word:
        if ch != " ":                 
            freq[ch] = freq.get(ch, 0) + 1

    return freq

print(character_frequency("apple"))
