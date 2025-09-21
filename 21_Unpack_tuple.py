fruits = ("apple", "banana", "cherry") # This is a tuple

(fruit1, fruit2, fruit3) = fruits # Unpacking the tuple into variables
# print(fruit1)  # Output: apple
# print(fruit2)  # Output: banana
# print(fruit3)  # Output: cherry

#? You can also use asterisk (*) to unpack remaining elements into a list
(fruitA, *fruitB) = fruits
print(fruitA)  # Output: apple
print(fruitB)  # Output: ['banana', 'cherry']
print(type(fruitB))  # Output: <class 'list'>
