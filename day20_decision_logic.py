# Task 1 :

# Write a function that:
# Takes a list of integers
# Counts how many are:
# positive
# negative
# zero
# Returns which category has the maximum count as a string:
# "positive", "negative", or "zero"

nums = [1, -2, 0, 3, 0, -1, 0]

def max_category(nums):
    counts = {"positive": 0, "negative": 0, "zero": 0}

    for n in nums:
        if n > 0:
            counts["positive"] += 1
        elif n < 0:
            counts["negative"] += 1
        else:
            counts["zero"] += 1

    max_count = 0
    max_category = ""

    for category in counts:
        if counts[category] > max_count:
            max_count = counts[category]
            max_category = category

    return max_category


print(max_category(nums))

#output:
#Zero





# Task 2 :

# Write a function that:
# Takes a string
# Counts how many vowels and consonants it has
# Returns which one is greater as a string:
# "vowels"
# "consonants"
# Ignore spaces
# Ignore case