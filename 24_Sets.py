# Set Operations

#? Creating sets
set_a = {1, 2, 3, 4, True, 3.0, 'apple', '3'}  # Note: True is treated as 1, so duplicates are removed
set_b = {3, 4, 5, 6}
print("Set A:", set_a)
print("Set B:", set_b)

#? Union
union_set = set_a | set_b
print("Union of Set A and Set B:", union_set)

#? Intersection
intersection_set = set_a & set_b
print("Intersection of Set A and Set B:", intersection_set)

#? Difference
difference_set = set_a - set_b
print("Difference of Set A and Set B (A - B):", difference_set)

#? Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference of Set A and Set B:", symmetric_difference_set)

#? Adding elements
set_a.add(5)
print("Set A after adding 5:", set_a)

#? Removing elements
set_a.remove(2)
print("Set A after removing 2:", set_a)

#? Checking membership
is_member = 3 in set_a
print("Is 3 a member of Set A?", is_member)

#? Set comprehension
squared_set = {x**2 for x in range(5)}
print("Set of squares from 0 to 4:", squared_set)

#? Length of set
set_length = len(set_a)
print("Length of Set A:", set_length)

#? Clearing a set
set_a.clear()
print("Set A after clearing:", set_a)

#? Frozen set (immutable set)
frozen_set = frozenset([1, 2, 3])
print("Frozen Set:", frozen_set)

#? Set from a list (removing duplicates)
list_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_set = set(list_with_duplicates)
print("Set from list (removing duplicates):", unique_set)


#? Iterating through a set
for element in unique_set:
    print("Element in unique set:", element)



#? Subset and Superset
is_subset = {1, 2}.issubset(unique_set)
is_superset = unique_set.issuperset({1, 2})
print("Is {1, 2} a subset of unique_set?", is_subset)
print("Is unique_set a superset of {1, 2}?", is_superset)



#? Copying a set
copied_set = unique_set.copy()
print("Copied Set:", copied_set)


#? Removing an element safely
unique_set.discard(10)  # Does not raise an error if 10 is not present
print("Unique Set after discarding 10 (no error if not present):", unique_set)


#? Set operations with methods
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.update(set_b)  # Union
print("Set A after update with Set B (Union):", set_a)
set_a.intersection_update({2, 3})  # Intersection
print("Set A after intersection update with {2, 3}:", set_a)
set_a.difference_update({3})  # Difference
print("Set A after difference update with {3}:", set_a)
set_a.symmetric_difference_update({1, 4})  # Symmetric Difference
print("Set A after symmetric difference update with {1, 4}:", set_a)


#? Frozen set (immutable set)
frozen_set = frozenset([1, 2, 3])
print("Frozen Set:", frozen_set)

#? Set from a list (removing duplicates)
list_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_set = set(list_with_duplicates)
print("Set from list (removing duplicates):", unique_set)