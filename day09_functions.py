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



