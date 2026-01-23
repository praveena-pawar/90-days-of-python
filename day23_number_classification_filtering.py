# Task 1 :

# From a list of numbers, return only:
# positive odd numbers
# negative even numbers

nums = nums = [2, -3, 4, -6, 7, -5, 0, 8, -10, 11]

def filter_numbers(nums):
    result = []
    for n in nums:
        if n == 0:
            continue
        if (n < 0) and (n % 2 == 0):
            result.append(n)
        elif (n > 0) and (n % 2 != 0):
            result.append(n)

    return result

print(filter_numbers(nums))

#output:
#[-6, 7, -10, 11]





# Task 2 :

# Given a list of integers, create a dictionary that stores the frequency of:
# positive numbers
# negative numbers
# zeros

nums = nums = [2, -3, 0, 4, 0, -1, 5, -6, 0]

def classify_frequency(nums):
    freq = {"positive": 0, "negative": 0, "zero": 0}

    for n in nums:
        if n > 0:
            freq["positive"] += 1
        elif n == 0:
            freq["zero"] += 1
        else:
            freq["negative"] += 1

    return freq

print(classify_frequency(nums))

#output:
#{'positive': 3, 'negative': 3, 'zero': 3}





# Task 3 :

# Final Problem: Category-wise Counting
# Given a list of numbers, create a dictionary that stores counts of:
# "positive_even"
# "positive_odd"
# "negative_even"
# "negative_odd"
# "zero"

nums = [2, -3, 0, 4, -6, 7, -5, 0, 8]

def full_classification(nums):
    result = {
    "positive_even": 0,
    "positive_odd": 0,
    "negative_even": 0,
    "negative_odd": 0,
    "zero": 0
     }
    for n in nums:
        if n == 0:
            result["zero"] += 1
        elif n > 0:
            if n % 2 == 0:
                result["positive_even"] +=1
            else:
                result["positive_odd"] += 1
        
        else:
            if n % 2 == 0:
                result["negative_even"] +=1
            else:
                result["negative_odd"] += 1
        
    return result
    
print(full_classification(nums))
            








