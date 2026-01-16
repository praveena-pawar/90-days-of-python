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

#output:
#{'a': 1, 'p': 2, 'l': 1, 'e': 1}





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

#output:
#{'vowels': 3, 'consonants': 7}






# Task 3 :

# Takes a string
# Counts frequency of each character (ignore spaces)
# Uses dict.get()
# Finds the character with the maximum frequency
# Returns that character
# If there is a tie, return any one of them

text = "banana"

def max_frequency_char(text):
    freq = {}

    for ch in text:
        if ch == " ":
            continue
        freq[ch] = freq.get(ch, 0) + 1

    max_count = 0
    max_char = ""

    for ch in freq:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch

    return max_char

print(max_frequency_char(text))

#output:
