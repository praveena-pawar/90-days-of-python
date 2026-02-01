# Task 1 :

# Count how many times the array goes up.

def count_ups(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
    return count

print(count_ups([1, 3, 2, 4, 6, 5]))