list1 = [12, 34, 36, 71, 3, 42]
list2 = [53, 23, 16, 24, 5, 15]
list3 = [1, 34, 10, 91, 43, 26]
number = 34

if number in list1 or (number in list2 and number in list3):
    print(list1[0])
elif number in list2 or (number in list3 and number in list1):
    print(list2[0])
elif number in list3 or (number in list1 and number in list2):
    print(list3[0])

