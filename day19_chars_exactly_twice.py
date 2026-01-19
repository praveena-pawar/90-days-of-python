# Task 1 :

# Write a function that:
# Takes a string
# Counts frequency of each character (ignore spaces)
# Returns a list of characters that appear exactly twice

text = "success"

def characters_appear_twice(text):
    freq = {}

    for ch in text:
        if ch == " ":
            continue
        freq[ch] = freq.get(ch, 0) + 1

    result = []
    for ch in freq:
        if freq[ch] == 2:
            result.append(ch)

    return result

print(characters_appear_twice(text))

#output:
#['c']