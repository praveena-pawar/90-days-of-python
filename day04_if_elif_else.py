# 1. Read & understand
num = 15

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

#output:
#positive


# Think:

# Why only one print runs?
# In an if–elif–else chain, Python checks conditions top to bottom.
# The first condition that becomes True runs.
# After that, Python skips the rest completely.

# Why order matters (> 0 first)?
# Python checks conditions in the order we write them
# If we write the wrong order, the logic can break



# 2. Now YOU write code
# Task 1️

# Write a program to:

# Take a number

# Print:

# "Divisible by 3" if divisible by 3

# "Divisible by 5" if divisible by 5

# "Divisible by both" if divisible by both

# "Not divisible by 3 or 5" otherwise