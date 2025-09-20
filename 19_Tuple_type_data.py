list1 = [1, 2, 3] # This is a list
list2 = (4, 5, 6)  # This is a tuple


# list is mutable where as tuple is immutable


NewTuple = list2 + (7, 8, 9) # Concatenating tuples
print(NewTuple)  # Output: (4, 5, 6, 7, 8, 9)

list1.append(4) # Adding element to list
print(list1)  # Output: [1, 2, 3, 4]

# list2.append(7) # This will raise an "AttributeError" as tuples do not have an append method

newList = NewTuple[2:5] # Slicing a tuple
print(newList)  # Output: (6, 7, 8)

print(type(newList))


for item in newList: # Iterating through a tuple
    print(item + 10)

thisTuple = (1, "Hello", 3.14, True) # Tuple with mixed data types
print(thisTuple)

tuple_to_list = list(thisTuple) # Converting tuple to list
print(tuple_to_list)  # Output: [1, 'Hello', 3.14, True]