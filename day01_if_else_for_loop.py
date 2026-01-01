# 1. # Count even numbers in a list
nums = [1, 4, 7, 10, 13, 16]
count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print("Number of even elements:", count)

#output:
#number of even elements is : 3
