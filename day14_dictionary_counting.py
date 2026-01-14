# Example (read only)
text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)




# Task 1 :

# Write a function that:
# Takes a string
# Counts how many times each character appears
# Returns a dictionary