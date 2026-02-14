# problem 1 :

# Check if Array is Palindrome

def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome([1, 2, 3, 2, 1]))

#output:
#True



# problem 2 :

# Move All Zeros to End

def move_zeros(arr):
    insert_pos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1

    return arr

print(move_zeros([0,1,0,3,12]))