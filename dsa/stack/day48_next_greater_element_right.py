# problem 1 :

# Next Greater Element to the Right

def next_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result


arr = [2, 1, 2, 4, 3]
print(next_greater(arr))

#output:
#[4, 2, 4, -1, -1]