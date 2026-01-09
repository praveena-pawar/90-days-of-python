# Task:1

# Write a function that:
# Takes a number
# Returns "Positive", "Negative", or "Zero"

def number(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"

n = int(input("Enter a number :")) 
result = number(n)
print("The number is :", result)





# Task 2 – Count Even Numbers (Using Function)

# Write a function that:
# Takes a list of numbers
# Counts how many numbers are even
# Returns the count

nums = [2, 5, 8, 10, 13]

def count_even(nums):
    even_count = 0
    for n in nums:
        if n % 2 == 0:
            even_count += 1

    return even_count
        
result = count_even(nums)
print("The total even numbers are :", result)

#output :
#The total even numbers are : 3




# Task 3 :

# Write a function that:
# Takes a list of numbers
# Finds the largest number
# Returns it

nums = [12, 45, 3, 89, 22]

def large_num(nums):
    largest_number = nums[0]
    for n in nums:
        if n > largest_number:
            largest_number = n

    return largest_number

result = large_num(nums)
print("The largest number is :", result)

#output:
#The largest number is : 89




# Task – String & Function Logic
# Write a function that:

# Takes a string as input
# Counts:
# Number of uppercase letters
# Number of lowercase letters
# Ignore spaces
# Returns both counts

def alphabet(name):
    count_uppercase = 0
    count_lowercase = 0
    for ch in name:
        if ch == " ":
            continue
        elif ch.islower():
            count_lowercase += 1
        elif ch.isupper():
            count_uppercase += 1
        
    return count_uppercase,  count_lowercase

name = input("Enter a string :")
uppercase, lowercase = alphabet(name)
print("The total number of uppercase letters :", uppercase)
print("The total Number of lowercase letters :", lowercase)