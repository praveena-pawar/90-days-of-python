# 1. Read & understand
num = 15

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

#output:
#positive


# Think:

# Why only one print runs?
# In an if–elif–else chain, Python checks conditions top to bottom.
# The first condition that becomes True runs.
# After that, Python skips the rest completely.

# Why order matters (> 0 first)?
# Python checks conditions in the order we write them
# If we write the wrong order, the logic can break

