# Task 1:

# Write a function that:
# Takes a string
# Creates a character frequency dictionary
# Returns a list of characters that appear more than once
# Ignore spaces

text = "programming"

def repeated_characters(text):
    freq = {}

    for ch in text:
        if ch == " ":
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    result = []
    for ch in freq:
        if freq[ch] > 1:
            result.append(ch)

    return result

print(repeated_characters(text))