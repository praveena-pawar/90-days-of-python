# Task 1 :

# You are given a list of numbers.
# Write a function that:
# Creates a new list
# Stores squares of only positive numbers
# Ignores zero and negative numbers
# Returns the new list

nums = [2, -3, 4, 0, -1, 5, 6]

def squares_of_positive_num(nums):
    positive_num = []
    for n in nums:
        if n < 0:
            continue
        elif n == 0:
            continue
        else:
            positive_num.append(n * n) 
            

    return positive_num

result = squares_of_positive_num(nums)
print(result)

#output:
# [4, 16, 25, 36]





# Task 2 : 

# You are given a list of numbers.
# Write a function that:
# Creates a new list
# Stores only numbers that are divisible by both 3 and 5
# Returns the new list

nums = [15, 9, 10, 30, 22, 45, 60]

def divisible_by_both_3_5(nums):
    numbers = []
    for n in nums:
        if (n % 3 == 0) and (n % 5 == 0):
            numbers.append(n)
    
    return numbers

result = divisible_by_both_3_5(nums)
print("Numbers that are divisible by both 3 and 5 :", result)

#output:
#Numbers that are divisible by both 3 and 5 : [15, 30, 45, 60]





# Task 3 :

# You are given a list of strings.
# Write a function that:
# Creates a new list
# Stores only the words that start with a vowel
# Ignores case (A/a, E/e, etc.)
# Returns the new list

words = ["Apple", "banana", "Orange", "grape", "umbrella", "Ink"]

def words_starts_with_vowel(words):
    vowel_words = []
    for ch in words:
            if ch[0].lower() in "aeiou":
                vowel_words.append(ch)
              
    return vowel_words

result = words_starts_with_vowel(words)
print(result)
