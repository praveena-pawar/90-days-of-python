# Example (read only)
text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)




# Task 1 :

# Write a function that:
# Takes a string
# Counts how many times each character appears
# Returns a dictionary

word = "hello world"

def count_characters_appears(word):
    characters = {}
    for ch in word:
        if ch == " ":
            continue
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1
    return characters

result = count_characters_appears(word)
print(result)





# Task 2 : Word Frequency Counter

# Write a function that:
# Takes a sentence (string)
# Counts how many times each word appears
# Returns a dictionary
# Ignore case (Python == python)
# Ignore extra spaces