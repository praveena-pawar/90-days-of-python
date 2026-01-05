# 1. Read & think
nums = [2, 5, 8, 11, 14]
even_count = 0
odd_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, odd_count)

# Think:

# Why do we need two counters?
# We use two counters because we are tracking two different results.

# What happens in each loop iteration?
# A for loop goes one element at a time.