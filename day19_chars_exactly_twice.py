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




# Task 2 :

# Write a function that:
# Takes a list of integers
# Counts how many times each number appears
# Returns the number that appears the most
# If there is a tie, return any one

nums = [1, 2, 2, 3, 3, 3, 4]

def most_frequent_number(nums):
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    max_count = 0
    max_num = None

    for n in freq:
        if freq[n] > max_count:
            max_count = freq[n]
            max_num = n

    return max_num

print(most_frequent_number(nums))

#output:
#3




# Task 3 :

# Write a function that:
# Takes a string
# Counts frequency of each word (ignore case)
# Returns a list of words that appear only once
# Ignore extra spaces