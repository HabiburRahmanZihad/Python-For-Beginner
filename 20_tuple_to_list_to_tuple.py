Tuple_data = (10, 20, 30, 40, 50) # This is a tuple
print(type(Tuple_data))


List_data = list(Tuple_data) # Converting tuple to list
print(type(List_data))

List_data.append(60) # Adding element to list
print(List_data)

List_data.insert(0, 5) # Inserting element at specific position
print(List_data)

Tuple_data = tuple(List_data) # Converting list back to tuple
print(type(Tuple_data))