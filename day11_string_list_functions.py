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