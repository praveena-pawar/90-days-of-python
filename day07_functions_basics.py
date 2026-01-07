# 1. Read & understand
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)


# Think:

# Why do we use def?
# def is used to define (create) a function.

# What does return do?
# return sends the result back to the place where the function was called.

# What happens after return?
# The function stops immediately
# Control goes back to the caller Any code after return inside the function does not run
# Example : 
# def test():
#     return 10
#     print("Hello")  # ❌ never runs
