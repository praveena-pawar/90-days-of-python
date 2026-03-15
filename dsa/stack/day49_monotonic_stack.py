# problem 1 :
# Next Smaller Element to the Left

arr = [4, 5, 2, 10, 8]

def next_smaller_left(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = arr[stack[-1]]

        stack.append(i)

    return result

print(next_smaller_left(arr))

#output:
#[-1, 4, -1, 2, 2]

