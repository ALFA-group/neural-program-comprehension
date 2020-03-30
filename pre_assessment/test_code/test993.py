import copy
a = [(1,2,3,4)]
b = copy.copy(a) #Shallow copy
print(a)
print(b)
b[0] = b[0]+(5,)
print(a)
print(b)