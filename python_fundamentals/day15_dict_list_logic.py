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

#output:
#['r', 'g', 'm']




# Task 2:

# You are given a list of numbers.
# Write a function that:
# Counts how many times each number appears
# Returns a dictionary
# Then returns a list of numbers that appear exactly once

numbers = [1, 2, 2, 3, 4, 4, 5]

def numbers_appears(numbers):
    number_count = {}
    for n in numbers:
        if n in number_count:
            number_count[n] += 1
        else:
            number_count[n] = 1

    result = []
    for n in number_count:
        if number_count[n] == 1:
            result.append(n)

    return result

print(numbers_appears(numbers))

#output:
#[1, 3, 5]




# Task 3:

# Write a function that:
# Finds the first non-repeating character
# Returns that character
# If all characters repeat, return "None"
# Ignore spaces

text = "swiss"

def first_non_repeating_char(text):
    freq = {}

    # Step 1: Build frequency dictionary (ignore spaces)
    for ch in text:
        if ch == " ":
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 2: Find first character with frequency 1
    for ch in text:
        if ch == " ":
            continue
        if freq[ch] == 1:
            return ch

    return "None"


result = first_non_repeating_char(text)
print(result)

#output:
#w
