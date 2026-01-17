# Task 1 :

# Write a function that:
# Takes a list of numbers
# Groups them into a dictionary:

nums = [1, 2, 3, 4, 5]

def group_even_odd(nums):
    result = {"even": [], "odd": []}

    for num in nums:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)

    return result

print(group_even_odd(nums))

#output:
#{'even': [2, 4], 'odd': [1, 3, 5]}




# Task 2 :

# Write a function that:
# Groups words into a dictionary based on word length
# The key should be the length of the word
# The value should be a list of words with that length
# Return the dictionary

words = ["hi", "hello", "bye", "python", "code"]

def group_words_by_length(words):
    result = {}

    for word in words:
        length = len(word)
        result[length] = result.get(length, []) + [word]

    return result

print(group_words_by_length(words))