# Concept : Function that RETURNS a LIST
# Until now, you returned numbers/strings.
# Today: return a list.

# Example idea (not code):

# Input list → [5, 12, 7, 20]

# Output list → [12, 20] (numbers > 10)


# Task: 1

# Write a function that:
# Takes a list of numbers
# Returns a new list of only EVEN numbers
nums = [1, 4, 7, 10, 3]

def get_even_numbers(nums):
    even_num = []
    for n in nums:
        if n % 2 == 0:
            even_num.append(n)

    return even_num

result = get_even_numbers(nums)
print(result)

#output:
#[4, 10]




# Task 2 : Filter Words by Length
# Write a function that:
# Takes a list of words (strings)
# Returns a new list containing only the words whose length is greater than 4

words = ["hi", "python", "code", "learning", "AI"]

def length_is_greater_than4(words):
    long_word = []
    for ch in words:
        if len(ch) > 4:
            long_word.append(ch)

    return long_word

result = length_is_greater_than4(words)
print(result)

#output:
#['python', 'learning']











# nums = [1, 4, 7, 10, 3]
# even = []

# for n in nums:
#     if n % 2 == 0:
#         even.append(n)
# print(even)