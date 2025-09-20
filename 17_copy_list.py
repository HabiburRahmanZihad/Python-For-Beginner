numbers = [1, 2, 3, 4, 5]
numbers_copy = numbers  # This creates a reference, not a copy
numbers_copy = numbers.copy()  # This creates a shallow copy
print("Original List:", numbers)
print("Copied List:", numbers_copy)