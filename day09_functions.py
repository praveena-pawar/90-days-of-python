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