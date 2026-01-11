# Topic: Functions with LIST + STRING + LOGIC (Mixed Problems)
# By the end of today, you’ll be comfortable with:
# 1️ Processing lists of strings
# 2️ Using functions that return counts & lists
# 3️ Writing clean, interview-style logic


# Task : 1

# Write a function that:
# Takes a list of words
# Counts how many words have length greater than 5
# Returns the count

words = ["python", "code", "learning", "AI", "programming"]

def count_words_longer_than_5(words):      
        large_count = 0
        for ch in words:
                if len(ch) > 5:
                        large_count += 1
        
        return large_count

result = count_words_longer_than_5(words)
print(result)





# Task 2 : Count Vowels in Each Word

# Write a function that:
# Takes a list of words
# Counts the total number of vowels across all words
# Returns the count

words = ["python", "is", "awesome"]

def count_total_number_of_vowels(words):
        total_vowels = 0
        for word in words:
                 for ch in word:
                          if ch.lower() in "aeiou":
                                  total_vowels += 1
                             
        return total_vowels

result = count_total_number_of_vowels(words)
print("The total number of vowels across all words :", result)





# Task 3 :

# Return the word that has the maximum number of vowels

words = ["python", "education", "AI", "awesome"]

def maximum_number_of_vowels(words):
    max_count = 0
    max_word = ""

    for word in words:
        count_vowels = 0  

        for ch in word:
            if ch.lower() in "aeiou":
                count_vowels += 1

        if count_vowels > max_count:
            max_count = count_vowels
            max_word = word

    return max_word

result = maximum_number_of_vowels(words)
print(result)
