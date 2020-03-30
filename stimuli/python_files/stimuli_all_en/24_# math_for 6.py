num = [3, 7, 0, 1, 2, 2]
new_num = 1

for x in range(1, len(num), 2):
    new_num *= num[x]

print(new_num)

