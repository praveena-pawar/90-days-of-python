# 1. Categorize numbers
nums = [-5, 0, 7, -2, 0, 4]
negative = 0
zero = 0
positive = 0

for n in nums:
    if n < 0:
        negative += 1
    elif n == 0:
        zero += 1
    else:
        positive +=1

print("Negative :", negative )
print("Zero :", zero)
print("Positive :", positive)