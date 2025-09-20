numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]


fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']


#? Sorting in descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]


fruits.sort(reverse=True)
print(fruits)  # Output: ['cherry', 'banana', 'apple']



#? Using sorted() to return a new sorted list
original_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(original_numbers)

print(original_numbers)  # Output: [5, 2, 9, 1, 5, 6]
print(sorted_numbers)    # Output: [1, 2, 5, 5, 6, 9]