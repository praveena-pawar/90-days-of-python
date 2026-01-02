# 1. Count even and odd numbers
nums = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)

#output
#Even : 3
#Odd : 3



# 2. Count numbers in ranges
nums = [5, 12, 18, 3, 25, 7, 11]
small = 0
large = 0

for n in nums:
    if n < 10 :
        small += 1
    else :
        large +=1 

print("Less the 10 :", small)
print("10 or more:", large)