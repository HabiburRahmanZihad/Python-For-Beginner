habib_List = [1,2,3,4,5,6,7,8,9,10]
print(type(habib_List))

# Byte array and Bytes are mutable sequences of integers in the range 0 <= x < 256
# Bytes are immutable, while bytearrays are mutable.
habib_Bytes = bytes(habib_List)

print(type(habib_Bytes))

# habib_Bytes[0] = 100 # This will raise an error because bytes are immutable


print(habib_Bytes)



# Creating a bytearray from the list
habib_BytesArray = bytearray(habib_List)

habib_BytesArray[0] = 246 # This will work because bytearrays are mutable

print(type(habib_BytesArray))

print(habib_BytesArray)
print(habib_BytesArray[0]) # Output: 246
