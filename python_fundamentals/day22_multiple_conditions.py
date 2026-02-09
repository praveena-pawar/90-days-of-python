# Task 1 :

# Write a function that:
# Takes a list of integers
# Counts:
# numbers greater than 0 and even
# numbers less than 0 and odd
# Returns the counts as a dictionary

nums = [2, -3, 4, -5, 0, 7, -8]

def count_numbers(nums):
    result = {"positive_even": 0,"negative_odd": 0}

    for n in nums:
        if n > 0 and n % 2 == 0:
            result["positive_even"] += 1
        elif n < 0 and n % 2 != 0:
            result["negative_odd"] += 1

    return result

print(count_numbers(nums))

#output:
#{'positive_even': 2, 'negative_odd': 2}





# Task 2 :

# Write a function that:
# Takes a string
# Counts how many characters are:
# vowels
# consonants
# digits
# Ignore spaces
# Return the result as a dictionary 

text = "Python3 is fun2"

def count_characters(text):
    result = {"vowels": 0,"consonants": 0,"digits": 0 }

    vowels = "aeiouAEIOU"

    for ch in text:
        if ch == " ":
            continue
        elif ch.isdigit():
            result["digits"] += 1
        elif ch.isalpha():
            if ch in vowels:
                result["vowels"] += 1
            else:
                result["consonants"] += 1

    return result

print(count_characters(text))

#output:
#{'vowels': 3, 'consonants': 8, 'digits': 2}






# Task 3 :

# Write a function that:
# Takes a list of integers
# Counts how many numbers are:
# positive even
# positive odd
# negative even
# negative odd
# Ignore 0
# Return the result as a dictionary

nums = [2, -3, 4, -6, 7, -5, 0, 8]

def count_numbers(nums):
    result = {
        "positive_even": 0,
        "positive_odd": 0,
        "negative_even": 0,
        "negative_odd": 0
    }

    for n in nums:
        if n == 0:
            continue
        elif n > 0:
            if n % 2 == 0:
                result["positive_even"] += 1
            else:
                result["positive_odd"] += 1
        else:  
            if n % 2 == 0:
                result["negative_even"] += 1
            else:
                result["negative_odd"] += 1

    return result

print(count_numbers(nums))

#output:
#{'positive_even': 3, 'positive_odd': 1, 'negative_even': 1, 'negative_odd': 2}
