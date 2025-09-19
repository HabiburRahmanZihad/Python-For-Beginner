# list - mutable
# li = [1, 2, 3, 4, 5]
# print(li) #? Output: [1, 2, 3, 4, 5]
# print(type(li))  #? Output: <class 'list'>
# li[2] = 10
# print(li) #? Output: [1, 2, 10, 4, 5]

#! tuple - immutable
# tu = (1, 2, 3, 4, 5)
# print(tu)
# print(type(tu))  #? Output: <class 'tuple'>
# # tu[2] = 10 #? TypeError: 'tuple' object does not support item assignment


#!range - immutable
ra = range(1, 11)
print(ra) #? Output: range(1, 11)


for i in ra:
    print(i, end=" ") #? Output: 1 2 3 4 5 6 7 8 9 10

print(type(ra))  #? Output: <class 'range'>