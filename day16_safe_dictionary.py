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





# Task 2 :

# Write a function that:
# Takes a string
# Counts vowels and consonants using a dictionary
# Ignores spaces
# Ignores case (A = a)
# Returns the dictionary in this format:

word = "Hello World"

def vowels_consonants_using_dictionary(word):
    frq = {"vowels": 0, "consonants": 0}
    for ch in word.lower():
        if ch == " ":
            continue
        if ch in "aeiou":
            frq["vowels"] = frq.get("vowels", 0) + 1
        else:
            frq["consonants"] = frq.get("consonants", 1) + 1

    return frq

print(vowels_consonants_using_dictionary(word))






# Task 3 :

# Takes a string
# Counts frequency of each character (ignore spaces)
# Uses dict.get()
# Finds the character with the maximum frequency
# Returns that character
# If there is a tie, return any one of them