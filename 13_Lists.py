list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [1, "hello", 3.14, True]
list4 = []

print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))


#? Accessing elements
print(list1[0])  # Output: 1
print(list2[1])  # Output: banana
print(list3[2])  # Output: 3.14
print(list1[-1]) # Output: 5 (last element)


#? Modifying elements
list1[0] = 10
print(list1)  # Output: [10, 2, 3, 4, 5]


#? Adding elements
list1.append(6)
print(list1)  # Output: [10, 2, 3, 4, 5, 6]


list2.insert(1, "orange")
print(list2)  # Output: ['apple', 'orange', 'banana', 'cherry']



#? Removing elements
list3.remove("hello")
print(list3)  # Output: [1, 3.14, True]

list1.pop(5)
# list1.pop()  #? Removes the last element
print(list1)  # Output: [10, 2, 3, 4, 5]


del list2[0]
print(list2)  # Output: ['orange', 'banana', 'cherry']

# Clear the entire list
list3.clear()
print(list3)  # Output: []