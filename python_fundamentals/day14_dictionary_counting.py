# Example (read only)
text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)

#output;
#{'b': 1, 'a': 3, 'n': 2}




# Task 1 :

# Write a function that:
# Takes a string
# Counts how many times each character appears
# Returns a dictionary

word = "hello world"

def count_characters_appears(word):
    characters = {}
    for ch in word:
        if ch == " ":
            continue
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1
    return characters

result = count_characters_appears(word)
print(result)

#output:
#{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}





# Task 2 : Word Frequency Counter

# Write a function that:
# Takes a sentence (string)
# Counts how many times each word appears
# Returns a dictionary
# Ignore case (Python == python)
# Ignore extra spaces

sentence = "Python is easy and Python is powerful"

def count_word_appears(sentence):
    word_count = {}
    words = sentence.lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

result = count_word_appears(sentence)
print(result)

#output:
# {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}





# Task 3 : 

# Write a function that:
# Takes a sentence (string)
# Finds the word that appears the most times
# Ignores case
# Returns only the word (not the count)

sentence = "AI is the future and AI is powerful"

def most_frequent_word(sentence):
    word_count = {}
    words = sentence.lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_count = 0
    max_word = ""

    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word

    return max_word

result = most_frequent_word(sentence)
print(result)

#output:
#ai