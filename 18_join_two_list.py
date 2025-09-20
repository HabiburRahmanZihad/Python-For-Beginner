numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]


fruits1 = ["apple", "banana"]
fruits2 = ["cherry", "date"]


#? Using + operator to concatenate two lists

combined = numbers1 + numbers2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

combined_fruits = fruits1 + fruits2
print(combined_fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

#? Using extend() to add elements of one list to another
numbers1.extend(numbers2)
print(numbers1)  # Output: [1, 2, 3, 4, 5, 6]

fruits1.extend(fruits2)
print(fruits1)  # Output: ['apple', 'banana', 'cherry', 'date']