studentInfo = {
    "name": "John",
    "age": 21,
    "courses": ["Math", "CompSci"]
}
# print(studentInfo)

studentInfo2 = {
  "Jamil": {
    "age": 21,
    "courses": ["Math", "CompSci"]
  },
  "Fahim": {
    "age": 22,
    "courses": ["Math", "Art", "Design"]
  },
  "Rafi": {
    "age": 23,
    "courses": ["Math", "CompSci", "Art"]
  },
  "year": 2024
}

# print(studentInfo2)

# print(studentInfo2["Jamil"])
# print(studentInfo2["Jamil"]["courses"])

# print(studentInfo2["Fahim"]["age"])
# print(studentInfo2["Rafi"]["courses"][1])

# print(studentInfo2["year"])


#? Accessing Items with get() Method
# print(studentInfo.get("name"))
# print(studentInfo2.get("year"))

#? Accessing Keys with keys() Method
# print(studentInfo.keys())
# print(studentInfo2.keys())


#? Accessing Values with values() Method
# print(studentInfo.values())
# print(studentInfo2.values())


#? Accessing Items with items() Method
# print(studentInfo.items())
# print(studentInfo2.items())


#? Change the value of a specific item
# studentInfo["age"] = 22
# print(studentInfo)
# studentInfo2["year"] = 2025
# print(studentInfo2)

#? Update the value of a specific item using update() method
# studentInfo.update({"age": 23})
# print(studentInfo)


#? Remove an item with pop() method
# studentInfo.pop("age")
# print(studentInfo)
# studentInfo2.pop("year")
# print(studentInfo2)


#? Remove the last inserted item with popitem() method
# studentInfo.popitem()
# print(studentInfo)
# studentInfo2.popitem()
# print(studentInfo2)

#? Remove an item with del keyword
# del studentInfo["age"]
# print(studentInfo)
# del studentInfo2["year"]
# print(studentInfo2)

#? Clear all items with clear() method
# studentInfo.clear()
# print(studentInfo)
# studentInfo2.clear()
# print(studentInfo2)

#? Loop through a dictionary
# for key in studentInfo2:
#     print(key)
#     print(studentInfo2[key])
#     print("---")




#? loop through keys
# for key in studentInfo2.keys():
#     print(key)

#? loop through values
# for value in studentInfo2.values():
#     print(value)

#? loop through items
# for item in studentInfo2.items():
#     print(item)


  # for key, value in studentInfo2.items():
  #     print("Key:", key)
  #     print("Value:", value)
  #    print("---")


#? Copy a dictionary with copy() method
# studentInfo3 = studentInfo2.copy()
# print(studentInfo3)

#? Copy a dictionary with dict() function
# studentInfo4 = dict(studentInfo2)
# print(studentInfo4)