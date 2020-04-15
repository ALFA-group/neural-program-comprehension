import copy
a = [1,2,3,4]
b = copy.copy(a) # Shallow copy

print(a)
print(b)

b.append(1)

print(a)
print(b)
