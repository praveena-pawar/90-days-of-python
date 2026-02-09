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

#output :
#Negative : 2
#zero : 2
#positive : 2



# 2. Grade system
marks = [45, 72, 88, 33, 60]
pass_count = 0
fail_count = 0

for n in marks:
    if n >= 40:
        pass_count +=1
    else:
        fail_count +=1

print("Passed :", pass_count)
print("Failed :", fail_count)

#output:
#passes : 4
#failed : 1



# 3. Character type
text = "aB3#"
letters = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Letters :", letters)
print("Digits :", digits)
print("Special :", special)

#output:
#letters : 2
#digits : 1
#special : 1