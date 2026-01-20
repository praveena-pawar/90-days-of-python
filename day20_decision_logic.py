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

def vowel_vs_consonant(text):
    counts = {"vowels": 0, "consonants": 0}

    for ch in text.lower():
        if ch == " ":
            continue
        if ch in "aeiou":
            counts["vowels"] += 1
        elif ch.isalpha():
            counts["consonants"] += 1

    if counts["vowels"] > counts["consonants"]:
        return "vowels"
    else:
        return "consonants"


print(vowel_vs_consonant("education"))
print(vowel_vs_consonant("python"))

#output:
#vowels
#consonsnts




# Task 3 :

# Write a function that:
# Takes a list of integers
# Groups them into a dictionary with keys:
# "even"
# "odd"
# Then decides which group has more elements
# Returns only the string:
# "even" or "odd

def even_or_odd(nums):
    groups = {"even": 0, "odd": 0}

    for n in nums:
        if n % 2 == 0:
            groups["even"] += 1
        else:
            groups["odd"] += 1

    if groups["even"] >= groups["odd"]:
        return "even"
    else:
        return "odd"

print(even_or_odd([2, 4, 6, 1, 3]))
print(even_or_odd([1, 3, 5, 2]))
