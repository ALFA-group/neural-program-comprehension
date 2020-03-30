list1 = [4, 4, 6]
list2 = [1, 2, 4]
list3 = [3, 2, 1]

for i in range(len(list1)):
    list3[i] += list1[i] + list2[i]

print(list3)

