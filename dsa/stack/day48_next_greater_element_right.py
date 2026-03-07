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




# problem 2 :

# Next Smaller Element to the Right

def next_smaller(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result


arr = [4, 8, 5, 2, 25]
print(next_smaller(arr))





# problem 3 :

# For each day, find how many days you have to wait until a warmer temperature.

def daily_temperatures(temps):
    stack = []
    result = [0] * len(temps)

    for i in range(len(temps)):
        
        while stack and temps[i] > temps[stack[-1]]:
            index = stack.pop()
            result[index] = i - index

        stack.append(i)

    return result


temps = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temps))