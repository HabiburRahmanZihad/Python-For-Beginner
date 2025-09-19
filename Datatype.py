# Int Type data
# hablu = 420
# print('the type of hablu is:', type(hablu))
# print('the value of hablu is:', hablu)

# # Float Type data
# pi = 3.14
# print('the type of pi is:', type(pi))
# print('the value of pi is:', pi)


# Complex Type data
# x = 3 + 5j
# print('the type of x is:', type(x))
# print('the value of x is:', x)
# print('the real part of x is:', x.real)

# String Type data
# name = "Hablu"
# print(type(name)) #<class 'str'>
# print(name) #Hablu
# print(name[0]) #H
# print(name[1]) #a
# print(name[2]) #b
# print(name[3]) #l
# print(name[4]) #u
# print(name[0:3]) #Hab
# print(name[1:4]) #abl
# print(name[2:]) #blu
# print(name[:4]) #Habl
# print(name[:]) #Hablu
# print(name * 3)  #HabluHabluHablu
# print(name + " Khan")  #Hablu Khan
# print(name + name)  #HabluHablu
# print(name +' ' + name)  #Hablu Hablu

# Boolean Type data
is_cool = True
is_hungry = False

print(type(is_cool)) #<class 'bool'>

print(is_cool) #True
print(is_hungry) #False

# not operator: used to reverse the value
# and operator: both values must be true to return true
# or operator: one of the values must be true to return true

# and not operator: both values must be true to return false
# or not operator: one of the values must be true to return false
# not not operator: reverses the value again

print(not is_hungry) #True
print(not is_cool) #False

print(is_cool and is_hungry) #False
print(is_cool or is_hungry) #True
print(is_cool and not is_hungry) #True
print(is_cool or not is_hungry) #True
print(is_hungry or not is_cool) #True
print(is_hungry and not is_cool) #False
print(is_hungry or not is_hungry) #True
print(is_hungry and not is_hungry) #False
print(is_cool or not is_cool) #True
print(is_cool and not is_cool) #False
print(is_cool and is_cool) #True
print(is_hungry or is_hungry) #False