# Example arrays
array1 = [1, 2, 3]
array2 = [4, 5, 6]

# Method 1: Using + operator
combined1 = array1 + array2
print("Using + operator:", combined1)

# Method 2: Using extend()
combined2 = array1.copy()
combined2.extend(array2)
print("Using extend():", combined2)
