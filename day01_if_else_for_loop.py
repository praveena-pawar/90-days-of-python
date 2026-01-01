# 1.  Count even numbers in a list
nums = [1, 4, 7, 10, 13, 16]
count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print("Number of even elements:", count)

#output:
#number of even elements is : 3



# 2. Sum only positive numbers
nums = [-2, 5, -1, 7, 3]
total = 0

for n in nums:
    if n > 0:
        total += n

print("sum of positive numbers:", total)

#output:
#sum of positive numbers is : 15



# 3. Print numbers divisible by 3
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

#output:
# 3
# 6
# 9
# 12
# 15
# 18 
